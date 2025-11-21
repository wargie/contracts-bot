from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_part import AddressPart


T = TypeVar("T", bound="AdministrativeDivision")


@_attrs_define
class AdministrativeDivision:
    """
    Attributes:
        area (AddressPart | Unset):
        city (AddressPart | Unset):
        city_district (AddressPart | Unset):
        planning_structure (AddressPart | Unset):
        settlement (AddressPart | Unset):
    """

    area: AddressPart | Unset = UNSET
    city: AddressPart | Unset = UNSET
    city_district: AddressPart | Unset = UNSET
    planning_structure: AddressPart | Unset = UNSET
    settlement: AddressPart | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        area: dict[str, Any] | Unset = UNSET
        if not isinstance(self.area, Unset):
            area = self.area.to_dict()

        city: dict[str, Any] | Unset = UNSET
        if not isinstance(self.city, Unset):
            city = self.city.to_dict()

        city_district: dict[str, Any] | Unset = UNSET
        if not isinstance(self.city_district, Unset):
            city_district = self.city_district.to_dict()

        planning_structure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.planning_structure, Unset):
            planning_structure = self.planning_structure.to_dict()

        settlement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settlement, Unset):
            settlement = self.settlement.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if area is not UNSET:
            field_dict["area"] = area
        if city is not UNSET:
            field_dict["city"] = city
        if city_district is not UNSET:
            field_dict["city_district"] = city_district
        if planning_structure is not UNSET:
            field_dict["planning_structure"] = planning_structure
        if settlement is not UNSET:
            field_dict["settlement"] = settlement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_part import AddressPart

        d = dict(src_dict)
        _area = d.pop("area", UNSET)
        area: AddressPart | Unset
        if isinstance(_area, Unset):
            area = UNSET
        else:
            area = AddressPart.from_dict(_area)

        _city = d.pop("city", UNSET)
        city: AddressPart | Unset
        if isinstance(_city, Unset):
            city = UNSET
        else:
            city = AddressPart.from_dict(_city)

        _city_district = d.pop("city_district", UNSET)
        city_district: AddressPart | Unset
        if isinstance(_city_district, Unset):
            city_district = UNSET
        else:
            city_district = AddressPart.from_dict(_city_district)

        _planning_structure = d.pop("planning_structure", UNSET)
        planning_structure: AddressPart | Unset
        if isinstance(_planning_structure, Unset):
            planning_structure = UNSET
        else:
            planning_structure = AddressPart.from_dict(_planning_structure)

        _settlement = d.pop("settlement", UNSET)
        settlement: AddressPart | Unset
        if isinstance(_settlement, Unset):
            settlement = UNSET
        else:
            settlement = AddressPart.from_dict(_settlement)

        administrative_division = cls(
            area=area,
            city=city,
            city_district=city_district,
            planning_structure=planning_structure,
            settlement=settlement,
        )

        administrative_division.additional_properties = d
        return administrative_division

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
