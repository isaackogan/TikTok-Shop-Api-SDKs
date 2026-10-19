from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSPSMetricProblemDetailsResponseDataImDsatChatItem")


@_attrs_define
class GetSPSMetricProblemDetailsResponseDataImDsatChatItem:
    """
    Attributes:
        chat_duration_hours (str | Unset): Chat duration in hours.
        chat_record_id (str | Unset): Chat record ID.
        customer_name (str | Unset): Masked customer name.
        customer_rating (int | Unset): Customer rating from 1 to 5.
        first_reply_time (int | Unset): First reply time. Unix timestamp in seconds.
        rating_reasons (list[str] | Unset): Customer rating reasons.
        service_agent (str | Unset): Service agent name.
    """

    chat_duration_hours: str | Unset = UNSET
    chat_record_id: str | Unset = UNSET
    customer_name: str | Unset = UNSET
    customer_rating: int | Unset = UNSET
    first_reply_time: int | Unset = UNSET
    rating_reasons: list[str] | Unset = UNSET
    service_agent: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_duration_hours = self.chat_duration_hours

        chat_record_id = self.chat_record_id

        customer_name = self.customer_name

        customer_rating = self.customer_rating

        first_reply_time = self.first_reply_time

        rating_reasons: list[str] | Unset = UNSET
        if not isinstance(self.rating_reasons, Unset):
            rating_reasons = self.rating_reasons

        service_agent = self.service_agent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chat_duration_hours is not UNSET:
            field_dict["chat_duration_hours"] = chat_duration_hours
        if chat_record_id is not UNSET:
            field_dict["chat_record_id"] = chat_record_id
        if customer_name is not UNSET:
            field_dict["customer_name"] = customer_name
        if customer_rating is not UNSET:
            field_dict["customer_rating"] = customer_rating
        if first_reply_time is not UNSET:
            field_dict["first_reply_time"] = first_reply_time
        if rating_reasons is not UNSET:
            field_dict["rating_reasons"] = rating_reasons
        if service_agent is not UNSET:
            field_dict["service_agent"] = service_agent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_duration_hours = d.pop("chat_duration_hours", UNSET)

        chat_record_id = d.pop("chat_record_id", UNSET)

        customer_name = d.pop("customer_name", UNSET)

        customer_rating = d.pop("customer_rating", UNSET)

        first_reply_time = d.pop("first_reply_time", UNSET)

        rating_reasons = cast(list[str], d.pop("rating_reasons", UNSET))

        service_agent = d.pop("service_agent", UNSET)

        get_sps_metric_problem_details_response_data_im_dsat_chat_item = cls(
            chat_duration_hours=chat_duration_hours,
            chat_record_id=chat_record_id,
            customer_name=customer_name,
            customer_rating=customer_rating,
            first_reply_time=first_reply_time,
            rating_reasons=rating_reasons,
            service_agent=service_agent,
        )

        get_sps_metric_problem_details_response_data_im_dsat_chat_item.additional_properties = d
        return get_sps_metric_problem_details_response_data_im_dsat_chat_item

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
