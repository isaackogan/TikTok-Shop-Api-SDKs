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





T = TypeVar("T", bound="GetAftersaleEligibilityResponseDataSkuEligibilityLineItemEligibility")



@_attrs_define
class GetAftersaleEligibilityResponseDataSkuEligibilityLineItemEligibility:
    """ 
        Attributes:
            request_type (str | Unset): Aftersale request type.
                Possible values:
                - `CANCEL`
                - `REFUND`
                - `RETURN_AND_REFUND`
            order_line_items_ids (list[str] | Unset): Specifies the order line IDs. **Note:** This is a legacy field for new
                integrations use `order_line_list` instead.
            eligible (bool | Unset): Indicates whether the order lines in this entry are eligible for the entry's aftersale
                request type:
                - `true`: The order lines are eligible for the request type.
                - `false`: The order lines are ineligible for the request type.
            ineligible_code (int | Unset): The reason code for an ineligible aftersale request.
            ineligible_reason (str | Unset): The reason for an ineligible aftersale request.
            available_reason_names (list[str] | Unset): A list of reason names that can be used when creating a follow-up
                aftersale request.
            order_line_list (list[OrderLineList] | Unset): Specifies the order line items. **Note:** This field is
                completely backward compatible with the previous `order_line_items_ids` field.
     """

    request_type: str | Unset = UNSET
    order_line_items_ids: list[str] | Unset = UNSET
    eligible: bool | Unset = UNSET
    ineligible_code: int | Unset = UNSET
    ineligible_reason: str | Unset = UNSET
    available_reason_names: list[str] | Unset = UNSET
    order_line_list: list[OrderLineList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.order_line_list import OrderLineList # noqa: PLC0415
        request_type = self.request_type

        order_line_items_ids: list[str] | Unset = UNSET
        if not isinstance(self.order_line_items_ids, Unset):
            order_line_items_ids = self.order_line_items_ids



        eligible = self.eligible

        ineligible_code = self.ineligible_code

        ineligible_reason = self.ineligible_reason

        available_reason_names: list[str] | Unset = UNSET
        if not isinstance(self.available_reason_names, Unset):
            available_reason_names = self.available_reason_names



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
        if request_type is not UNSET:
            field_dict["request_type"] = request_type
        if order_line_items_ids is not UNSET:
            field_dict["order_line_items_ids"] = order_line_items_ids
        if eligible is not UNSET:
            field_dict["eligible"] = eligible
        if ineligible_code is not UNSET:
            field_dict["ineligible_code"] = ineligible_code
        if ineligible_reason is not UNSET:
            field_dict["ineligible_reason"] = ineligible_reason
        if available_reason_names is not UNSET:
            field_dict["available_reason_names"] = available_reason_names
        if order_line_list is not UNSET:
            field_dict["order_line_list"] = order_line_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_line_list import OrderLineList # noqa: PLC0415
        d = dict(src_dict)
        request_type = d.pop("request_type", UNSET)

        order_line_items_ids = cast(list[str], d.pop("order_line_items_ids", UNSET))


        eligible = d.pop("eligible", UNSET)

        ineligible_code = d.pop("ineligible_code", UNSET)

        ineligible_reason = d.pop("ineligible_reason", UNSET)

        available_reason_names = cast(list[str], d.pop("available_reason_names", UNSET))


        _order_line_list = d.pop("order_line_list", UNSET)
        order_line_list: list[OrderLineList] | Unset = UNSET
        if _order_line_list is not UNSET:
            order_line_list = []
            for order_line_list_item_data in _order_line_list:
                order_line_list_item = OrderLineList.from_dict(order_line_list_item_data)



                order_line_list.append(order_line_list_item)


        get_aftersale_eligibility_response_data_sku_eligibility_line_item_eligibility = cls(
            request_type=request_type,
            order_line_items_ids=order_line_items_ids,
            eligible=eligible,
            ineligible_code=ineligible_code,
            ineligible_reason=ineligible_reason,
            available_reason_names=available_reason_names,
            order_line_list=order_line_list,
        )


        get_aftersale_eligibility_response_data_sku_eligibility_line_item_eligibility.additional_properties = d
        return get_aftersale_eligibility_response_data_sku_eligibility_line_item_eligibility

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
