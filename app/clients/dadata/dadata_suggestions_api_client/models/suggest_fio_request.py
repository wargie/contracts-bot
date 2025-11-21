from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.suggest_fio_request_gender import SuggestFioRequestGender
from ..models.suggest_fio_request_parts_type_0_item import SuggestFioRequestPartsType0Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="SuggestFioRequest")


@_attrs_define
class SuggestFioRequest:
    """
    Attributes:
        query (str):
        count (int | None | Unset):  Default: 10.
        gender (SuggestFioRequestGender | Unset):  Default: SuggestFioRequestGender.UNKNOWN.
        parts (list[SuggestFioRequestPartsType0Item] | None | Unset):
    """

    query: str
    count: int | None | Unset = 10
    gender: SuggestFioRequestGender | Unset = SuggestFioRequestGender.UNKNOWN
    parts: list[SuggestFioRequestPartsType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        count: int | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        gender: str | Unset = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        parts: list[str] | None | Unset
        if isinstance(self.parts, Unset):
            parts = UNSET
        elif isinstance(self.parts, list):
            parts = []
            for parts_type_0_item_data in self.parts:
                parts_type_0_item = parts_type_0_item_data.value
                parts.append(parts_type_0_item)

        else:
            parts = self.parts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count
        if gender is not UNSET:
            field_dict["gender"] = gender
        if parts is not UNSET:
            field_dict["parts"] = parts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        def _parse_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count = _parse_count(d.pop("count", UNSET))

        _gender = d.pop("gender", UNSET)
        gender: SuggestFioRequestGender | Unset
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = SuggestFioRequestGender(_gender)

        def _parse_parts(data: object) -> list[SuggestFioRequestPartsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                parts_type_0 = []
                _parts_type_0 = data
                for parts_type_0_item_data in _parts_type_0:
                    parts_type_0_item = SuggestFioRequestPartsType0Item(parts_type_0_item_data)

                    parts_type_0.append(parts_type_0_item)

                return parts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SuggestFioRequestPartsType0Item] | None | Unset, data)

        parts = _parse_parts(d.pop("parts", UNSET))

        suggest_fio_request = cls(
            query=query,
            count=count,
            gender=gender,
            parts=parts,
        )

        suggest_fio_request.additional_properties = d
        return suggest_fio_request

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
