from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.manager_physical_party_type import ManagerPhysicalPartyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fio import Fio
    from ..models.party_invalidity import PartyInvalidity


T = TypeVar("T", bound="ManagerPhysicalParty")


@_attrs_define
class ManagerPhysicalParty:
    """
    Attributes:
        fio (Fio | Unset):
        hid (None | str | Unset):
        inn (None | str | Unset):
        invalidity (PartyInvalidity | Unset):
        post (None | str | Unset):
        start_date (int | None | Unset):
        type_ (ManagerPhysicalPartyType | Unset):
    """

    fio: Fio | Unset = UNSET
    hid: None | str | Unset = UNSET
    inn: None | str | Unset = UNSET
    invalidity: PartyInvalidity | Unset = UNSET
    post: None | str | Unset = UNSET
    start_date: int | None | Unset = UNSET
    type_: ManagerPhysicalPartyType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fio: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fio, Unset):
            fio = self.fio.to_dict()

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

        post: None | str | Unset
        if isinstance(self.post, Unset):
            post = UNSET
        else:
            post = self.post

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
        if fio is not UNSET:
            field_dict["fio"] = fio
        if hid is not UNSET:
            field_dict["hid"] = hid
        if inn is not UNSET:
            field_dict["inn"] = inn
        if invalidity is not UNSET:
            field_dict["invalidity"] = invalidity
        if post is not UNSET:
            field_dict["post"] = post
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fio import Fio
        from ..models.party_invalidity import PartyInvalidity

        d = dict(src_dict)
        _fio = d.pop("fio", UNSET)
        fio: Fio | Unset
        if isinstance(_fio, Unset):
            fio = UNSET
        else:
            fio = Fio.from_dict(_fio)

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

        def _parse_post(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post = _parse_post(d.pop("post", UNSET))

        def _parse_start_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: ManagerPhysicalPartyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ManagerPhysicalPartyType(_type_)

        manager_physical_party = cls(
            fio=fio,
            hid=hid,
            inn=inn,
            invalidity=invalidity,
            post=post,
            start_date=start_date,
            type_=type_,
        )

        manager_physical_party.additional_properties = d
        return manager_physical_party

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
