from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.creator import Creator





T = TypeVar("T", bound="QueryAIReportDataResponseDataRowDetailField")



@_attrs_define
class QueryAIReportDataResponseDataRowDetailField:
    """ 
        Attributes:
            code (str | Unset): Column code from the catalog.
            creator (Creator | Unset):
            currency (str | Unset): ISO 4217 currency code, present for currency values.
            display_value (str | Unset): Optional display text for value, such as an enum label, a formatted amount or a
                percentage. Display text may be empty or absent; it is not a calculation or filtering value. Enum dimensions use
                value for the option code and display_value for its display label when available. Enum detail fields may repeat
                the code when no display label is available. Creator identities and DATETIME values do not include
                display_value.
            image_url (str | Unset): Image for the entity represented by this value, when available.
            name (str | Unset): Display name of the product, Creator or other entity represented by this value, when
                available.
            value (datetime.datetime | Unset): Value represented as a string. Enum dimensions and enum detail fields return
                the catalog option code, such as PRODUCT_CARD. Numeric strings preserve precision; parse them only when
                nonempty. RATIO uses 0.1234 for 12.34%; DATETIME uses UTC RFC 3339. An absent or empty string means unavailable,
                not zero. For Creator identities, this field is omitted; read creator.creator_open_id instead. An unknown
                Creator may have no creator identity.
     """

    code: str | Unset = UNSET
    creator: Creator | Unset = UNSET
    currency: str | Unset = UNSET
    display_value: str | Unset = UNSET
    image_url: str | Unset = UNSET
    name: str | Unset = UNSET
    value: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.creator import Creator # noqa: PLC0415
        code = self.code

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        currency = self.currency

        display_value = self.display_value

        image_url = self.image_url

        name = self.name

        value: str | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if creator is not UNSET:
            field_dict["creator"] = creator
        if currency is not UNSET:
            field_dict["currency"] = currency
        if display_value is not UNSET:
            field_dict["display_value"] = display_value
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creator import Creator # noqa: PLC0415
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        _creator = d.pop("creator", UNSET)
        creator: Creator | Unset
        if isinstance(_creator,  Unset):
            creator = UNSET
        else:
            creator = Creator.from_dict(_creator)




        currency = d.pop("currency", UNSET)

        display_value = d.pop("display_value", UNSET)

        image_url = d.pop("image_url", UNSET)

        name = d.pop("name", UNSET)

        _value = d.pop("value", UNSET)
        value: datetime.datetime | Unset
        if isinstance(_value,  Unset):
            value = UNSET
        else:
            value = datetime.datetime.fromisoformat(_value)




        query_ai_report_data_response_data_row_detail_field = cls(
            code=code,
            creator=creator,
            currency=currency,
            display_value=display_value,
            image_url=image_url,
            name=name,
            value=value,
        )


        query_ai_report_data_response_data_row_detail_field.additional_properties = d
        return query_ai_report_data_response_data_row_detail_field

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
