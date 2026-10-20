from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_custom_engagement_task_request_custom_message import CreateCustomEngagementTaskRequestCustomMessage





T = TypeVar("T", bound="CreateCustomEngagementTaskRequest")



@_attrs_define
class CreateCustomEngagementTaskRequest:
    """ 
        Attributes:
            task_name (str): The name of the task. Length: 1–256 bytes when UTF-8 encoded.
            end_time (int): The time at which the task ends, and messages will no longer be sent. Unix timestamp (seconds).
            channel (str): The engagement channel. Only `TIKTOK_IM` is supported.
            product_ids (list[str] | Unset): The product IDs that you want to include as interactive cards in the message.
                Retrieve this value from the [Search Products
                API](https://partner.tiktokshop.com/docv2/page/65854ffb8f559302d8a6acda).
                Max count: 4
            coupon_ids (list[str] | Unset): The coupon IDs that you want to include as interactive cards in the message.
                Max count: 1
                You can only add coupons that have one of these sets of property:
                - `coupons.display_type=REGULAR` and `coupons.target_buyer_segment=ALL`
                - `coupons.display_type=REGULAR` and `coupons.target_buyer_segment=REPEAT_CUSTOMERS`.
                Find out the coupon ID and properties from the [Search Coupons
                API](https://partner.tiktokshop.com/docv2/page/6699dcdf115ebe02f841e4cd).
            custom_message (CreateCustomEngagementTaskRequestCustomMessage | Unset):
     """

    task_name: str
    end_time: int
    channel: str
    product_ids: list[str] | Unset = UNSET
    coupon_ids: list[str] | Unset = UNSET
    custom_message: CreateCustomEngagementTaskRequestCustomMessage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_custom_engagement_task_request_custom_message import CreateCustomEngagementTaskRequestCustomMessage # noqa: PLC0415
        task_name = self.task_name

        end_time = self.end_time

        channel = self.channel

        product_ids: list[str] | Unset = UNSET
        if not isinstance(self.product_ids, Unset):
            product_ids = self.product_ids



        coupon_ids: list[str] | Unset = UNSET
        if not isinstance(self.coupon_ids, Unset):
            coupon_ids = self.coupon_ids



        custom_message: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_message, Unset):
            custom_message = self.custom_message.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "task_name": task_name,
            "end_time": end_time,
            "channel": channel,
        })
        if product_ids is not UNSET:
            field_dict["product_ids"] = product_ids
        if coupon_ids is not UNSET:
            field_dict["coupon_ids"] = coupon_ids
        if custom_message is not UNSET:
            field_dict["custom_message"] = custom_message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_custom_engagement_task_request_custom_message import CreateCustomEngagementTaskRequestCustomMessage # noqa: PLC0415
        d = dict(src_dict)
        task_name = d.pop("task_name")

        end_time = d.pop("end_time")

        channel = d.pop("channel")

        product_ids = cast(list[str], d.pop("product_ids", UNSET))


        coupon_ids = cast(list[str], d.pop("coupon_ids", UNSET))


        _custom_message = d.pop("custom_message", UNSET)
        custom_message: CreateCustomEngagementTaskRequestCustomMessage | Unset
        if isinstance(_custom_message,  Unset):
            custom_message = UNSET
        else:
            custom_message = CreateCustomEngagementTaskRequestCustomMessage.from_dict(_custom_message)




        create_custom_engagement_task_request = cls(
            task_name=task_name,
            end_time=end_time,
            channel=channel,
            product_ids=product_ids,
            coupon_ids=coupon_ids,
            custom_message=custom_message,
        )


        create_custom_engagement_task_request.additional_properties = d
        return create_custom_engagement_task_request

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
