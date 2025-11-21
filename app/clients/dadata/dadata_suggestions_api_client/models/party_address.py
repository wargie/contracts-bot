from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.party_invalidity import PartyInvalidity


T = TypeVar("T", bound="PartyAddress")


@_attrs_define
class PartyAddress:
    """
    Attributes:
        data (Address | Unset):
        invalidity (PartyInvalidity | Unset):
        unrestricted_value (None | str | Unset):
        value (None | str | Unset):
    """

    data: Address | Unset = UNSET
    invalidity: PartyInvalidity | Unset = UNSET
    unrestricted_value: None | str | Unset = UNSET
    value: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        invalidity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.invalidity, Unset):
            invalidity = self.invalidity.to_dict()

        unrestricted_value: None | str | Unset
        if isinstance(self.unrestricted_value, Unset):
            unrestricted_value = UNSET
        else:
            unrestricted_value = self.unrestricted_value

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if invalidity is not UNSET:
            field_dict["invalidity"] = invalidity
        if unrestricted_value is not UNSET:
            field_dict["unrestricted_value"] = unrestricted_value
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.party_invalidity import PartyInvalidity

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Address | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = Address.from_dict(_data)

        _invalidity = d.pop("invalidity", UNSET)
        invalidity: PartyInvalidity | Unset
        if isinstance(_invalidity, Unset):
            invalidity = UNSET
        else:
            invalidity = PartyInvalidity.from_dict(_invalidity)

        def _parse_unrestricted_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unrestricted_value = _parse_unrestricted_value(d.pop("unrestricted_value", UNSET))

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        party_address = cls(
            data=data,
            invalidity=invalidity,
            unrestricted_value=unrestricted_value,
            value=value,
        )

        party_address.additional_properties = d
        return party_address

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
