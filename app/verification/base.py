from abc import ABC, abstractmethod
from typing import Optional, Dict

class VerificationProvider(ABC):
    @abstractmethod
    async def verify(self, *, inn: str, kpp: Optional[str] = None) -> Dict:
        """Возвращает словарь с ключами: name, inn, kpp, ogrn, address, management, status."""
        raise NotImplementedError
