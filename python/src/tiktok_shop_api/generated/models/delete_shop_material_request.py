from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.delete_shop_material_request_delete_type import DeleteShopMaterialRequestDeleteType
from ..types import UNSET, Unset






T = TypeVar("T", bound="DeleteShopMaterialRequest")



@_attrs_define
class DeleteShopMaterialRequest:
    """ 
        Attributes:
            delete_type (DeleteShopMaterialRequestDeleteType): The deletion mode for the material.
                Possible values:
                - ONE_PRODUCT_MULTIPLE_IMAGES: Delete a grouped material set by `image_group_id`.
                - ONE_PRODUCT_ONE_IMAGE: Delete one standalone material by `material_id`.
            image_group_id (str | Unset): The image group ID to delete when `delete_type` is `ONE_PRODUCT_MULTIPLE_IMAGES`.
            material_id (str | Unset): The material ID to delete when `delete_type` is `ONE_PRODUCT_ONE_IMAGE`.
     """

    delete_type: DeleteShopMaterialRequestDeleteType
    image_group_id: str | Unset = UNSET
    material_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        delete_type = self.delete_type.value

        image_group_id = self.image_group_id

        material_id = self.material_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "delete_type": delete_type,
        })
        if image_group_id is not UNSET:
            field_dict["image_group_id"] = image_group_id
        if material_id is not UNSET:
            field_dict["material_id"] = material_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delete_type = DeleteShopMaterialRequestDeleteType(d.pop("delete_type"))




        image_group_id = d.pop("image_group_id", UNSET)

        material_id = d.pop("material_id", UNSET)

        delete_shop_material_request = cls(
            delete_type=delete_type,
            image_group_id=image_group_id,
            material_id=material_id,
        )


        delete_shop_material_request.additional_properties = d
        return delete_shop_material_request

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
