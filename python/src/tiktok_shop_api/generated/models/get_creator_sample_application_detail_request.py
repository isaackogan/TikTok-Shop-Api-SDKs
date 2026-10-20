from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetCreatorSampleApplicationDetailRequest")



@_attrs_define
class GetCreatorSampleApplicationDetailRequest:
    """ 
        Attributes:
            product_id (str): The product identifier.
            application_type (str): The type of creator sample application.
                - FREE_SAMPLE : free sample supplied by seller which creator can apply for by themselves from product detail
                page.
                - SAMPLE_COUPON: creator claimed sample coupon (a type of coupon) and used it to place orders at a discount
                price.
                - SAMPLE_CAMPAIGN: activity organized by the platform. Creators can participate in this activity to obtain
                sample products provided by the platform for free.
            application_id (str | Unset): Free sample application ID. When `application_type` is `FREE_SAMPLE`, provide
                `application_id`; if it is omitted, provide `main_order_id` in addition to the required `product_id`.
            main_order_id (str | Unset): The real main order identifier, required when application  is "SAMPLE_COUPON"  or
                "SAMPLE_CAMPAIGN" or "REFUNDABLE_SAMPLE".
     """

    product_id: str
    application_type: str
    application_id: str | Unset = UNSET
    main_order_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        application_type = self.application_type

        application_id = self.application_id

        main_order_id = self.main_order_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "product_id": product_id,
            "application_type": application_type,
        })
        if application_id is not UNSET:
            field_dict["application_id"] = application_id
        if main_order_id is not UNSET:
            field_dict["main_order_id"] = main_order_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id")

        application_type = d.pop("application_type")

        application_id = d.pop("application_id", UNSET)

        main_order_id = d.pop("main_order_id", UNSET)

        get_creator_sample_application_detail_request = cls(
            product_id=product_id,
            application_type=application_type,
            application_id=application_id,
            main_order_id=main_order_id,
        )


        get_creator_sample_application_detail_request.additional_properties = d
        return get_creator_sample_application_detail_request

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
