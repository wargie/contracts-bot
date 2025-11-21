from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BankName")


@_attrs_define
class BankName:
    """
    Attributes:
        full_value (None | str | Unset):
        payment (None | str | Unset):
        short_value (None | str | Unset):
    """

    full_value: None | str | Unset = UNSET
    payment: None | str | Unset = UNSET
    short_value: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_value: None | str | Unset
        if isinstance(self.full_value, Unset):
            full_value = UNSET
        else:
            full_value = self.full_value

        payment: None | str | Unset
        if isinstance(self.payment, Unset):
            payment = UNSET
        else:
            payment = self.payment

        short_value: None | str | Unset
        if isinstance(self.short_value, Unset):
            short_value = UNSET
        else:
            short_value = self.short_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if full_value is not UNSET:
            field_dict["full_value"] = full_value
        if payment is not UNSET:
            field_dict["payment"] = payment
        if short_value is not UNSET:
            field_dict["short_value"] = short_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_full_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_value = _parse_full_value(d.pop("full_value", UNSET))

        def _parse_payment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment = _parse_payment(d.pop("payment", UNSET))

        def _parse_short_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        short_value = _parse_short_value(d.pop("short_value", UNSET))

        bank_name = cls(
            full_value=full_value,
            payment=payment,
            short_value=short_value,
        )

        bank_name.additional_properties = d
        return bank_name

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
