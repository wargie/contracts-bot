from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.founder_party_type import FounderPartyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.decimal_founder_share import DecimalFounderShare
    from ..models.fraction_founder_share import FractionFounderShare
    from ..models.party_invalidity import PartyInvalidity


T = TypeVar("T", bound="FounderParty")


@_attrs_define
class FounderParty:
    """
    Attributes:
        hid (None | str | Unset):
        invalidity (PartyInvalidity | Unset):
        share (DecimalFounderShare | FractionFounderShare | Unset):
        start_date (int | None | Unset):
        type_ (FounderPartyType | Unset):
    """

    hid: None | str | Unset = UNSET
    invalidity: PartyInvalidity | Unset = UNSET
    share: DecimalFounderShare | FractionFounderShare | Unset = UNSET
    start_date: int | None | Unset = UNSET
    type_: FounderPartyType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.decimal_founder_share import DecimalFounderShare

        hid: None | str | Unset
        if isinstance(self.hid, Unset):
            hid = UNSET
        else:
            hid = self.hid

        invalidity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.invalidity, Unset):
            invalidity = self.invalidity.to_dict()

        share: dict[str, Any] | Unset
        if isinstance(self.share, Unset):
            share = UNSET
        elif isinstance(self.share, DecimalFounderShare):
            share = self.share.to_dict()
        else:
            share = self.share.to_dict()

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
        if invalidity is not UNSET:
            field_dict["invalidity"] = invalidity
        if share is not UNSET:
            field_dict["share"] = share
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.decimal_founder_share import DecimalFounderShare
        from ..models.fraction_founder_share import FractionFounderShare
        from ..models.party_invalidity import PartyInvalidity

        d = dict(src_dict)

        def _parse_hid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hid = _parse_hid(d.pop("hid", UNSET))

        _invalidity = d.pop("invalidity", UNSET)
        invalidity: PartyInvalidity | Unset
        if isinstance(_invalidity, Unset):
            invalidity = UNSET
        else:
            invalidity = PartyInvalidity.from_dict(_invalidity)

        def _parse_share(data: object) -> DecimalFounderShare | FractionFounderShare | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                share_type_0 = DecimalFounderShare.from_dict(data)

                return share_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            share_type_1 = FractionFounderShare.from_dict(data)

            return share_type_1

        share = _parse_share(d.pop("share", UNSET))

        def _parse_start_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: FounderPartyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FounderPartyType(_type_)

        founder_party = cls(
            hid=hid,
            invalidity=invalidity,
            share=share,
            start_date=start_date,
            type_=type_,
        )

        founder_party.additional_properties = d
        return founder_party

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
