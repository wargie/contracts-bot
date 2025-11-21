from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationGeo")


@_attrs_define
class LocationGeo:
    """
    Attributes:
        lat (float | None | Unset):
        lon (float | None | Unset):
        radius_meters (float | None | Unset):
    """

    lat: float | None | Unset = UNSET
    lon: float | None | Unset = UNSET
    radius_meters: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lat: float | None | Unset
        if isinstance(self.lat, Unset):
            lat = UNSET
        else:
            lat = self.lat

        lon: float | None | Unset
        if isinstance(self.lon, Unset):
            lon = UNSET
        else:
            lon = self.lon

        radius_meters: float | None | Unset
        if isinstance(self.radius_meters, Unset):
            radius_meters = UNSET
        else:
            radius_meters = self.radius_meters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lon is not UNSET:
            field_dict["lon"] = lon
        if radius_meters is not UNSET:
            field_dict["radius_meters"] = radius_meters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_lat(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lat = _parse_lat(d.pop("lat", UNSET))

        def _parse_lon(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lon = _parse_lon(d.pop("lon", UNSET))

        def _parse_radius_meters(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        radius_meters = _parse_radius_meters(d.pop("radius_meters", UNSET))

        location_geo = cls(
            lat=lat,
            lon=lon,
            radius_meters=radius_meters,
        )

        location_geo.additional_properties = d
        return location_geo

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
