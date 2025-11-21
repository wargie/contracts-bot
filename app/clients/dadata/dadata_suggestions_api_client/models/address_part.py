from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddressPart")


@_attrs_define
class AddressPart:
    """
    Attributes:
        fias_id (None | str | Unset):
        kladr_id (None | str | Unset):
        name (None | str | Unset):
        name_with_type (None | str | Unset):
        type_ (None | str | Unset):
        type_full (None | str | Unset):
    """

    fias_id: None | str | Unset = UNSET
    kladr_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    name_with_type: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    type_full: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fias_id: None | str | Unset
        if isinstance(self.fias_id, Unset):
            fias_id = UNSET
        else:
            fias_id = self.fias_id

        kladr_id: None | str | Unset
        if isinstance(self.kladr_id, Unset):
            kladr_id = UNSET
        else:
            kladr_id = self.kladr_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        name_with_type: None | str | Unset
        if isinstance(self.name_with_type, Unset):
            name_with_type = UNSET
        else:
            name_with_type = self.name_with_type

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        type_full: None | str | Unset
        if isinstance(self.type_full, Unset):
            type_full = UNSET
        else:
            type_full = self.type_full

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fias_id is not UNSET:
            field_dict["fias_id"] = fias_id
        if kladr_id is not UNSET:
            field_dict["kladr_id"] = kladr_id
        if name is not UNSET:
            field_dict["name"] = name
        if name_with_type is not UNSET:
            field_dict["name_with_type"] = name_with_type
        if type_ is not UNSET:
            field_dict["type"] = type_
        if type_full is not UNSET:
            field_dict["type_full"] = type_full

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_fias_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fias_id = _parse_fias_id(d.pop("fias_id", UNSET))

        def _parse_kladr_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kladr_id = _parse_kladr_id(d.pop("kladr_id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_name_with_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_with_type = _parse_name_with_type(d.pop("name_with_type", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_full = _parse_type_full(d.pop("type_full", UNSET))

        address_part = cls(
            fias_id=fias_id,
            kladr_id=kladr_id,
            name=name,
            name_with_type=name_with_type,
            type_=type_,
            type_full=type_full,
        )

        address_part.additional_properties = d
        return address_part

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
