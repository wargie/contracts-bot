from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartyCourtDecision")


@_attrs_define
class PartyCourtDecision:
    """
    Attributes:
        number (str):
        court_name (str | Unset):
        date (int | None | Unset):
    """

    number: str
    court_name: str | Unset = UNSET
    date: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        court_name = self.court_name

        date: int | None | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
            }
        )
        if court_name is not UNSET:
            field_dict["court_name"] = court_name
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number = d.pop("number")

        court_name = d.pop("court_name", UNSET)

        def _parse_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        party_court_decision = cls(
            number=number,
            court_name=court_name,
            date=date,
        )

        party_court_decision.additional_properties = d
        return party_court_decision

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
