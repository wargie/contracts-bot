from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartyCodeUnit")


@_attrs_define
class PartyCodeUnit:
    """
    Attributes:
        alpha3 (None | str | Unset):
        numeric (int | None | Unset):
    """

    alpha3: None | str | Unset = UNSET
    numeric: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alpha3: None | str | Unset
        if isinstance(self.alpha3, Unset):
            alpha3 = UNSET
        else:
            alpha3 = self.alpha3

        numeric: int | None | Unset
        if isinstance(self.numeric, Unset):
            numeric = UNSET
        else:
            numeric = self.numeric

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alpha3 is not UNSET:
            field_dict["alpha3"] = alpha3
        if numeric is not UNSET:
            field_dict["numeric"] = numeric

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_alpha3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alpha3 = _parse_alpha3(d.pop("alpha3", UNSET))

        def _parse_numeric(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        numeric = _parse_numeric(d.pop("numeric", UNSET))

        party_code_unit = cls(
            alpha3=alpha3,
            numeric=numeric,
        )

        party_code_unit.additional_properties = d
        return party_code_unit

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
