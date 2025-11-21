from pydantic import BaseModel, Field
from typing import Literal, Optional
from .party import Party

ContractType = Literal["services"]

class ContractParams(BaseModel):
    number: str = Field(..., description="Номер договора")
    date: str = Field(..., description="Дата (например, 30.09.2025)")
    city: str = Field(..., description="Город заключения")
    subject: str = Field(..., description="Предмет договора")
    price: str = Field(..., description="Стоимость (с валютой)")
    payment_terms: str = Field(..., description="Порядок расчетов")
    term: str = Field(..., description="Срок оказания услуг/действия договора")
    jurisdiction: str = Field("РФ", description="Применимое право")
    penalties: Optional[str] = Field(None, description="Штрафные санкции")

class ContractInput(BaseModel):
    contract_type: ContractType
    customer: Party
    contractor: Party
    params: ContractParams
    output: Literal["docx", "pdf", "both"] = "both"
    verification_report: Optional[dict] = None
