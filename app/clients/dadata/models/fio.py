from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fio_gender import FioGender
from ..types import UNSET, Unset

T = TypeVar("T", bound="Fio")


@_attrs_define
class Fio:
    """
    Attributes:
        gender (FioGender | Unset):
        name (None | str | Unset):
        patronymic (None | str | Unset):
        qc (None | str | Unset):
        source (None | str | Unset):
        surname (None | str | Unset):
    """

    gender: FioGender | Unset = UNSET
    name: None | str | Unset = UNSET
    patronymic: None | str | Unset = UNSET
    qc: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    surname: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gender: str | Unset = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        patronymic: None | str | Unset
        if isinstance(self.patronymic, Unset):
            patronymic = UNSET
        else:
            patronymic = self.patronymic

        qc: None | str | Unset
        if isinstance(self.qc, Unset):
            qc = UNSET
        else:
            qc = self.qc

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        surname: None | str | Unset
        if isinstance(self.surname, Unset):
            surname = UNSET
        else:
            surname = self.surname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gender is not UNSET:
            field_dict["gender"] = gender
        if name is not UNSET:
            field_dict["name"] = name
        if patronymic is not UNSET:
            field_dict["patronymic"] = patronymic
        if qc is not UNSET:
            field_dict["qc"] = qc
        if source is not UNSET:
            field_dict["source"] = source
        if surname is not UNSET:
            field_dict["surname"] = surname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _gender = d.pop("gender", UNSET)
        gender: FioGender | Unset
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = FioGender(_gender)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_patronymic(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        patronymic = _parse_patronymic(d.pop("patronymic", UNSET))

        def _parse_qc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        qc = _parse_qc(d.pop("qc", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_surname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        surname = _parse_surname(d.pop("surname", UNSET))

        fio = cls(
            gender=gender,
            name=name,
            patronymic=patronymic,
            qc=qc,
            source=source,
            surname=surname,
        )

        fio.additional_properties = d
        return fio

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
