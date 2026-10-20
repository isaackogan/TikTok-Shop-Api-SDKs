from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_global_product_request_sku_price_currency import CreateGlobalProductRequestSkuPriceCurrency






T = TypeVar("T", bound="CreateGlobalProductRequestSkuPrice")



@_attrs_define
class CreateGlobalProductRequestSkuPrice:
    """ 
        Attributes:
            amount (str): The price amount.
                Max: 99,999,999.99
            currency (CreateGlobalProductRequestSkuPriceCurrency): The currency.
                Possible values:
                - `USD`: Applicable for global sellers
                - `EUR`: Applicable for intra-EU sellers
     """

    amount: str
    currency: CreateGlobalProductRequestSkuPriceCurrency
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        currency = self.currency.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "amount": amount,
            "currency": currency,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        currency = CreateGlobalProductRequestSkuPriceCurrency(d.pop("currency"))




        create_global_product_request_sku_price = cls(
            amount=amount,
            currency=currency,
        )


        create_global_product_request_sku_price.additional_properties = d
        return create_global_product_request_sku_price

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
