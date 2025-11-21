import os
import json
import sqlite3
from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional, List, Dict, Any


DB_PATH_DEFAULT = os.path.join("data", "contracts.sqlite3")


def _ensure_dir(path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)


def _dict_factory(cursor, row):
    """Возвращает строки sqlite как dict."""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def _parse_date(d: Any) -> date:
    """Поддерживаем 'DD.MM.YYYY', 'DD/MM/YYYY', 'YYYY-MM-DD' или date."""
    if isinstance(d, date):
        return d
    if not isinstance(d, str):
        raise ValueError("Unsupported date format")

    for fmt in ("%d.%m.%Y", "%d/%m/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(d, fmt).date()
        except Exception:
            pass
    raise ValueError(f"Cannot parse date: {d}")


def _to_iso(d: date) -> str:
    return d.strftime("%Y-%m-%d")


def _to_slash(d: date) -> str:
    """Формат для номера: DD/MM/YYYY."""
    return d.strftime("%d/%m/%Y")


@dataclass
class ContractRecord:
    full_number: str                 # пример: '29/04/2025/ФП01'
    date_iso: str                    # 'YYYY-MM-DD'
    sequence: int                    # порядковый № за день
    company_prefix: str              # 'ФП' для Флексопринт
    payment_form: str                # 'prepay' | 'delay' | '5050' | и т.п.
    counterparty_name: str
    counterparty_inn: str
    our_entity: str                  # наше юрлицо (ООО «ФЛЕКСПРИНТ»)
    manager_surname: str             # фамилия менеджера, ответственного за договор
    filename: str                    # имя/путь итогового файла
    meta_json: Optional[str] = None  # произвольные поля (JSON)
    created_at: Optional[str] = None # ISO timestamp (заполняется БД)


class Registry:
    """
    Реестр договоров:
      - нумерация: DD/MM/YYYY/<PREFIX><NN>, где NN — порядковый номер за день (2 знака).
      - поиск: по ИНН, по дате, по названию контрагента (LIKE).
    """

    def __init__(self, db_path: str = DB_PATH_DEFAULT) -> None:
        self.db_path = db_path
        _ensure_dir(db_path)
        self._init_db()

    # ---------- schema ----------

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = _dict_factory
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.execute("PRAGMA journal_mode = WAL;")
        conn.execute("PRAGMA synchronous = NORMAL;")
        return conn

    def _init_db(self) -> None:
        with self._connect() as con:
            con.executescript(
                """
                CREATE TABLE IF NOT EXISTS contracts (
                    id                INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_number       TEXT NOT NULL UNIQUE,
                    date_iso          TEXT NOT NULL,            -- YYYY-MM-DD
                    sequence          INTEGER NOT NULL,
                    company_prefix    TEXT NOT NULL,            -- 'ФП' и т.п.
                    payment_form      TEXT NOT NULL,            -- 'prepay' / 'delay' / '5050' / ...
                    counterparty_name TEXT NOT NULL,
                    counterparty_inn  TEXT NOT NULL,
                    our_entity        TEXT NOT NULL,
                    manager_surname   TEXT,                     -- фамилия менеджера
                    filename          TEXT NOT NULL,
                    meta_json         TEXT,
                    created_at        TEXT NOT NULL DEFAULT (datetime('now'))
                );
                CREATE INDEX IF NOT EXISTS idx_contracts_inn ON contracts(counterparty_inn);
                CREATE INDEX IF NOT EXISTS idx_contracts_date ON contracts(date_iso);
                CREATE INDEX IF NOT EXISTS idx_contracts_name ON contracts(counterparty_name);
                CREATE INDEX IF NOT EXISTS idx_contracts_prefix_date ON contracts(company_prefix, date_iso);
                """
            )
            # Ленивая миграция для старых БД
            try:
                con.execute("ALTER TABLE contracts ADD COLUMN manager_surname TEXT")
            except Exception:
                pass

    # ---------- numbering ----------

    def _next_sequence_for_day(self, con: sqlite3.Connection, dt: date, prefix: str) -> int:
        cur = con.execute(
            "SELECT COALESCE(MAX(sequence), 0) AS max_seq "
            "FROM contracts WHERE date_iso = ? AND company_prefix = ?",
            (_to_iso(dt), prefix),
        )
        row = cur.fetchone()
        return int(row["max_seq"]) + 1

    @staticmethod
    def build_full_number(dt: date, prefix: str, seq: int) -> str:
        return f"{_to_slash(dt)}/{prefix}{seq:02d}"

    # ---------- write ----------

    def save_contract(
        self,
        *,
        date_value: Any,
        company_prefix: str,
        payment_form: str,
        counterparty_name: str,
        counterparty_inn: str,
        our_entity: str,
        manager_surname: str,
        filename: str,
        meta: Optional[Dict[str, Any]] = None,
    ) -> ContractRecord:
        """
        Атомарно резервирует порядковый номер и сохраняет запись.
        Возвращает сохранённую запись с полным номером.
        """
        dt = _parse_date(date_value)
        with self._connect() as con:
            con.execute("BEGIN IMMEDIATE;")
            seq = self._next_sequence_for_day(con, dt, company_prefix)
            full_num = self.build_full_number(dt, company_prefix, seq)
            meta_json = json.dumps(meta, ensure_ascii=False) if meta else None

            con.execute(
                """
                INSERT INTO contracts
                  (full_number, date_iso, sequence, company_prefix, payment_form,
                   counterparty_name, counterparty_inn, our_entity, manager_surname, filename, meta_json)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    full_num,
                    _to_iso(dt),
                    seq,
                    company_prefix,
                    payment_form,
                    counterparty_name,
                    counterparty_inn,
                    our_entity,
                    manager_surname,
                    filename,
                    meta_json,
                ),
            )
            row = con.execute(
                "SELECT * FROM contracts WHERE full_number = ?",
                (full_num,),
            ).fetchone()

        return ContractRecord(
            full_number=row["full_number"],
            date_iso=row["date_iso"],
            sequence=row["sequence"],
            company_prefix=row["company_prefix"],
            payment_form=row["payment_form"],
            counterparty_name=row["counterparty_name"],
            counterparty_inn=row["counterparty_inn"],
            our_entity=row["our_entity"],
            manager_surname=row.get("manager_surname") or "",
            filename=row["filename"],
            meta_json=row.get("meta_json"),
            created_at=row.get("created_at"),
        )

    def update_filename(self, full_number: str, filename: str) -> None:
        """Обновляет путь к файлу по полному номеру."""
        with self._connect() as con:
            con.execute(
                "UPDATE contracts SET filename = ? WHERE full_number = ?",
                (filename, full_number),
            )

    # ---------- read/search ----------

    def get_by_full_number(self, full_number: str) -> Optional[Dict[str, Any]]:
        with self._connect() as con:
            return con.execute(
                "SELECT * FROM contracts WHERE full_number = ?",
                (full_number,),
            ).fetchone()

    def find_by_inn(self, inn: str) -> List[Dict[str, Any]]:
        with self._connect() as con:
            return con.execute(
                "SELECT * FROM contracts WHERE counterparty_inn = ? "
                "ORDER BY date_iso DESC, sequence DESC",
                (inn,),
            ).fetchall()

    def find_by_date(self, date_value: Any) -> List[Dict[str, Any]]:
        dt = _parse_date(date_value)
        with self._connect() as con:
            return con.execute(
                "SELECT * FROM contracts WHERE date_iso = ? ORDER BY sequence ASC",
                (_to_iso(dt),),
            ).fetchall()

    def find_by_name(self, name_query: str) -> List[Dict[str, Any]]:
        q = f"%{name_query}%"
        with self._connect() as con:
            return con.execute(
                "SELECT * FROM contracts WHERE counterparty_name LIKE ? "
                "ORDER BY date_iso DESC, sequence DESC",
                (q,),
            ).fetchall()

    def list_all(self, limit: int = 100, offset: int = 0) -> List[Dict[str, Any]]:
        with self._connect() as con:
            return con.execute(
                "SELECT * FROM contracts ORDER BY date_iso DESC, sequence DESC LIMIT ? OFFSET ?",
                (limit, offset),
            ).fetchall()