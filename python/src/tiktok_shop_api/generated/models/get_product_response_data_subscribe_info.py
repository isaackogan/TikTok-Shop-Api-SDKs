from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_product_response_data_subscribe_info_subscribe_discount_detail import (
        GetProductResponseDataSubscribeInfoSubscribeDiscountDetail,
    )
    from ..models.get_product_response_data_subscribe_info_subscribe_promotion_config import (
        GetProductResponseDataSubscribeInfoSubscribePromotionConfig,
    )


T = TypeVar("T", bound="GetProductResponseDataSubscribeInfo")


@_attrs_define
class GetProductResponseDataSubscribeInfo:
    """
    Attributes:
        subscribe_discount_details (list[GetProductResponseDataSubscribeInfoSubscribeDiscountDetail] | Unset): All of
            the Save and Subscribe discount details.
        subscribe_promotion_config (list[GetProductResponseDataSubscribeInfoSubscribePromotionConfig] | Unset): A
            subscription configuration specific to the seller. It outlines the different types of promotions and associated
            constraints that are available for use.
        subscribe_status (str | Unset): An enum outlining whether the given product has an active Subscribe and Save
            promotion:
            - ENABLED
            - NOT_ENABLED
        support_subscribe (bool | Unset): A flag outlining whether the seller and given product support Subscribe and
            Save promotions.
    """

    subscribe_discount_details: list[GetProductResponseDataSubscribeInfoSubscribeDiscountDetail] | Unset = UNSET
    subscribe_promotion_config: list[GetProductResponseDataSubscribeInfoSubscribePromotionConfig] | Unset = UNSET
    subscribe_status: str | Unset = UNSET
    support_subscribe: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscribe_discount_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subscribe_discount_details, Unset):
            subscribe_discount_details = []
            for subscribe_discount_details_item_data in self.subscribe_discount_details:
                subscribe_discount_details_item = subscribe_discount_details_item_data.to_dict()
                subscribe_discount_details.append(subscribe_discount_details_item)

        subscribe_promotion_config: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subscribe_promotion_config, Unset):
            subscribe_promotion_config = []
            for subscribe_promotion_config_item_data in self.subscribe_promotion_config:
                subscribe_promotion_config_item = subscribe_promotion_config_item_data.to_dict()
                subscribe_promotion_config.append(subscribe_promotion_config_item)

        subscribe_status = self.subscribe_status

        support_subscribe = self.support_subscribe

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscribe_discount_details is not UNSET:
            field_dict["subscribe_discount_details"] = subscribe_discount_details
        if subscribe_promotion_config is not UNSET:
            field_dict["subscribe_promotion_config"] = subscribe_promotion_config
        if subscribe_status is not UNSET:
            field_dict["subscribe_status"] = subscribe_status
        if support_subscribe is not UNSET:
            field_dict["support_subscribe"] = support_subscribe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_product_response_data_subscribe_info_subscribe_discount_detail import (
            GetProductResponseDataSubscribeInfoSubscribeDiscountDetail,  # noqa: PLC0415
        )
        from ..models.get_product_response_data_subscribe_info_subscribe_promotion_config import (
            GetProductResponseDataSubscribeInfoSubscribePromotionConfig,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _subscribe_discount_details = d.pop("subscribe_discount_details", UNSET)
        subscribe_discount_details: list[GetProductResponseDataSubscribeInfoSubscribeDiscountDetail] | Unset = UNSET
        if _subscribe_discount_details is not UNSET:
            subscribe_discount_details = []
            for subscribe_discount_details_item_data in _subscribe_discount_details:
                subscribe_discount_details_item = GetProductResponseDataSubscribeInfoSubscribeDiscountDetail.from_dict(
                    subscribe_discount_details_item_data
                )

                subscribe_discount_details.append(subscribe_discount_details_item)

        _subscribe_promotion_config = d.pop("subscribe_promotion_config", UNSET)
        subscribe_promotion_config: list[GetProductResponseDataSubscribeInfoSubscribePromotionConfig] | Unset = UNSET
        if _subscribe_promotion_config is not UNSET:
            subscribe_promotion_config = []
            for subscribe_promotion_config_item_data in _subscribe_promotion_config:
                subscribe_promotion_config_item = GetProductResponseDataSubscribeInfoSubscribePromotionConfig.from_dict(
                    subscribe_promotion_config_item_data
                )

                subscribe_promotion_config.append(subscribe_promotion_config_item)

        subscribe_status = d.pop("subscribe_status", UNSET)

        support_subscribe = d.pop("support_subscribe", UNSET)

        get_product_response_data_subscribe_info = cls(
            subscribe_discount_details=subscribe_discount_details,
            subscribe_promotion_config=subscribe_promotion_config,
            subscribe_status=subscribe_status,
            support_subscribe=support_subscribe,
        )

        get_product_response_data_subscribe_info.additional_properties = d
        return get_product_response_data_subscribe_info

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
