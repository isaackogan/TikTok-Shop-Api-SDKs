from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_global_product_response_data_product_sku_mapping import GetGlobalProductResponseDataProductSkuMapping





T = TypeVar("T", bound="GetGlobalProductResponseDataProduct")



@_attrs_define
class GetGlobalProductResponseDataProduct:
    """ 
        Attributes:
            region (str | Unset): The market where the local product is listed.
            id (str | Unset): The local product ID.
            sku_mappings (list[GetGlobalProductResponseDataProductSkuMapping] | Unset): The list of sku mappings between the
                global and local products.
     """

    region: str | Unset = UNSET
    id: str | Unset = UNSET
    sku_mappings: list[GetGlobalProductResponseDataProductSkuMapping] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_global_product_response_data_product_sku_mapping import GetGlobalProductResponseDataProductSkuMapping # noqa: PLC0415
        region = self.region

        id = self.id

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
        if region is not UNSET:
            field_dict["region"] = region
        if id is not UNSET:
            field_dict["id"] = id
        if sku_mappings is not UNSET:
            field_dict["sku_mappings"] = sku_mappings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_global_product_response_data_product_sku_mapping import GetGlobalProductResponseDataProductSkuMapping # noqa: PLC0415
        d = dict(src_dict)
        region = d.pop("region", UNSET)

        id = d.pop("id", UNSET)

        _sku_mappings = d.pop("sku_mappings", UNSET)
        sku_mappings: list[GetGlobalProductResponseDataProductSkuMapping] | Unset = UNSET
        if _sku_mappings is not UNSET:
            sku_mappings = []
            for sku_mappings_item_data in _sku_mappings:
                sku_mappings_item = GetGlobalProductResponseDataProductSkuMapping.from_dict(sku_mappings_item_data)



                sku_mappings.append(sku_mappings_item)


        get_global_product_response_data_product = cls(
            region=region,
            id=id,
            sku_mappings=sku_mappings,
        )


        get_global_product_response_data_product.additional_properties = d
        return get_global_product_response_data_product

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
