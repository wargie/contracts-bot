from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FiasAddress")


@_attrs_define
class FiasAddress:
    """
    Attributes:
        area (None | str | Unset):
        area_fias_id (None | str | Unset):
        area_kladr_id (None | str | Unset):
        area_type (None | str | Unset):
        area_type_full (None | str | Unset):
        area_with_type (None | str | Unset):
        block (None | str | Unset):
        building (None | str | Unset):
        building_type (None | str | Unset):
        cadastral_number (None | str | Unset):
        capital_marker (None | str | Unset):
        city (None | str | Unset):
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
        fias_actuality_state (None | str | Unset):
        fias_code (None | str | Unset):
        fias_id (None | str | Unset):
        fias_level (None | str | Unset):
        history_values (list[str] | None | Unset):
        house (None | str | Unset):
        house_fias_id (None | str | Unset):
        house_kladr_id (None | str | Unset):
        house_type (None | str | Unset):
        kladr_id (None | str | Unset):
        okato (None | str | Unset):
        oktmo (None | str | Unset):
        planning_structure (None | str | Unset):
        planning_structure_fias_id (None | str | Unset):
        planning_structure_kladr_id (None | str | Unset):
        planning_structure_type (None | str | Unset):
        planning_structure_type_full (None | str | Unset):
        planning_structure_with_type (None | str | Unset):
        postal_code (None | str | Unset):
        qc (None | str | Unset):
        region (None | str | Unset):
        region_fias_id (None | str | Unset):
        region_kladr_id (None | str | Unset):
        region_type (None | str | Unset):
        region_type_full (None | str | Unset):
        region_with_type (None | str | Unset):
        settlement (None | str | Unset):
        settlement_fias_id (None | str | Unset):
        settlement_kladr_id (None | str | Unset):
        settlement_type (None | str | Unset):
        settlement_type_full (None | str | Unset):
        settlement_with_type (None | str | Unset):
        source (None | str | Unset):
        street (None | str | Unset):
        street_fias_id (None | str | Unset):
        street_kladr_id (None | str | Unset):
        street_type (None | str | Unset):
        street_type_full (None | str | Unset):
        street_with_type (None | str | Unset):
        tax_office (None | str | Unset):
        tax_office_legal (None | str | Unset):
    """

    area: None | str | Unset = UNSET
    area_fias_id: None | str | Unset = UNSET
    area_kladr_id: None | str | Unset = UNSET
    area_type: None | str | Unset = UNSET
    area_type_full: None | str | Unset = UNSET
    area_with_type: None | str | Unset = UNSET
    block: None | str | Unset = UNSET
    building: None | str | Unset = UNSET
    building_type: None | str | Unset = UNSET
    cadastral_number: None | str | Unset = UNSET
    capital_marker: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
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
    fias_actuality_state: None | str | Unset = UNSET
    fias_code: None | str | Unset = UNSET
    fias_id: None | str | Unset = UNSET
    fias_level: None | str | Unset = UNSET
    history_values: list[str] | None | Unset = UNSET
    house: None | str | Unset = UNSET
    house_fias_id: None | str | Unset = UNSET
    house_kladr_id: None | str | Unset = UNSET
    house_type: None | str | Unset = UNSET
    kladr_id: None | str | Unset = UNSET
    okato: None | str | Unset = UNSET
    oktmo: None | str | Unset = UNSET
    planning_structure: None | str | Unset = UNSET
    planning_structure_fias_id: None | str | Unset = UNSET
    planning_structure_kladr_id: None | str | Unset = UNSET
    planning_structure_type: None | str | Unset = UNSET
    planning_structure_type_full: None | str | Unset = UNSET
    planning_structure_with_type: None | str | Unset = UNSET
    postal_code: None | str | Unset = UNSET
    qc: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    region_fias_id: None | str | Unset = UNSET
    region_kladr_id: None | str | Unset = UNSET
    region_type: None | str | Unset = UNSET
    region_type_full: None | str | Unset = UNSET
    region_with_type: None | str | Unset = UNSET
    settlement: None | str | Unset = UNSET
    settlement_fias_id: None | str | Unset = UNSET
    settlement_kladr_id: None | str | Unset = UNSET
    settlement_type: None | str | Unset = UNSET
    settlement_type_full: None | str | Unset = UNSET
    settlement_with_type: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    street: None | str | Unset = UNSET
    street_fias_id: None | str | Unset = UNSET
    street_kladr_id: None | str | Unset = UNSET
    street_type: None | str | Unset = UNSET
    street_type_full: None | str | Unset = UNSET
    street_with_type: None | str | Unset = UNSET
    tax_office: None | str | Unset = UNSET
    tax_office_legal: None | str | Unset = UNSET
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

        block: None | str | Unset
        if isinstance(self.block, Unset):
            block = UNSET
        else:
            block = self.block

        building: None | str | Unset
        if isinstance(self.building, Unset):
            building = UNSET
        else:
            building = self.building

        building_type: None | str | Unset
        if isinstance(self.building_type, Unset):
            building_type = UNSET
        else:
            building_type = self.building_type

        cadastral_number: None | str | Unset
        if isinstance(self.cadastral_number, Unset):
            cadastral_number = UNSET
        else:
            cadastral_number = self.cadastral_number

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

        house_fias_id: None | str | Unset
        if isinstance(self.house_fias_id, Unset):
            house_fias_id = UNSET
        else:
            house_fias_id = self.house_fias_id

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

        kladr_id: None | str | Unset
        if isinstance(self.kladr_id, Unset):
            kladr_id = UNSET
        else:
            kladr_id = self.kladr_id

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

        planning_structure: None | str | Unset
        if isinstance(self.planning_structure, Unset):
            planning_structure = UNSET
        else:
            planning_structure = self.planning_structure

        planning_structure_fias_id: None | str | Unset
        if isinstance(self.planning_structure_fias_id, Unset):
            planning_structure_fias_id = UNSET
        else:
            planning_structure_fias_id = self.planning_structure_fias_id

        planning_structure_kladr_id: None | str | Unset
        if isinstance(self.planning_structure_kladr_id, Unset):
            planning_structure_kladr_id = UNSET
        else:
            planning_structure_kladr_id = self.planning_structure_kladr_id

        planning_structure_type: None | str | Unset
        if isinstance(self.planning_structure_type, Unset):
            planning_structure_type = UNSET
        else:
            planning_structure_type = self.planning_structure_type

        planning_structure_type_full: None | str | Unset
        if isinstance(self.planning_structure_type_full, Unset):
            planning_structure_type_full = UNSET
        else:
            planning_structure_type_full = self.planning_structure_type_full

        planning_structure_with_type: None | str | Unset
        if isinstance(self.planning_structure_with_type, Unset):
            planning_structure_with_type = UNSET
        else:
            planning_structure_with_type = self.planning_structure_with_type

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
        if block is not UNSET:
            field_dict["block"] = block
        if building is not UNSET:
            field_dict["building"] = building
        if building_type is not UNSET:
            field_dict["building_type"] = building_type
        if cadastral_number is not UNSET:
            field_dict["cadastral_number"] = cadastral_number
        if capital_marker is not UNSET:
            field_dict["capital_marker"] = capital_marker
        if city is not UNSET:
            field_dict["city"] = city
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
        if fias_actuality_state is not UNSET:
            field_dict["fias_actuality_state"] = fias_actuality_state
        if fias_code is not UNSET:
            field_dict["fias_code"] = fias_code
        if fias_id is not UNSET:
            field_dict["fias_id"] = fias_id
        if fias_level is not UNSET:
            field_dict["fias_level"] = fias_level
        if history_values is not UNSET:
            field_dict["history_values"] = history_values
        if house is not UNSET:
            field_dict["house"] = house
        if house_fias_id is not UNSET:
            field_dict["house_fias_id"] = house_fias_id
        if house_kladr_id is not UNSET:
            field_dict["house_kladr_id"] = house_kladr_id
        if house_type is not UNSET:
            field_dict["house_type"] = house_type
        if kladr_id is not UNSET:
            field_dict["kladr_id"] = kladr_id
        if okato is not UNSET:
            field_dict["okato"] = okato
        if oktmo is not UNSET:
            field_dict["oktmo"] = oktmo
        if planning_structure is not UNSET:
            field_dict["planning_structure"] = planning_structure
        if planning_structure_fias_id is not UNSET:
            field_dict["planning_structure_fias_id"] = planning_structure_fias_id
        if planning_structure_kladr_id is not UNSET:
            field_dict["planning_structure_kladr_id"] = planning_structure_kladr_id
        if planning_structure_type is not UNSET:
            field_dict["planning_structure_type"] = planning_structure_type
        if planning_structure_type_full is not UNSET:
            field_dict["planning_structure_type_full"] = planning_structure_type_full
        if planning_structure_with_type is not UNSET:
            field_dict["planning_structure_with_type"] = planning_structure_with_type
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if qc is not UNSET:
            field_dict["qc"] = qc
        if region is not UNSET:
            field_dict["region"] = region
        if region_fias_id is not UNSET:
            field_dict["region_fias_id"] = region_fias_id
        if region_kladr_id is not UNSET:
            field_dict["region_kladr_id"] = region_kladr_id
        if region_type is not UNSET:
            field_dict["region_type"] = region_type
        if region_type_full is not UNSET:
            field_dict["region_type_full"] = region_type_full
        if region_with_type is not UNSET:
            field_dict["region_with_type"] = region_with_type
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
        if tax_office is not UNSET:
            field_dict["tax_office"] = tax_office
        if tax_office_legal is not UNSET:
            field_dict["tax_office_legal"] = tax_office_legal

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

        def _parse_block(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        block = _parse_block(d.pop("block", UNSET))

        def _parse_building(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building = _parse_building(d.pop("building", UNSET))

        def _parse_building_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_type = _parse_building_type(d.pop("building_type", UNSET))

        def _parse_cadastral_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cadastral_number = _parse_cadastral_number(d.pop("cadastral_number", UNSET))

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

        def _parse_house_fias_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        house_fias_id = _parse_house_fias_id(d.pop("house_fias_id", UNSET))

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

        def _parse_kladr_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kladr_id = _parse_kladr_id(d.pop("kladr_id", UNSET))

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

        def _parse_planning_structure(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planning_structure = _parse_planning_structure(d.pop("planning_structure", UNSET))

        def _parse_planning_structure_fias_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planning_structure_fias_id = _parse_planning_structure_fias_id(d.pop("planning_structure_fias_id", UNSET))

        def _parse_planning_structure_kladr_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planning_structure_kladr_id = _parse_planning_structure_kladr_id(d.pop("planning_structure_kladr_id", UNSET))

        def _parse_planning_structure_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planning_structure_type = _parse_planning_structure_type(d.pop("planning_structure_type", UNSET))

        def _parse_planning_structure_type_full(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planning_structure_type_full = _parse_planning_structure_type_full(d.pop("planning_structure_type_full", UNSET))

        def _parse_planning_structure_with_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planning_structure_with_type = _parse_planning_structure_with_type(d.pop("planning_structure_with_type", UNSET))

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

        fias_address = cls(
            area=area,
            area_fias_id=area_fias_id,
            area_kladr_id=area_kladr_id,
            area_type=area_type,
            area_type_full=area_type_full,
            area_with_type=area_with_type,
            block=block,
            building=building,
            building_type=building_type,
            cadastral_number=cadastral_number,
            capital_marker=capital_marker,
            city=city,
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
            fias_actuality_state=fias_actuality_state,
            fias_code=fias_code,
            fias_id=fias_id,
            fias_level=fias_level,
            history_values=history_values,
            house=house,
            house_fias_id=house_fias_id,
            house_kladr_id=house_kladr_id,
            house_type=house_type,
            kladr_id=kladr_id,
            okato=okato,
            oktmo=oktmo,
            planning_structure=planning_structure,
            planning_structure_fias_id=planning_structure_fias_id,
            planning_structure_kladr_id=planning_structure_kladr_id,
            planning_structure_type=planning_structure_type,
            planning_structure_type_full=planning_structure_type_full,
            planning_structure_with_type=planning_structure_with_type,
            postal_code=postal_code,
            qc=qc,
            region=region,
            region_fias_id=region_fias_id,
            region_kladr_id=region_kladr_id,
            region_type=region_type,
            region_type_full=region_type_full,
            region_with_type=region_with_type,
            settlement=settlement,
            settlement_fias_id=settlement_fias_id,
            settlement_kladr_id=settlement_kladr_id,
            settlement_type=settlement_type,
            settlement_type_full=settlement_type_full,
            settlement_with_type=settlement_with_type,
            source=source,
            street=street,
            street_fias_id=street_fias_id,
            street_kladr_id=street_kladr_id,
            street_type=street_type,
            street_type_full=street_type_full,
            street_with_type=street_with_type,
            tax_office=tax_office,
            tax_office_legal=tax_office_legal,
        )

        fias_address.additional_properties = d
        return fias_address

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
