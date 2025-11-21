from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.party_finance_tax_system import PartyFinanceTaxSystem
from ..types import UNSET, Unset

T = TypeVar("T", bound="PartyFinance")


@_attrs_define
class PartyFinance:
    """
    Attributes:
        debt (float | None | Unset):
        expense (float | None | Unset):
        income (float | None | Unset):
        penalty (float | None | Unset):
        revenue (float | None | Unset):
        tax_system (PartyFinanceTaxSystem | Unset):
        year (int | None | Unset):
    """

    debt: float | None | Unset = UNSET
    expense: float | None | Unset = UNSET
    income: float | None | Unset = UNSET
    penalty: float | None | Unset = UNSET
    revenue: float | None | Unset = UNSET
    tax_system: PartyFinanceTaxSystem | Unset = UNSET
    year: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        debt: float | None | Unset
        if isinstance(self.debt, Unset):
            debt = UNSET
        else:
            debt = self.debt

        expense: float | None | Unset
        if isinstance(self.expense, Unset):
            expense = UNSET
        else:
            expense = self.expense

        income: float | None | Unset
        if isinstance(self.income, Unset):
            income = UNSET
        else:
            income = self.income

        penalty: float | None | Unset
        if isinstance(self.penalty, Unset):
            penalty = UNSET
        else:
            penalty = self.penalty

        revenue: float | None | Unset
        if isinstance(self.revenue, Unset):
            revenue = UNSET
        else:
            revenue = self.revenue

        tax_system: str | Unset = UNSET
        if not isinstance(self.tax_system, Unset):
            tax_system = self.tax_system.value

        year: int | None | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if debt is not UNSET:
            field_dict["debt"] = debt
        if expense is not UNSET:
            field_dict["expense"] = expense
        if income is not UNSET:
            field_dict["income"] = income
        if penalty is not UNSET:
            field_dict["penalty"] = penalty
        if revenue is not UNSET:
            field_dict["revenue"] = revenue
        if tax_system is not UNSET:
            field_dict["tax_system"] = tax_system
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_debt(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        debt = _parse_debt(d.pop("debt", UNSET))

        def _parse_expense(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        expense = _parse_expense(d.pop("expense", UNSET))

        def _parse_income(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        income = _parse_income(d.pop("income", UNSET))

        def _parse_penalty(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        penalty = _parse_penalty(d.pop("penalty", UNSET))

        def _parse_revenue(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        revenue = _parse_revenue(d.pop("revenue", UNSET))

        _tax_system = d.pop("tax_system", UNSET)
        tax_system: PartyFinanceTaxSystem | Unset
        if isinstance(_tax_system, Unset):
            tax_system = UNSET
        else:
            tax_system = PartyFinanceTaxSystem(_tax_system)

        def _parse_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        year = _parse_year(d.pop("year", UNSET))

        party_finance = cls(
            debt=debt,
            expense=expense,
            income=income,
            penalty=penalty,
            revenue=revenue,
            tax_system=tax_system,
            year=year,
        )

        party_finance.additional_properties = d
        return party_finance

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
