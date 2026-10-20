from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_global_product_response_data_sku_sales_attribute_sku_img import GetGlobalProductResponseDataSkuSalesAttributeSkuImg





T = TypeVar("T", bound="GetGlobalProductResponseDataSkuSalesAttribute")



@_attrs_define
class GetGlobalProductResponseDataSkuSalesAttribute:
    """ 
        Attributes:
            id (str | Unset): The sales attribute ID.
            name (str | Unset): The sales attribute name.
            value_id (str | Unset): The sales attribute value ID.
            value_name (str | Unset): The sales attribute value name.
            sku_img (GetGlobalProductResponseDataSkuSalesAttributeSkuImg | Unset):
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    value_id: str | Unset = UNSET
    value_name: str | Unset = UNSET
    sku_img: GetGlobalProductResponseDataSkuSalesAttributeSkuImg | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_global_product_response_data_sku_sales_attribute_sku_img import GetGlobalProductResponseDataSkuSalesAttributeSkuImg # noqa: PLC0415
        id = self.id

        name = self.name

        value_id = self.value_id

        value_name = self.value_name

        sku_img: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sku_img, Unset):
            sku_img = self.sku_img.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if value_id is not UNSET:
            field_dict["value_id"] = value_id
        if value_name is not UNSET:
            field_dict["value_name"] = value_name
        if sku_img is not UNSET:
            field_dict["sku_img"] = sku_img

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_global_product_response_data_sku_sales_attribute_sku_img import GetGlobalProductResponseDataSkuSalesAttributeSkuImg # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        value_id = d.pop("value_id", UNSET)

        value_name = d.pop("value_name", UNSET)

        _sku_img = d.pop("sku_img", UNSET)
        sku_img: GetGlobalProductResponseDataSkuSalesAttributeSkuImg | Unset
        if isinstance(_sku_img,  Unset):
            sku_img = UNSET
        else:
            sku_img = GetGlobalProductResponseDataSkuSalesAttributeSkuImg.from_dict(_sku_img)




        get_global_product_response_data_sku_sales_attribute = cls(
            id=id,
            name=name,
            value_id=value_id,
            value_name=value_name,
            sku_img=sku_img,
        )


        get_global_product_response_data_sku_sales_attribute.additional_properties = d
        return get_global_product_response_data_sku_sales_attribute

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
