from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_product_response_data_global_product_association_sku_mapping import GetProductResponseDataGlobalProductAssociationSkuMapping





T = TypeVar("T", bound="GetProductResponseDataGlobalProductAssociation")



@_attrs_define
class GetProductResponseDataGlobalProductAssociation:
    """ 
        Attributes:
            global_product_id (str | Unset): The global product ID in TikTok Shop.
            sku_mappings (list[GetProductResponseDataGlobalProductAssociationSkuMapping] | Unset): The list of sku mappings
                between the global and local products.
     """

    global_product_id: str | Unset = UNSET
    sku_mappings: list[GetProductResponseDataGlobalProductAssociationSkuMapping] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_product_response_data_global_product_association_sku_mapping import GetProductResponseDataGlobalProductAssociationSkuMapping # noqa: PLC0415
        global_product_id = self.global_product_id

        sku_mappings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sku_mappings, Unset):
            sku_mappings = []
            for sku_mappings_item_data in self.sku_mappings:
                sku_mappings_item = sku_mappings_item_data.to_dict()
                sku_mappings.append(sku_mappings_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if global_product_id is not UNSET:
            field_dict["global_product_id"] = global_product_id
        if sku_mappings is not UNSET:
            field_dict["sku_mappings"] = sku_mappings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_product_response_data_global_product_association_sku_mapping import GetProductResponseDataGlobalProductAssociationSkuMapping # noqa: PLC0415
        d = dict(src_dict)
        global_product_id = d.pop("global_product_id", UNSET)

        _sku_mappings = d.pop("sku_mappings", UNSET)
        sku_mappings: list[GetProductResponseDataGlobalProductAssociationSkuMapping] | Unset = UNSET
        if _sku_mappings is not UNSET:
            sku_mappings = []
            for sku_mappings_item_data in _sku_mappings:
                sku_mappings_item = GetProductResponseDataGlobalProductAssociationSkuMapping.from_dict(sku_mappings_item_data)



                sku_mappings.append(sku_mappings_item)


        get_product_response_data_global_product_association = cls(
            global_product_id=global_product_id,
            sku_mappings=sku_mappings,
        )


        get_product_response_data_global_product_association.additional_properties = d
        return get_product_response_data_global_product_association

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
