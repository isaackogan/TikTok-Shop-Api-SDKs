from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_packages_request_dimension import CreatePackagesRequestDimension
  from ..models.create_packages_request_order_line_item import CreatePackagesRequestOrderLineItem
  from ..models.create_packages_request_weight import CreatePackagesRequestWeight





T = TypeVar("T", bound="CreatePackagesRequest")



@_attrs_define
class CreatePackagesRequest:
    """ 
        Attributes:
            ship_type (str): 1:All the products in one order are shipped in one package with one tracking number
                  2:Partical products in one parent order are shipped in multiple packages with multiple tracking numbers
                  3:All the products in multiple orders are shipped in one package with one tracking number.
            order_id (str | Unset): The TikTok Shop order ID. Required when `ship_type` is `1` or `2`; not used when
                `ship_type` is `3`.
            order_line_item (list[CreatePackagesRequestOrderLineItem] | Unset): List of order line item IDs.
                If ship_type=2,This is a required field;If ship_type=1&3,we will not use this field
            order_list_ids (list[str] | Unset): The TikTok Shop order IDs to combine into one package. Required when
                `ship_type` is `3`; provide at least two order IDs.
            dimension (CreatePackagesRequestDimension | Unset):
            shipping_service_id (str | Unset): Specify the shipping service used.
                If not specified, use the default service obtained from [Get Eligible Shipping
                Service](https://partner.tiktokshop.com/docv2/page/650aa6b2bace3e02b75dda4e).
            weight (CreatePackagesRequestWeight | Unset):
     """

    ship_type: str
    order_id: str | Unset = UNSET
    order_line_item: list[CreatePackagesRequestOrderLineItem] | Unset = UNSET
    order_list_ids: list[str] | Unset = UNSET
    dimension: CreatePackagesRequestDimension | Unset = UNSET
    shipping_service_id: str | Unset = UNSET
    weight: CreatePackagesRequestWeight | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_packages_request_dimension import CreatePackagesRequestDimension # noqa: PLC0415
        from ..models.create_packages_request_order_line_item import CreatePackagesRequestOrderLineItem # noqa: PLC0415
        from ..models.create_packages_request_weight import CreatePackagesRequestWeight # noqa: PLC0415
        ship_type = self.ship_type

        order_id = self.order_id

        order_line_item: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.order_line_item, Unset):
            order_line_item = []
            for order_line_item_item_data in self.order_line_item:
                order_line_item_item = order_line_item_item_data.to_dict()
                order_line_item.append(order_line_item_item)



        order_list_ids: list[str] | Unset = UNSET
        if not isinstance(self.order_list_ids, Unset):
            order_list_ids = self.order_list_ids



        dimension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dimension, Unset):
            dimension = self.dimension.to_dict()

        shipping_service_id = self.shipping_service_id

        weight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ship_type": ship_type,
        })
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if order_line_item is not UNSET:
            field_dict["order_line_item"] = order_line_item
        if order_list_ids is not UNSET:
            field_dict["order_list_ids"] = order_list_ids
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if shipping_service_id is not UNSET:
            field_dict["shipping_service_id"] = shipping_service_id
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_packages_request_dimension import CreatePackagesRequestDimension # noqa: PLC0415
        from ..models.create_packages_request_order_line_item import CreatePackagesRequestOrderLineItem # noqa: PLC0415
        from ..models.create_packages_request_weight import CreatePackagesRequestWeight # noqa: PLC0415
        d = dict(src_dict)
        ship_type = d.pop("ship_type")

        order_id = d.pop("order_id", UNSET)

        _order_line_item = d.pop("order_line_item", UNSET)
        order_line_item: list[CreatePackagesRequestOrderLineItem] | Unset = UNSET
        if _order_line_item is not UNSET:
            order_line_item = []
            for order_line_item_item_data in _order_line_item:
                order_line_item_item = CreatePackagesRequestOrderLineItem.from_dict(order_line_item_item_data)



                order_line_item.append(order_line_item_item)


        order_list_ids = cast(list[str], d.pop("order_list_ids", UNSET))


        _dimension = d.pop("dimension", UNSET)
        dimension: CreatePackagesRequestDimension | Unset
        if isinstance(_dimension,  Unset):
            dimension = UNSET
        else:
            dimension = CreatePackagesRequestDimension.from_dict(_dimension)




        shipping_service_id = d.pop("shipping_service_id", UNSET)

        _weight = d.pop("weight", UNSET)
        weight: CreatePackagesRequestWeight | Unset
        if isinstance(_weight,  Unset):
            weight = UNSET
        else:
            weight = CreatePackagesRequestWeight.from_dict(_weight)




        create_packages_request = cls(
            ship_type=ship_type,
            order_id=order_id,
            order_line_item=order_line_item,
            order_list_ids=order_list_ids,
            dimension=dimension,
            shipping_service_id=shipping_service_id,
            weight=weight,
        )


        create_packages_request.additional_properties = d
        return create_packages_request

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
