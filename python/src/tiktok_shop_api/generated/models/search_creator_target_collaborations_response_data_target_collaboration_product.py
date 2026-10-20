from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_creator_target_collaborations_response_data_target_collaboration_product_commission import SearchCreatorTargetCollaborationsResponseDataTargetCollaborationProductCommission





T = TypeVar("T", bound="SearchCreatorTargetCollaborationsResponseDataTargetCollaborationProduct")



@_attrs_define
class SearchCreatorTargetCollaborationsResponseDataTargetCollaborationProduct:
    """ 
        Attributes:
            id (str | Unset): The product identifier.
            title (str | Unset): The product name.
            main_image_url (str | Unset): The product image URL in the TikTok Shop.
            commission (SearchCreatorTargetCollaborationsResponseDataTargetCollaborationProductCommission | Unset):
     """

    id: str | Unset = UNSET
    title: str | Unset = UNSET
    main_image_url: str | Unset = UNSET
    commission: SearchCreatorTargetCollaborationsResponseDataTargetCollaborationProductCommission | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_creator_target_collaborations_response_data_target_collaboration_product_commission import SearchCreatorTargetCollaborationsResponseDataTargetCollaborationProductCommission # noqa: PLC0415
        id = self.id

        title = self.title

        main_image_url = self.main_image_url

        commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commission, Unset):
            commission = self.commission.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if main_image_url is not UNSET:
            field_dict["main_image_url"] = main_image_url
        if commission is not UNSET:
            field_dict["commission"] = commission

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_creator_target_collaborations_response_data_target_collaboration_product_commission import SearchCreatorTargetCollaborationsResponseDataTargetCollaborationProductCommission # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        main_image_url = d.pop("main_image_url", UNSET)

        _commission = d.pop("commission", UNSET)
        commission: SearchCreatorTargetCollaborationsResponseDataTargetCollaborationProductCommission | Unset
        if isinstance(_commission,  Unset):
            commission = UNSET
        else:
            commission = SearchCreatorTargetCollaborationsResponseDataTargetCollaborationProductCommission.from_dict(_commission)




        search_creator_target_collaborations_response_data_target_collaboration_product = cls(
            id=id,
            title=title,
            main_image_url=main_image_url,
            commission=commission,
        )


        search_creator_target_collaborations_response_data_target_collaboration_product.additional_properties = d
        return search_creator_target_collaborations_response_data_target_collaboration_product

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
