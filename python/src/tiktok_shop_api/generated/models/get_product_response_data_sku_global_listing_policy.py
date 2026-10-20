from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_product_response_data_sku_global_listing_policy_replicate_source import GetProductResponseDataSkuGlobalListingPolicyReplicateSource





T = TypeVar("T", bound="GetProductResponseDataSkuGlobalListingPolicy")



@_attrs_define
class GetProductResponseDataSkuGlobalListingPolicy:
    """ 
        Attributes:
            inventory_type (str | Unset): The type of inventory to synchronize.
                Possible values:
                - SHARED: Inventory Area Sharing
                - EXCLUSIVE: Inventory Exclusive
            price_sync (bool | Unset): A flag indicating whether the product price is synchronized.
            replicate_source (GetProductResponseDataSkuGlobalListingPolicyReplicateSource | Unset):
     """

    inventory_type: str | Unset = UNSET
    price_sync: bool | Unset = UNSET
    replicate_source: GetProductResponseDataSkuGlobalListingPolicyReplicateSource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_product_response_data_sku_global_listing_policy_replicate_source import GetProductResponseDataSkuGlobalListingPolicyReplicateSource # noqa: PLC0415
        inventory_type = self.inventory_type

        price_sync = self.price_sync

        replicate_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.replicate_source, Unset):
            replicate_source = self.replicate_source.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if inventory_type is not UNSET:
            field_dict["inventory_type"] = inventory_type
        if price_sync is not UNSET:
            field_dict["price_sync"] = price_sync
        if replicate_source is not UNSET:
            field_dict["replicate_source"] = replicate_source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_product_response_data_sku_global_listing_policy_replicate_source import GetProductResponseDataSkuGlobalListingPolicyReplicateSource # noqa: PLC0415
        d = dict(src_dict)
        inventory_type = d.pop("inventory_type", UNSET)

        price_sync = d.pop("price_sync", UNSET)

        _replicate_source = d.pop("replicate_source", UNSET)
        replicate_source: GetProductResponseDataSkuGlobalListingPolicyReplicateSource | Unset
        if isinstance(_replicate_source,  Unset):
            replicate_source = UNSET
        else:
            replicate_source = GetProductResponseDataSkuGlobalListingPolicyReplicateSource.from_dict(_replicate_source)




        get_product_response_data_sku_global_listing_policy = cls(
            inventory_type=inventory_type,
            price_sync=price_sync,
            replicate_source=replicate_source,
        )


        get_product_response_data_sku_global_listing_policy.additional_properties = d
        return get_product_response_data_sku_global_listing_policy

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
