from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.publish_global_product_response_data_product_sku_sale_attribute import PublishGlobalProductResponseDataProductSkuSaleAttribute





T = TypeVar("T", bound="PublishGlobalProductResponseDataProductSku")



@_attrs_define
class PublishGlobalProductResponseDataProductSku:
    """ 
        Attributes:
            related_global_sku_id (str | Unset): The associated global SKU ID.
            id (str | Unset): The newly generated local SKU ID.
            seller_sku (str | Unset): An internal code/name for managing SKUs, not visible to buyers.
            sale_attributes (list[PublishGlobalProductResponseDataProductSkuSaleAttribute] | Unset): A list of attributes
                (e.g. size, color, length) that define each variant of a product.
     """

    related_global_sku_id: str | Unset = UNSET
    id: str | Unset = UNSET
    seller_sku: str | Unset = UNSET
    sale_attributes: list[PublishGlobalProductResponseDataProductSkuSaleAttribute] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.publish_global_product_response_data_product_sku_sale_attribute import PublishGlobalProductResponseDataProductSkuSaleAttribute # noqa: PLC0415
        related_global_sku_id = self.related_global_sku_id

        id = self.id

        seller_sku = self.seller_sku

        sale_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sale_attributes, Unset):
            sale_attributes = []
            for sale_attributes_item_data in self.sale_attributes:
                sale_attributes_item = sale_attributes_item_data.to_dict()
                sale_attributes.append(sale_attributes_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if related_global_sku_id is not UNSET:
            field_dict["related_global_sku_id"] = related_global_sku_id
        if id is not UNSET:
            field_dict["id"] = id
        if seller_sku is not UNSET:
            field_dict["seller_sku"] = seller_sku
        if sale_attributes is not UNSET:
            field_dict["sale_attributes"] = sale_attributes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.publish_global_product_response_data_product_sku_sale_attribute import PublishGlobalProductResponseDataProductSkuSaleAttribute # noqa: PLC0415
        d = dict(src_dict)
        related_global_sku_id = d.pop("related_global_sku_id", UNSET)

        id = d.pop("id", UNSET)

        seller_sku = d.pop("seller_sku", UNSET)

        _sale_attributes = d.pop("sale_attributes", UNSET)
        sale_attributes: list[PublishGlobalProductResponseDataProductSkuSaleAttribute] | Unset = UNSET
        if _sale_attributes is not UNSET:
            sale_attributes = []
            for sale_attributes_item_data in _sale_attributes:
                sale_attributes_item = PublishGlobalProductResponseDataProductSkuSaleAttribute.from_dict(sale_attributes_item_data)



                sale_attributes.append(sale_attributes_item)


        publish_global_product_response_data_product_sku = cls(
            related_global_sku_id=related_global_sku_id,
            id=id,
            seller_sku=seller_sku,
            sale_attributes=sale_attributes,
        )


        publish_global_product_response_data_product_sku.additional_properties = d
        return publish_global_product_response_data_product_sku

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
