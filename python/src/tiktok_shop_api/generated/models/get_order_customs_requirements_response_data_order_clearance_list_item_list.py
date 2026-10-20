from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_order_customs_requirements_response_data_order_clearance_list_item_list_related_item_detail import GetOrderCustomsRequirementsResponseDataOrderClearanceListItemListRelatedItemDetail





T = TypeVar("T", bound="GetOrderCustomsRequirementsResponseDataOrderClearanceListItemList")



@_attrs_define
class GetOrderCustomsRequirementsResponseDataOrderClearanceListItemList:
    """ 
        Attributes:
            order_line_id (str | Unset): Sub order ID
            product_id (str | Unset): Product ID.
            sku_id (str | Unset): SKU ID.
            is_virtual_unboxing (bool | Unset): Whether this sub order is virtual_unboxing
            is_temporary_listing (bool | Unset): Whether this sub order is temporary_listing
            related_item_detail (list[GetOrderCustomsRequirementsResponseDataOrderClearanceListItemListRelatedItemDetail] |
                Unset): Submitted customs clearance item details for this order line, aggregated by SKU.
     """

    order_line_id: str | Unset = UNSET
    product_id: str | Unset = UNSET
    sku_id: str | Unset = UNSET
    is_virtual_unboxing: bool | Unset = UNSET
    is_temporary_listing: bool | Unset = UNSET
    related_item_detail: list[GetOrderCustomsRequirementsResponseDataOrderClearanceListItemListRelatedItemDetail] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_order_customs_requirements_response_data_order_clearance_list_item_list_related_item_detail import GetOrderCustomsRequirementsResponseDataOrderClearanceListItemListRelatedItemDetail # noqa: PLC0415
        order_line_id = self.order_line_id

        product_id = self.product_id

        sku_id = self.sku_id

        is_virtual_unboxing = self.is_virtual_unboxing

        is_temporary_listing = self.is_temporary_listing

        related_item_detail: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.related_item_detail, Unset):
            related_item_detail = []
            for related_item_detail_item_data in self.related_item_detail:
                related_item_detail_item = related_item_detail_item_data.to_dict()
                related_item_detail.append(related_item_detail_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if is_virtual_unboxing is not UNSET:
            field_dict["is_virtual_unboxing"] = is_virtual_unboxing
        if is_temporary_listing is not UNSET:
            field_dict["is_temporary_listing"] = is_temporary_listing
        if related_item_detail is not UNSET:
            field_dict["related_item_detail"] = related_item_detail

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_order_customs_requirements_response_data_order_clearance_list_item_list_related_item_detail import GetOrderCustomsRequirementsResponseDataOrderClearanceListItemListRelatedItemDetail # noqa: PLC0415
        d = dict(src_dict)
        order_line_id = d.pop("order_line_id", UNSET)

        product_id = d.pop("product_id", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        is_virtual_unboxing = d.pop("is_virtual_unboxing", UNSET)

        is_temporary_listing = d.pop("is_temporary_listing", UNSET)

        _related_item_detail = d.pop("related_item_detail", UNSET)
        related_item_detail: list[GetOrderCustomsRequirementsResponseDataOrderClearanceListItemListRelatedItemDetail] | Unset = UNSET
        if _related_item_detail is not UNSET:
            related_item_detail = []
            for related_item_detail_item_data in _related_item_detail:
                related_item_detail_item = GetOrderCustomsRequirementsResponseDataOrderClearanceListItemListRelatedItemDetail.from_dict(related_item_detail_item_data)



                related_item_detail.append(related_item_detail_item)


        get_order_customs_requirements_response_data_order_clearance_list_item_list = cls(
            order_line_id=order_line_id,
            product_id=product_id,
            sku_id=sku_id,
            is_virtual_unboxing=is_virtual_unboxing,
            is_temporary_listing=is_temporary_listing,
            related_item_detail=related_item_detail,
        )


        get_order_customs_requirements_response_data_order_clearance_list_item_list.additional_properties = d
        return get_order_customs_requirements_response_data_order_clearance_list_item_list

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
