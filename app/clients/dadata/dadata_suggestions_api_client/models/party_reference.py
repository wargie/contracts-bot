from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartyReference")


@_attrs_define
class PartyReference:
    """
    Attributes:
        inn (None | str | Unset):
        name (None | str | Unset):
        ogrn (None | str | Unset):
    """

    inn: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    ogrn: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inn is not UNSET:
            field_dict["inn"] = inn
        if name is not UNSET:
            field_dict["name"] = name
        if ogrn is not UNSET:
            field_dict["ogrn"] = ogrn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        party_reference = cls(
            inn=inn,
            name=name,
            ogrn=ogrn,
        )

        party_reference.additional_properties = d
        return party_reference

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
