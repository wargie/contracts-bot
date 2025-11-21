from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_custom_type_0_item import AddressCustomType0Item
    from ..models.address_divisions import AddressDivisions
    from ..models.metro import Metro


T = TypeVar("T", bound="Address")


@_attrs_define
class Address:
    """
    Attributes:
        area (None | str | Unset):
        area_fias_id (None | str | Unset):
        area_kladr_id (None | str | Unset):
        area_type (None | str | Unset):
        area_type_full (None | str | Unset):
        area_with_type (None | str | Unset):
        beltway_distance (None | str | Unset):
        beltway_hit (None | str | Unset):
        block (None | str | Unset):
        block_type (None | str | Unset):
        block_type_full (None | str | Unset):
        capital_marker (None | str | Unset):
        city (None | str | Unset):
        city_area (None | str | Unset):
        city_district (None | str | Unset):
        city_district_fias_id (None | str | Unset):
        city_district_kladr_id (None | str | Unset):
        city_district_type (None | str | Unset):
        city_district_type_full (None | str | Unset):
        city_district_with_type (None | str | Unset):
        city_fias_id (None | str | Unset):
        city_kladr_id (None | str | Unset):
        city_type (None | str | Unset):
        city_type_full (None | str | Unset):
        city_with_type (None | str | Unset):
        country (None | str | Unset):
        country_iso_code (None | str | Unset):
        custom (list[AddressCustomType0Item] | None | Unset):
        divisions (AddressDivisions | Unset):
        entrance (None | str | Unset):
        federal_district (None | str | Unset):
        fias_actuality_state (None | str | Unset):
        fias_code (None | str | Unset):
        fias_id (None | str | Unset):
        fias_level (None | str | Unset):
        flat (None | str | Unset):
        flat_area (None | str | Unset):
        flat_cadnum (None | str | Unset):
        flat_fias_id (None | str | Unset):
        flat_price (None | str | Unset):
        flat_type (None | str | Unset):
        flat_type_full (None | str | Unset):
        floor (None | str | Unset):
        geo_lat (None | str | Unset):
        geo_lon (None | str | Unset):
        geoname_id (None | str | Unset):
        history_values (list[str] | None | Unset):
        house (None | str | Unset):
        house_cadnum (None | str | Unset):
        house_fias_id (None | str | Unset):
        house_flat_count (None | str | Unset):
        house_kladr_id (None | str | Unset):
        house_type (None | str | Unset):
        house_type_full (None | str | Unset):
        kladr_id (None | str | Unset):
        metro (list[Metro] | None | Unset):
        okato (None | str | Unset):
        oktmo (None | str | Unset):
        postal_box (None | str | Unset):
        postal_code (None | str | Unset):
        qc (None | str | Unset):
        qc_complete (None | str | Unset):
        qc_geo (None | str | Unset):
        qc_house (None | str | Unset):
        region (None | str | Unset):
        region_fias_id (None | str | Unset):
        region_iso_code (None | str | Unset):
        region_kladr_id (None | str | Unset):
        region_type (None | str | Unset):
        region_type_full (None | str | Unset):
        region_with_type (None | str | Unset):
        room (None | str | Unset):
        room_cadnum (None | str | Unset):
        room_fias_id (None | str | Unset):
        room_type (None | str | Unset):
        room_type_full (None | str | Unset):
        settlement (None | str | Unset):
        settlement_fias_id (None | str | Unset):
        settlement_kladr_id (None | str | Unset):
        settlement_type (None | str | Unset):
        settlement_type_full (None | str | Unset):
        settlement_with_type (None | str | Unset):
        source (None | str | Unset):
        square_meter_price (None | str | Unset):
        stead (None | str | Unset):
        stead_cadnum (None | str | Unset):
        stead_fias_id (None | str | Unset):
        stead_type (None | str | Unset):
        stead_type_full (None | str | Unset):
        street (None | str | Unset):
        street_fias_id (None | str | Unset):
        street_kladr_id (None | str | Unset):
        street_type (None | str | Unset):
        street_type_full (None | str | Unset):
        street_with_type (None | str | Unset):
        sub_area (None | str | Unset):
        sub_area_fias_id (None | str | Unset):
        sub_area_kladr_id (None | str | Unset):
        sub_area_type (None | str | Unset):
        sub_area_type_full (None | str | Unset):
        sub_area_with_type (None | str | Unset):
        tax_office (None | str | Unset):
        tax_office_legal (None | str | Unset):
        timezone (None | str | Unset):
        unparsed_parts (None | str | Unset):
    """

    area: None | str | Unset = UNSET
    area_fias_id: None | str | Unset = UNSET
    area_kladr_id: None | str | Unset = UNSET
    area_type: None | str | Unset = UNSET
    area_type_full: None | str | Unset = UNSET
    area_with_type: None | str | Unset = UNSET
    beltway_distance: None | str | Unset = UNSET
    beltway_hit: None | str | Unset = UNSET
    block: None | str | Unset = UNSET
    block_type: None | str | Unset = UNSET
    block_type_full: None | str | Unset = UNSET
    capital_marker: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    city_area: None | str | Unset = UNSET
    city_district: None | str | Unset = UNSET
    city_district_fias_id: None | str | Unset = UNSET
    city_district_kladr_id: None | str | Unset = UNSET
    city_district_type: None | str | Unset = UNSET
    city_district_type_full: None | str | Unset = UNSET
    city_district_with_type: None | str | Unset = UNSET
    city_fias_id: None | str | Unset = UNSET
    city_kladr_id: None | str | Unset = UNSET
    city_type: None | str | Unset = UNSET
    city_type_full: None | str | Unset = UNSET
    city_with_type: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    country_iso_code: None | str | Unset = UNSET
    custom: list[AddressCustomType0Item] | None | Unset = UNSET
    divisions: AddressDivisions | Unset = UNSET
    entrance: None | str | Unset = UNSET
    federal_district: None | str | Unset = UNSET
    fias_actuality_state: None | str | Unset = UNSET
    fias_code: None | str | Unset = UNSET
    fias_id: None | str | Unset = UNSET
    fias_level: None | str | Unset = UNSET
    flat: None | str | Unset = UNSET
    flat_area: None | str | Unset = UNSET
    flat_cadnum: None | str | Unset = UNSET
    flat_fias_id: None | str | Unset = UNSET
    flat_price: None | str | Unset = UNSET
    flat_type: None | str | Unset = UNSET
    flat_type_full: None | str | Unset = UNSET
    floor: None | str | Unset = UNSET
    geo_lat: None | str | Unset = UNSET
    geo_lon: None | str | Unset = UNSET
    geoname_id: None | str | Unset = UNSET
    history_values: list[str] | None | Unset = UNSET
    house: None | str | Unset = UNSET
    house_cadnum: None | str | Unset = UNSET
    house_fias_id: None | str | Unset = UNSET
    house_flat_count: None | str | Unset = UNSET
    house_kladr_id: None | str | Unset = UNSET
    house_type: None | str | Unset = UNSET
    house_type_full: None | str | Unset = UNSET
    kladr_id: None | str | Unset = UNSET
    metro: list[Metro] | None | Unset = UNSET
    okato: None | str | Unset = UNSET
    oktmo: None | str | Unset = UNSET
    postal_box: None | str | Unset = UNSET
    postal_code: None | str | Unset = UNSET
    qc: None | str | Unset = UNSET
    qc_complete: None | str | Unset = UNSET
    qc_geo: None | str | Unset = UNSET
    qc_house: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    region_fias_id: None | str | Unset = UNSET
    region_iso_code: None | str | Unset = UNSET
    region_kladr_id: None | str | Unset = UNSET
    region_type: None | str | Unset = UNSET
    region_type_full: None | str | Unset = UNSET
    region_with_type: None | str | Unset = UNSET
    room: None | str | Unset = UNSET
    room_cadnum: None | str | Unset = UNSET
    room_fias_id: None | str | Unset = UNSET
    room_type: None | str | Unset = UNSET
    room_type_full: None | str | Unset = UNSET
    settlement: None | str | Unset = UNSET
    settlement_fias_id: None | str | Unset = UNSET
    settlement_kladr_id: None | str | Unset = UNSET
    settlement_type: None | str | Unset = UNSET
    settlement_type_full: None | str | Unset = UNSET
    settlement_with_type: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    square_meter_price: None | str | Unset = UNSET
    stead: None | str | Unset = UNSET
    stead_cadnum: None | str | Unset = UNSET
    stead_fias_id: None | str | Unset = UNSET
    stead_type: None | str | Unset = UNSET
    stead_type_full: None | str | Unset = UNSET
    street: None | str | Unset = UNSET
    street_fias_id: None | str | Unset = UNSET
    street_kladr_id: None | str | Unset = UNSET
    street_type: None | str | Unset = UNSET
    street_type_full: None | str | Unset = UNSET
    street_with_type: None | str | Unset = UNSET
    sub_area: None | str | Unset = UNSET
    sub_area_fias_id: None | str | Unset = UNSET
    sub_area_kladr_id: None | str | Unset = UNSET
    sub_area_type: None | str | Unset = UNSET
    sub_area_type_full: None | str | Unset = UNSET
    sub_area_with_type: None | str | Unset = UNSET
    tax_office: None | str | Unset = UNSET
    tax_office_legal: None | str | Unset = UNSET
    timezone: None | str | Unset = UNSET
    unparsed_parts: None | str | Unset = UNSET
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

        area_kladr_id: None | str | Unset
        if isinstance(self.area_kladr_id, Unset):
            area_kladr_id = UNSET
        else:
            area_kladr_id = self.area_kladr_id

        area_type: None | str | Unset
        if isinstance(self.area_type, Unset):
            area_type = UNSET
        else:
            area_type = self.area_type

        area_type_full: None | str | Unset
        if isinstance(self.area_type_full, Unset):
            area_type_full = UNSET
        else:
            area_type_full = self.area_type_full

        area_with_type: None | str | Unset
        if isinstance(self.area_with_type, Unset):
            area_with_type = UNSET
        else:
            area_with_type = self.area_with_type

        beltway_distance: None | str | Unset
        if isinstance(self.beltway_distance, Unset):
            beltway_distance = UNSET
        else:
            beltway_distance = self.beltway_distance

        beltway_hit: None | str | Unset
        if isinstance(self.beltway_hit, Unset):
            beltway_hit = UNSET
        else:
            beltway_hit = self.beltway_hit

        block: None | str | Unset
        if isinstance(self.block, Unset):
            block = UNSET
        else:
            block = self.block

        block_type: None | str | Unset
        if isinstance(self.block_type, Unset):
            block_type = UNSET
        else:
            block_type = self.block_type

        block_type_full: None | str | Unset
        if isinstance(self.block_type_full, Unset):
            block_type_full = UNSET
        else:
            block_type_full = self.block_type_full

        capital_marker: None | str | Unset
        if isinstance(self.capital_marker, Unset):
            capital_marker = UNSET
        else:
            capital_marker = self.capital_marker

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        city_area: None | str | Unset
        if isinstance(self.city_area, Unset):
            city_area = UNSET
        else:
            city_area = self.city_area

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

        city_district_kladr_id: None | str | Unset
        if isinstance(self.city_district_kladr_id, Unset):
            city_district_kladr_id = UNSET
        else:
            city_district_kladr_id = self.city_district_kladr_id

        city_district_type: None | str | Unset
        if isinstance(self.city_district_type, Unset):
            city_district_type = UNSET
        else:
            city_district_type = self.city_district_type

        city_district_type_full: None | str | Unset
        if isinstance(self.city_district_type_full, Unset):
            city_district_type_full = UNSET
        else:
            city_district_type_full = self.city_district_type_full

        city_district_with_type: None | str | Unset
        if isinstance(self.city_district_with_type, Unset):
            city_district_with_type = UNSET
        else:
            city_district_with_type = self.city_district_with_type

        city_fias_id: None | str | Unset
        if isinstance(self.city_fias_id, Unset):
            city_fias_id = UNSET
        else:
            city_fias_id = self.city_fias_id

        city_kladr_id: None | str | Unset
        if isinstance(self.city_kladr_id, Unset):
            city_kladr_id = UNSET
        else:
            city_kladr_id = self.city_kladr_id

        city_type: None | str | Unset
        if isinstance(self.city_type, Unset):
            city_type = UNSET
        else:
            city_type = self.city_type

        city_type_full: None | str | Unset
        if isinstance(self.city_type_full, Unset):
            city_type_full = UNSET
        else:
            city_type_full = self.city_type_full

        city_with_type: None | str | Unset
        if isinstance(self.city_with_type, Unset):
            city_with_type = UNSET
        else:
            city_with_type = self.city_with_type

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

        custom: list[dict[str, Any]] | None | Unset
        if isinstance(self.custom, Unset):
            custom = UNSET
        elif isinstance(self.custom, list):
            custom = []
            for custom_type_0_item_data in self.custom:
                custom_type_0_item = custom_type_0_item_data.to_dict()
                custom.append(custom_type_0_item)

        else:
            custom = self.custom

        divisions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.divisions, Unset):
            divisions = self.divisions.to_dict()

        entrance: None | str | Unset
        if isinstance(self.entrance, Unset):
            entrance = UNSET
        else:
            entrance = self.entrance

        federal_district: None | str | Unset
        if isinstance(self.federal_district, Unset):
            federal_district = UNSET
        else:
            federal_district = self.federal_district

        fias_actuality_state: None | str | Unset
        if isinstance(self.fias_actuality_state, Unset):
            fias_actuality_state = UNSET
        else:
            fias_actuality_state = self.fias_actuality_state

        fias_code: None | str | Unset
        if isinstance(self.fias_code, Unset):
            fias_code = UNSET
        else:
            fias_code = self.fias_code

        fias_id: None | str | Unset
        if isinstance(self.fias_id, Unset):
            fias_id = UNSET
        else:
            fias_id = self.fias_id

        fias_level: None | str | Unset
        if isinstance(self.fias_level, Unset):
            fias_level = UNSET
        else:
            fias_level = self.fias_level

        flat: None | str | Unset
        if isinstance(self.flat, Unset):
            flat = UNSET
        else:
            flat = self.flat

        flat_area: None | str | Unset
        if isinstance(self.flat_area, Unset):
            flat_area = UNSET
        else:
            flat_area = self.flat_area

        flat_cadnum: None | str | Unset
        if isinstance(self.flat_cadnum, Unset):
            flat_cadnum = UNSET
        else:
            flat_cadnum = self.flat_cadnum

        flat_fias_id: None | str | Unset
        if isinstance(self.flat_fias_id, Unset):
            flat_fias_id = UNSET
        else:
            flat_fias_id = self.flat_fias_id

        flat_price: None | str | Unset
        if isinstance(self.flat_price, Unset):
            flat_price = UNSET
        else:
            flat_price = self.flat_price

        flat_type: None | str | Unset
        if isinstance(self.flat_type, Unset):
            flat_type = UNSET
        else:
            flat_type = self.flat_type

        flat_type_full: None | str | Unset
        if isinstance(self.flat_type_full, Unset):
            flat_type_full = UNSET
        else:
            flat_type_full = self.flat_type_full

        floor: None | str | Unset
        if isinstance(self.floor, Unset):
            floor = UNSET
        else:
            floor = self.floor

        geo_lat: None | str | Unset
        if isinstance(self.geo_lat, Unset):
            geo_lat = UNSET
        else:
            geo_lat = self.geo_lat

        geo_lon: None | str | Unset
        if isinstance(self.geo_lon, Unset):
            geo_lon = UNSET
        else:
            geo_lon = self.geo_lon

        geoname_id: None | str | Unset
        if isinstance(self.geoname_id, Unset):
            geoname_id = UNSET
        else:
            geoname_id = self.geoname_id

        history_values: list[str] | None | Unset
        if isinstance(self.history_values, Unset):
            history_values = UNSET
        elif isinstance(self.history_values, list):
            history_values = self.history_values

        else:
            history_values = self.history_values

        house: None | str | Unset
        if isinstance(self.house, Unset):
            house = UNSET
        else:
            house = self.house

        house_cadnum: None | str | Unset
        if isinstance(self.house_cadnum, Unset):
            house_cadnum = UNSET
        else:
            house_cadnum = self.house_cadnum

        house_fias_id: None | str | Unset
        if isinstance(self.house_fias_id, Unset):
            house_fias_id = UNSET
        else:
            house_fias_id = self.house_fias_id

        house_flat_count: None | str | Unset
        if isinstance(self.house_flat_count, Unset):
            house_flat_count = UNSET
        else:
            house_flat_count = self.house_flat_count

        house_kladr_id: None | str | Unset
        if isinstance(self.house_kladr_id, Unset):
            house_kladr_id = UNSET
        else:
            house_kladr_id = self.house_kladr_id

        house_type: None | str | Unset
        if isinstance(self.house_type, Unset):
            house_type = UNSET
        else:
            house_type = self.house_type

        house_type_full: None | str | Unset
        if isinstance(self.house_type_full, Unset):
            house_type_full = UNSET
        else:
            house_type_full = self.house_type_full

        kladr_id: None | str | Unset
        if isinstance(self.kladr_id, Unset):
            kladr_id = UNSET
        else:
            kladr_id = self.kladr_id

        metro: list[dict[str, Any]] | None | Unset
        if isinstance(self.metro, Unset):
            metro = UNSET
        elif isinstance(self.metro, list):
            metro = []
            for metro_type_0_item_data in self.metro:
                metro_type_0_item = metro_type_0_item_data.to_dict()
                metro.append(metro_type_0_item)

        else:
            metro = self.metro

        okato: None | str | Unset
        if isinstance(self.okato, Unset):
            okato = UNSET
        else:
            okato = self.okato

        oktmo: None | str | Unset
        if isinstance(self.oktmo, Unset):
            oktmo = UNSET
        else:
            oktmo = self.oktmo

        postal_box: None | str | Unset
        if isinstance(self.postal_box, Unset):
            postal_box = UNSET
        else:
            postal_box = self.postal_box

        postal_code: None | str | Unset
        if isinstance(self.postal_code, Unset):
            postal_code = UNSET
        else:
            postal_code = self.postal_code

        qc: None | str | Unset
        if isinstance(self.qc, Unset):
            qc = UNSET
        else:
            qc = self.qc

        qc_complete: None | str | Unset
        if isinstance(self.qc_complete, Unset):
            qc_complete = UNSET
        else:
            qc_complete = self.qc_complete

        qc_geo: None | str | Unset
        if isinstance(self.qc_geo, Unset):
            qc_geo = UNSET
        else:
            qc_geo = self.qc_geo

        qc_house: None | str | Unset
        if isinstance(self.qc_house, Unset):
            qc_house = UNSET
        else:
            qc_house = self.qc_house

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

        region_kladr_id: None | str | Unset
        if isinstance(self.region_kladr_id, Unset):
            region_kladr_id = UNSET
        else:
            region_kladr_id = self.region_kladr_id

        region_type: None | str | Unset
        if isinstance(self.region_type, Unset):
            region_type = UNSET
        else:
            region_type = self.region_type

        region_type_full: None | str | Unset
        if isinstance(self.region_type_full, Unset):
            region_type_full = UNSET
        else:
            region_type_full = self.region_type_full

        region_with_type: None | str | Unset
        if isinstance(self.region_with_type, Unset):
            region_with_type = UNSET
        else:
            region_with_type = self.region_with_type

        room: None | str | Unset
        if isinstance(self.room, Unset):
            room = UNSET
        else:
            room = self.room

        room_cadnum: None | str | Unset
        if isinstance(self.room_cadnum, Unset):
            room_cadnum = UNSET
        else:
            room_cadnum = self.room_cadnum

        room_fias_id: None | str | Unset
        if isinstance(self.room_fias_id, Unset):
            room_fias_id = UNSET
        else:
            room_fias_id = self.room_fias_id

        room_type: None | str | Unset
        if isinstance(self.room_type, Unset):
            room_type = UNSET
        else:
            room_type = self.room_type

        room_type_full: None | str | Unset
        if isinstance(self.room_type_full, Unset):
            room_type_full = UNSET
        else:
            room_type_full = self.room_type_full

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

        settlement_kladr_id: None | str | Unset
        if isinstance(self.settlement_kladr_id, Unset):
            settlement_kladr_id = UNSET
        else:
            settlement_kladr_id = self.settlement_kladr_id

        settlement_type: None | str | Unset
        if isinstance(self.settlement_type, Unset):
            settlement_type = UNSET
        else:
            settlement_type = self.settlement_type

        settlement_type_full: None | str | Unset
        if isinstance(self.settlement_type_full, Unset):
            settlement_type_full = UNSET
        else:
            settlement_type_full = self.settlement_type_full

        settlement_with_type: None | str | Unset
        if isinstance(self.settlement_with_type, Unset):
            settlement_with_type = UNSET
        else:
            settlement_with_type = self.settlement_with_type

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        square_meter_price: None | str | Unset
        if isinstance(self.square_meter_price, Unset):
            square_meter_price = UNSET
        else:
            square_meter_price = self.square_meter_price

        stead: None | str | Unset
        if isinstance(self.stead, Unset):
            stead = UNSET
        else:
            stead = self.stead

        stead_cadnum: None | str | Unset
        if isinstance(self.stead_cadnum, Unset):
            stead_cadnum = UNSET
        else:
            stead_cadnum = self.stead_cadnum

        stead_fias_id: None | str | Unset
        if isinstance(self.stead_fias_id, Unset):
            stead_fias_id = UNSET
        else:
            stead_fias_id = self.stead_fias_id

        stead_type: None | str | Unset
        if isinstance(self.stead_type, Unset):
            stead_type = UNSET
        else:
            stead_type = self.stead_type

        stead_type_full: None | str | Unset
        if isinstance(self.stead_type_full, Unset):
            stead_type_full = UNSET
        else:
            stead_type_full = self.stead_type_full

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

        street_kladr_id: None | str | Unset
        if isinstance(self.street_kladr_id, Unset):
            street_kladr_id = UNSET
        else:
            street_kladr_id = self.street_kladr_id

        street_type: None | str | Unset
        if isinstance(self.street_type, Unset):
            street_type = UNSET
        else:
            street_type = self.street_type

        street_type_full: None | str | Unset
        if isinstance(self.street_type_full, Unset):
            street_type_full = UNSET
        else:
            street_type_full = self.street_type_full

        street_with_type: None | str | Unset
        if isinstance(self.street_with_type, Unset):
            street_with_type = UNSET
        else:
            street_with_type = self.street_with_type

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

        sub_area_kladr_id: None | str | Unset
        if isinstance(self.sub_area_kladr_id, Unset):
            sub_area_kladr_id = UNSET
        else:
            sub_area_kladr_id = self.sub_area_kladr_id

        sub_area_type: None | str | Unset
        if isinstance(self.sub_area_type, Unset):
            sub_area_type = UNSET
        else:
            sub_area_type = self.sub_area_type

        sub_area_type_full: None | str | Unset
        if isinstance(self.sub_area_type_full, Unset):
            sub_area_type_full = UNSET
        else:
            sub_area_type_full = self.sub_area_type_full

        sub_area_with_type: None | str | Unset
        if isinstance(self.sub_area_with_type, Unset):
            sub_area_with_type = UNSET
        else:
            sub_area_with_type = self.sub_area_with_type

        tax_office: None | str | Unset
        if isinstance(self.tax_office, Unset):
            tax_office = UNSET
        else:
            tax_office = self.tax_office

        tax_office_legal: None | str | Unset
        if isinstance(self.tax_office_legal, Unset):
            tax_office_legal = UNSET
        else:
            tax_office_legal = self.tax_office_legal

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        unparsed_parts: None | str | Unset
        if isinstance(self.unparsed_parts, Unset):
            unparsed_parts = UNSET
        else:
            unparsed_parts = self.unparsed_parts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if area is not UNSET:
            field_dict["area"] = area
        if area_fias_id is not UNSET:
            field_dict["area_fias_id"] = area_fias_id
        if area_kladr_id is not UNSET:
            field_dict["area_kladr_id"] = area_kladr_id
        if area_type is not UNSET:
            field_dict["area_type"] = area_type
        if area_type_full is not UNSET:
            field_dict["area_type_full"] = area_type_full
        if area_with_type is not UNSET:
            field_dict["area_with_type"] = area_with_type
        if beltway_distance is not UNSET:
            field_dict["beltway_distance"] = beltway_distance
        if beltway_hit is not UNSET:
            field_dict["beltway_hit"] = beltway_hit
        if block is not UNSET:
            field_dict["block"] = block
        if block_type is not UNSET:
            field_dict["block_type"] = block_type
        if block_type_full is not UNSET:
            field_dict["block_type_full"] = block_type_full
        if capital_marker is not UNSET:
            field_dict["capital_marker"] = capital_marker
        if city is not UNSET:
            field_dict["city"] = city
        if city_area is not UNSET:
            field_dict["city_area"] = city_area
        if city_district is not UNSET:
            field_dict["city_district"] = city_district
        if city_district_fias_id is not UNSET:
            field_dict["city_district_fias_id"] = city_district_fias_id
        if city_district_kladr_id is not UNSET:
            field_dict["city_district_kladr_id"] = city_district_kladr_id
        if city_district_type is not UNSET:
            field_dict["city_district_type"] = city_district_type
        if city_district_type_full is not UNSET:
            field_dict["city_district_type_full"] = city_district_type_full
        if city_district_with_type is not UNSET:
            field_dict["city_district_with_type"] = city_district_with_type
        if city_fias_id is not UNSET:
            field_dict["city_fias_id"] = city_fias_id
        if city_kladr_id is not UNSET:
            field_dict["city_kladr_id"] = city_kladr_id
        if city_type is not UNSET:
            field_dict["city_type"] = city_type
        if city_type_full is not UNSET:
            field_dict["city_type_full"] = city_type_full
        if city_with_type is not UNSET:
            field_dict["city_with_type"] = city_with_type
        if country is not UNSET:
            field_dict["country"] = country
        if country_iso_code is not UNSET:
            field_dict["country_iso_code"] = country_iso_code
        if custom is not UNSET:
            field_dict["custom"] = custom
        if divisions is not UNSET:
            field_dict["divisions"] = divisions
        if entrance is not UNSET:
            field_dict["entrance"] = entrance
        if federal_district is not UNSET:
            field_dict["federal_district"] = federal_district
        if fias_actuality_state is not UNSET:
            field_dict["fias_actuality_state"] = fias_actuality_state
        if fias_code is not UNSET:
            field_dict["fias_code"] = fias_code
        if fias_id is not UNSET:
            field_dict["fias_id"] = fias_id
        if fias_level is not UNSET:
            field_dict["fias_level"] = fias_level
        if flat is not UNSET:
            field_dict["flat"] = flat
        if flat_area is not UNSET:
            field_dict["flat_area"] = flat_area
        if flat_cadnum is not UNSET:
            field_dict["flat_cadnum"] = flat_cadnum
        if flat_fias_id is not UNSET:
            field_dict["flat_fias_id"] = flat_fias_id
        if flat_price is not UNSET:
            field_dict["flat_price"] = flat_price
        if flat_type is not UNSET:
            field_dict["flat_type"] = flat_type
        if flat_type_full is not UNSET:
            field_dict["flat_type_full"] = flat_type_full
        if floor is not UNSET:
            field_dict["floor"] = floor
        if geo_lat is not UNSET:
            field_dict["geo_lat"] = geo_lat
        if geo_lon is not UNSET:
            field_dict["geo_lon"] = geo_lon
        if geoname_id is not UNSET:
            field_dict["geoname_id"] = geoname_id
        if history_values is not UNSET:
            field_dict["history_values"] = history_values
        if house is not UNSET:
            field_dict["house"] = house
        if house_cadnum is not UNSET:
            field_dict["house_cadnum"] = house_cadnum
        if house_fias_id is not UNSET:
            field_dict["house_fias_id"] = house_fias_id
        if house_flat_count is not UNSET:
            field_dict["house_flat_count"] = house_flat_count
        if house_kladr_id is not UNSET:
            field_dict["house_kladr_id"] = house_kladr_id
        if house_type is not UNSET:
            field_dict["house_type"] = house_type
        if house_type_full is not UNSET:
            field_dict["house_type_full"] = house_type_full
        if kladr_id is not UNSET:
            field_dict["kladr_id"] = kladr_id
        if metro is not UNSET:
            field_dict["metro"] = metro
        if okato is not UNSET:
            field_dict["okato"] = okato
        if oktmo is not UNSET:
            field_dict["oktmo"] = oktmo
        if postal_box is not UNSET:
            field_dict["postal_box"] = postal_box
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if qc is not UNSET:
            field_dict["qc"] = qc
        if qc_complete is not UNSET:
            field_dict["qc_complete"] = qc_complete
        if qc_geo is not UNSET:
            field_dict["qc_geo"] = qc_geo
        if qc_house is not UNSET:
            field_dict["qc_house"] = qc_house
        if region is not UNSET:
            field_dict["region"] = region
        if region_fias_id is not UNSET:
            field_dict["region_fias_id"] = region_fias_id
        if region_iso_code is not UNSET:
            field_dict["region_iso_code"] = region_iso_code
        if region_kladr_id is not UNSET:
            field_dict["region_kladr_id"] = region_kladr_id
        if region_type is not UNSET:
            field_dict["region_type"] = region_type
        if region_type_full is not UNSET:
            field_dict["region_type_full"] = region_type_full
        if region_with_type is not UNSET:
            field_dict["region_with_type"] = region_with_type
        if room is not UNSET:
            field_dict["room"] = room
        if room_cadnum is not UNSET:
            field_dict["room_cadnum"] = room_cadnum
        if room_fias_id is not UNSET:
            field_dict["room_fias_id"] = room_fias_id
        if room_type is not UNSET:
            field_dict["room_type"] = room_type
        if room_type_full is not UNSET:
            field_dict["room_type_full"] = room_type_full
        if settlement is not UNSET:
            field_dict["settlement"] = settlement
        if settlement_fias_id is not UNSET:
            field_dict["settlement_fias_id"] = settlement_fias_id
        if settlement_kladr_id is not UNSET:
            field_dict["settlement_kladr_id"] = settlement_kladr_id
        if settlement_type is not UNSET:
            field_dict["settlement_type"] = settlement_type
        if settlement_type_full is not UNSET:
            field_dict["settlement_type_full"] = settlement_type_full
        if settlement_with_type is not UNSET:
            field_dict["settlement_with_type"] = settlement_with_type
        if source is not UNSET:
            field_dict["source"] = source
        if square_meter_price is not UNSET:
            field_dict["square_meter_price"] = square_meter_price
        if stead is not UNSET:
            field_dict["stead"] = stead
        if stead_cadnum is not UNSET:
            field_dict["stead_cadnum"] = stead_cadnum
        if stead_fias_id is not UNSET:
            field_dict["stead_fias_id"] = stead_fias_id
        if stead_type is not UNSET:
            field_dict["stead_type"] = stead_type
        if stead_type_full is not UNSET:
            field_dict["stead_type_full"] = stead_type_full
        if street is not UNSET:
            field_dict["street"] = street
        if street_fias_id is not UNSET:
            field_dict["street_fias_id"] = street_fias_id
        if street_kladr_id is not UNSET:
            field_dict["street_kladr_id"] = street_kladr_id
        if street_type is not UNSET:
            field_dict["street_type"] = street_type
        if street_type_full is not UNSET:
            field_dict["street_type_full"] = street_type_full
        if street_with_type is not UNSET:
            field_dict["street_with_type"] = street_with_type
        if sub_area is not UNSET:
            field_dict["sub_area"] = sub_area
        if sub_area_fias_id is not UNSET:
            field_dict["sub_area_fias_id"] = sub_area_fias_id
        if sub_area_kladr_id is not UNSET:
            field_dict["sub_area_kladr_id"] = sub_area_kladr_id
        if sub_area_type is not UNSET:
            field_dict["sub_area_type"] = sub_area_type
        if sub_area_type_full is not UNSET:
            field_dict["sub_area_type_full"] = sub_area_type_full
        if sub_area_with_type is not UNSET:
            field_dict["sub_area_with_type"] = sub_area_with_type
        if tax_office is not UNSET:
            field_dict["tax_office"] = tax_office
        if tax_office_legal is not UNSET:
            field_dict["tax_office_legal"] = tax_office_legal
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if unparsed_parts is not UNSET:
            field_dict["unparsed_parts"] = unparsed_parts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_custom_type_0_item import AddressCustomType0Item
        from ..models.address_divisions import AddressDivisions
        from ..models.metro import Metro

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

        def _parse_area_kladr_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_kladr_id = _parse_area_kladr_id(d.pop("area_kladr_id", UNSET))

        def _parse_area_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_type = _parse_area_type(d.pop("area_type", UNSET))

        def _parse_area_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_type_full = _parse_area_type_full(d.pop("area_type_full", UNSET))

        def _parse_area_with_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_with_type = _parse_area_with_type(d.pop("area_with_type", UNSET))

        def _parse_beltway_distance(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beltway_distance = _parse_beltway_distance(d.pop("beltway_distance", UNSET))

        def _parse_beltway_hit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beltway_hit = _parse_beltway_hit(d.pop("beltway_hit", UNSET))

        def _parse_block(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        block = _parse_block(d.pop("block", UNSET))

        def _parse_block_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        block_type = _parse_block_type(d.pop("block_type", UNSET))

        def _parse_block_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        block_type_full = _parse_block_type_full(d.pop("block_type_full", UNSET))

        def _parse_capital_marker(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        capital_marker = _parse_capital_marker(d.pop("capital_marker", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_city_area(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city_area = _parse_city_area(d.pop("city_area", UNSET))

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

        def _parse_city_district_kladr_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city_district_kladr_id = _parse_city_district_kladr_id(d.pop("city_district_kladr_id", UNSET))

        def _parse_city_district_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city_district_type = _parse_city_district_type(d.pop("city_district_type", UNSET))

        def _parse_city_district_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city_district_type_full = _parse_city_district_type_full(d.pop("city_district_type_full", UNSET))

        def _parse_city_district_with_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city_district_with_type = _parse_city_district_with_type(d.pop("city_district_with_type", UNSET))

        def _parse_city_fias_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city_fias_id = _parse_city_fias_id(d.pop("city_fias_id", UNSET))

        def _parse_city_kladr_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city_kladr_id = _parse_city_kladr_id(d.pop("city_kladr_id", UNSET))

        def _parse_city_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city_type = _parse_city_type(d.pop("city_type", UNSET))

        def _parse_city_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city_type_full = _parse_city_type_full(d.pop("city_type_full", UNSET))

        def _parse_city_with_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city_with_type = _parse_city_with_type(d.pop("city_with_type", UNSET))

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

        def _parse_custom(data: object) -> list[AddressCustomType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_type_0 = []
                _custom_type_0 = data
                for custom_type_0_item_data in _custom_type_0:
                    custom_type_0_item = AddressCustomType0Item.from_dict(custom_type_0_item_data)

                    custom_type_0.append(custom_type_0_item)

                return custom_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AddressCustomType0Item] | None | Unset, data)

        custom = _parse_custom(d.pop("custom", UNSET))

        _divisions = d.pop("divisions", UNSET)
        divisions: AddressDivisions | Unset
        if isinstance(_divisions, Unset):
            divisions = UNSET
        else:
            divisions = AddressDivisions.from_dict(_divisions)

        def _parse_entrance(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entrance = _parse_entrance(d.pop("entrance", UNSET))

        def _parse_federal_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        federal_district = _parse_federal_district(d.pop("federal_district", UNSET))

        def _parse_fias_actuality_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fias_actuality_state = _parse_fias_actuality_state(d.pop("fias_actuality_state", UNSET))

        def _parse_fias_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fias_code = _parse_fias_code(d.pop("fias_code", UNSET))

        def _parse_fias_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fias_id = _parse_fias_id(d.pop("fias_id", UNSET))

        def _parse_fias_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fias_level = _parse_fias_level(d.pop("fias_level", UNSET))

        def _parse_flat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flat = _parse_flat(d.pop("flat", UNSET))

        def _parse_flat_area(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flat_area = _parse_flat_area(d.pop("flat_area", UNSET))

        def _parse_flat_cadnum(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flat_cadnum = _parse_flat_cadnum(d.pop("flat_cadnum", UNSET))

        def _parse_flat_fias_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flat_fias_id = _parse_flat_fias_id(d.pop("flat_fias_id", UNSET))

        def _parse_flat_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flat_price = _parse_flat_price(d.pop("flat_price", UNSET))

        def _parse_flat_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flat_type = _parse_flat_type(d.pop("flat_type", UNSET))

        def _parse_flat_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flat_type_full = _parse_flat_type_full(d.pop("flat_type_full", UNSET))

        def _parse_floor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        floor = _parse_floor(d.pop("floor", UNSET))

        def _parse_geo_lat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geo_lat = _parse_geo_lat(d.pop("geo_lat", UNSET))

        def _parse_geo_lon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geo_lon = _parse_geo_lon(d.pop("geo_lon", UNSET))

        def _parse_geoname_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geoname_id = _parse_geoname_id(d.pop("geoname_id", UNSET))

        def _parse_history_values(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                history_values_type_0 = cast(list[str], data)

                return history_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        history_values = _parse_history_values(d.pop("history_values", UNSET))

        def _parse_house(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        house = _parse_house(d.pop("house", UNSET))

        def _parse_house_cadnum(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        house_cadnum = _parse_house_cadnum(d.pop("house_cadnum", UNSET))

        def _parse_house_fias_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        house_fias_id = _parse_house_fias_id(d.pop("house_fias_id", UNSET))

        def _parse_house_flat_count(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        house_flat_count = _parse_house_flat_count(d.pop("house_flat_count", UNSET))

        def _parse_house_kladr_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        house_kladr_id = _parse_house_kladr_id(d.pop("house_kladr_id", UNSET))

        def _parse_house_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        house_type = _parse_house_type(d.pop("house_type", UNSET))

        def _parse_house_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        house_type_full = _parse_house_type_full(d.pop("house_type_full", UNSET))

        def _parse_kladr_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kladr_id = _parse_kladr_id(d.pop("kladr_id", UNSET))

        def _parse_metro(data: object) -> list[Metro] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                metro_type_0 = []
                _metro_type_0 = data
                for metro_type_0_item_data in _metro_type_0:
                    metro_type_0_item = Metro.from_dict(metro_type_0_item_data)

                    metro_type_0.append(metro_type_0_item)

                return metro_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Metro] | None | Unset, data)

        metro = _parse_metro(d.pop("metro", UNSET))

        def _parse_okato(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        okato = _parse_okato(d.pop("okato", UNSET))

        def _parse_oktmo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        oktmo = _parse_oktmo(d.pop("oktmo", UNSET))

        def _parse_postal_box(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postal_box = _parse_postal_box(d.pop("postal_box", UNSET))

        def _parse_postal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postal_code = _parse_postal_code(d.pop("postal_code", UNSET))

        def _parse_qc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        qc = _parse_qc(d.pop("qc", UNSET))

        def _parse_qc_complete(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        qc_complete = _parse_qc_complete(d.pop("qc_complete", UNSET))

        def _parse_qc_geo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        qc_geo = _parse_qc_geo(d.pop("qc_geo", UNSET))

        def _parse_qc_house(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        qc_house = _parse_qc_house(d.pop("qc_house", UNSET))

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

        def _parse_region_kladr_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_kladr_id = _parse_region_kladr_id(d.pop("region_kladr_id", UNSET))

        def _parse_region_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_type = _parse_region_type(d.pop("region_type", UNSET))

        def _parse_region_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_type_full = _parse_region_type_full(d.pop("region_type_full", UNSET))

        def _parse_region_with_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_with_type = _parse_region_with_type(d.pop("region_with_type", UNSET))

        def _parse_room(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room = _parse_room(d.pop("room", UNSET))

        def _parse_room_cadnum(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_cadnum = _parse_room_cadnum(d.pop("room_cadnum", UNSET))

        def _parse_room_fias_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_fias_id = _parse_room_fias_id(d.pop("room_fias_id", UNSET))

        def _parse_room_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_type = _parse_room_type(d.pop("room_type", UNSET))

        def _parse_room_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_type_full = _parse_room_type_full(d.pop("room_type_full", UNSET))

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

        def _parse_settlement_kladr_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        settlement_kladr_id = _parse_settlement_kladr_id(d.pop("settlement_kladr_id", UNSET))

        def _parse_settlement_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        settlement_type = _parse_settlement_type(d.pop("settlement_type", UNSET))

        def _parse_settlement_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        settlement_type_full = _parse_settlement_type_full(d.pop("settlement_type_full", UNSET))

        def _parse_settlement_with_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        settlement_with_type = _parse_settlement_with_type(d.pop("settlement_with_type", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_square_meter_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        square_meter_price = _parse_square_meter_price(d.pop("square_meter_price", UNSET))

        def _parse_stead(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stead = _parse_stead(d.pop("stead", UNSET))

        def _parse_stead_cadnum(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stead_cadnum = _parse_stead_cadnum(d.pop("stead_cadnum", UNSET))

        def _parse_stead_fias_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stead_fias_id = _parse_stead_fias_id(d.pop("stead_fias_id", UNSET))

        def _parse_stead_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stead_type = _parse_stead_type(d.pop("stead_type", UNSET))

        def _parse_stead_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stead_type_full = _parse_stead_type_full(d.pop("stead_type_full", UNSET))

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

        def _parse_street_kladr_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_kladr_id = _parse_street_kladr_id(d.pop("street_kladr_id", UNSET))

        def _parse_street_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_type = _parse_street_type(d.pop("street_type", UNSET))

        def _parse_street_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_type_full = _parse_street_type_full(d.pop("street_type_full", UNSET))

        def _parse_street_with_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_with_type = _parse_street_with_type(d.pop("street_with_type", UNSET))

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

        def _parse_sub_area_kladr_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_area_kladr_id = _parse_sub_area_kladr_id(d.pop("sub_area_kladr_id", UNSET))

        def _parse_sub_area_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_area_type = _parse_sub_area_type(d.pop("sub_area_type", UNSET))

        def _parse_sub_area_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_area_type_full = _parse_sub_area_type_full(d.pop("sub_area_type_full", UNSET))

        def _parse_sub_area_with_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_area_with_type = _parse_sub_area_with_type(d.pop("sub_area_with_type", UNSET))

        def _parse_tax_office(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_office = _parse_tax_office(d.pop("tax_office", UNSET))

        def _parse_tax_office_legal(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_office_legal = _parse_tax_office_legal(d.pop("tax_office_legal", UNSET))

        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        def _parse_unparsed_parts(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unparsed_parts = _parse_unparsed_parts(d.pop("unparsed_parts", UNSET))

        address = cls(
            area=area,
            area_fias_id=area_fias_id,
            area_kladr_id=area_kladr_id,
            area_type=area_type,
            area_type_full=area_type_full,
            area_with_type=area_with_type,
            beltway_distance=beltway_distance,
            beltway_hit=beltway_hit,
            block=block,
            block_type=block_type,
            block_type_full=block_type_full,
            capital_marker=capital_marker,
            city=city,
            city_area=city_area,
            city_district=city_district,
            city_district_fias_id=city_district_fias_id,
            city_district_kladr_id=city_district_kladr_id,
            city_district_type=city_district_type,
            city_district_type_full=city_district_type_full,
            city_district_with_type=city_district_with_type,
            city_fias_id=city_fias_id,
            city_kladr_id=city_kladr_id,
            city_type=city_type,
            city_type_full=city_type_full,
            city_with_type=city_with_type,
            country=country,
            country_iso_code=country_iso_code,
            custom=custom,
            divisions=divisions,
            entrance=entrance,
            federal_district=federal_district,
            fias_actuality_state=fias_actuality_state,
            fias_code=fias_code,
            fias_id=fias_id,
            fias_level=fias_level,
            flat=flat,
            flat_area=flat_area,
            flat_cadnum=flat_cadnum,
            flat_fias_id=flat_fias_id,
            flat_price=flat_price,
            flat_type=flat_type,
            flat_type_full=flat_type_full,
            floor=floor,
            geo_lat=geo_lat,
            geo_lon=geo_lon,
            geoname_id=geoname_id,
            history_values=history_values,
            house=house,
            house_cadnum=house_cadnum,
            house_fias_id=house_fias_id,
            house_flat_count=house_flat_count,
            house_kladr_id=house_kladr_id,
            house_type=house_type,
            house_type_full=house_type_full,
            kladr_id=kladr_id,
            metro=metro,
            okato=okato,
            oktmo=oktmo,
            postal_box=postal_box,
            postal_code=postal_code,
            qc=qc,
            qc_complete=qc_complete,
            qc_geo=qc_geo,
            qc_house=qc_house,
            region=region,
            region_fias_id=region_fias_id,
            region_iso_code=region_iso_code,
            region_kladr_id=region_kladr_id,
            region_type=region_type,
            region_type_full=region_type_full,
            region_with_type=region_with_type,
            room=room,
            room_cadnum=room_cadnum,
            room_fias_id=room_fias_id,
            room_type=room_type,
            room_type_full=room_type_full,
            settlement=settlement,
            settlement_fias_id=settlement_fias_id,
            settlement_kladr_id=settlement_kladr_id,
            settlement_type=settlement_type,
            settlement_type_full=settlement_type_full,
            settlement_with_type=settlement_with_type,
            source=source,
            square_meter_price=square_meter_price,
            stead=stead,
            stead_cadnum=stead_cadnum,
            stead_fias_id=stead_fias_id,
            stead_type=stead_type,
            stead_type_full=stead_type_full,
            street=street,
            street_fias_id=street_fias_id,
            street_kladr_id=street_kladr_id,
            street_type=street_type,
            street_type_full=street_type_full,
            street_with_type=street_with_type,
            sub_area=sub_area,
            sub_area_fias_id=sub_area_fias_id,
            sub_area_kladr_id=sub_area_kladr_id,
            sub_area_type=sub_area_type,
            sub_area_type_full=sub_area_type_full,
            sub_area_with_type=sub_area_with_type,
            tax_office=tax_office,
            tax_office_legal=tax_office_legal,
            timezone=timezone,
            unparsed_parts=unparsed_parts,
        )

        address.additional_properties = d
        return address

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
