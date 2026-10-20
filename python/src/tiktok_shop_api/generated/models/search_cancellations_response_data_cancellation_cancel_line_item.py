from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_image import ProductImage
    from ..models.refund_amount import RefundAmount
    from ..models.search_cancellations_response_data_cancellation_cancel_line_item_cancel_sub_line_item import (
        SearchCancellationsResponseDataCancellationCancelLineItemCancelSubLineItem,
    )


T = TypeVar("T", bound="SearchCancellationsResponseDataCancellationCancelLineItem")


@_attrs_define
class SearchCancellationsResponseDataCancellationCancelLineItem:
    """
    Attributes:
        cancel_line_item_id (str | Unset): Cancellation line item ID.
        order_line_item_id (str | Unset): Order line item ID.
        sku_id (str | Unset): SKU ID.
        sku_name (str | Unset): SKU name.
        product_image (ProductImage | Unset):
        product_name (str | Unset): Product name.
        seller_sku (str | Unset): SKU name defined by the seller.
        refund_amount (RefundAmount | Unset):
        cancel_sub_line_items (list[SearchCancellationsResponseDataCancellationCancelLineItemCancelSubLineItem] |
            Unset): Cancellation sub line items.
            Sub items represent skus that belong to a "virtual bundle" that has been defined by a seller. The sub_items will
            include all relevant information about each item that is a part of the virtual bundle.
    """

    cancel_line_item_id: str | Unset = UNSET
    order_line_item_id: str | Unset = UNSET
    sku_id: str | Unset = UNSET
    sku_name: str | Unset = UNSET
    product_image: ProductImage | Unset = UNSET
    product_name: str | Unset = UNSET
    seller_sku: str | Unset = UNSET
    refund_amount: RefundAmount | Unset = UNSET
    cancel_sub_line_items: list[SearchCancellationsResponseDataCancellationCancelLineItemCancelSubLineItem] | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cancel_line_item_id = self.cancel_line_item_id

        order_line_item_id = self.order_line_item_id

        sku_id = self.sku_id

        sku_name = self.sku_name

        product_image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_image, Unset):
            product_image = self.product_image.to_dict()

        product_name = self.product_name

        seller_sku = self.seller_sku

        refund_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.refund_amount, Unset):
            refund_amount = self.refund_amount.to_dict()

        cancel_sub_line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cancel_sub_line_items, Unset):
            cancel_sub_line_items = []
            for cancel_sub_line_items_item_data in self.cancel_sub_line_items:
                cancel_sub_line_items_item = cancel_sub_line_items_item_data.to_dict()
                cancel_sub_line_items.append(cancel_sub_line_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cancel_line_item_id is not UNSET:
            field_dict["cancel_line_item_id"] = cancel_line_item_id
        if order_line_item_id is not UNSET:
            field_dict["order_line_item_id"] = order_line_item_id
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if sku_name is not UNSET:
            field_dict["sku_name"] = sku_name
        if product_image is not UNSET:
            field_dict["product_image"] = product_image
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if seller_sku is not UNSET:
            field_dict["seller_sku"] = seller_sku
        if refund_amount is not UNSET:
            field_dict["refund_amount"] = refund_amount
        if cancel_sub_line_items is not UNSET:
            field_dict["cancel_sub_line_items"] = cancel_sub_line_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_image import ProductImage  # noqa: PLC0415
        from ..models.refund_amount import RefundAmount  # noqa: PLC0415
        from ..models.search_cancellations_response_data_cancellation_cancel_line_item_cancel_sub_line_item import (
            SearchCancellationsResponseDataCancellationCancelLineItemCancelSubLineItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        cancel_line_item_id = d.pop("cancel_line_item_id", UNSET)

        order_line_item_id = d.pop("order_line_item_id", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        sku_name = d.pop("sku_name", UNSET)

        _product_image = d.pop("product_image", UNSET)
        product_image: ProductImage | Unset
        if isinstance(_product_image, Unset):
            product_image = UNSET
        else:
            product_image = ProductImage.from_dict(_product_image)

        product_name = d.pop("product_name", UNSET)

        seller_sku = d.pop("seller_sku", UNSET)

        _refund_amount = d.pop("refund_amount", UNSET)
        refund_amount: RefundAmount | Unset
        if isinstance(_refund_amount, Unset):
            refund_amount = UNSET
        else:
            refund_amount = RefundAmount.from_dict(_refund_amount)

        _cancel_sub_line_items = d.pop("cancel_sub_line_items", UNSET)
        cancel_sub_line_items: (
            list[SearchCancellationsResponseDataCancellationCancelLineItemCancelSubLineItem] | Unset
        ) = UNSET
        if _cancel_sub_line_items is not UNSET:
            cancel_sub_line_items = []
            for cancel_sub_line_items_item_data in _cancel_sub_line_items:
                cancel_sub_line_items_item = (
                    SearchCancellationsResponseDataCancellationCancelLineItemCancelSubLineItem.from_dict(
                        cancel_sub_line_items_item_data
                    )
                )

                cancel_sub_line_items.append(cancel_sub_line_items_item)

        search_cancellations_response_data_cancellation_cancel_line_item = cls(
            cancel_line_item_id=cancel_line_item_id,
            order_line_item_id=order_line_item_id,
            sku_id=sku_id,
            sku_name=sku_name,
            product_image=product_image,
            product_name=product_name,
            seller_sku=seller_sku,
            refund_amount=refund_amount,
            cancel_sub_line_items=cancel_sub_line_items,
        )

        search_cancellations_response_data_cancellation_cancel_line_item.additional_properties = d
        return search_cancellations_response_data_cancellation_cancel_line_item

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
