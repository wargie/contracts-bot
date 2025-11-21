from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationAddress")


@_attrs_define
class LocationAddress:
    """
    Attributes:
        area (None | str | Unset):
        area_fias_id (None | str | Unset):
        area_type_full (None | str | Unset):
        city (None | str | Unset):
        city_district (None | str | Unset):
        city_district_fias_id (None | str | Unset):
        city_district_type_full (None | str | Unset):
        city_fias_id (None | str | Unset):
        city_type_full (None | str | Unset):
        country (None | str | Unset):
        country_iso_code (None | str | Unset):
        fias_id (None | str | Unset):
        kladr_id (None | str | Unset):
        postal_code (None | str | Unset):
        region (None | str | Unset):
        region_fias_id (None | str | Unset):
        region_iso_code (None | str | Unset):
        region_type_full (None | str | Unset):
        settlement (None | str | Unset):
        settlement_fias_id (None | str | Unset):
        settlement_type_full (None | str | Unset):
        street (None | str | Unset):
        street_fias_id (None | str | Unset):
        street_type_full (None | str | Unset):
        sub_area (None | str | Unset):
        sub_area_fias_id (None | str | Unset):
        sub_area_type_full (None | str | Unset):
    """

    area: None | str | Unset = UNSET
    area_fias_id: None | str | Unset = UNSET
    area_type_full: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    city_district: None | str | Unset = UNSET
    city_district_fias_id: None | str | Unset = UNSET
    city_district_type_full: None | str | Unset = UNSET
    city_fias_id: None | str | Unset = UNSET
    city_type_full: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    country_iso_code: None | str | Unset = UNSET
    fias_id: None | str | Unset = UNSET
    kladr_id: None | str | Unset = UNSET
    postal_code: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    region_fias_id: None | str | Unset = UNSET
    region_iso_code: None | str | Unset = UNSET
    region_type_full: None | str | Unset = UNSET
    settlement: None | str | Unset = UNSET
    settlement_fias_id: None | str | Unset = UNSET
    settlement_type_full: None | str | Unset = UNSET
    street: None | str | Unset = UNSET
    street_fias_id: None | str | Unset = UNSET
    street_type_full: None | str | Unset = UNSET
    sub_area: None | str | Unset = UNSET
    sub_area_fias_id: None | str | Unset = UNSET
    sub_area_type_full: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        area: None | str | Unset
        if isinstance(self.area, Unset):
            area = UNSET
        else:
            area = self.area

        area_fias_id: None | str | Unset
        if isinstance(self.area_fias_id, Unset):
            area_fias_id = UNSET
        else:
            area_fias_id = self.area_fias_id

        area_type_full: None | str | Unset
        if isinstance(self.area_type_full, Unset):
            area_type_full = UNSET
        else:
            area_type_full = self.area_type_full

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        city_district: None | str | Unset
        if isinstance(self.city_district, Unset):
            city_district = UNSET
        else:
            city_district = self.city_district

        city_district_fias_id: None | str | Unset
        if isinstance(self.city_district_fias_id, Unset):
            city_district_fias_id = UNSET
        else:
            city_district_fias_id = self.city_district_fias_id

        city_district_type_full: None | str | Unset
        if isinstance(self.city_district_type_full, Unset):
            city_district_type_full = UNSET
        else:
            city_district_type_full = self.city_district_type_full

        city_fias_id: None | str | Unset
        if isinstance(self.city_fias_id, Unset):
            city_fias_id = UNSET
        else:
            city_fias_id = self.city_fias_id

        city_type_full: None | str | Unset
        if isinstance(self.city_type_full, Unset):
            city_type_full = UNSET
        else:
            city_type_full = self.city_type_full

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        country_iso_code: None | str | Unset
        if isinstance(self.country_iso_code, Unset):
            country_iso_code = UNSET
        else:
            country_iso_code = self.country_iso_code

        fias_id: None | str | Unset
        if isinstance(self.fias_id, Unset):
            fias_id = UNSET
        else:
            fias_id = self.fias_id

        kladr_id: None | str | Unset
        if isinstance(self.kladr_id, Unset):
            kladr_id = UNSET
        else:
            kladr_id = self.kladr_id

        postal_code: None | str | Unset
        if isinstance(self.postal_code, Unset):
            postal_code = UNSET
        else:
            postal_code = self.postal_code

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        region_fias_id: None | str | Unset
        if isinstance(self.region_fias_id, Unset):
            region_fias_id = UNSET
        else:
            region_fias_id = self.region_fias_id

        region_iso_code: None | str | Unset
        if isinstance(self.region_iso_code, Unset):
            region_iso_code = UNSET
        else:
            region_iso_code = self.region_iso_code

        region_type_full: None | str | Unset
        if isinstance(self.region_type_full, Unset):
            region_type_full = UNSET
        else:
            region_type_full = self.region_type_full

        settlement: None | str | Unset
        if isinstance(self.settlement, Unset):
            settlement = UNSET
        else:
            settlement = self.settlement

        settlement_fias_id: None | str | Unset
        if isinstance(self.settlement_fias_id, Unset):
            settlement_fias_id = UNSET
        else:
            settlement_fias_id = self.settlement_fias_id

        settlement_type_full: None | str | Unset
        if isinstance(self.settlement_type_full, Unset):
            settlement_type_full = UNSET
        else:
            settlement_type_full = self.settlement_type_full

        street: None | str | Unset
        if isinstance(self.street, Unset):
            street = UNSET
        else:
            street = self.street

        street_fias_id: None | str | Unset
        if isinstance(self.street_fias_id, Unset):
            street_fias_id = UNSET
        else:
            street_fias_id = self.street_fias_id

        street_type_full: None | str | Unset
        if isinstance(self.street_type_full, Unset):
            street_type_full = UNSET
        else:
            street_type_full = self.street_type_full

        sub_area: None | str | Unset
        if isinstance(self.sub_area, Unset):
            sub_area = UNSET
        else:
            sub_area = self.sub_area

        sub_area_fias_id: None | str | Unset
        if isinstance(self.sub_area_fias_id, Unset):
            sub_area_fias_id = UNSET
        else:
            sub_area_fias_id = self.sub_area_fias_id

        sub_area_type_full: None | str | Unset
        if isinstance(self.sub_area_type_full, Unset):
            sub_area_type_full = UNSET
        else:
            sub_area_type_full = self.sub_area_type_full

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if area is not UNSET:
            field_dict["area"] = area
        if area_fias_id is not UNSET:
            field_dict["area_fias_id"] = area_fias_id
        if area_type_full is not UNSET:
            field_dict["area_type_full"] = area_type_full
        if city is not UNSET:
            field_dict["city"] = city
        if city_district is not UNSET:
            field_dict["city_district"] = city_district
        if city_district_fias_id is not UNSET:
            field_dict["city_district_fias_id"] = city_district_fias_id
        if city_district_type_full is not UNSET:
            field_dict["city_district_type_full"] = city_district_type_full
        if city_fias_id is not UNSET:
            field_dict["city_fias_id"] = city_fias_id
        if city_type_full is not UNSET:
            field_dict["city_type_full"] = city_type_full
        if country is not UNSET:
            field_dict["country"] = country
        if country_iso_code is not UNSET:
            field_dict["country_iso_code"] = country_iso_code
        if fias_id is not UNSET:
            field_dict["fias_id"] = fias_id
        if kladr_id is not UNSET:
            field_dict["kladr_id"] = kladr_id
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if region is not UNSET:
            field_dict["region"] = region
        if region_fias_id is not UNSET:
            field_dict["region_fias_id"] = region_fias_id
        if region_iso_code is not UNSET:
            field_dict["region_iso_code"] = region_iso_code
        if region_type_full is not UNSET:
            field_dict["region_type_full"] = region_type_full
        if settlement is not UNSET:
            field_dict["settlement"] = settlement
        if settlement_fias_id is not UNSET:
            field_dict["settlement_fias_id"] = settlement_fias_id
        if settlement_type_full is not UNSET:
            field_dict["settlement_type_full"] = settlement_type_full
        if street is not UNSET:
            field_dict["street"] = street
        if street_fias_id is not UNSET:
            field_dict["street_fias_id"] = street_fias_id
        if street_type_full is not UNSET:
            field_dict["street_type_full"] = street_type_full
        if sub_area is not UNSET:
            field_dict["sub_area"] = sub_area
        if sub_area_fias_id is not UNSET:
            field_dict["sub_area_fias_id"] = sub_area_fias_id
        if sub_area_type_full is not UNSET:
            field_dict["sub_area_type_full"] = sub_area_type_full

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_area(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area = _parse_area(d.pop("area", UNSET))

        def _parse_area_fias_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_fias_id = _parse_area_fias_id(d.pop("area_fias_id", UNSET))

        def _parse_area_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_type_full = _parse_area_type_full(d.pop("area_type_full", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_city_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city_district = _parse_city_district(d.pop("city_district", UNSET))

        def _parse_city_district_fias_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city_district_fias_id = _parse_city_district_fias_id(d.pop("city_district_fias_id", UNSET))

        def _parse_city_district_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city_district_type_full = _parse_city_district_type_full(d.pop("city_district_type_full", UNSET))

        def _parse_city_fias_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city_fias_id = _parse_city_fias_id(d.pop("city_fias_id", UNSET))

        def _parse_city_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city_type_full = _parse_city_type_full(d.pop("city_type_full", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_country_iso_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_iso_code = _parse_country_iso_code(d.pop("country_iso_code", UNSET))

        def _parse_fias_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fias_id = _parse_fias_id(d.pop("fias_id", UNSET))

        def _parse_kladr_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kladr_id = _parse_kladr_id(d.pop("kladr_id", UNSET))

        def _parse_postal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postal_code = _parse_postal_code(d.pop("postal_code", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_region_fias_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_fias_id = _parse_region_fias_id(d.pop("region_fias_id", UNSET))

        def _parse_region_iso_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_iso_code = _parse_region_iso_code(d.pop("region_iso_code", UNSET))

        def _parse_region_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_type_full = _parse_region_type_full(d.pop("region_type_full", UNSET))

        def _parse_settlement(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        settlement = _parse_settlement(d.pop("settlement", UNSET))

        def _parse_settlement_fias_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        settlement_fias_id = _parse_settlement_fias_id(d.pop("settlement_fias_id", UNSET))

        def _parse_settlement_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        settlement_type_full = _parse_settlement_type_full(d.pop("settlement_type_full", UNSET))

        def _parse_street(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street = _parse_street(d.pop("street", UNSET))

        def _parse_street_fias_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_fias_id = _parse_street_fias_id(d.pop("street_fias_id", UNSET))

        def _parse_street_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_type_full = _parse_street_type_full(d.pop("street_type_full", UNSET))

        def _parse_sub_area(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_area = _parse_sub_area(d.pop("sub_area", UNSET))

        def _parse_sub_area_fias_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_area_fias_id = _parse_sub_area_fias_id(d.pop("sub_area_fias_id", UNSET))

        def _parse_sub_area_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_area_type_full = _parse_sub_area_type_full(d.pop("sub_area_type_full", UNSET))

        location_address = cls(
            area=area,
            area_fias_id=area_fias_id,
            area_type_full=area_type_full,
            city=city,
            city_district=city_district,
            city_district_fias_id=city_district_fias_id,
            city_district_type_full=city_district_type_full,
            city_fias_id=city_fias_id,
            city_type_full=city_type_full,
            country=country,
            country_iso_code=country_iso_code,
            fias_id=fias_id,
            kladr_id=kladr_id,
            postal_code=postal_code,
            region=region,
            region_fias_id=region_fias_id,
            region_iso_code=region_iso_code,
            region_type_full=region_type_full,
            settlement=settlement,
            settlement_fias_id=settlement_fias_id,
            settlement_type_full=settlement_type_full,
            street=street,
            street_fias_id=street_fias_id,
            street_type_full=street_type_full,
            sub_area=sub_area,
            sub_area_fias_id=sub_area_fias_id,
            sub_area_type_full=sub_area_type_full,
        )

        location_address.additional_properties = d
        return location_address

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
