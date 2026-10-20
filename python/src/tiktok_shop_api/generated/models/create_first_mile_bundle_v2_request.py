from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_first_mile_bundle_v2_request_handover_method import CreateFirstMileBundleV2RequestHandoverMethod
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CreateFirstMileBundleV2Request")



@_attrs_define
class CreateFirstMileBundleV2Request:
    """ 
        Attributes:
            order_ids (list[str]): The IDs of all the orders sent in a single first-mile bundle. Maximum: 9,999 order IDs
                per request.
                The orders must follow the restrictions:
                - Each of the orders must exist and be RTS and shipping label printed.
                - The orders are sent by the same seller.
                - The orders belong to a single group of TikTok Shop service districts. The groups are:
                  - Group 1: PH, SG, MY, VN, TH, and JP.
                  - Group 2: DE, FR, IT, ES.

                You can not create first mile bundles for US/UK orders using this API.
            handover_method (CreateFirstMileBundleV2RequestHandoverMethod): The way you send the first-mile bundle. Possible
                enumerations are:
                - `PICKUP`: You use the logistic service provided by TikTok Shop to send the bundle.
                - `DROP_OFF`: You contact the logistic provider and send the bundle. The logistic provider must be registered at
                TikTok Shop.
            shipping_provider_id (str | Unset): The logistic provider ID in TikTok Shop. Required when `handover_method ==
                DROP_OFF`.
            tracking_number (str | Unset): The logistic tracking number of the bundle. Required when `handover_method ==
                DROP_OFF`.
            phone_tail_number (str | Unset): Last 4 digits of the sender's phone number. Required when `handover_method ==
                DROP_OFF`.
     """

    order_ids: list[str]
    handover_method: CreateFirstMileBundleV2RequestHandoverMethod
    shipping_provider_id: str | Unset = UNSET
    tracking_number: str | Unset = UNSET
    phone_tail_number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        order_ids = self.order_ids



        handover_method = self.handover_method.value

        shipping_provider_id = self.shipping_provider_id

        tracking_number = self.tracking_number

        phone_tail_number = self.phone_tail_number


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "order_ids": order_ids,
            "handover_method": handover_method,
        })
        if shipping_provider_id is not UNSET:
            field_dict["shipping_provider_id"] = shipping_provider_id
        if tracking_number is not UNSET:
            field_dict["tracking_number"] = tracking_number
        if phone_tail_number is not UNSET:
            field_dict["phone_tail_number"] = phone_tail_number

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_ids = cast(list[str], d.pop("order_ids"))


        handover_method = CreateFirstMileBundleV2RequestHandoverMethod(d.pop("handover_method"))




        shipping_provider_id = d.pop("shipping_provider_id", UNSET)

        tracking_number = d.pop("tracking_number", UNSET)

        phone_tail_number = d.pop("phone_tail_number", UNSET)

        create_first_mile_bundle_v2_request = cls(
            order_ids=order_ids,
            handover_method=handover_method,
            shipping_provider_id=shipping_provider_id,
            tracking_number=tracking_number,
            phone_tail_number=phone_tail_number,
        )


        create_first_mile_bundle_v2_request.additional_properties = d
        return create_first_mile_bundle_v2_request

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
