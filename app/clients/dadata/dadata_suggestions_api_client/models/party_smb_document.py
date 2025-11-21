from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.party_smb_document_category import PartySmbDocumentCategory
from ..models.party_smb_document_type import PartySmbDocumentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PartySmbDocument")


@_attrs_define
class PartySmbDocument:
    """
    Attributes:
        category (PartySmbDocumentCategory):
        type_ (PartySmbDocumentType):
        issue_authority (None | str | Unset):
        issue_date (int | None | Unset):
        number (None | str | Unset):
        series (None | str | Unset):
    """

    category: PartySmbDocumentCategory
    type_: PartySmbDocumentType
    issue_authority: None | str | Unset = UNSET
    issue_date: int | None | Unset = UNSET
    number: None | str | Unset = UNSET
    series: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        type_ = self.type_.value

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "type": type_,
            }
        )
        if issue_authority is not UNSET:
            field_dict["issue_authority"] = issue_authority
        if issue_date is not UNSET:
            field_dict["issue_date"] = issue_date
        if number is not UNSET:
            field_dict["number"] = number
        if series is not UNSET:
            field_dict["series"] = series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = PartySmbDocumentCategory(d.pop("category"))

        type_ = PartySmbDocumentType(d.pop("type"))

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

        party_smb_document = cls(
            category=category,
            type_=type_,
            issue_authority=issue_authority,
            issue_date=issue_date,
            number=number,
            series=series,
        )

        party_smb_document.additional_properties = d
        return party_smb_document

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
