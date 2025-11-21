from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.suggestion_address import SuggestionAddress


T = TypeVar("T", bound="DetectAddressResponse")


@_attrs_define
class DetectAddressResponse:
    """
    Attributes:
        location (SuggestionAddress | Unset):
    """

    location: SuggestionAddress | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.suggestion_address import SuggestionAddress

        d = dict(src_dict)
        _location = d.pop("location", UNSET)
        location: SuggestionAddress | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = SuggestionAddress.from_dict(_location)

        detect_address_response = cls(
            location=location,
        )

        detect_address_response.additional_properties = d
        return detect_address_response

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
