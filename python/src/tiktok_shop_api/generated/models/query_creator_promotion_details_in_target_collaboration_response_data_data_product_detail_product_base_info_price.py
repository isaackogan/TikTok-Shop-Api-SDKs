from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.max_price import MaxPrice
  from ..models.min_price import MinPrice





T = TypeVar("T", bound="QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoPrice")



@_attrs_define
class QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoPrice:
    """ 
        Attributes:
            min_price (MinPrice | Unset):
            max_price (MaxPrice | Unset):
     """

    min_price: MinPrice | Unset = UNSET
    max_price: MaxPrice | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.max_price import MaxPrice # noqa: PLC0415
        from ..models.min_price import MinPrice # noqa: PLC0415
        min_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.min_price, Unset):
            min_price = self.min_price.to_dict()

        max_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.max_price, Unset):
            max_price = self.max_price.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if min_price is not UNSET:
            field_dict["min_price"] = min_price
        if max_price is not UNSET:
            field_dict["max_price"] = max_price

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.max_price import MaxPrice # noqa: PLC0415
        from ..models.min_price import MinPrice # noqa: PLC0415
        d = dict(src_dict)
        _min_price = d.pop("min_price", UNSET)
        min_price: MinPrice | Unset
        if isinstance(_min_price,  Unset):
            min_price = UNSET
        else:
            min_price = MinPrice.from_dict(_min_price)




        _max_price = d.pop("max_price", UNSET)
        max_price: MaxPrice | Unset
        if isinstance(_max_price,  Unset):
            max_price = UNSET
        else:
            max_price = MaxPrice.from_dict(_max_price)




        query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail_product_base_info_price = cls(
            min_price=min_price,
            max_price=max_price,
        )


        query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail_product_base_info_price.additional_properties = d
        return query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail_product_base_info_price

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
