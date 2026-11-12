from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.material import Material





T = TypeVar("T", bound="UploadSellerMaterialsRequestMaterialGroup")



@_attrs_define
class UploadSellerMaterialsRequestMaterialGroup:
    """ 
        Attributes:
            materials (list[Material]): Materials in the same group, sorted by array index. Each group must contain 2 to 35
                materials.
            post_type (str): The posting mode for this material group. Use `ONE_PRODUCT_MULTIPLE_IMAGES` and keep it
                consistent with the request-level `post_type`.
     """

    materials: list[Material]
    post_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.material import Material # noqa: PLC0415
        materials = []
        for materials_item_data in self.materials:
            materials_item = materials_item_data.to_dict()
            materials.append(materials_item)



        post_type = self.post_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "materials": materials,
            "post_type": post_type,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.material import Material # noqa: PLC0415
        d = dict(src_dict)
        materials = []
        _materials = d.pop("materials")
        for materials_item_data in (_materials):
            materials_item = Material.from_dict(materials_item_data)



            materials.append(materials_item)


        post_type = d.pop("post_type")

        upload_seller_materials_request_material_group = cls(
            materials=materials,
            post_type=post_type,
        )


        upload_seller_materials_request_material_group.additional_properties = d
        return upload_seller_materials_request_material_group

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
