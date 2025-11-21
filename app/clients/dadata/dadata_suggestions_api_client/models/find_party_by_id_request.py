from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.find_party_by_id_request_branch_type_type_0_item import FindPartyByIdRequestBranchTypeType0Item
from ..models.find_party_by_id_request_status_type_0_item import FindPartyByIdRequestStatusType0Item
from ..models.find_party_by_id_request_type import FindPartyByIdRequestType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FindPartyByIdRequest")


@_attrs_define
class FindPartyByIdRequest:
    """
    Attributes:
        query (str):
        branch_type (list[FindPartyByIdRequestBranchTypeType0Item] | None | Unset):
        count (int | None | Unset):  Default: 10.
        kpp (None | str | Unset):
        status (list[FindPartyByIdRequestStatusType0Item] | None | Unset):
        type_ (FindPartyByIdRequestType | Unset):
    """

    query: str
    branch_type: list[FindPartyByIdRequestBranchTypeType0Item] | None | Unset = UNSET
    count: int | None | Unset = 10
    kpp: None | str | Unset = UNSET
    status: list[FindPartyByIdRequestStatusType0Item] | None | Unset = UNSET
    type_: FindPartyByIdRequestType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        branch_type: list[str] | None | Unset
        if isinstance(self.branch_type, Unset):
            branch_type = UNSET
        elif isinstance(self.branch_type, list):
            branch_type = []
            for branch_type_type_0_item_data in self.branch_type:
                branch_type_type_0_item = branch_type_type_0_item_data.value
                branch_type.append(branch_type_type_0_item)

        else:
            branch_type = self.branch_type

        count: int | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        kpp: None | str | Unset
        if isinstance(self.kpp, Unset):
            kpp = UNSET
        else:
            kpp = self.kpp

        status: list[str] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, list):
            status = []
            for status_type_0_item_data in self.status:
                status_type_0_item = status_type_0_item_data.value
                status.append(status_type_0_item)

        else:
            status = self.status

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if branch_type is not UNSET:
            field_dict["branch_type"] = branch_type
        if count is not UNSET:
            field_dict["count"] = count
        if kpp is not UNSET:
            field_dict["kpp"] = kpp
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        def _parse_branch_type(data: object) -> list[FindPartyByIdRequestBranchTypeType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                branch_type_type_0 = []
                _branch_type_type_0 = data
                for branch_type_type_0_item_data in _branch_type_type_0:
                    branch_type_type_0_item = FindPartyByIdRequestBranchTypeType0Item(branch_type_type_0_item_data)

                    branch_type_type_0.append(branch_type_type_0_item)

                return branch_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FindPartyByIdRequestBranchTypeType0Item] | None | Unset, data)

        branch_type = _parse_branch_type(d.pop("branch_type", UNSET))

        def _parse_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count = _parse_count(d.pop("count", UNSET))

        def _parse_kpp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kpp = _parse_kpp(d.pop("kpp", UNSET))

        def _parse_status(data: object) -> list[FindPartyByIdRequestStatusType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                status_type_0 = []
                _status_type_0 = data
                for status_type_0_item_data in _status_type_0:
                    status_type_0_item = FindPartyByIdRequestStatusType0Item(status_type_0_item_data)

                    status_type_0.append(status_type_0_item)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FindPartyByIdRequestStatusType0Item] | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: FindPartyByIdRequestType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FindPartyByIdRequestType(_type_)

        find_party_by_id_request = cls(
            query=query,
            branch_type=branch_type,
            count=count,
            kpp=kpp,
            status=status,
            type_=type_,
        )

        find_party_by_id_request.additional_properties = d
        return find_party_by_id_request

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
