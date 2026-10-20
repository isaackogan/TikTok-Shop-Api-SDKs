from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SearchCreatorTargetCollaborationsResponseDataTargetCollaborationProductCommission")



@_attrs_define
class SearchCreatorTargetCollaborationsResponseDataTargetCollaborationProductCommission:
    """ 
        Attributes:
            rate (int | Unset): The commission rate for the target collaboration in hundredths of a percent. For example,
                `3587` is a commission rate of `35.87%`.
            amount (str | Unset): The estimated commission amount calculated from the product's minimum price, in the
                currency specified by `currency`.
            currency (str | Unset): The currency code.
     """

    rate: int | Unset = UNSET
    amount: str | Unset = UNSET
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rate = self.rate

        amount = self.amount

        currency = self.currency


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rate is not UNSET:
            field_dict["rate"] = rate
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rate = d.pop("rate", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        search_creator_target_collaborations_response_data_target_collaboration_product_commission = cls(
            rate=rate,
            amount=amount,
            currency=currency,
        )


        search_creator_target_collaborations_response_data_target_collaboration_product_commission.additional_properties = d
        return search_creator_target_collaborations_response_data_target_collaboration_product_commission

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
