from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bank_state_status import BankStateStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BankState")


@_attrs_define
class BankState:
    """
    Attributes:
        status (BankStateStatus):
        actuality_date (int | None | Unset):
        code (None | str | Unset):
        liquidation_date (int | None | Unset):
        registration_date (int | None | Unset):
    """

    status: BankStateStatus
    actuality_date: int | None | Unset = UNSET
    code: None | str | Unset = UNSET
    liquidation_date: int | None | Unset = UNSET
    registration_date: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        actuality_date: int | None | Unset
        if isinstance(self.actuality_date, Unset):
            actuality_date = UNSET
        else:
            actuality_date = self.actuality_date

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        liquidation_date: int | None | Unset
        if isinstance(self.liquidation_date, Unset):
            liquidation_date = UNSET
        else:
            liquidation_date = self.liquidation_date

        registration_date: int | None | Unset
        if isinstance(self.registration_date, Unset):
            registration_date = UNSET
        else:
            registration_date = self.registration_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if actuality_date is not UNSET:
            field_dict["actuality_date"] = actuality_date
        if code is not UNSET:
            field_dict["code"] = code
        if liquidation_date is not UNSET:
            field_dict["liquidation_date"] = liquidation_date
        if registration_date is not UNSET:
            field_dict["registration_date"] = registration_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = BankStateStatus(d.pop("status"))

        def _parse_actuality_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        actuality_date = _parse_actuality_date(d.pop("actuality_date", UNSET))

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_liquidation_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        liquidation_date = _parse_liquidation_date(d.pop("liquidation_date", UNSET))

        def _parse_registration_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        registration_date = _parse_registration_date(d.pop("registration_date", UNSET))

        bank_state = cls(
            status=status,
            actuality_date=actuality_date,
            code=code,
            liquidation_date=liquidation_date,
            registration_date=registration_date,
        )

        bank_state.additional_properties = d
        return bank_state

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
