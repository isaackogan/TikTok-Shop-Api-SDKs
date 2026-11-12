from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.upload_seller_materials_response_data_material_group_material import UploadSellerMaterialsResponseDataMaterialGroupMaterial





T = TypeVar("T", bound="UploadSellerMaterialsResponseDataMaterialGroup")



@_attrs_define
class UploadSellerMaterialsResponseDataMaterialGroup:
    """ 
        Attributes:
            image_group_id (str | Unset): The generated image group ID for the uploaded material group.
            materials (list[UploadSellerMaterialsResponseDataMaterialGroupMaterial] | Unset): Materials in the uploaded
                group with generated material IDs.
     """

    image_group_id: str | Unset = UNSET
    materials: list[UploadSellerMaterialsResponseDataMaterialGroupMaterial] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.upload_seller_materials_response_data_material_group_material import UploadSellerMaterialsResponseDataMaterialGroupMaterial # noqa: PLC0415
        image_group_id = self.image_group_id

        materials: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.materials, Unset):
            materials = []
            for materials_item_data in self.materials:
                materials_item = materials_item_data.to_dict()
                materials.append(materials_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if image_group_id is not UNSET:
            field_dict["image_group_id"] = image_group_id
        if materials is not UNSET:
            field_dict["materials"] = materials

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upload_seller_materials_response_data_material_group_material import UploadSellerMaterialsResponseDataMaterialGroupMaterial # noqa: PLC0415
        d = dict(src_dict)
        image_group_id = d.pop("image_group_id", UNSET)

        _materials = d.pop("materials", UNSET)
        materials: list[UploadSellerMaterialsResponseDataMaterialGroupMaterial] | Unset = UNSET
        if _materials is not UNSET:
            materials = []
            for materials_item_data in _materials:
                materials_item = UploadSellerMaterialsResponseDataMaterialGroupMaterial.from_dict(materials_item_data)



                materials.append(materials_item)


        upload_seller_materials_response_data_material_group = cls(
            image_group_id=image_group_id,
            materials=materials,
        )


        upload_seller_materials_response_data_material_group.additional_properties = d
        return upload_seller_materials_response_data_material_group

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
