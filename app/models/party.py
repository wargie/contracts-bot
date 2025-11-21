from pydantic import BaseModel, Field
from typing import Optional

class Party(BaseModel):
    name: str = Field(..., description="Полное наименование")
    inn: str = Field(..., description="ИНН")
    kpp: Optional[str] = Field(None, description="КПП (для юрлиц)")
    ogrn: Optional[str] = Field(None, description="ОГРН/ОГРНИП")
    address: Optional[str] = None
    manager: Optional[str] = Field(None, description="Руководитель: ФИО, должность")
    bank_name: Optional[str] = None
    bank_bik: Optional[str] = None
    bank_account: Optional[str] = None
    bank_corr: Optional[str] = None
