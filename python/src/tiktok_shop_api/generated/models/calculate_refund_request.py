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





T = TypeVar("T", bound="CalculateRefundRequest")



@_attrs_define
class CalculateRefundRequest:
    """ 
        Attributes:
            order_id (str): TikTok Shop order id.
            request_type (str): Request type
                - CANCEL
                - REFUND
                - RETURN_AND_REFUND
                Note: different request types are used for different aftersales scenarios. Also, different request types might
                have different refund amounts, because the refund amount calculation policy is different.
            reason_name (str): Seller's reason for the selected cancellation, refund, or return-and-refund request. Use the
                [Get Aftersale Eligibility](https://partner.tiktokshop.com/docv2/page/69c3070c66dee40493fdfe2e) endpoint to
                retrieve the currently available reasons, and submit the returned reason name in this field.
            shipment_type (str | Unset): How buyer ships items to seller when in a return request, could be:
                - `PLATFORM`
                - `BUYER_ARRANGE`
            handover_method (str | Unset): Which handover method buyer chooses to use when returning goods to seller by
                platform
                - `DROP_OFF`: buyer drops off the parcel in logistics service collect point.
                - `PICKUP`: logistics service picks up the buyer package.
            order_line_item_ids (list[str] | Unset): TikTok Shop order line item IDs to include in the refund calculation.
                Do not provide non-empty values in both `order_line_item_ids` and `order_line_list` in the same request.
            skus (list[Sku] | Unset): skus
            order_line_list (list[OrderLineList] | Unset): Order lines to include in the refund calculation. Use this field
                when you need to identify individual sub-items in a bundle product. **Note:** This field is completely backward
                compatible with the previous `order_line_item_ids` field. Do not provide non-empty values in both
                `order_line_list` and `order_line_item_ids` in the same request.
     """

    order_id: str
    request_type: str
    reason_name: str
    shipment_type: str | Unset = UNSET
    handover_method: str | Unset = UNSET
    order_line_item_ids: list[str] | Unset = UNSET
    skus: list[Sku] | Unset = UNSET
    order_line_list: list[OrderLineList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.order_line_list import OrderLineList # noqa: PLC0415
        from ..models.sku import Sku # noqa: PLC0415
        order_id = self.order_id

        request_type = self.request_type

        reason_name = self.reason_name

        shipment_type = self.shipment_type

        handover_method = self.handover_method

        order_line_item_ids: list[str] | Unset = UNSET
        if not isinstance(self.order_line_item_ids, Unset):
            order_line_item_ids = self.order_line_item_ids



        skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skus, Unset):
            skus = []
            for skus_item_data in self.skus:
                skus_item = skus_item_data.to_dict()
                skus.append(skus_item)



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
            "request_type": request_type,
            "reason_name": reason_name,
        })
        if shipment_type is not UNSET:
            field_dict["shipment_type"] = shipment_type
        if handover_method is not UNSET:
            field_dict["handover_method"] = handover_method
        if order_line_item_ids is not UNSET:
            field_dict["order_line_item_ids"] = order_line_item_ids
        if skus is not UNSET:
            field_dict["skus"] = skus
        if order_line_list is not UNSET:
            field_dict["order_line_list"] = order_line_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_line_list import OrderLineList # noqa: PLC0415
        from ..models.sku import Sku # noqa: PLC0415
        d = dict(src_dict)
        order_id = d.pop("order_id")

        request_type = d.pop("request_type")

        reason_name = d.pop("reason_name")

        shipment_type = d.pop("shipment_type", UNSET)

        handover_method = d.pop("handover_method", UNSET)

        order_line_item_ids = cast(list[str], d.pop("order_line_item_ids", UNSET))


        _skus = d.pop("skus", UNSET)
        skus: list[Sku] | Unset = UNSET
        if _skus is not UNSET:
            skus = []
            for skus_item_data in _skus:
                skus_item = Sku.from_dict(skus_item_data)



                skus.append(skus_item)


        _order_line_list = d.pop("order_line_list", UNSET)
        order_line_list: list[OrderLineList] | Unset = UNSET
        if _order_line_list is not UNSET:
            order_line_list = []
            for order_line_list_item_data in _order_line_list:
                order_line_list_item = OrderLineList.from_dict(order_line_list_item_data)



                order_line_list.append(order_line_list_item)


        calculate_refund_request = cls(
            order_id=order_id,
            request_type=request_type,
            reason_name=reason_name,
            shipment_type=shipment_type,
            handover_method=handover_method,
            order_line_item_ids=order_line_item_ids,
            skus=skus,
            order_line_list=order_line_list,
        )


        calculate_refund_request.additional_properties = d
        return calculate_refund_request

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
