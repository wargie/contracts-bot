from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.find_affiliated_party_request_scope_type_0_item import (
    FindAffiliatedPartyRequestScopeType0Item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FindAffiliatedPartyRequest")


@_attrs_define
class FindAffiliatedPartyRequest:
    """
    Attributes:
        query (str):
        count (int | None | Unset):  Default: 10.
        scope (list[FindAffiliatedPartyRequestScopeType0Item] | None | Unset):
    """

    query: str
    count: int | None | Unset = 10
    scope: list[FindAffiliatedPartyRequestScopeType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        count: int | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        scope: list[str] | None | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        elif isinstance(self.scope, list):
            scope = []
            for scope_type_0_item_data in self.scope:
                scope_type_0_item = scope_type_0_item_data.value
                scope.append(scope_type_0_item)

        else:
            scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        def _parse_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count = _parse_count(d.pop("count", UNSET))

        def _parse_scope(
            data: object,
        ) -> list[FindAffiliatedPartyRequestScopeType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scope_type_0 = []
                _scope_type_0 = data
                for scope_type_0_item_data in _scope_type_0:
                    scope_type_0_item = FindAffiliatedPartyRequestScopeType0Item(scope_type_0_item_data)

                    scope_type_0.append(scope_type_0_item)

                return scope_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FindAffiliatedPartyRequestScopeType0Item] | None | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))

        find_affiliated_party_request = cls(
            query=query,
            count=count,
            scope=scope,
        )

        find_affiliated_party_request.additional_properties = d
        return find_affiliated_party_request

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
