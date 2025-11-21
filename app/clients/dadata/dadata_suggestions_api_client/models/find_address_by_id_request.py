from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.find_address_by_id_request_division import FindAddressByIdRequestDivision
from ..models.find_address_by_id_request_language import FindAddressByIdRequestLanguage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bound import Bound


T = TypeVar("T", bound="FindAddressByIdRequest")


@_attrs_define
class FindAddressByIdRequest:
    """
    Attributes:
        query (str):
        count (int | None | Unset):  Default: 10.
        division (FindAddressByIdRequestDivision | Unset):
        from_bound (Bound | Unset):
        language (FindAddressByIdRequestLanguage | Unset):
        to_bound (Bound | Unset):
    """

    query: str
    count: int | None | Unset = 10
    division: FindAddressByIdRequestDivision | Unset = UNSET
    from_bound: Bound | Unset = UNSET
    language: FindAddressByIdRequestLanguage | Unset = UNSET
    to_bound: Bound | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        count: int | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        division: str | Unset = UNSET
        if not isinstance(self.division, Unset):
            division = self.division.value

        from_bound: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_bound, Unset):
            from_bound = self.from_bound.to_dict()

        language: str | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

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
        if division is not UNSET:
            field_dict["division"] = division
        if from_bound is not UNSET:
            field_dict["from_bound"] = from_bound
        if language is not UNSET:
            field_dict["language"] = language
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

        _division = d.pop("division", UNSET)
        division: FindAddressByIdRequestDivision | Unset
        if isinstance(_division, Unset):
            division = UNSET
        else:
            division = FindAddressByIdRequestDivision(_division)

        _from_bound = d.pop("from_bound", UNSET)
        from_bound: Bound | Unset
        if isinstance(_from_bound, Unset):
            from_bound = UNSET
        else:
            from_bound = Bound.from_dict(_from_bound)

        _language = d.pop("language", UNSET)
        language: FindAddressByIdRequestLanguage | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = FindAddressByIdRequestLanguage(_language)

        _to_bound = d.pop("to_bound", UNSET)
        to_bound: Bound | Unset
        if isinstance(_to_bound, Unset):
            to_bound = UNSET
        else:
            to_bound = Bound.from_dict(_to_bound)

        find_address_by_id_request = cls(
            query=query,
            count=count,
            division=division,
            from_bound=from_bound,
            language=language,
            to_bound=to_bound,
        )

        find_address_by_id_request.additional_properties = d
        return find_address_by_id_request

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
