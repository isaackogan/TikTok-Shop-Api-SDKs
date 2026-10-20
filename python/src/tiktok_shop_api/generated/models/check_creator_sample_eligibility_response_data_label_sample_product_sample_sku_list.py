from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_creator_sample_eligibility_response_data_label_sample_product_sample_sku_list_sale_property import (
        CheckCreatorSampleEligibilityResponseDataLabelSampleProductSampleSkuListSaleProperty,
    )
    from ..models.price import Price


T = TypeVar("T", bound="CheckCreatorSampleEligibilityResponseDataLabelSampleProductSampleSkuList")


@_attrs_define
class CheckCreatorSampleEligibilityResponseDataLabelSampleProductSampleSkuList:
    """
    Attributes:
        id (str | Unset): The SKU identifier.
        sale_property_value_ids (str | Unset): The SKU property value identifiers joined with underscores (`_`) in the
            same order as the entries in `sale_properties`.
        price (Price | Unset):
        sale_properties (list[CheckCreatorSampleEligibilityResponseDataLabelSampleProductSampleSkuListSaleProperty] |
            Unset): The SKU property information.
        is_available (bool | Unset): Whether this SKU is available for the creator to apply for as a sample.
        unavailable_reason (str | Unset): The reason code associated with SKU sample availability. Interpret a specific
            unavailability reason only when `is_available` is `false`. `UNKNOWN` can also be returned when `is_available` is
            `true` because no unavailability reason applies.
            Possible values:
            - IS_PREORDER: The product is a preorder product and does not support free samples.
            - IS_GIFT: The product is a gift and does not support free samples.
            - OUT_OF_STOCK: The product is out of stock.
            - EXCEED_CB_PRICE_THRESHOLD: The SKU price exceeds the applicable cross-border price threshold.
            - ALREADY_APPLYED: The creator has already applied for this SKU.
            - UNKNOWN: No mapped unavailability reason is available.
    """

    id: str | Unset = UNSET
    sale_property_value_ids: str | Unset = UNSET
    price: Price | Unset = UNSET
    sale_properties: (
        list[CheckCreatorSampleEligibilityResponseDataLabelSampleProductSampleSkuListSaleProperty] | Unset
    ) = UNSET
    is_available: bool | Unset = UNSET
    unavailable_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sale_property_value_ids = self.sale_property_value_ids

        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        sale_properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sale_properties, Unset):
            sale_properties = []
            for sale_properties_item_data in self.sale_properties:
                sale_properties_item = sale_properties_item_data.to_dict()
                sale_properties.append(sale_properties_item)

        is_available = self.is_available

        unavailable_reason = self.unavailable_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if sale_property_value_ids is not UNSET:
            field_dict["sale_property_value_ids"] = sale_property_value_ids
        if price is not UNSET:
            field_dict["price"] = price
        if sale_properties is not UNSET:
            field_dict["sale_properties"] = sale_properties
        if is_available is not UNSET:
            field_dict["is_available"] = is_available
        if unavailable_reason is not UNSET:
            field_dict["unavailable_reason"] = unavailable_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_creator_sample_eligibility_response_data_label_sample_product_sample_sku_list_sale_property import (
            CheckCreatorSampleEligibilityResponseDataLabelSampleProductSampleSkuListSaleProperty,  # noqa: PLC0415
        )
        from ..models.price import Price  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        sale_property_value_ids = d.pop("sale_property_value_ids", UNSET)

        _price = d.pop("price", UNSET)
        price: Price | Unset
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = Price.from_dict(_price)

        _sale_properties = d.pop("sale_properties", UNSET)
        sale_properties: (
            list[CheckCreatorSampleEligibilityResponseDataLabelSampleProductSampleSkuListSaleProperty] | Unset
        ) = UNSET
        if _sale_properties is not UNSET:
            sale_properties = []
            for sale_properties_item_data in _sale_properties:
                sale_properties_item = (
                    CheckCreatorSampleEligibilityResponseDataLabelSampleProductSampleSkuListSaleProperty.from_dict(
                        sale_properties_item_data
                    )
                )

                sale_properties.append(sale_properties_item)

        is_available = d.pop("is_available", UNSET)

        unavailable_reason = d.pop("unavailable_reason", UNSET)

        check_creator_sample_eligibility_response_data_label_sample_product_sample_sku_list = cls(
            id=id,
            sale_property_value_ids=sale_property_value_ids,
            price=price,
            sale_properties=sale_properties,
            is_available=is_available,
            unavailable_reason=unavailable_reason,
        )

        check_creator_sample_eligibility_response_data_label_sample_product_sample_sku_list.additional_properties = d
        return check_creator_sample_eligibility_response_data_label_sample_product_sample_sku_list

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
