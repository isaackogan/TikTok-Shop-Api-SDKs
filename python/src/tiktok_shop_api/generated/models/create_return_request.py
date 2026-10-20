from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.order_line_list import OrderLineList
  from ..models.sku import Sku





T = TypeVar("T", bound="CreateReturnRequest")



@_attrs_define
class CreateReturnRequest:
    """ 
        Attributes:
            order_id (str): Tiktok Shop order id
            return_reason (str): Seller's reason to create a return
            return_type (str): Which type to create:
                - REFUND
                - RETURN_AND_REFUND
            skus (list[Sku] | Unset): Skus
            order_line_item_ids (list[str] | Unset): Specifies the order line IDs to include in the return request. Use this
                field to select order lines when an order is split into multiple packages. Do not provide non-empty values in
                both `order_line_item_ids` and `order_line_list` in the same request. If `order_line_item_ids`,
                `order_line_list`, and `skus` are all omitted, all order lines in the order are included. **Note:** This is a
                legacy field; new integrations should use `order_line_list` instead.
            refund_total (str | Unset): Total refund amount to the buyer.
                The total refund amount can not exceed the refundable amount
            currency (str | Unset): Currency of the refund amount. It should be the same as the currency of the TikTok Shop
                order. Required when `refund_total` is provided.
            shipment_type (str | Unset): Specifies the return shipping method the buyer uses to send items back to the
                seller in a return request. Supported values:
                - `PLATFORM`
                - `BUYER_ARRANGE`
            handover_method (str | Unset): **Optional**. Only applicable when shipment_type is `PLATFORM`. Specifies the
                handover method the buyer uses to return the item through platform-supported shipping. Supported values:
                - `DROP_OFF`
                - `PICKUP`
            order_line_list (list[OrderLineList] | Unset): Specifies the line items to include in the return request and
                supports bundle order splitting. Every entry must include `order_line_item_id`. For a bundle sub-item, also
                include `sub_order_line_item_id`; omit `sub_order_line_item_id` for a normal order line. Do not mix normal order
                lines and bundle sub-items in the same request. **Note:** This field is completely backward compatible with the
                legacy `order_line_item_ids` field.
     """

    order_id: str
    return_reason: str
    return_type: str
    skus: list[Sku] | Unset = UNSET
    order_line_item_ids: list[str] | Unset = UNSET
    refund_total: str | Unset = UNSET
    currency: str | Unset = UNSET
    shipment_type: str | Unset = UNSET
    handover_method: str | Unset = UNSET
    order_line_list: list[OrderLineList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.order_line_list import OrderLineList # noqa: PLC0415
        from ..models.sku import Sku # noqa: PLC0415
        order_id = self.order_id

        return_reason = self.return_reason

        return_type = self.return_type

        skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skus, Unset):
            skus = []
            for skus_item_data in self.skus:
                skus_item = skus_item_data.to_dict()
                skus.append(skus_item)



        order_line_item_ids: list[str] | Unset = UNSET
        if not isinstance(self.order_line_item_ids, Unset):
            order_line_item_ids = self.order_line_item_ids



        refund_total = self.refund_total

        currency = self.currency

        shipment_type = self.shipment_type

        handover_method = self.handover_method

        order_line_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.order_line_list, Unset):
            order_line_list = []
            for order_line_list_item_data in self.order_line_list:
                order_line_list_item = order_line_list_item_data.to_dict()
                order_line_list.append(order_line_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "order_id": order_id,
            "return_reason": return_reason,
            "return_type": return_type,
        })
        if skus is not UNSET:
            field_dict["skus"] = skus
        if order_line_item_ids is not UNSET:
            field_dict["order_line_item_ids"] = order_line_item_ids
        if refund_total is not UNSET:
            field_dict["refund_total"] = refund_total
        if currency is not UNSET:
            field_dict["currency"] = currency
        if shipment_type is not UNSET:
            field_dict["shipment_type"] = shipment_type
        if handover_method is not UNSET:
            field_dict["handover_method"] = handover_method
        if order_line_list is not UNSET:
            field_dict["order_line_list"] = order_line_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_line_list import OrderLineList # noqa: PLC0415
        from ..models.sku import Sku # noqa: PLC0415
        d = dict(src_dict)
        order_id = d.pop("order_id")

        return_reason = d.pop("return_reason")

        return_type = d.pop("return_type")

        _skus = d.pop("skus", UNSET)
        skus: list[Sku] | Unset = UNSET
        if _skus is not UNSET:
            skus = []
            for skus_item_data in _skus:
                skus_item = Sku.from_dict(skus_item_data)



                skus.append(skus_item)


        order_line_item_ids = cast(list[str], d.pop("order_line_item_ids", UNSET))


        refund_total = d.pop("refund_total", UNSET)

        currency = d.pop("currency", UNSET)

        shipment_type = d.pop("shipment_type", UNSET)

        handover_method = d.pop("handover_method", UNSET)

        _order_line_list = d.pop("order_line_list", UNSET)
        order_line_list: list[OrderLineList] | Unset = UNSET
        if _order_line_list is not UNSET:
            order_line_list = []
            for order_line_list_item_data in _order_line_list:
                order_line_list_item = OrderLineList.from_dict(order_line_list_item_data)



                order_line_list.append(order_line_list_item)


        create_return_request = cls(
            order_id=order_id,
            return_reason=return_reason,
            return_type=return_type,
            skus=skus,
            order_line_item_ids=order_line_item_ids,
            refund_total=refund_total,
            currency=currency,
            shipment_type=shipment_type,
            handover_method=handover_method,
            order_line_list=order_line_list,
        )


        create_return_request.additional_properties = d
        return create_return_request

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
