from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_creator_target_collaborations_response_data_target_collaboration_product import SearchCreatorTargetCollaborationsResponseDataTargetCollaborationProduct





T = TypeVar("T", bound="SearchCreatorTargetCollaborationsResponseDataTargetCollaboration")



@_attrs_define
class SearchCreatorTargetCollaborationsResponseDataTargetCollaboration:
    """ 
        Attributes:
            id (str | Unset): The target collaboration identifier.
            name (str | Unset): The target collaboration name.
            status (str | Unset): The target collaboration state. This is an enumerated type with values:
                - LIVE
                - EXPIRED
                - DELETED
                - ENDED
            products (list[SearchCreatorTargetCollaborationsResponseDataTargetCollaborationProduct] | Unset): A list of
                products associated with the target collaboration.
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    status: str | Unset = UNSET
    products: list[SearchCreatorTargetCollaborationsResponseDataTargetCollaborationProduct] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_creator_target_collaborations_response_data_target_collaboration_product import SearchCreatorTargetCollaborationsResponseDataTargetCollaborationProduct # noqa: PLC0415
        id = self.id

        name = self.name

        status = self.status

        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if products is not UNSET:
            field_dict["products"] = products

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_creator_target_collaborations_response_data_target_collaboration_product import SearchCreatorTargetCollaborationsResponseDataTargetCollaborationProduct # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        _products = d.pop("products", UNSET)
        products: list[SearchCreatorTargetCollaborationsResponseDataTargetCollaborationProduct] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = SearchCreatorTargetCollaborationsResponseDataTargetCollaborationProduct.from_dict(products_item_data)



                products.append(products_item)


        search_creator_target_collaborations_response_data_target_collaboration = cls(
            id=id,
            name=name,
            status=status,
            products=products,
        )


        search_creator_target_collaborations_response_data_target_collaboration.additional_properties = d
        return search_creator_target_collaborations_response_data_target_collaboration

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
