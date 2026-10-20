from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="CheckTargetCollaborationConflictsRequest")



@_attrs_define
class CheckTargetCollaborationConflictsRequest:
    """ 
        Attributes:
            creator_open_id_list (list[str]): Creator Open ID List. [More
                details](https://partner.tiktokshop.com/docv2/page/3obfokj6)
            product_id_list (list[str]): product id list
     """

    creator_open_id_list: list[str]
    product_id_list: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        creator_open_id_list = self.creator_open_id_list



        product_id_list = self.product_id_list




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "creator_open_id_list": creator_open_id_list,
            "product_id_list": product_id_list,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator_open_id_list = cast(list[str], d.pop("creator_open_id_list"))


        product_id_list = cast(list[str], d.pop("product_id_list"))


        check_target_collaboration_conflicts_request = cls(
            creator_open_id_list=creator_open_id_list,
            product_id_list=product_id_list,
        )


        check_target_collaboration_conflicts_request.additional_properties = d
        return check_target_collaboration_conflicts_request

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
