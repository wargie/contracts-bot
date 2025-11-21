from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.suggestion_fias_address import SuggestionFiasAddress


T = TypeVar("T", bound="SuggestResponseFiasAddress")


@_attrs_define
class SuggestResponseFiasAddress:
    """
    Attributes:
        suggestions (list[SuggestionFiasAddress] | None | Unset):
    """

    suggestions: list[SuggestionFiasAddress] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        suggestions: list[dict[str, Any]] | None | Unset
        if isinstance(self.suggestions, Unset):
            suggestions = UNSET
        elif isinstance(self.suggestions, list):
            suggestions = []
            for suggestions_type_0_item_data in self.suggestions:
                suggestions_type_0_item = suggestions_type_0_item_data.to_dict()
                suggestions.append(suggestions_type_0_item)

        else:
            suggestions = self.suggestions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.suggestion_fias_address import SuggestionFiasAddress

        d = dict(src_dict)

        def _parse_suggestions(
            data: object,
        ) -> list[SuggestionFiasAddress] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                suggestions_type_0 = []
                _suggestions_type_0 = data
                for suggestions_type_0_item_data in _suggestions_type_0:
                    suggestions_type_0_item = SuggestionFiasAddress.from_dict(suggestions_type_0_item_data)

                    suggestions_type_0.append(suggestions_type_0_item)

                return suggestions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SuggestionFiasAddress] | None | Unset, data)

        suggestions = _parse_suggestions(d.pop("suggestions", UNSET))

        suggest_response_fias_address = cls(
            suggestions=suggestions,
        )

        suggest_response_fias_address.additional_properties = d
        return suggest_response_fias_address

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
