from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.party_invalidity_code import PartyInvalidityCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.party_court_decision import PartyCourtDecision


T = TypeVar("T", bound="PartyInvalidity")


@_attrs_define
class PartyInvalidity:
    """
    Attributes:
        code (PartyInvalidityCode):
        decision (PartyCourtDecision | Unset):
    """

    code: PartyInvalidityCode
    decision: PartyCourtDecision | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        decision: dict[str, Any] | Unset = UNSET
        if not isinstance(self.decision, Unset):
            decision = self.decision.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if decision is not UNSET:
            field_dict["decision"] = decision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.party_court_decision import PartyCourtDecision

        d = dict(src_dict)
        code = PartyInvalidityCode(d.pop("code"))

        _decision = d.pop("decision", UNSET)
        decision: PartyCourtDecision | Unset
        if isinstance(_decision, Unset):
            decision = UNSET
        else:
            decision = PartyCourtDecision.from_dict(_decision)

        party_invalidity = cls(
            code=code,
            decision=decision,
        )

        party_invalidity.additional_properties = d
        return party_invalidity

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
