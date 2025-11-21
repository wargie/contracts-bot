from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bank_name import BankName
    from ..models.bank_opf import BankOpf
    from ..models.bank_state import BankState
    from ..models.suggestion_address import SuggestionAddress
    from ..models.suggestion_phone import SuggestionPhone


T = TypeVar("T", bound="BankParty")


@_attrs_define
class BankParty:
    """
    Attributes:
        name (BankName):
        opf (BankOpf):
        state (BankState):
        address (SuggestionAddress | Unset):
        bic (None | str | Unset):
        cbr (BankParty | Unset):
        correspondent_account (None | str | Unset):
        inn (None | str | Unset):
        kpp (None | str | Unset):
        okpo (None | str | Unset):
        payment_city (None | str | Unset):
        phones (list[SuggestionPhone] | None | Unset):
        registration_number (None | str | Unset):
        rkc (BankParty | Unset):
        swift (None | str | Unset):
        treasury_accounts (list[str] | None | Unset):
    """

    name: BankName
    opf: BankOpf
    state: BankState
    address: SuggestionAddress | Unset = UNSET
    bic: None | str | Unset = UNSET
    cbr: BankParty | Unset = UNSET
    correspondent_account: None | str | Unset = UNSET
    inn: None | str | Unset = UNSET
    kpp: None | str | Unset = UNSET
    okpo: None | str | Unset = UNSET
    payment_city: None | str | Unset = UNSET
    phones: list[SuggestionPhone] | None | Unset = UNSET
    registration_number: None | str | Unset = UNSET
    rkc: BankParty | Unset = UNSET
    swift: None | str | Unset = UNSET
    treasury_accounts: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name.to_dict()

        opf = self.opf.to_dict()

        state = self.state.to_dict()

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        bic: None | str | Unset
        if isinstance(self.bic, Unset):
            bic = UNSET
        else:
            bic = self.bic

        cbr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cbr, Unset):
            cbr = self.cbr.to_dict()

        correspondent_account: None | str | Unset
        if isinstance(self.correspondent_account, Unset):
            correspondent_account = UNSET
        else:
            correspondent_account = self.correspondent_account

        inn: None | str | Unset
        if isinstance(self.inn, Unset):
            inn = UNSET
        else:
            inn = self.inn

        kpp: None | str | Unset
        if isinstance(self.kpp, Unset):
            kpp = UNSET
        else:
            kpp = self.kpp

        okpo: None | str | Unset
        if isinstance(self.okpo, Unset):
            okpo = UNSET
        else:
            okpo = self.okpo

        payment_city: None | str | Unset
        if isinstance(self.payment_city, Unset):
            payment_city = UNSET
        else:
            payment_city = self.payment_city

        phones: list[dict[str, Any]] | None | Unset
        if isinstance(self.phones, Unset):
            phones = UNSET
        elif isinstance(self.phones, list):
            phones = []
            for phones_type_0_item_data in self.phones:
                phones_type_0_item = phones_type_0_item_data.to_dict()
                phones.append(phones_type_0_item)

        else:
            phones = self.phones

        registration_number: None | str | Unset
        if isinstance(self.registration_number, Unset):
            registration_number = UNSET
        else:
            registration_number = self.registration_number

        rkc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rkc, Unset):
            rkc = self.rkc.to_dict()

        swift: None | str | Unset
        if isinstance(self.swift, Unset):
            swift = UNSET
        else:
            swift = self.swift

        treasury_accounts: list[str] | None | Unset
        if isinstance(self.treasury_accounts, Unset):
            treasury_accounts = UNSET
        elif isinstance(self.treasury_accounts, list):
            treasury_accounts = self.treasury_accounts

        else:
            treasury_accounts = self.treasury_accounts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "opf": opf,
                "state": state,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if bic is not UNSET:
            field_dict["bic"] = bic
        if cbr is not UNSET:
            field_dict["cbr"] = cbr
        if correspondent_account is not UNSET:
            field_dict["correspondent_account"] = correspondent_account
        if inn is not UNSET:
            field_dict["inn"] = inn
        if kpp is not UNSET:
            field_dict["kpp"] = kpp
        if okpo is not UNSET:
            field_dict["okpo"] = okpo
        if payment_city is not UNSET:
            field_dict["payment_city"] = payment_city
        if phones is not UNSET:
            field_dict["phones"] = phones
        if registration_number is not UNSET:
            field_dict["registration_number"] = registration_number
        if rkc is not UNSET:
            field_dict["rkc"] = rkc
        if swift is not UNSET:
            field_dict["swift"] = swift
        if treasury_accounts is not UNSET:
            field_dict["treasury_accounts"] = treasury_accounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bank_name import BankName
        from ..models.bank_opf import BankOpf
        from ..models.bank_state import BankState
        from ..models.suggestion_address import SuggestionAddress
        from ..models.suggestion_phone import SuggestionPhone

        d = dict(src_dict)
        name = BankName.from_dict(d.pop("name"))

        opf = BankOpf.from_dict(d.pop("opf"))

        state = BankState.from_dict(d.pop("state"))

        _address = d.pop("address", UNSET)
        address: SuggestionAddress | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = SuggestionAddress.from_dict(_address)

        def _parse_bic(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bic = _parse_bic(d.pop("bic", UNSET))

        _cbr = d.pop("cbr", UNSET)
        cbr: BankParty | Unset
        if isinstance(_cbr, Unset):
            cbr = UNSET
        else:
            cbr = BankParty.from_dict(_cbr)

        def _parse_correspondent_account(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        correspondent_account = _parse_correspondent_account(d.pop("correspondent_account", UNSET))

        def _parse_inn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inn = _parse_inn(d.pop("inn", UNSET))

        def _parse_kpp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kpp = _parse_kpp(d.pop("kpp", UNSET))

        def _parse_okpo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        okpo = _parse_okpo(d.pop("okpo", UNSET))

        def _parse_payment_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_city = _parse_payment_city(d.pop("payment_city", UNSET))

        def _parse_phones(data: object) -> list[SuggestionPhone] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                phones_type_0 = []
                _phones_type_0 = data
                for phones_type_0_item_data in _phones_type_0:
                    phones_type_0_item = SuggestionPhone.from_dict(phones_type_0_item_data)

                    phones_type_0.append(phones_type_0_item)

                return phones_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SuggestionPhone] | None | Unset, data)

        phones = _parse_phones(d.pop("phones", UNSET))

        def _parse_registration_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_number = _parse_registration_number(d.pop("registration_number", UNSET))

        _rkc = d.pop("rkc", UNSET)
        rkc: BankParty | Unset
        if isinstance(_rkc, Unset):
            rkc = UNSET
        else:
            rkc = BankParty.from_dict(_rkc)

        def _parse_swift(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        swift = _parse_swift(d.pop("swift", UNSET))

        def _parse_treasury_accounts(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                treasury_accounts_type_0 = cast(list[str], data)

                return treasury_accounts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        treasury_accounts = _parse_treasury_accounts(d.pop("treasury_accounts", UNSET))

        bank_party = cls(
            name=name,
            opf=opf,
            state=state,
            address=address,
            bic=bic,
            cbr=cbr,
            correspondent_account=correspondent_account,
            inn=inn,
            kpp=kpp,
            okpo=okpo,
            payment_city=payment_city,
            phones=phones,
            registration_number=registration_number,
            rkc=rkc,
            swift=swift,
            treasury_accounts=treasury_accounts,
        )

        bank_party.additional_properties = d
        return bank_party

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
