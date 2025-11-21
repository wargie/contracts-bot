from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartyLicense")


@_attrs_define
class PartyLicense:
    """
    Attributes:
        activities (list[str] | None | Unset):
        addresses (list[str] | None | Unset):
        issue_authority (None | str | Unset):
        issue_date (int | None | Unset):
        number (None | str | Unset):
        series (None | str | Unset):
        suspend_authority (None | str | Unset):
        suspend_date (int | None | Unset):
        valid_from (int | None | Unset):
        valid_to (int | None | Unset):
    """

    activities: list[str] | None | Unset = UNSET
    addresses: list[str] | None | Unset = UNSET
    issue_authority: None | str | Unset = UNSET
    issue_date: int | None | Unset = UNSET
    number: None | str | Unset = UNSET
    series: None | str | Unset = UNSET
    suspend_authority: None | str | Unset = UNSET
    suspend_date: int | None | Unset = UNSET
    valid_from: int | None | Unset = UNSET
    valid_to: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activities: list[str] | None | Unset
        if isinstance(self.activities, Unset):
            activities = UNSET
        elif isinstance(self.activities, list):
            activities = self.activities

        else:
            activities = self.activities

        addresses: list[str] | None | Unset
        if isinstance(self.addresses, Unset):
            addresses = UNSET
        elif isinstance(self.addresses, list):
            addresses = self.addresses

        else:
            addresses = self.addresses

        issue_authority: None | str | Unset
        if isinstance(self.issue_authority, Unset):
            issue_authority = UNSET
        else:
            issue_authority = self.issue_authority

        issue_date: int | None | Unset
        if isinstance(self.issue_date, Unset):
            issue_date = UNSET
        else:
            issue_date = self.issue_date

        number: None | str | Unset
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        series: None | str | Unset
        if isinstance(self.series, Unset):
            series = UNSET
        else:
            series = self.series

        suspend_authority: None | str | Unset
        if isinstance(self.suspend_authority, Unset):
            suspend_authority = UNSET
        else:
            suspend_authority = self.suspend_authority

        suspend_date: int | None | Unset
        if isinstance(self.suspend_date, Unset):
            suspend_date = UNSET
        else:
            suspend_date = self.suspend_date

        valid_from: int | None | Unset
        if isinstance(self.valid_from, Unset):
            valid_from = UNSET
        else:
            valid_from = self.valid_from

        valid_to: int | None | Unset
        if isinstance(self.valid_to, Unset):
            valid_to = UNSET
        else:
            valid_to = self.valid_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activities is not UNSET:
            field_dict["activities"] = activities
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if issue_authority is not UNSET:
            field_dict["issue_authority"] = issue_authority
        if issue_date is not UNSET:
            field_dict["issue_date"] = issue_date
        if number is not UNSET:
            field_dict["number"] = number
        if series is not UNSET:
            field_dict["series"] = series
        if suspend_authority is not UNSET:
            field_dict["suspend_authority"] = suspend_authority
        if suspend_date is not UNSET:
            field_dict["suspend_date"] = suspend_date
        if valid_from is not UNSET:
            field_dict["valid_from"] = valid_from
        if valid_to is not UNSET:
            field_dict["valid_to"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_activities(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                activities_type_0 = cast(list[str], data)

                return activities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        activities = _parse_activities(d.pop("activities", UNSET))

        def _parse_addresses(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                addresses_type_0 = cast(list[str], data)

                return addresses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        addresses = _parse_addresses(d.pop("addresses", UNSET))

        def _parse_issue_authority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issue_authority = _parse_issue_authority(d.pop("issue_authority", UNSET))

        def _parse_issue_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        issue_date = _parse_issue_date(d.pop("issue_date", UNSET))

        def _parse_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        number = _parse_number(d.pop("number", UNSET))

        def _parse_series(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        series = _parse_series(d.pop("series", UNSET))

        def _parse_suspend_authority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        suspend_authority = _parse_suspend_authority(d.pop("suspend_authority", UNSET))

        def _parse_suspend_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        suspend_date = _parse_suspend_date(d.pop("suspend_date", UNSET))

        def _parse_valid_from(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        valid_from = _parse_valid_from(d.pop("valid_from", UNSET))

        def _parse_valid_to(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        valid_to = _parse_valid_to(d.pop("valid_to", UNSET))

        party_license = cls(
            activities=activities,
            addresses=addresses,
            issue_authority=issue_authority,
            issue_date=issue_date,
            number=number,
            series=series,
            suspend_authority=suspend_authority,
            suspend_date=suspend_date,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        party_license.additional_properties = d
        return party_license

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
