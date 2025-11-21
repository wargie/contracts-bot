from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bound import Bound


T = TypeVar("T", bound="FindFiasByIdRequest")


@_attrs_define
class FindFiasByIdRequest:
    """
    Attributes:
        query (str):
        count (int | None | Unset):  Default: 10.
        from_bound (Bound | Unset):
        to_bound (Bound | Unset):
    """

    query: str
    count: int | None | Unset = 10
    from_bound: Bound | Unset = UNSET
    to_bound: Bound | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        count: int | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        from_bound: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_bound, Unset):
            from_bound = self.from_bound.to_dict()

        to_bound: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_bound, Unset):
            to_bound = self.to_bound.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count
        if from_bound is not UNSET:
            field_dict["from_bound"] = from_bound
        if to_bound is not UNSET:
            field_dict["to_bound"] = to_bound

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bound import Bound

        d = dict(src_dict)
        query = d.pop("query")

        def _parse_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count = _parse_count(d.pop("count", UNSET))

        _from_bound = d.pop("from_bound", UNSET)
        from_bound: Bound | Unset
        if isinstance(_from_bound, Unset):
            from_bound = UNSET
        else:
            from_bound = Bound.from_dict(_from_bound)

        _to_bound = d.pop("to_bound", UNSET)
        to_bound: Bound | Unset
        if isinstance(_to_bound, Unset):
            to_bound = UNSET
        else:
            to_bound = Bound.from_dict(_to_bound)

        find_fias_by_id_request = cls(
            query=query,
            count=count,
            from_bound=from_bound,
            to_bound=to_bound,
        )

        find_fias_by_id_request.additional_properties = d
        return find_fias_by_id_request

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
