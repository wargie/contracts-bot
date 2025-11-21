from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.individual_party_type import IndividualPartyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fio import Fio
    from ..models.party_address import PartyAddress
    from ..models.party_authorities import PartyAuthorities
    from ..models.party_country import PartyCountry
    from ..models.party_documents import PartyDocuments
    from ..models.party_finance import PartyFinance
    from ..models.party_license import PartyLicense
    from ..models.party_name import PartyName
    from ..models.party_okved import PartyOkved
    from ..models.party_opf import PartyOpf
    from ..models.party_state import PartyState
    from ..models.suggestion_email import SuggestionEmail
    from ..models.suggestion_party_phone import SuggestionPartyPhone


T = TypeVar("T", bound="IndividualParty")


@_attrs_define
class IndividualParty:
    """
    Attributes:
        name (PartyName):
        state (PartyState):
        type_ (IndividualPartyType):
        address (PartyAddress | Unset):
        authorities (PartyAuthorities | Unset):
        citizenship (PartyCountry | Unset):
        documents (PartyDocuments | Unset):
        emails (list[SuggestionEmail] | None | Unset):
        employee_count (int | None | Unset):
        finance (PartyFinance | Unset):
        fio (Fio | Unset):
        hid (None | str | Unset):
        inn (None | str | Unset):
        licenses (list[PartyLicense] | None | Unset):
        ogrn (None | str | Unset):
        ogrn_date (int | None | Unset):
        okato (None | str | Unset):
        okfs (None | str | Unset):
        okogu (None | str | Unset):
        okpo (None | str | Unset):
        oktmo (None | str | Unset):
        okved (None | str | Unset):
        okved_type (None | str | Unset):
        okveds (list[PartyOkved] | None | Unset):
        opf (PartyOpf | Unset):
        phones (list[SuggestionPartyPhone] | None | Unset):
        qc (None | str | Unset):
        source (None | str | Unset):
    """

    name: PartyName
    state: PartyState
    type_: IndividualPartyType
    address: PartyAddress | Unset = UNSET
    authorities: PartyAuthorities | Unset = UNSET
    citizenship: PartyCountry | Unset = UNSET
    documents: PartyDocuments | Unset = UNSET
    emails: list[SuggestionEmail] | None | Unset = UNSET
    employee_count: int | None | Unset = UNSET
    finance: PartyFinance | Unset = UNSET
    fio: Fio | Unset = UNSET
    hid: None | str | Unset = UNSET
    inn: None | str | Unset = UNSET
    licenses: list[PartyLicense] | None | Unset = UNSET
    ogrn: None | str | Unset = UNSET
    ogrn_date: int | None | Unset = UNSET
    okato: None | str | Unset = UNSET
    okfs: None | str | Unset = UNSET
    okogu: None | str | Unset = UNSET
    okpo: None | str | Unset = UNSET
    oktmo: None | str | Unset = UNSET
    okved: None | str | Unset = UNSET
    okved_type: None | str | Unset = UNSET
    okveds: list[PartyOkved] | None | Unset = UNSET
    opf: PartyOpf | Unset = UNSET
    phones: list[SuggestionPartyPhone] | None | Unset = UNSET
    qc: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name.to_dict()

        state = self.state.to_dict()

        type_ = self.type_.value

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        authorities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authorities, Unset):
            authorities = self.authorities.to_dict()

        citizenship: dict[str, Any] | Unset = UNSET
        if not isinstance(self.citizenship, Unset):
            citizenship = self.citizenship.to_dict()

        documents: dict[str, Any] | Unset = UNSET
        if not isinstance(self.documents, Unset):
            documents = self.documents.to_dict()

        emails: list[dict[str, Any]] | None | Unset
        if isinstance(self.emails, Unset):
            emails = UNSET
        elif isinstance(self.emails, list):
            emails = []
            for emails_type_0_item_data in self.emails:
                emails_type_0_item = emails_type_0_item_data.to_dict()
                emails.append(emails_type_0_item)

        else:
            emails = self.emails

        employee_count: int | None | Unset
        if isinstance(self.employee_count, Unset):
            employee_count = UNSET
        else:
            employee_count = self.employee_count

        finance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.finance, Unset):
            finance = self.finance.to_dict()

        fio: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fio, Unset):
            fio = self.fio.to_dict()

        hid: None | str | Unset
        if isinstance(self.hid, Unset):
            hid = UNSET
        else:
            hid = self.hid

        inn: None | str | Unset
        if isinstance(self.inn, Unset):
            inn = UNSET
        else:
            inn = self.inn

        licenses: list[dict[str, Any]] | None | Unset
        if isinstance(self.licenses, Unset):
            licenses = UNSET
        elif isinstance(self.licenses, list):
            licenses = []
            for licenses_type_0_item_data in self.licenses:
                licenses_type_0_item = licenses_type_0_item_data.to_dict()
                licenses.append(licenses_type_0_item)

        else:
            licenses = self.licenses

        ogrn: None | str | Unset
        if isinstance(self.ogrn, Unset):
            ogrn = UNSET
        else:
            ogrn = self.ogrn

        ogrn_date: int | None | Unset
        if isinstance(self.ogrn_date, Unset):
            ogrn_date = UNSET
        else:
            ogrn_date = self.ogrn_date

        okato: None | str | Unset
        if isinstance(self.okato, Unset):
            okato = UNSET
        else:
            okato = self.okato

        okfs: None | str | Unset
        if isinstance(self.okfs, Unset):
            okfs = UNSET
        else:
            okfs = self.okfs

        okogu: None | str | Unset
        if isinstance(self.okogu, Unset):
            okogu = UNSET
        else:
            okogu = self.okogu

        okpo: None | str | Unset
        if isinstance(self.okpo, Unset):
            okpo = UNSET
        else:
            okpo = self.okpo

        oktmo: None | str | Unset
        if isinstance(self.oktmo, Unset):
            oktmo = UNSET
        else:
            oktmo = self.oktmo

        okved: None | str | Unset
        if isinstance(self.okved, Unset):
            okved = UNSET
        else:
            okved = self.okved

        okved_type: None | str | Unset
        if isinstance(self.okved_type, Unset):
            okved_type = UNSET
        else:
            okved_type = self.okved_type

        okveds: list[dict[str, Any]] | None | Unset
        if isinstance(self.okveds, Unset):
            okveds = UNSET
        elif isinstance(self.okveds, list):
            okveds = []
            for okveds_type_0_item_data in self.okveds:
                okveds_type_0_item = okveds_type_0_item_data.to_dict()
                okveds.append(okveds_type_0_item)

        else:
            okveds = self.okveds

        opf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.opf, Unset):
            opf = self.opf.to_dict()

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "state": state,
                "type": type_,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if authorities is not UNSET:
            field_dict["authorities"] = authorities
        if citizenship is not UNSET:
            field_dict["citizenship"] = citizenship
        if documents is not UNSET:
            field_dict["documents"] = documents
        if emails is not UNSET:
            field_dict["emails"] = emails
        if employee_count is not UNSET:
            field_dict["employee_count"] = employee_count
        if finance is not UNSET:
            field_dict["finance"] = finance
        if fio is not UNSET:
            field_dict["fio"] = fio
        if hid is not UNSET:
            field_dict["hid"] = hid
        if inn is not UNSET:
            field_dict["inn"] = inn
        if licenses is not UNSET:
            field_dict["licenses"] = licenses
        if ogrn is not UNSET:
            field_dict["ogrn"] = ogrn
        if ogrn_date is not UNSET:
            field_dict["ogrn_date"] = ogrn_date
        if okato is not UNSET:
            field_dict["okato"] = okato
        if okfs is not UNSET:
            field_dict["okfs"] = okfs
        if okogu is not UNSET:
            field_dict["okogu"] = okogu
        if okpo is not UNSET:
            field_dict["okpo"] = okpo
        if oktmo is not UNSET:
            field_dict["oktmo"] = oktmo
        if okved is not UNSET:
            field_dict["okved"] = okved
        if okved_type is not UNSET:
            field_dict["okved_type"] = okved_type
        if okveds is not UNSET:
            field_dict["okveds"] = okveds
        if opf is not UNSET:
            field_dict["opf"] = opf
        if phones is not UNSET:
            field_dict["phones"] = phones
        if qc is not UNSET:
            field_dict["qc"] = qc
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fio import Fio
        from ..models.party_address import PartyAddress
        from ..models.party_authorities import PartyAuthorities
        from ..models.party_country import PartyCountry
        from ..models.party_documents import PartyDocuments
        from ..models.party_finance import PartyFinance
        from ..models.party_license import PartyLicense
        from ..models.party_name import PartyName
        from ..models.party_okved import PartyOkved
        from ..models.party_opf import PartyOpf
        from ..models.party_state import PartyState
        from ..models.suggestion_email import SuggestionEmail
        from ..models.suggestion_party_phone import SuggestionPartyPhone

        d = dict(src_dict)
        name = PartyName.from_dict(d.pop("name"))

        state = PartyState.from_dict(d.pop("state"))

        type_ = IndividualPartyType(d.pop("type"))

        _address = d.pop("address", UNSET)
        address: PartyAddress | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = PartyAddress.from_dict(_address)

        _authorities = d.pop("authorities", UNSET)
        authorities: PartyAuthorities | Unset
        if isinstance(_authorities, Unset):
            authorities = UNSET
        else:
            authorities = PartyAuthorities.from_dict(_authorities)

        _citizenship = d.pop("citizenship", UNSET)
        citizenship: PartyCountry | Unset
        if isinstance(_citizenship, Unset):
            citizenship = UNSET
        else:
            citizenship = PartyCountry.from_dict(_citizenship)

        _documents = d.pop("documents", UNSET)
        documents: PartyDocuments | Unset
        if isinstance(_documents, Unset):
            documents = UNSET
        else:
            documents = PartyDocuments.from_dict(_documents)

        def _parse_emails(data: object) -> list[SuggestionEmail] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                emails_type_0 = []
                _emails_type_0 = data
                for emails_type_0_item_data in _emails_type_0:
                    emails_type_0_item = SuggestionEmail.from_dict(emails_type_0_item_data)

                    emails_type_0.append(emails_type_0_item)

                return emails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SuggestionEmail] | None | Unset, data)

        emails = _parse_emails(d.pop("emails", UNSET))

        def _parse_employee_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        employee_count = _parse_employee_count(d.pop("employee_count", UNSET))

        _finance = d.pop("finance", UNSET)
        finance: PartyFinance | Unset
        if isinstance(_finance, Unset):
            finance = UNSET
        else:
            finance = PartyFinance.from_dict(_finance)

        _fio = d.pop("fio", UNSET)
        fio: Fio | Unset
        if isinstance(_fio, Unset):
            fio = UNSET
        else:
            fio = Fio.from_dict(_fio)

        def _parse_hid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hid = _parse_hid(d.pop("hid", UNSET))

        def _parse_inn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inn = _parse_inn(d.pop("inn", UNSET))

        def _parse_licenses(data: object) -> list[PartyLicense] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                licenses_type_0 = []
                _licenses_type_0 = data
                for licenses_type_0_item_data in _licenses_type_0:
                    licenses_type_0_item = PartyLicense.from_dict(licenses_type_0_item_data)

                    licenses_type_0.append(licenses_type_0_item)

                return licenses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PartyLicense] | None | Unset, data)

        licenses = _parse_licenses(d.pop("licenses", UNSET))

        def _parse_ogrn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ogrn = _parse_ogrn(d.pop("ogrn", UNSET))

        def _parse_ogrn_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ogrn_date = _parse_ogrn_date(d.pop("ogrn_date", UNSET))

        def _parse_okato(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        okato = _parse_okato(d.pop("okato", UNSET))

        def _parse_okfs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        okfs = _parse_okfs(d.pop("okfs", UNSET))

        def _parse_okogu(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        okogu = _parse_okogu(d.pop("okogu", UNSET))

        def _parse_okpo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        okpo = _parse_okpo(d.pop("okpo", UNSET))

        def _parse_oktmo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        oktmo = _parse_oktmo(d.pop("oktmo", UNSET))

        def _parse_okved(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        okved = _parse_okved(d.pop("okved", UNSET))

        def _parse_okved_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        okved_type = _parse_okved_type(d.pop("okved_type", UNSET))

        def _parse_okveds(data: object) -> list[PartyOkved] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                okveds_type_0 = []
                _okveds_type_0 = data
                for okveds_type_0_item_data in _okveds_type_0:
                    okveds_type_0_item = PartyOkved.from_dict(okveds_type_0_item_data)

                    okveds_type_0.append(okveds_type_0_item)

                return okveds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PartyOkved] | None | Unset, data)

        okveds = _parse_okveds(d.pop("okveds", UNSET))

        _opf = d.pop("opf", UNSET)
        opf: PartyOpf | Unset
        if isinstance(_opf, Unset):
            opf = UNSET
        else:
            opf = PartyOpf.from_dict(_opf)

        def _parse_phones(data: object) -> list[SuggestionPartyPhone] | None | Unset:
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
                    phones_type_0_item = SuggestionPartyPhone.from_dict(phones_type_0_item_data)

                    phones_type_0.append(phones_type_0_item)

                return phones_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SuggestionPartyPhone] | None | Unset, data)

        phones = _parse_phones(d.pop("phones", UNSET))

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

        individual_party = cls(
            name=name,
            state=state,
            type_=type_,
            address=address,
            authorities=authorities,
            citizenship=citizenship,
            documents=documents,
            emails=emails,
            employee_count=employee_count,
            finance=finance,
            fio=fio,
            hid=hid,
            inn=inn,
            licenses=licenses,
            ogrn=ogrn,
            ogrn_date=ogrn_date,
            okato=okato,
            okfs=okfs,
            okogu=okogu,
            okpo=okpo,
            oktmo=oktmo,
            okved=okved,
            okved_type=okved_type,
            okveds=okveds,
            opf=opf,
            phones=phones,
            qc=qc,
            source=source,
        )

        individual_party.additional_properties = d
        return individual_party

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
