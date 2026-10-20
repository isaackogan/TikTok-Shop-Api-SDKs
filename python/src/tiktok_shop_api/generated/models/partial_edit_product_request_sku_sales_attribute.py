from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.sku_img import SkuImg
  from ..models.supplementary_sku_image import SupplementarySkuImage





T = TypeVar("T", bound="PartialEditProductRequestSkuSalesAttribute")



@_attrs_define
class PartialEditProductRequestSkuSalesAttribute:
    """ 
        Attributes:
            id (str | Unset): The ID of the sales attribute.
                This is either a built-in sales attribute ID from [Get Attributes
                API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8) or a custom attribute ID returned after
                calling [Create Product API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a).
            name (str | Unset): A self-defined custom sales attribute name if the existing attributes do not satisfy your
                needs. The system will auto-generate an ID after editing.

                **Note**:
                - Do not include sensitive characters.
                - Max length: 20 characters
            sku_img (SkuImg | Unset):
            supplementary_sku_images (list[SupplementarySkuImage] | Unset): A list of supplementary images for each value
                (e.g. red) of the primary sales attribute (e.g. color) to provide multiple views or details of the product for
                that attribute value. These appear in the product options gallery on TikTok Shop.

                **Note**:
                - Max number of image URIs: 8.
                - Arrange your image URIs in the sequence that they should appear on TikTok Shop.
                - Applicable only for the US market.
            value_id (str | Unset): The ID of the sales attribute value.
                This is either a built-in sales attribute value ID from [Get Attributes
                API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8) or a custom sales attribute value ID
                returned after calling [Create Product API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a).
            value_name (str | Unset): A self-defined custom sales attribute value if the existing values do not satisfy your
                needs. The system will auto-generate an ID after editing.

                **Note**:
                - No duplicates allowed under the same attribute.
                - Max length: 50 characters.
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    sku_img: SkuImg | Unset = UNSET
    supplementary_sku_images: list[SupplementarySkuImage] | Unset = UNSET
    value_id: str | Unset = UNSET
    value_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sku_img import SkuImg # noqa: PLC0415
        from ..models.supplementary_sku_image import SupplementarySkuImage # noqa: PLC0415
        id = self.id

        name = self.name

        sku_img: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sku_img, Unset):
            sku_img = self.sku_img.to_dict()

        supplementary_sku_images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.supplementary_sku_images, Unset):
            supplementary_sku_images = []
            for supplementary_sku_images_item_data in self.supplementary_sku_images:
                supplementary_sku_images_item = supplementary_sku_images_item_data.to_dict()
                supplementary_sku_images.append(supplementary_sku_images_item)



        value_id = self.value_id

        value_name = self.value_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if sku_img is not UNSET:
            field_dict["sku_img"] = sku_img
        if supplementary_sku_images is not UNSET:
            field_dict["supplementary_sku_images"] = supplementary_sku_images
        if value_id is not UNSET:
            field_dict["value_id"] = value_id
        if value_name is not UNSET:
            field_dict["value_name"] = value_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sku_img import SkuImg # noqa: PLC0415
        from ..models.supplementary_sku_image import SupplementarySkuImage # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _sku_img = d.pop("sku_img", UNSET)
        sku_img: SkuImg | Unset
        if isinstance(_sku_img,  Unset):
            sku_img = UNSET
        else:
            sku_img = SkuImg.from_dict(_sku_img)




        _supplementary_sku_images = d.pop("supplementary_sku_images", UNSET)
        supplementary_sku_images: list[SupplementarySkuImage] | Unset = UNSET
        if _supplementary_sku_images is not UNSET:
            supplementary_sku_images = []
            for supplementary_sku_images_item_data in _supplementary_sku_images:
                supplementary_sku_images_item = SupplementarySkuImage.from_dict(supplementary_sku_images_item_data)



                supplementary_sku_images.append(supplementary_sku_images_item)


        value_id = d.pop("value_id", UNSET)

        value_name = d.pop("value_name", UNSET)

        partial_edit_product_request_sku_sales_attribute = cls(
            id=id,
            name=name,
            sku_img=sku_img,
            supplementary_sku_images=supplementary_sku_images,
            value_id=value_id,
            value_name=value_name,
        )


        partial_edit_product_request_sku_sales_attribute.additional_properties = d
        return partial_edit_product_request_sku_sales_attribute

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
