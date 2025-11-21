from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartyOpf")


@_attrs_define
class PartyOpf:
    """
    Attributes:
        code (None | str | Unset):
        full_value (None | str | Unset):
        short_value (None | str | Unset):
        type_ (None | str | Unset):
    """

    code: None | str | Unset = UNSET
    full_value: None | str | Unset = UNSET
    short_value: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

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

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
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

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

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

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        party_opf = cls(
            code=code,
            full_value=full_value,
            short_value=short_value,
            type_=type_,
        )

        party_opf.additional_properties = d
        return party_opf

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
