from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Commission")



@_attrs_define
class Commission:
    """ 
        Attributes:
            rate (int | Unset): - The commission rate for this product is set by merchants for creators public promotion.
                - The range of this value is [100, 8000].
                - This value equals actual commission rate multi 10000. For example: 3000 means the actual commission rate is
                30.00%, and 3555 means 35.55%
            currency (str | Unset): Currency code for the commission amount.
            amount (str | Unset): The commission amount calculated from the product's promotional price and commission rate.
                When both minimum and maximum promotional prices are available, the value is formatted as `<minimum commission>
                - <maximum commission>`; otherwise, it contains the available commission amount. If neither price is available,
                the value is `0`. The currency is specified by `commission.currency`.
     """

    rate: int | Unset = UNSET
    currency: str | Unset = UNSET
    amount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rate = self.rate

        currency = self.currency

        amount = self.amount


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rate is not UNSET:
            field_dict["rate"] = rate
        if currency is not UNSET:
            field_dict["currency"] = currency
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rate = d.pop("rate", UNSET)

        currency = d.pop("currency", UNSET)

        amount = d.pop("amount", UNSET)

        commission = cls(
            rate=rate,
            currency=currency,
            amount=amount,
        )


        commission.additional_properties = d
        return commission

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
