from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_order_customs_requirements_response_data_order_clearance_list_item_list import GetOrderCustomsRequirementsResponseDataOrderClearanceListItemList





T = TypeVar("T", bound="GetOrderCustomsRequirementsResponseDataOrderClearanceList")



@_attrs_define
class GetOrderCustomsRequirementsResponseDataOrderClearanceList:
    """ 
        Attributes:
            order_id (str | Unset): TikTok Shop order ID
            need_fill_clearance (bool | Unset): Whether an order needs to fill customs infomation:
                - true: The order needs to fill in customs information.
                - false: The order does not need to fill in custom information.
            already_filled_clearance (bool | Unset): When `need_fill_clearance` is `true`, whether customs clearance
                information has been submitted for every order line that requires it. This value is `false` when
                `need_fill_clearance` is `false`.
            target_country (str | Unset): Country Alpha-2 Code
            biz_type (int | Unset): enum CustomsBusinessType {
                    CustomsBusinessTypeFS = 1;
                    CustomsBusinessTypePOP = 2;
                }
            shipment_type (int | Unset): enum ShipmentType{
                    CROSS_BORDER = 1,
                    LOCAL = 2,
                }
            item_list (list[GetOrderCustomsRequirementsResponseDataOrderClearanceListItemList] | Unset): Order-line details
                for the order.
     """

    order_id: str | Unset = UNSET
    need_fill_clearance: bool | Unset = UNSET
    already_filled_clearance: bool | Unset = UNSET
    target_country: str | Unset = UNSET
    biz_type: int | Unset = UNSET
    shipment_type: int | Unset = UNSET
    item_list: list[GetOrderCustomsRequirementsResponseDataOrderClearanceListItemList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_order_customs_requirements_response_data_order_clearance_list_item_list import GetOrderCustomsRequirementsResponseDataOrderClearanceListItemList # noqa: PLC0415
        order_id = self.order_id

        need_fill_clearance = self.need_fill_clearance

        already_filled_clearance = self.already_filled_clearance

        target_country = self.target_country

        biz_type = self.biz_type

        shipment_type = self.shipment_type

        item_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.item_list, Unset):
            item_list = []
            for item_list_item_data in self.item_list:
                item_list_item = item_list_item_data.to_dict()
                item_list.append(item_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if need_fill_clearance is not UNSET:
            field_dict["need_fill_clearance"] = need_fill_clearance
        if already_filled_clearance is not UNSET:
            field_dict["already_filled_clearance"] = already_filled_clearance
        if target_country is not UNSET:
            field_dict["target_country"] = target_country
        if biz_type is not UNSET:
            field_dict["biz_type"] = biz_type
        if shipment_type is not UNSET:
            field_dict["shipment_type"] = shipment_type
        if item_list is not UNSET:
            field_dict["item_list"] = item_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_order_customs_requirements_response_data_order_clearance_list_item_list import GetOrderCustomsRequirementsResponseDataOrderClearanceListItemList # noqa: PLC0415
        d = dict(src_dict)
        order_id = d.pop("order_id", UNSET)

        need_fill_clearance = d.pop("need_fill_clearance", UNSET)

        already_filled_clearance = d.pop("already_filled_clearance", UNSET)

        target_country = d.pop("target_country", UNSET)

        biz_type = d.pop("biz_type", UNSET)

        shipment_type = d.pop("shipment_type", UNSET)

        _item_list = d.pop("item_list", UNSET)
        item_list: list[GetOrderCustomsRequirementsResponseDataOrderClearanceListItemList] | Unset = UNSET
        if _item_list is not UNSET:
            item_list = []
            for item_list_item_data in _item_list:
                item_list_item = GetOrderCustomsRequirementsResponseDataOrderClearanceListItemList.from_dict(item_list_item_data)



                item_list.append(item_list_item)


        get_order_customs_requirements_response_data_order_clearance_list = cls(
            order_id=order_id,
            need_fill_clearance=need_fill_clearance,
            already_filled_clearance=already_filled_clearance,
            target_country=target_country,
            biz_type=biz_type,
            shipment_type=shipment_type,
            item_list=item_list,
        )


        get_order_customs_requirements_response_data_order_clearance_list.additional_properties = d
        return get_order_customs_requirements_response_data_order_clearance_list

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
