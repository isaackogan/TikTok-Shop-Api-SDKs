from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.confirm_order_split_request_splittable_groups_v2_order_line_list import ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList
  from ..models.get_eligible_shipping_services_request_dimension import GetEligibleShippingServicesRequestDimension
  from ..models.get_eligible_shipping_services_request_weight import GetEligibleShippingServicesRequestWeight





T = TypeVar("T", bound="GetEligibleShippingServicesRequest")



@_attrs_define
class GetEligibleShippingServicesRequest:
    """ 
        Attributes:
            order_line_item_ids (list[str] | Unset): Order line item ID list
            weight (GetEligibleShippingServicesRequestWeight | Unset):
            dimension (GetEligibleShippingServicesRequestDimension | Unset):
            order_line_list (list[ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList] | Unset): This new parameter is
                completely backward compatible with the previous oder_line_items_ids field and in addition this supports bundle
                order splitting, use the sub items accordingly
     """

    order_line_item_ids: list[str] | Unset = UNSET
    weight: GetEligibleShippingServicesRequestWeight | Unset = UNSET
    dimension: GetEligibleShippingServicesRequestDimension | Unset = UNSET
    order_line_list: list[ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.confirm_order_split_request_splittable_groups_v2_order_line_list import ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList # noqa: PLC0415
        from ..models.get_eligible_shipping_services_request_dimension import GetEligibleShippingServicesRequestDimension # noqa: PLC0415
        from ..models.get_eligible_shipping_services_request_weight import GetEligibleShippingServicesRequestWeight # noqa: PLC0415
        order_line_item_ids: list[str] | Unset = UNSET
        if not isinstance(self.order_line_item_ids, Unset):
            order_line_item_ids = self.order_line_item_ids



        weight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()

        dimension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dimension, Unset):
            dimension = self.dimension.to_dict()

        order_line_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.order_line_list, Unset):
            order_line_list = []
            for order_line_list_item_data in self.order_line_list:
                order_line_list_item = order_line_list_item_data.to_dict()
                order_line_list.append(order_line_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_line_item_ids is not UNSET:
            field_dict["order_line_item_ids"] = order_line_item_ids
        if weight is not UNSET:
            field_dict["weight"] = weight
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if order_line_list is not UNSET:
            field_dict["order_line_list"] = order_line_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.confirm_order_split_request_splittable_groups_v2_order_line_list import ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList # noqa: PLC0415
        from ..models.get_eligible_shipping_services_request_dimension import GetEligibleShippingServicesRequestDimension # noqa: PLC0415
        from ..models.get_eligible_shipping_services_request_weight import GetEligibleShippingServicesRequestWeight # noqa: PLC0415
        d = dict(src_dict)
        order_line_item_ids = cast(list[str], d.pop("order_line_item_ids", UNSET))


        _weight = d.pop("weight", UNSET)
        weight: GetEligibleShippingServicesRequestWeight | Unset
        if isinstance(_weight,  Unset):
            weight = UNSET
        else:
            weight = GetEligibleShippingServicesRequestWeight.from_dict(_weight)




        _dimension = d.pop("dimension", UNSET)
        dimension: GetEligibleShippingServicesRequestDimension | Unset
        if isinstance(_dimension,  Unset):
            dimension = UNSET
        else:
            dimension = GetEligibleShippingServicesRequestDimension.from_dict(_dimension)




        _order_line_list = d.pop("order_line_list", UNSET)
        order_line_list: list[ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList] | Unset = UNSET
        if _order_line_list is not UNSET:
            order_line_list = []
            for order_line_list_item_data in _order_line_list:
                order_line_list_item = ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList.from_dict(order_line_list_item_data)



                order_line_list.append(order_line_list_item)


        get_eligible_shipping_services_request = cls(
            order_line_item_ids=order_line_item_ids,
            weight=weight,
            dimension=dimension,
            order_line_list=order_line_list,
        )


        get_eligible_shipping_services_request.additional_properties = d
        return get_eligible_shipping_services_request

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
