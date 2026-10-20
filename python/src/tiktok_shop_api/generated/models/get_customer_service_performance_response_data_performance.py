from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetCustomerServicePerformanceResponseDataPerformance")



@_attrs_define
class GetCustomerServicePerformanceResponseDataPerformance:
    """ 
        Attributes:
            support_session_count (int | Unset): The total number of chat support sessions initiated by customers. A session
                starts when a customer first clicks an FAQ card or sends a message (text, image, video, emoji, product card,
                order card, etc.) in chat. The sessions which started in the specified time slot are included in calculation.
            response_percentage (str | Unset): The percentage of chat support sessions of which the first response happens
                within 24 hours. The sessions which started in the specified time slot are included in calculation.
                - Automated responses such as FAQ cards are regarded as responses within 24 hours.
                - Sessions initiated during vacation mode are excluded from this calculation.
            satisfaction_percentage (str | Unset): The percentage of chat support sessions rated 'Satisfied' (4 or 5 stars).
                The sessions of which the rating occurred in the specified time slot are included in the calculation; the
                sessions without rate are not included in the calculation.
            response_time_mins (str | Unset): The average first response time in minutes for chat support sessions. The
                sessions which started in the specified time slot are included in calculation.
            conversion_rate (str | Unset): The percentage of successfully converted customers based on the total number of
                potential customers.
            cs_guided_gmv (str | Unset): The revenue generated from orders placed by customers within 7 days of your
                response to their chat.
            currency (str | Unset): The ISO 4217 three-letter currency code used for `cs_guided_gmv`. See [Currency
                Codes](https://www.iso.org/iso-4217-currency-codes.html).
     """

    support_session_count: int | Unset = UNSET
    response_percentage: str | Unset = UNSET
    satisfaction_percentage: str | Unset = UNSET
    response_time_mins: str | Unset = UNSET
    conversion_rate: str | Unset = UNSET
    cs_guided_gmv: str | Unset = UNSET
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        support_session_count = self.support_session_count

        response_percentage = self.response_percentage

        satisfaction_percentage = self.satisfaction_percentage

        response_time_mins = self.response_time_mins

        conversion_rate = self.conversion_rate

        cs_guided_gmv = self.cs_guided_gmv

        currency = self.currency


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if support_session_count is not UNSET:
            field_dict["support_session_count"] = support_session_count
        if response_percentage is not UNSET:
            field_dict["response_percentage"] = response_percentage
        if satisfaction_percentage is not UNSET:
            field_dict["satisfaction_percentage"] = satisfaction_percentage
        if response_time_mins is not UNSET:
            field_dict["response_time_mins"] = response_time_mins
        if conversion_rate is not UNSET:
            field_dict["conversion_rate"] = conversion_rate
        if cs_guided_gmv is not UNSET:
            field_dict["cs_guided_gmv"] = cs_guided_gmv
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        support_session_count = d.pop("support_session_count", UNSET)

        response_percentage = d.pop("response_percentage", UNSET)

        satisfaction_percentage = d.pop("satisfaction_percentage", UNSET)

        response_time_mins = d.pop("response_time_mins", UNSET)

        conversion_rate = d.pop("conversion_rate", UNSET)

        cs_guided_gmv = d.pop("cs_guided_gmv", UNSET)

        currency = d.pop("currency", UNSET)

        get_customer_service_performance_response_data_performance = cls(
            support_session_count=support_session_count,
            response_percentage=response_percentage,
            satisfaction_percentage=satisfaction_percentage,
            response_time_mins=response_time_mins,
            conversion_rate=conversion_rate,
            cs_guided_gmv=cs_guided_gmv,
            currency=currency,
        )


        get_customer_service_performance_response_data_performance.additional_properties = d
        return get_customer_service_performance_response_data_performance

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
