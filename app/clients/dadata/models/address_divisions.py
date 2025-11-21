from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.administrative_division import AdministrativeDivision
    from ..models.municipal_division import MunicipalDivision


T = TypeVar("T", bound="AddressDivisions")


@_attrs_define
class AddressDivisions:
    """
    Attributes:
        administrative (AdministrativeDivision | Unset):
        municipal (MunicipalDivision | Unset):
    """

    administrative: AdministrativeDivision | Unset = UNSET
    municipal: MunicipalDivision | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        administrative: dict[str, Any] | Unset = UNSET
        if not isinstance(self.administrative, Unset):
            administrative = self.administrative.to_dict()

        municipal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.municipal, Unset):
            municipal = self.municipal.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if administrative is not UNSET:
            field_dict["administrative"] = administrative
        if municipal is not UNSET:
            field_dict["municipal"] = municipal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.administrative_division import AdministrativeDivision
        from ..models.municipal_division import MunicipalDivision

        d = dict(src_dict)
        _administrative = d.pop("administrative", UNSET)
        administrative: AdministrativeDivision | Unset
        if isinstance(_administrative, Unset):
            administrative = UNSET
        else:
            administrative = AdministrativeDivision.from_dict(_administrative)

        _municipal = d.pop("municipal", UNSET)
        municipal: MunicipalDivision | Unset
        if isinstance(_municipal, Unset):
            municipal = UNSET
        else:
            municipal = MunicipalDivision.from_dict(_municipal)

        address_divisions = cls(
            administrative=administrative,
            municipal=municipal,
        )

        address_divisions.additional_properties = d
        return address_divisions

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
