from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bank_opf_type import BankOpfType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BankOpf")


@_attrs_define
class BankOpf:
    """
    Attributes:
        full_value (None | str | Unset):
        short_value (None | str | Unset):
        type_ (BankOpfType | Unset):
    """

    full_value: None | str | Unset = UNSET
    short_value: None | str | Unset = UNSET
    type_: BankOpfType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_value: None | str | Unset
        if isinstance(self.full_value, Unset):
            full_value = UNSET
        else:
            full_value = self.full_value

        short_value: None | str | Unset
        if isinstance(self.short_value, Unset):
            short_value = UNSET
        else:
            short_value = self.short_value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if full_value is not UNSET:
            field_dict["full_value"] = full_value
        if short_value is not UNSET:
            field_dict["short_value"] = short_value
        if type_ is not UNSET:
            field_dict["type"] = type_

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

        def _parse_short_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        short_value = _parse_short_value(d.pop("short_value", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: BankOpfType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BankOpfType(_type_)

        bank_opf = cls(
            full_value=full_value,
            short_value=short_value,
            type_=type_,
        )

        bank_opf.additional_properties = d
        return bank_opf

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
