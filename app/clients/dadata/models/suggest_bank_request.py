from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.suggest_bank_request_status_type_0_item import (
    SuggestBankRequestStatusType0Item,
)
from ..models.suggest_bank_request_type_type_0_item import (
    SuggestBankRequestTypeType0Item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_code import LocationCode


T = TypeVar("T", bound="SuggestBankRequest")


@_attrs_define
class SuggestBankRequest:
    """
    Attributes:
        query (str):
        count (int | None | Unset):  Default: 10.
        locations (list[LocationCode] | None | Unset):
        locations_boost (list[LocationCode] | None | Unset):
        status (list[SuggestBankRequestStatusType0Item] | None | Unset):
        type_ (list[SuggestBankRequestTypeType0Item] | None | Unset):
    """

    query: str
    count: int | None | Unset = 10
    locations: list[LocationCode] | None | Unset = UNSET
    locations_boost: list[LocationCode] | None | Unset = UNSET
    status: list[SuggestBankRequestStatusType0Item] | None | Unset = UNSET
    type_: list[SuggestBankRequestTypeType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        count: int | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        locations: list[dict[str, Any]] | None | Unset
        if isinstance(self.locations, Unset):
            locations = UNSET
        elif isinstance(self.locations, list):
            locations = []
            for locations_type_0_item_data in self.locations:
                locations_type_0_item = locations_type_0_item_data.to_dict()
                locations.append(locations_type_0_item)

        else:
            locations = self.locations

        locations_boost: list[dict[str, Any]] | None | Unset
        if isinstance(self.locations_boost, Unset):
            locations_boost = UNSET
        elif isinstance(self.locations_boost, list):
            locations_boost = []
            for locations_boost_type_0_item_data in self.locations_boost:
                locations_boost_type_0_item = locations_boost_type_0_item_data.to_dict()
                locations_boost.append(locations_boost_type_0_item)

        else:
            locations_boost = self.locations_boost

        status: list[str] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, list):
            status = []
            for status_type_0_item_data in self.status:
                status_type_0_item = status_type_0_item_data.value
                status.append(status_type_0_item)

        else:
            status = self.status

        type_: list[str] | None | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, list):
            type_ = []
            for type_type_0_item_data in self.type_:
                type_type_0_item = type_type_0_item_data.value
                type_.append(type_type_0_item)

        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count
        if locations is not UNSET:
            field_dict["locations"] = locations
        if locations_boost is not UNSET:
            field_dict["locations_boost"] = locations_boost
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_code import LocationCode

        d = dict(src_dict)
        query = d.pop("query")

        def _parse_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count = _parse_count(d.pop("count", UNSET))

        def _parse_locations(data: object) -> list[LocationCode] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                locations_type_0 = []
                _locations_type_0 = data
                for locations_type_0_item_data in _locations_type_0:
                    locations_type_0_item = LocationCode.from_dict(locations_type_0_item_data)

                    locations_type_0.append(locations_type_0_item)

                return locations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LocationCode] | None | Unset, data)

        locations = _parse_locations(d.pop("locations", UNSET))

        def _parse_locations_boost(data: object) -> list[LocationCode] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                locations_boost_type_0 = []
                _locations_boost_type_0 = data
                for locations_boost_type_0_item_data in _locations_boost_type_0:
                    locations_boost_type_0_item = LocationCode.from_dict(locations_boost_type_0_item_data)

                    locations_boost_type_0.append(locations_boost_type_0_item)

                return locations_boost_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LocationCode] | None | Unset, data)

        locations_boost = _parse_locations_boost(d.pop("locations_boost", UNSET))

        def _parse_status(
            data: object,
        ) -> list[SuggestBankRequestStatusType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                status_type_0 = []
                _status_type_0 = data
                for status_type_0_item_data in _status_type_0:
                    status_type_0_item = SuggestBankRequestStatusType0Item(status_type_0_item_data)

                    status_type_0.append(status_type_0_item)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SuggestBankRequestStatusType0Item] | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_type_(
            data: object,
        ) -> list[SuggestBankRequestTypeType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                type_type_0 = []
                _type_type_0 = data
                for type_type_0_item_data in _type_type_0:
                    type_type_0_item = SuggestBankRequestTypeType0Item(type_type_0_item_data)

                    type_type_0.append(type_type_0_item)

                return type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SuggestBankRequestTypeType0Item] | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        suggest_bank_request = cls(
            query=query,
            count=count,
            locations=locations,
            locations_boost=locations_boost,
            status=status,
            type_=type_,
        )

        suggest_bank_request.additional_properties = d
        return suggest_bank_request

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
