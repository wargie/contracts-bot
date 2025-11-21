from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.party_code_unit import PartyCodeUnit
    from ..models.party_name_unit import PartyNameUnit


T = TypeVar("T", bound="PartyCountry")


@_attrs_define
class PartyCountry:
    """
    Attributes:
        code (PartyCodeUnit):
        name (PartyNameUnit):
    """

    code: PartyCodeUnit
    name: PartyNameUnit
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.to_dict()

        name = self.name.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.party_code_unit import PartyCodeUnit
        from ..models.party_name_unit import PartyNameUnit

        d = dict(src_dict)
        code = PartyCodeUnit.from_dict(d.pop("code"))

        name = PartyNameUnit.from_dict(d.pop("name"))

        party_country = cls(
            code=code,
            name=name,
        )

        party_country.additional_properties = d
        return party_country

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
