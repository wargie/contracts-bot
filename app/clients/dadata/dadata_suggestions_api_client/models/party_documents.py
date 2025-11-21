from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.party_document import PartyDocument
    from ..models.party_smb_document import PartySmbDocument


T = TypeVar("T", bound="PartyDocuments")


@_attrs_define
class PartyDocuments:
    """
    Attributes:
        fts_registration (PartyDocument | Unset):
        fts_report (PartyDocument | Unset):
        pf_registration (PartyDocument | Unset):
        sif_registration (PartyDocument | Unset):
        smb (PartySmbDocument | Unset):
    """

    fts_registration: PartyDocument | Unset = UNSET
    fts_report: PartyDocument | Unset = UNSET
    pf_registration: PartyDocument | Unset = UNSET
    sif_registration: PartyDocument | Unset = UNSET
    smb: PartySmbDocument | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fts_registration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fts_registration, Unset):
            fts_registration = self.fts_registration.to_dict()

        fts_report: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fts_report, Unset):
            fts_report = self.fts_report.to_dict()

        pf_registration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pf_registration, Unset):
            pf_registration = self.pf_registration.to_dict()

        sif_registration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sif_registration, Unset):
            sif_registration = self.sif_registration.to_dict()

        smb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.smb, Unset):
            smb = self.smb.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fts_registration is not UNSET:
            field_dict["fts_registration"] = fts_registration
        if fts_report is not UNSET:
            field_dict["fts_report"] = fts_report
        if pf_registration is not UNSET:
            field_dict["pf_registration"] = pf_registration
        if sif_registration is not UNSET:
            field_dict["sif_registration"] = sif_registration
        if smb is not UNSET:
            field_dict["smb"] = smb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.party_document import PartyDocument
        from ..models.party_smb_document import PartySmbDocument

        d = dict(src_dict)
        _fts_registration = d.pop("fts_registration", UNSET)
        fts_registration: PartyDocument | Unset
        if isinstance(_fts_registration, Unset):
            fts_registration = UNSET
        else:
            fts_registration = PartyDocument.from_dict(_fts_registration)

        _fts_report = d.pop("fts_report", UNSET)
        fts_report: PartyDocument | Unset
        if isinstance(_fts_report, Unset):
            fts_report = UNSET
        else:
            fts_report = PartyDocument.from_dict(_fts_report)

        _pf_registration = d.pop("pf_registration", UNSET)
        pf_registration: PartyDocument | Unset
        if isinstance(_pf_registration, Unset):
            pf_registration = UNSET
        else:
            pf_registration = PartyDocument.from_dict(_pf_registration)

        _sif_registration = d.pop("sif_registration", UNSET)
        sif_registration: PartyDocument | Unset
        if isinstance(_sif_registration, Unset):
            sif_registration = UNSET
        else:
            sif_registration = PartyDocument.from_dict(_sif_registration)

        _smb = d.pop("smb", UNSET)
        smb: PartySmbDocument | Unset
        if isinstance(_smb, Unset):
            smb = UNSET
        else:
            smb = PartySmbDocument.from_dict(_smb)

        party_documents = cls(
            fts_registration=fts_registration,
            fts_report=fts_report,
            pf_registration=pf_registration,
            sif_registration=sif_registration,
            smb=smb,
        )

        party_documents.additional_properties = d
        return party_documents

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
