from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bound import Bound
    from ..models.location_code import LocationCode
    from ..models.location_fias import LocationFias


T = TypeVar("T", bound="SuggestFiasRequest")


@_attrs_define
class SuggestFiasRequest:
    """
    Attributes:
        query (str):
        count (int | None | Unset):  Default: 10.
        from_bound (Bound | Unset):
        locations (list[LocationFias] | None | Unset):
        locations_boost (list[LocationCode] | None | Unset):
        restrict_value (bool | None | Unset):  Default: False.
        to_bound (Bound | Unset):
    """

    query: str
    count: int | None | Unset = 10
    from_bound: Bound | Unset = UNSET
    locations: list[LocationFias] | None | Unset = UNSET
    locations_boost: list[LocationCode] | None | Unset = UNSET
    restrict_value: bool | None | Unset = False
    to_bound: Bound | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        count: int | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        from_bound: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_bound, Unset):
            from_bound = self.from_bound.to_dict()

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

        restrict_value: bool | None | Unset
        if isinstance(self.restrict_value, Unset):
            restrict_value = UNSET
        else:
            restrict_value = self.restrict_value

        to_bound: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_bound, Unset):
            to_bound = self.to_bound.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count
        if from_bound is not UNSET:
            field_dict["from_bound"] = from_bound
        if locations is not UNSET:
            field_dict["locations"] = locations
        if locations_boost is not UNSET:
            field_dict["locations_boost"] = locations_boost
        if restrict_value is not UNSET:
            field_dict["restrict_value"] = restrict_value
        if to_bound is not UNSET:
            field_dict["to_bound"] = to_bound

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bound import Bound
        from ..models.location_code import LocationCode
        from ..models.location_fias import LocationFias

        d = dict(src_dict)
        query = d.pop("query")

        def _parse_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count = _parse_count(d.pop("count", UNSET))

        _from_bound = d.pop("from_bound", UNSET)
        from_bound: Bound | Unset
        if isinstance(_from_bound, Unset):
            from_bound = UNSET
        else:
            from_bound = Bound.from_dict(_from_bound)

        def _parse_locations(data: object) -> list[LocationFias] | None | Unset:
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
                    locations_type_0_item = LocationFias.from_dict(locations_type_0_item_data)

                    locations_type_0.append(locations_type_0_item)

                return locations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LocationFias] | None | Unset, data)

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

        def _parse_restrict_value(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        restrict_value = _parse_restrict_value(d.pop("restrict_value", UNSET))

        _to_bound = d.pop("to_bound", UNSET)
        to_bound: Bound | Unset
        if isinstance(_to_bound, Unset):
            to_bound = UNSET
        else:
            to_bound = Bound.from_dict(_to_bound)

        suggest_fias_request = cls(
            query=query,
            count=count,
            from_bound=from_bound,
            locations=locations,
            locations_boost=locations_boost,
            restrict_value=restrict_value,
            to_bound=to_bound,
        )

        suggest_fias_request.additional_properties = d
        return suggest_fias_request

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
