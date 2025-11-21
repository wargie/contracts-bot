from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.manager_legal_party_type import ManagerLegalPartyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.party_invalidity import PartyInvalidity


T = TypeVar("T", bound="ManagerLegalParty")


@_attrs_define
class ManagerLegalParty:
    """
    Attributes:
        hid (None | str | Unset):
        inn (None | str | Unset):
        invalidity (PartyInvalidity | Unset):
        name (None | str | Unset):
        ogrn (None | str | Unset):
        start_date (int | None | Unset):
        type_ (ManagerLegalPartyType | Unset):
    """

    hid: None | str | Unset = UNSET
    inn: None | str | Unset = UNSET
    invalidity: PartyInvalidity | Unset = UNSET
    name: None | str | Unset = UNSET
    ogrn: None | str | Unset = UNSET
    start_date: int | None | Unset = UNSET
    type_: ManagerLegalPartyType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hid: None | str | Unset
        if isinstance(self.hid, Unset):
            hid = UNSET
        else:
            hid = self.hid

        inn: None | str | Unset
        if isinstance(self.inn, Unset):
            inn = UNSET
        else:
            inn = self.inn

        invalidity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.invalidity, Unset):
            invalidity = self.invalidity.to_dict()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        ogrn: None | str | Unset
        if isinstance(self.ogrn, Unset):
            ogrn = UNSET
        else:
            ogrn = self.ogrn

        start_date: int | None | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hid is not UNSET:
            field_dict["hid"] = hid
        if inn is not UNSET:
            field_dict["inn"] = inn
        if invalidity is not UNSET:
            field_dict["invalidity"] = invalidity
        if name is not UNSET:
            field_dict["name"] = name
        if ogrn is not UNSET:
            field_dict["ogrn"] = ogrn
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.party_invalidity import PartyInvalidity

        d = dict(src_dict)

        def _parse_hid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hid = _parse_hid(d.pop("hid", UNSET))

        def _parse_inn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inn = _parse_inn(d.pop("inn", UNSET))

        _invalidity = d.pop("invalidity", UNSET)
        invalidity: PartyInvalidity | Unset
        if isinstance(_invalidity, Unset):
            invalidity = UNSET
        else:
            invalidity = PartyInvalidity.from_dict(_invalidity)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_ogrn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ogrn = _parse_ogrn(d.pop("ogrn", UNSET))

        def _parse_start_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: ManagerLegalPartyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ManagerLegalPartyType(_type_)

        manager_legal_party = cls(
            hid=hid,
            inn=inn,
            invalidity=invalidity,
            name=name,
            ogrn=ogrn,
            start_date=start_date,
            type_=type_,
        )

        manager_legal_party.additional_properties = d
        return manager_legal_party

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
