from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.max_discount import MaxDiscount
  from ..models.reduction_amount import ReductionAmount





T = TypeVar("T", bound="GetCouponResponseDataCouponDiscount")



@_attrs_define
class GetCouponResponseDataCouponDiscount:
    """ 
        Attributes:
            type_ (str | Unset): The type of discount offered by the coupon. Possible enumerations are:
                - `AMOUNT_OFF`: Reduces the final price of the item by the specified `reduction_amount`
                - `PERCENT_OFF`: Reduces the final price by the specified `percentage`.
            reduction_amount (ReductionAmount | Unset):
            percentage (str | Unset): The discount offered by the coupon, in percentage points. Will appear when `type ==
                'PERCENT_OFF'`.
            max_discount (MaxDiscount | Unset):
     """

    type_: str | Unset = UNSET
    reduction_amount: ReductionAmount | Unset = UNSET
    percentage: str | Unset = UNSET
    max_discount: MaxDiscount | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.max_discount import MaxDiscount # noqa: PLC0415
        from ..models.reduction_amount import ReductionAmount # noqa: PLC0415
        type_ = self.type_

        reduction_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reduction_amount, Unset):
            reduction_amount = self.reduction_amount.to_dict()

        percentage = self.percentage

        max_discount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.max_discount, Unset):
            max_discount = self.max_discount.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if reduction_amount is not UNSET:
            field_dict["reduction_amount"] = reduction_amount
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if max_discount is not UNSET:
            field_dict["max_discount"] = max_discount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.max_discount import MaxDiscount # noqa: PLC0415
        from ..models.reduction_amount import ReductionAmount # noqa: PLC0415
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _reduction_amount = d.pop("reduction_amount", UNSET)
        reduction_amount: ReductionAmount | Unset
        if isinstance(_reduction_amount,  Unset):
            reduction_amount = UNSET
        else:
            reduction_amount = ReductionAmount.from_dict(_reduction_amount)




        percentage = d.pop("percentage", UNSET)

        _max_discount = d.pop("max_discount", UNSET)
        max_discount: MaxDiscount | Unset
        if isinstance(_max_discount,  Unset):
            max_discount = UNSET
        else:
            max_discount = MaxDiscount.from_dict(_max_discount)




        get_coupon_response_data_coupon_discount = cls(
            type_=type_,
            reduction_amount=reduction_amount,
            percentage=percentage,
            max_discount=max_discount,
        )


        get_coupon_response_data_coupon_discount.additional_properties = d
        return get_coupon_response_data_coupon_discount

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
