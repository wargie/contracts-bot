from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Company")


@_attrs_define
class Company:
    """
    Attributes:
        city (None | str | Unset):
        domain (None | str | Unset):
        employee_count (int | None | Unset):
        income (float | None | Unset):
        inn (None | str | Unset):
        name (None | str | Unset):
        ogrn (None | str | Unset):
        okved (None | str | Unset):
        okved_name (None | str | Unset):
        timezone (None | str | Unset):
    """

    city: None | str | Unset = UNSET
    domain: None | str | Unset = UNSET
    employee_count: int | None | Unset = UNSET
    income: float | None | Unset = UNSET
    inn: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    ogrn: None | str | Unset = UNSET
    okved: None | str | Unset = UNSET
    okved_name: None | str | Unset = UNSET
    timezone: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        employee_count: int | None | Unset
        if isinstance(self.employee_count, Unset):
            employee_count = UNSET
        else:
            employee_count = self.employee_count

        income: float | None | Unset
        if isinstance(self.income, Unset):
            income = UNSET
        else:
            income = self.income

        inn: None | str | Unset
        if isinstance(self.inn, Unset):
            inn = UNSET
        else:
            inn = self.inn

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        ogrn: None | str | Unset
        if isinstance(self.ogrn, Unset):
            ogrn = UNSET
        else:
            ogrn = self.ogrn

        okved: None | str | Unset
        if isinstance(self.okved, Unset):
            okved = UNSET
        else:
            okved = self.okved

        okved_name: None | str | Unset
        if isinstance(self.okved_name, Unset):
            okved_name = UNSET
        else:
            okved_name = self.okved_name

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if domain is not UNSET:
            field_dict["domain"] = domain
        if employee_count is not UNSET:
            field_dict["employee_count"] = employee_count
        if income is not UNSET:
            field_dict["income"] = income
        if inn is not UNSET:
            field_dict["inn"] = inn
        if name is not UNSET:
            field_dict["name"] = name
        if ogrn is not UNSET:
            field_dict["ogrn"] = ogrn
        if okved is not UNSET:
            field_dict["okved"] = okved
        if okved_name is not UNSET:
            field_dict["okved_name"] = okved_name
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        def _parse_employee_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        employee_count = _parse_employee_count(d.pop("employee_count", UNSET))

        def _parse_income(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        income = _parse_income(d.pop("income", UNSET))

        def _parse_inn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inn = _parse_inn(d.pop("inn", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_ogrn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ogrn = _parse_ogrn(d.pop("ogrn", UNSET))

        def _parse_okved(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        okved = _parse_okved(d.pop("okved", UNSET))

        def _parse_okved_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        okved_name = _parse_okved_name(d.pop("okved_name", UNSET))

        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        company = cls(
            city=city,
            domain=domain,
            employee_count=employee_count,
            income=income,
            inn=inn,
            name=name,
            ogrn=ogrn,
            okved=okved,
            okved_name=okved_name,
            timezone=timezone,
        )

        company.additional_properties = d
        return company

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
