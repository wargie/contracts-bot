from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_part import AddressPart


T = TypeVar("T", bound="MunicipalDivision")


@_attrs_define
class MunicipalDivision:
    """
    Attributes:
        area (AddressPart | Unset):
        city (AddressPart | Unset):
        planning_structure (AddressPart | Unset):
        settlement (AddressPart | Unset):
        sub_area (AddressPart | Unset):
    """

    area: AddressPart | Unset = UNSET
    city: AddressPart | Unset = UNSET
    planning_structure: AddressPart | Unset = UNSET
    settlement: AddressPart | Unset = UNSET
    sub_area: AddressPart | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        area: dict[str, Any] | Unset = UNSET
        if not isinstance(self.area, Unset):
            area = self.area.to_dict()

        city: dict[str, Any] | Unset = UNSET
        if not isinstance(self.city, Unset):
            city = self.city.to_dict()

        planning_structure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.planning_structure, Unset):
            planning_structure = self.planning_structure.to_dict()

        settlement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settlement, Unset):
            settlement = self.settlement.to_dict()

        sub_area: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sub_area, Unset):
            sub_area = self.sub_area.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if area is not UNSET:
            field_dict["area"] = area
        if city is not UNSET:
            field_dict["city"] = city
        if planning_structure is not UNSET:
            field_dict["planning_structure"] = planning_structure
        if settlement is not UNSET:
            field_dict["settlement"] = settlement
        if sub_area is not UNSET:
            field_dict["sub_area"] = sub_area

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

        _sub_area = d.pop("sub_area", UNSET)
        sub_area: AddressPart | Unset
        if isinstance(_sub_area, Unset):
            sub_area = UNSET
        else:
            sub_area = AddressPart.from_dict(_sub_area)

        municipal_division = cls(
            area=area,
            city=city,
            planning_structure=planning_structure,
            settlement=settlement,
            sub_area=sub_area,
        )

        municipal_division.additional_properties = d
        return municipal_division

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
