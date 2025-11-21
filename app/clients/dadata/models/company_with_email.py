from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company import Company
    from ..models.email import Email


T = TypeVar("T", bound="CompanyWithEmail")


@_attrs_define
class CompanyWithEmail:
    """
    Attributes:
        company (Company | Unset):
        email (Email | Unset):
    """

    company: Company | Unset = UNSET
    email: Email | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company: dict[str, Any] | Unset = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict()

        email: dict[str, Any] | Unset = UNSET
        if not isinstance(self.email, Unset):
            email = self.email.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company is not UNSET:
            field_dict["company"] = company
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company import Company
        from ..models.email import Email

        d = dict(src_dict)
        _company = d.pop("company", UNSET)
        company: Company | Unset
        if isinstance(_company, Unset):
            company = UNSET
        else:
            company = Company.from_dict(_company)

        _email = d.pop("email", UNSET)
        email: Email | Unset
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = Email.from_dict(_email)

        company_with_email = cls(
            company=company,
            email=email,
        )

        company_with_email.additional_properties = d
        return company_with_email

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
