from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CreateEngagementTaskRequest")



@_attrs_define
class CreateEngagementTaskRequest:
    """ 
        Attributes:
            template_id (str): The ID of engagement message templates predefined by TikTok Shop. Retrieve the value from
                [Get Message Templates](67777e44223fde02fdfdc157).
            task_name (str): The name of the task. Length: 1–256 bytes.
            end_time (int): The time at which the task ends, and messages will no longer be sent. Unix timestamp (seconds).
            channel (str): The engagement channel. Only `TIKTOK_IM` is supported.
            product_ids (list[str] | Unset): The product ID. Retrieve this value from the [Search Products
                API](https://partner.tiktokshop.com/docv2/page/65854ffb8f559302d8a6acda).
            coupon_ids (list[str] | Unset): The coupon ID. Retrieve this value and other coupon-related information from the
                [Search Coupons API](https://partner.tiktokshop.com/docv2/page/6699dcdf115ebe02f841e4cd).

                **Note**: The coupon properties must comply with the rules defined in `coupon_card_rules.coupon_type` of the
                [Get Message Templates API](67777e44223fde02fdfdc157).
     """

    template_id: str
    task_name: str
    end_time: int
    channel: str
    product_ids: list[str] | Unset = UNSET
    coupon_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        task_name = self.task_name

        end_time = self.end_time

        channel = self.channel

        product_ids: list[str] | Unset = UNSET
        if not isinstance(self.product_ids, Unset):
            product_ids = self.product_ids



        coupon_ids: list[str] | Unset = UNSET
        if not isinstance(self.coupon_ids, Unset):
            coupon_ids = self.coupon_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "template_id": template_id,
            "task_name": task_name,
            "end_time": end_time,
            "channel": channel,
        })
        if product_ids is not UNSET:
            field_dict["product_ids"] = product_ids
        if coupon_ids is not UNSET:
            field_dict["coupon_ids"] = coupon_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template_id = d.pop("template_id")

        task_name = d.pop("task_name")

        end_time = d.pop("end_time")

        channel = d.pop("channel")

        product_ids = cast(list[str], d.pop("product_ids", UNSET))


        coupon_ids = cast(list[str], d.pop("coupon_ids", UNSET))


        create_engagement_task_request = cls(
            template_id=template_id,
            task_name=task_name,
            end_time=end_time,
            channel=channel,
            product_ids=product_ids,
            coupon_ids=coupon_ids,
        )


        create_engagement_task_request.additional_properties = d
        return create_engagement_task_request

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
