from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_product_response_data_global_product_association_sku_mapping_sales_attribute_mapping import (
        GetProductResponseDataGlobalProductAssociationSkuMappingSalesAttributeMapping,
    )


T = TypeVar("T", bound="GetProductResponseDataGlobalProductAssociationSkuMapping")


@_attrs_define
class GetProductResponseDataGlobalProductAssociationSkuMapping:
    """
    Attributes:
        global_sku_id (str | Unset): The global SKU ID in TikTok Shop.
        local_sku_id (str | Unset): The local SKU ID in TikTok Shop.
        sales_attribute_mappings (list[GetProductResponseDataGlobalProductAssociationSkuMappingSalesAttributeMapping] |
            Unset): The list of sales attribute mappings between the global and local SKUs.
    """

    global_sku_id: str | Unset = UNSET
    local_sku_id: str | Unset = UNSET
    sales_attribute_mappings: (
        list[GetProductResponseDataGlobalProductAssociationSkuMappingSalesAttributeMapping] | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        global_sku_id = self.global_sku_id

        local_sku_id = self.local_sku_id

        sales_attribute_mappings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sales_attribute_mappings, Unset):
            sales_attribute_mappings = []
            for sales_attribute_mappings_item_data in self.sales_attribute_mappings:
                sales_attribute_mappings_item = sales_attribute_mappings_item_data.to_dict()
                sales_attribute_mappings.append(sales_attribute_mappings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if global_sku_id is not UNSET:
            field_dict["global_sku_id"] = global_sku_id
        if local_sku_id is not UNSET:
            field_dict["local_sku_id"] = local_sku_id
        if sales_attribute_mappings is not UNSET:
            field_dict["sales_attribute_mappings"] = sales_attribute_mappings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_product_response_data_global_product_association_sku_mapping_sales_attribute_mapping import (
            GetProductResponseDataGlobalProductAssociationSkuMappingSalesAttributeMapping,  # noqa: PLC0415
        )

        d = dict(src_dict)
        global_sku_id = d.pop("global_sku_id", UNSET)

        local_sku_id = d.pop("local_sku_id", UNSET)

        _sales_attribute_mappings = d.pop("sales_attribute_mappings", UNSET)
        sales_attribute_mappings: (
            list[GetProductResponseDataGlobalProductAssociationSkuMappingSalesAttributeMapping] | Unset
        ) = UNSET
        if _sales_attribute_mappings is not UNSET:
            sales_attribute_mappings = []
            for sales_attribute_mappings_item_data in _sales_attribute_mappings:
                sales_attribute_mappings_item = (
                    GetProductResponseDataGlobalProductAssociationSkuMappingSalesAttributeMapping.from_dict(
                        sales_attribute_mappings_item_data
                    )
                )

                sales_attribute_mappings.append(sales_attribute_mappings_item)

        get_product_response_data_global_product_association_sku_mapping = cls(
            global_sku_id=global_sku_id,
            local_sku_id=local_sku_id,
            sales_attribute_mappings=sales_attribute_mappings,
        )

        get_product_response_data_global_product_association_sku_mapping.additional_properties = d
        return get_product_response_data_global_product_association_sku_mapping

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
