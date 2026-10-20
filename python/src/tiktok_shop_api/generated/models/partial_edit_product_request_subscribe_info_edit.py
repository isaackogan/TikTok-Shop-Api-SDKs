from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.discount_detail import DiscountDetail





T = TypeVar("T", bound="PartialEditProductRequestSubscribeInfoEdit")



@_attrs_define
class PartialEditProductRequestSubscribeInfoEdit:
    """ 
        Attributes:
            discount_details (list[DiscountDetail] | Unset): All of the Save and Subscribe discount details.
            subscribe_status (str | Unset): An enum outlining whether the given product has an active Subscribe and Save
                promotion:
                - ENABLED
                - NOT_ENABLED

                This field is required if the subscription is being created or modified.
     """

    discount_details: list[DiscountDetail] | Unset = UNSET
    subscribe_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.discount_detail import DiscountDetail # noqa: PLC0415
        discount_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.discount_details, Unset):
            discount_details = []
            for discount_details_item_data in self.discount_details:
                discount_details_item = discount_details_item_data.to_dict()
                discount_details.append(discount_details_item)



        subscribe_status = self.subscribe_status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if discount_details is not UNSET:
            field_dict["discount_details"] = discount_details
        if subscribe_status is not UNSET:
            field_dict["subscribe_status"] = subscribe_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discount_detail import DiscountDetail # noqa: PLC0415
        d = dict(src_dict)
        _discount_details = d.pop("discount_details", UNSET)
        discount_details: list[DiscountDetail] | Unset = UNSET
        if _discount_details is not UNSET:
            discount_details = []
            for discount_details_item_data in _discount_details:
                discount_details_item = DiscountDetail.from_dict(discount_details_item_data)



                discount_details.append(discount_details_item)


        subscribe_status = d.pop("subscribe_status", UNSET)

        partial_edit_product_request_subscribe_info_edit = cls(
            discount_details=discount_details,
            subscribe_status=subscribe_status,
        )


        partial_edit_product_request_subscribe_info_edit.additional_properties = d
        return partial_edit_product_request_subscribe_info_edit

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
