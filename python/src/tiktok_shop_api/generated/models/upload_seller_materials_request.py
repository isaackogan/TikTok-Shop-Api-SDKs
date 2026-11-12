from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.upload_seller_materials_request_post_type import UploadSellerMaterialsRequestPostType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.material import Material
  from ..models.upload_seller_materials_request_material_group import UploadSellerMaterialsRequestMaterialGroup





T = TypeVar("T", bound="UploadSellerMaterialsRequest")



@_attrs_define
class UploadSellerMaterialsRequest:
    """ 
        Attributes:
            post_type (UploadSellerMaterialsRequestPostType): The posting mode for the uploaded materials.
                Possible values:
                - ONE_PRODUCT_MULTIPLE_IMAGES: Upload one or more ordered groups for one product. Use `material_groups` only.
                - ONE_PRODUCT_ONE_IMAGE: Upload standalone images for one product. Use `materials` only.
            product_id (str): The product ID that the uploaded materials belong to.
            material_groups (list[UploadSellerMaterialsRequestMaterialGroup] | Unset): Grouped materials for the
                `ONE_PRODUCT_MULTIPLE_IMAGES` mode. Provide 1 to 10 groups, omit `materials`, and keep the total number of
                uploaded images in one request within 30.
            materials (list[Material] | Unset): Materials for the `ONE_PRODUCT_ONE_IMAGE` mode. Provide 1 to 30 items and
                omit `material_groups`.
     """

    post_type: UploadSellerMaterialsRequestPostType
    product_id: str
    material_groups: list[UploadSellerMaterialsRequestMaterialGroup] | Unset = UNSET
    materials: list[Material] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.material import Material # noqa: PLC0415
        from ..models.upload_seller_materials_request_material_group import UploadSellerMaterialsRequestMaterialGroup # noqa: PLC0415
        post_type = self.post_type.value

        product_id = self.product_id

        material_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.material_groups, Unset):
            material_groups = []
            for material_groups_item_data in self.material_groups:
                material_groups_item = material_groups_item_data.to_dict()
                material_groups.append(material_groups_item)



        materials: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.materials, Unset):
            materials = []
            for materials_item_data in self.materials:
                materials_item = materials_item_data.to_dict()
                materials.append(materials_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "post_type": post_type,
            "product_id": product_id,
        })
        if material_groups is not UNSET:
            field_dict["material_groups"] = material_groups
        if materials is not UNSET:
            field_dict["materials"] = materials

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.material import Material # noqa: PLC0415
        from ..models.upload_seller_materials_request_material_group import UploadSellerMaterialsRequestMaterialGroup # noqa: PLC0415
        d = dict(src_dict)
        post_type = UploadSellerMaterialsRequestPostType(d.pop("post_type"))




        product_id = d.pop("product_id")

        _material_groups = d.pop("material_groups", UNSET)
        material_groups: list[UploadSellerMaterialsRequestMaterialGroup] | Unset = UNSET
        if _material_groups is not UNSET:
            material_groups = []
            for material_groups_item_data in _material_groups:
                material_groups_item = UploadSellerMaterialsRequestMaterialGroup.from_dict(material_groups_item_data)



                material_groups.append(material_groups_item)


        _materials = d.pop("materials", UNSET)
        materials: list[Material] | Unset = UNSET
        if _materials is not UNSET:
            materials = []
            for materials_item_data in _materials:
                materials_item = Material.from_dict(materials_item_data)



                materials.append(materials_item)


        upload_seller_materials_request = cls(
            post_type=post_type,
            product_id=product_id,
            material_groups=material_groups,
            materials=materials,
        )


        upload_seller_materials_request.additional_properties = d
        return upload_seller_materials_request

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
