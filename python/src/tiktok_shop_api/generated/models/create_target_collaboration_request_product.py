from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateTargetCollaborationRequestProduct")



@_attrs_define
class CreateTargetCollaborationRequestProduct:
    """ 
        Attributes:
            id (str): The product identifier.
            target_commission_rate (int): The desired commission rate for the target collaboration. The desired commission
                rate is expressed in hundredths of a percent. For example, `3587` is a commission rate of `35.87%`. This value
                must a minimum of `100`.
            shop_ads_commission_rate (int | Unset): The commission rate applies only to orders generated from ads. If a
                creator’s video is used as an ad without this rate being set, the resulting orders will instead earn either:
                - The Shop Ads commission you configured in open collaboration, or
                - The standard commission defined in this invitation.
                The commission rate is specified in increments of 1/10,000.
                For example, 1000 stands for 0.1 or 10%.
     """

    id: str
    target_commission_rate: int
    shop_ads_commission_rate: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        target_commission_rate = self.target_commission_rate

        shop_ads_commission_rate = self.shop_ads_commission_rate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "target_commission_rate": target_commission_rate,
        })
        if shop_ads_commission_rate is not UNSET:
            field_dict["shop_ads_commission_rate"] = shop_ads_commission_rate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        target_commission_rate = d.pop("target_commission_rate")

        shop_ads_commission_rate = d.pop("shop_ads_commission_rate", UNSET)

        create_target_collaboration_request_product = cls(
            id=id,
            target_commission_rate=target_commission_rate,
            shop_ads_commission_rate=shop_ads_commission_rate,
        )


        create_target_collaboration_request_product.additional_properties = d
        return create_target_collaboration_request_product

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
