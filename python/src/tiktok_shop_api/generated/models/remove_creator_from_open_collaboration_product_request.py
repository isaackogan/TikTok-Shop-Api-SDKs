from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="RemoveCreatorFromOpenCollaborationProductRequest")



@_attrs_define
class RemoveCreatorFromOpenCollaborationProductRequest:
    """ 
        Attributes:
            creator_user_open_id (str): Creator Open ID. [More details](https://partner.tiktokshop.com/docv2/page/3obfokj6)
            product_id (str): The product identifier.
     """

    creator_user_open_id: str
    product_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        creator_user_open_id = self.creator_user_open_id

        product_id = self.product_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "creator_user_open_id": creator_user_open_id,
            "product_id": product_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator_user_open_id = d.pop("creator_user_open_id")

        product_id = d.pop("product_id")

        remove_creator_from_open_collaboration_product_request = cls(
            creator_user_open_id=creator_user_open_id,
            product_id=product_id,
        )


        remove_creator_from_open_collaboration_product_request.additional_properties = d
        return remove_creator_from_open_collaboration_product_request

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
