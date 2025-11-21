from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.founder_share_type import FounderShareType

T = TypeVar("T", bound="DecimalFounderShare")


@_attrs_define
class DecimalFounderShare:
    """
    Attributes:
        type_ (FounderShareType):
        value (float | None):
    """

    type_: FounderShareType
    value: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        value: float | None
        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = FounderShareType(d.pop("type"))

        def _parse_value(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        value = _parse_value(d.pop("value"))

        decimal_founder_share = cls(
            type_=type_,
            value=value,
        )

        decimal_founder_share.additional_properties = d
        return decimal_founder_share

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
