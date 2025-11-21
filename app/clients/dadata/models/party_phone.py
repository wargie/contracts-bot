from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.party_phone_contact import PartyPhoneContact


T = TypeVar("T", bound="PartyPhone")


@_attrs_define
class PartyPhone:
    """
    Attributes:
        city (None | str | Unset):
        city_code (None | str | Unset):
        contact (PartyPhoneContact | Unset):
        country (None | str | Unset):
        country_code (None | str | Unset):
        extension (None | str | Unset):
        number (None | str | Unset):
        provider (None | str | Unset):
        qc (None | str | Unset):
        qc_conflict (None | str | Unset):
        region (None | str | Unset):
        source (None | str | Unset):
        timezone (None | str | Unset):
        type_ (None | str | Unset):
    """

    city: None | str | Unset = UNSET
    city_code: None | str | Unset = UNSET
    contact: PartyPhoneContact | Unset = UNSET
    country: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    extension: None | str | Unset = UNSET
    number: None | str | Unset = UNSET
    provider: None | str | Unset = UNSET
    qc: None | str | Unset = UNSET
    qc_conflict: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    timezone: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        city_code: None | str | Unset
        if isinstance(self.city_code, Unset):
            city_code = UNSET
        else:
            city_code = self.city_code

        contact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        extension: None | str | Unset
        if isinstance(self.extension, Unset):
            extension = UNSET
        else:
            extension = self.extension

        number: None | str | Unset
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        qc: None | str | Unset
        if isinstance(self.qc, Unset):
            qc = UNSET
        else:
            qc = self.qc

        qc_conflict: None | str | Unset
        if isinstance(self.qc_conflict, Unset):
            qc_conflict = UNSET
        else:
            qc_conflict = self.qc_conflict

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if city_code is not UNSET:
            field_dict["city_code"] = city_code
        if contact is not UNSET:
            field_dict["contact"] = contact
        if country is not UNSET:
            field_dict["country"] = country
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if extension is not UNSET:
            field_dict["extension"] = extension
        if number is not UNSET:
            field_dict["number"] = number
        if provider is not UNSET:
            field_dict["provider"] = provider
        if qc is not UNSET:
            field_dict["qc"] = qc
        if qc_conflict is not UNSET:
            field_dict["qc_conflict"] = qc_conflict
        if region is not UNSET:
            field_dict["region"] = region
        if source is not UNSET:
            field_dict["source"] = source
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.party_phone_contact import PartyPhoneContact

        d = dict(src_dict)

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_city_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city_code = _parse_city_code(d.pop("city_code", UNSET))

        _contact = d.pop("contact", UNSET)
        contact: PartyPhoneContact | Unset
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = PartyPhoneContact.from_dict(_contact)

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("country_code", UNSET))

        def _parse_extension(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extension = _parse_extension(d.pop("extension", UNSET))

        def _parse_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        number = _parse_number(d.pop("number", UNSET))

        def _parse_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        def _parse_qc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        qc = _parse_qc(d.pop("qc", UNSET))

        def _parse_qc_conflict(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        qc_conflict = _parse_qc_conflict(d.pop("qc_conflict", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        party_phone = cls(
            city=city,
            city_code=city_code,
            contact=contact,
            country=country,
            country_code=country_code,
            extension=extension,
            number=number,
            provider=provider,
            qc=qc,
            qc_conflict=qc_conflict,
            region=region,
            source=source,
            timezone=timezone,
            type_=type_,
        )

        party_phone.additional_properties = d
        return party_phone

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
