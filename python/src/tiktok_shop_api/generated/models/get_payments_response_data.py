from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_payments_response_data_payment import GetPaymentsResponseDataPayment





T = TypeVar("T", bound="GetPaymentsResponseData")



@_attrs_define
class GetPaymentsResponseData:
    """ 
        Attributes:
            next_page_token (str | Unset): An opaque token used to retrieve the next page of a paginated result set. Provide
                this value in the `page_token` parameter of your request if the current response does not return all the
                results. An empty string means there is no next page.
            payments (list[GetPaymentsResponseDataPayment] | Unset): The list of payments that meet the query conditions.
     """

    next_page_token: str | Unset = UNSET
    payments: list[GetPaymentsResponseDataPayment] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_payments_response_data_payment import GetPaymentsResponseDataPayment # noqa: PLC0415
        next_page_token = self.next_page_token

        payments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.payments, Unset):
            payments = []
            for payments_item_data in self.payments:
                payments_item = payments_item_data.to_dict()
                payments.append(payments_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if payments is not UNSET:
            field_dict["payments"] = payments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_payments_response_data_payment import GetPaymentsResponseDataPayment # noqa: PLC0415
        d = dict(src_dict)
        next_page_token = d.pop("next_page_token", UNSET)

        _payments = d.pop("payments", UNSET)
        payments: list[GetPaymentsResponseDataPayment] | Unset = UNSET
        if _payments is not UNSET:
            payments = []
            for payments_item_data in _payments:
                payments_item = GetPaymentsResponseDataPayment.from_dict(payments_item_data)



                payments.append(payments_item)


        get_payments_response_data = cls(
            next_page_token=next_page_token,
            payments=payments,
        )


        get_payments_response_data.additional_properties = d
        return get_payments_response_data

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
