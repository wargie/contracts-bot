from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartyManagement")


@_attrs_define
class PartyManagement:
    """
    Attributes:
        disqualified (bool | None | Unset):
        name (None | str | Unset):
        post (None | str | Unset):
        start_date (int | None | Unset):
    """

    disqualified: bool | None | Unset = UNSET
    name: None | str | Unset = UNSET
    post: None | str | Unset = UNSET
    start_date: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disqualified: bool | None | Unset
        if isinstance(self.disqualified, Unset):
            disqualified = UNSET
        else:
            disqualified = self.disqualified

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        post: None | str | Unset
        if isinstance(self.post, Unset):
            post = UNSET
        else:
            post = self.post

        start_date: int | None | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disqualified is not UNSET:
            field_dict["disqualified"] = disqualified
        if name is not UNSET:
            field_dict["name"] = name
        if post is not UNSET:
            field_dict["post"] = post
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_disqualified(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        disqualified = _parse_disqualified(d.pop("disqualified", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_post(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post = _parse_post(d.pop("post", UNSET))

        def _parse_start_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        party_management = cls(
            disqualified=disqualified,
            name=name,
            post=post,
            start_date=start_date,
        )

        party_management.additional_properties = d
        return party_management

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
