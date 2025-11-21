from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.geo_locate_address_request_division import GeoLocateAddressRequestDivision
from ..models.geo_locate_address_request_language import GeoLocateAddressRequestLanguage
from ..types import UNSET, Unset

T = TypeVar("T", bound="GeoLocateAddressRequest")


@_attrs_define
class GeoLocateAddressRequest:
    """
    Attributes:
        count (int | None | Unset):  Default: 10.
        division (GeoLocateAddressRequestDivision | Unset):
        language (GeoLocateAddressRequestLanguage | Unset):
        lat (float | None | Unset):
        lon (float | None | Unset):
        radius_meters (float | None | Unset):
    """

    count: int | None | Unset = 10
    division: GeoLocateAddressRequestDivision | Unset = UNSET
    language: GeoLocateAddressRequestLanguage | Unset = UNSET
    lat: float | None | Unset = UNSET
    lon: float | None | Unset = UNSET
    radius_meters: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count: int | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        division: str | Unset = UNSET
        if not isinstance(self.division, Unset):
            division = self.division.value

        language: str | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

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
        if count is not UNSET:
            field_dict["count"] = count
        if division is not UNSET:
            field_dict["division"] = division
        if language is not UNSET:
            field_dict["language"] = language
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

        def _parse_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count = _parse_count(d.pop("count", UNSET))

        _division = d.pop("division", UNSET)
        division: GeoLocateAddressRequestDivision | Unset
        if isinstance(_division, Unset):
            division = UNSET
        else:
            division = GeoLocateAddressRequestDivision(_division)

        _language = d.pop("language", UNSET)
        language: GeoLocateAddressRequestLanguage | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = GeoLocateAddressRequestLanguage(_language)

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

        geo_locate_address_request = cls(
            count=count,
            division=division,
            language=language,
            lat=lat,
            lon=lon,
            radius_meters=radius_meters,
        )

        geo_locate_address_request.additional_properties = d
        return geo_locate_address_request

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
