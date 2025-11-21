from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.suggest_outward_request_filters_type_0_item import SuggestOutwardRequestFiltersType0Item


T = TypeVar("T", bound="SuggestOutwardRequest")


@_attrs_define
class SuggestOutwardRequest:
    """
    Attributes:
        query (str):
        count (int | None | Unset):  Default: 10.
        filters (list[SuggestOutwardRequestFiltersType0Item] | None | Unset):
    """

    query: str
    count: int | None | Unset = 10
    filters: list[SuggestOutwardRequestFiltersType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        count: int | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        filters: list[dict[str, Any]] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, list):
            filters = []
            for filters_type_0_item_data in self.filters:
                filters_type_0_item = filters_type_0_item_data.to_dict()
                filters.append(filters_type_0_item)

        else:
            filters = self.filters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.suggest_outward_request_filters_type_0_item import SuggestOutwardRequestFiltersType0Item

        d = dict(src_dict)
        query = d.pop("query")

        def _parse_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count = _parse_count(d.pop("count", UNSET))

        def _parse_filters(data: object) -> list[SuggestOutwardRequestFiltersType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filters_type_0 = []
                _filters_type_0 = data
                for filters_type_0_item_data in _filters_type_0:
                    filters_type_0_item = SuggestOutwardRequestFiltersType0Item.from_dict(filters_type_0_item_data)

                    filters_type_0.append(filters_type_0_item)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SuggestOutwardRequestFiltersType0Item] | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        suggest_outward_request = cls(
            query=query,
            count=count,
            filters=filters,
        )

        suggest_outward_request.additional_properties = d
        return suggest_outward_request

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
