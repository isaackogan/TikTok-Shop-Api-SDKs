from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_global_replicated_products_response_data_replicated_product_product_status import (
    GetGlobalReplicatedProductsResponseDataReplicatedProductProductStatus,
)
from ..models.get_global_replicated_products_response_data_replicated_product_region import (
    GetGlobalReplicatedProductsResponseDataReplicatedProductRegion,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGlobalReplicatedProductsResponseDataReplicatedProduct")


@_attrs_define
class GetGlobalReplicatedProductsResponseDataReplicatedProduct:
    """
    Attributes:
        region (GetGlobalReplicatedProductsResponseDataReplicatedProductRegion | Unset): The market associated with the
            replicated product.
            Possible values:
            - AT: Austria
            - BE:Belgium
            - CZ:Czech Republic
            - DE: Germany
            - ES: Spain
            - FR: France
            - GB: United Kingdom
            - GR: Greece
            - HU:Hungary
            - ID: Indonesia
            - IE: Ireland
            - IT: Italy
            - JP: Japan
            - MY: Malaysia
            - NL: Netherlands(NL)
            - PH: Philippines
            - PO: Poland
            - PT:Portugal
            - SG: Singapore
            - TH: Thailand
            - US: United States
            - VN: Vietnam
            - MX: Mexico
        shop_id (str | Unset): The TikTok Shop ID.
        product_id (str | Unset): The ID of the product.
        product_status (GetGlobalReplicatedProductsResponseDataReplicatedProductProductStatus | Unset): The status of
            the replicated product.
            Possible values:
            - UNKNOWN
            - DRAFT
            - PENDING
            - FAILED
            - ACTIVATE
            - SELLER_DEACTIVATED
            - PLATFORM_DEACTIVATED
            - FREEZE
            - DELETED
    """

    region: GetGlobalReplicatedProductsResponseDataReplicatedProductRegion | Unset = UNSET
    shop_id: str | Unset = UNSET
    product_id: str | Unset = UNSET
    product_status: GetGlobalReplicatedProductsResponseDataReplicatedProductProductStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region: str | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        shop_id = self.shop_id

        product_id = self.product_id

        product_status: str | Unset = UNSET
        if not isinstance(self.product_status, Unset):
            product_status = self.product_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region is not UNSET:
            field_dict["region"] = region
        if shop_id is not UNSET:
            field_dict["shop_id"] = shop_id
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_status is not UNSET:
            field_dict["product_status"] = product_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _region = d.pop("region", UNSET)
        region: GetGlobalReplicatedProductsResponseDataReplicatedProductRegion | Unset
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = GetGlobalReplicatedProductsResponseDataReplicatedProductRegion(_region)

        shop_id = d.pop("shop_id", UNSET)

        product_id = d.pop("product_id", UNSET)

        _product_status = d.pop("product_status", UNSET)
        product_status: GetGlobalReplicatedProductsResponseDataReplicatedProductProductStatus | Unset
        if isinstance(_product_status, Unset):
            product_status = UNSET
        else:
            product_status = GetGlobalReplicatedProductsResponseDataReplicatedProductProductStatus(_product_status)

        get_global_replicated_products_response_data_replicated_product = cls(
            region=region,
            shop_id=shop_id,
            product_id=product_id,
            product_status=product_status,
        )

        get_global_replicated_products_response_data_replicated_product.additional_properties = d
        return get_global_replicated_products_response_data_replicated_product

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
