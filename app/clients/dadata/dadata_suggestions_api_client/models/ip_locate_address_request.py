from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ip_locate_address_request_division import IpLocateAddressRequestDivision
from ..models.ip_locate_address_request_language import IpLocateAddressRequestLanguage
from ..types import UNSET, Unset

T = TypeVar("T", bound="IpLocateAddressRequest")


@_attrs_define
class IpLocateAddressRequest:
    """
    Attributes:
        division (IpLocateAddressRequestDivision | Unset):
        ip (None | str | Unset):
        language (IpLocateAddressRequestLanguage | Unset):
    """

    division: IpLocateAddressRequestDivision | Unset = UNSET
    ip: None | str | Unset = UNSET
    language: IpLocateAddressRequestLanguage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        division: str | Unset = UNSET
        if not isinstance(self.division, Unset):
            division = self.division.value

        ip: None | str | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        language: str | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if division is not UNSET:
            field_dict["division"] = division
        if ip is not UNSET:
            field_dict["ip"] = ip
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _division = d.pop("division", UNSET)
        division: IpLocateAddressRequestDivision | Unset
        if isinstance(_division, Unset):
            division = UNSET
        else:
            division = IpLocateAddressRequestDivision(_division)

        def _parse_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))

        _language = d.pop("language", UNSET)
        language: IpLocateAddressRequestLanguage | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = IpLocateAddressRequestLanguage(_language)

        ip_locate_address_request = cls(
            division=division,
            ip=ip,
            language=language,
        )

        ip_locate_address_request.additional_properties = d
        return ip_locate_address_request

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
