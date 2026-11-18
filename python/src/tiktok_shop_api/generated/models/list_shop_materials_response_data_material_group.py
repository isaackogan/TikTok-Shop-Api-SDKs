from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.list_shop_materials_response_data_material_group_material import ListShopMaterialsResponseDataMaterialGroupMaterial





T = TypeVar("T", bound="ListShopMaterialsResponseDataMaterialGroup")



@_attrs_define
class ListShopMaterialsResponseDataMaterialGroup:
    """ 
        Attributes:
            post_type (str): The posting mode of the material group.
                Possible values:
                - POST_TYPE_UNSPECIFIED: The posting mode is not specified.
                - ONE_PRODUCT_MULTIPLE_IMAGES: One product is associated with multiple ordered images in the same group.
                - ONE_PRODUCT_ONE_IMAGE: One product is associated with one standalone image.
            image_group_id (str | Unset): The image group ID. The value is `0` for a single-image material.
            material_status (str | Unset): The business status shared by the material group.
                Possible values:
                - MATERIAL_STATUS_UNSPECIFIED: The business status is not specified.
                - LIVE: The material group is effective online.
                - UNDER_REVIEW: The material group is still under review.
                - REJECTED: The material group was rejected.
                - PENDING_SELLER_REVIEW: The material group is waiting for seller review.
            materials (list[ListShopMaterialsResponseDataMaterialGroupMaterial] | Unset): Materials contained in this group.
                Single-image groups contain one item.
     """

    post_type: str
    image_group_id: str | Unset = UNSET
    material_status: str | Unset = UNSET
    materials: list[ListShopMaterialsResponseDataMaterialGroupMaterial] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_shop_materials_response_data_material_group_material import ListShopMaterialsResponseDataMaterialGroupMaterial # noqa: PLC0415
        post_type = self.post_type

        image_group_id = self.image_group_id

        material_status = self.material_status

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
        })
        if image_group_id is not UNSET:
            field_dict["image_group_id"] = image_group_id
        if material_status is not UNSET:
            field_dict["material_status"] = material_status
        if materials is not UNSET:
            field_dict["materials"] = materials

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_shop_materials_response_data_material_group_material import ListShopMaterialsResponseDataMaterialGroupMaterial # noqa: PLC0415
        d = dict(src_dict)
        post_type = d.pop("post_type")

        image_group_id = d.pop("image_group_id", UNSET)

        material_status = d.pop("material_status", UNSET)

        _materials = d.pop("materials", UNSET)
        materials: list[ListShopMaterialsResponseDataMaterialGroupMaterial] | Unset = UNSET
        if _materials is not UNSET:
            materials = []
            for materials_item_data in _materials:
                materials_item = ListShopMaterialsResponseDataMaterialGroupMaterial.from_dict(materials_item_data)



                materials.append(materials_item)


        list_shop_materials_response_data_material_group = cls(
            post_type=post_type,
            image_group_id=image_group_id,
            material_status=material_status,
            materials=materials,
        )


        list_shop_materials_response_data_material_group.additional_properties = d
        return list_shop_materials_response_data_material_group

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
