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
  from ..models.image import Image





T = TypeVar("T", bound="SubmitStrikethroughPriceRequestSkuExternalTransactionPrice")



@_attrs_define
class SubmitStrikethroughPriceRequestSkuExternalTransactionPrice:
    """ 
        Attributes:
            amount (str): The transaction price amount. The valid range is 0.01 to 7600, and the value must be equal to or
                greater than the list price specified when the product was created or edited.
            currency (str): The ISO 4217 currency code. The supported value is `USD`.
            transaction_time (datetime.datetime): The RFC 3339 time when the highest transaction price was recorded. The
                time must include a timezone and be within the 90 days before the request.
            image (Image | Unset):
     """

    amount: str
    currency: str
    transaction_time: datetime.datetime
    image: Image | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.image import Image # noqa: PLC0415
        amount = self.amount

        currency = self.currency

        transaction_time = self.transaction_time.isoformat()

        image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "amount": amount,
            "currency": currency,
            "transaction_time": transaction_time,
        })
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image import Image # noqa: PLC0415
        d = dict(src_dict)
        amount = d.pop("amount")

        currency = d.pop("currency")

        transaction_time = datetime.datetime.fromisoformat(d.pop("transaction_time"))




        _image = d.pop("image", UNSET)
        image: Image | Unset
        if isinstance(_image,  Unset):
            image = UNSET
        else:
            image = Image.from_dict(_image)




        submit_strikethrough_price_request_sku_external_transaction_price = cls(
            amount=amount,
            currency=currency,
            transaction_time=transaction_time,
            image=image,
        )


        submit_strikethrough_price_request_sku_external_transaction_price.additional_properties = d
        return submit_strikethrough_price_request_sku_external_transaction_price

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
