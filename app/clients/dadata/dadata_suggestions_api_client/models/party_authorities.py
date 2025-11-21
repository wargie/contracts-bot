from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.party_authority import PartyAuthority


T = TypeVar("T", bound="PartyAuthorities")


@_attrs_define
class PartyAuthorities:
    """
    Attributes:
        fts_registration (PartyAuthority | Unset):
        fts_report (PartyAuthority | Unset):
        pf (PartyAuthority | Unset):
        sif (PartyAuthority | Unset):
    """

    fts_registration: PartyAuthority | Unset = UNSET
    fts_report: PartyAuthority | Unset = UNSET
    pf: PartyAuthority | Unset = UNSET
    sif: PartyAuthority | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fts_registration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fts_registration, Unset):
            fts_registration = self.fts_registration.to_dict()

        fts_report: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fts_report, Unset):
            fts_report = self.fts_report.to_dict()

        pf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pf, Unset):
            pf = self.pf.to_dict()

        sif: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sif, Unset):
            sif = self.sif.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fts_registration is not UNSET:
            field_dict["fts_registration"] = fts_registration
        if fts_report is not UNSET:
            field_dict["fts_report"] = fts_report
        if pf is not UNSET:
            field_dict["pf"] = pf
        if sif is not UNSET:
            field_dict["sif"] = sif

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.party_authority import PartyAuthority

        d = dict(src_dict)
        _fts_registration = d.pop("fts_registration", UNSET)
        fts_registration: PartyAuthority | Unset
        if isinstance(_fts_registration, Unset):
            fts_registration = UNSET
        else:
            fts_registration = PartyAuthority.from_dict(_fts_registration)

        _fts_report = d.pop("fts_report", UNSET)
        fts_report: PartyAuthority | Unset
        if isinstance(_fts_report, Unset):
            fts_report = UNSET
        else:
            fts_report = PartyAuthority.from_dict(_fts_report)

        _pf = d.pop("pf", UNSET)
        pf: PartyAuthority | Unset
        if isinstance(_pf, Unset):
            pf = UNSET
        else:
            pf = PartyAuthority.from_dict(_pf)

        _sif = d.pop("sif", UNSET)
        sif: PartyAuthority | Unset
        if isinstance(_sif, Unset):
            sif = UNSET
        else:
            sif = PartyAuthority.from_dict(_sif)

        party_authorities = cls(
            fts_registration=fts_registration,
            fts_report=fts_report,
            pf=pf,
            sif=sif,
        )

        party_authorities.additional_properties = d
        return party_authorities

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
