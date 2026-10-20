from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_open_collaboration_creator_content_details_response_data_creator_content_detail import GetOpenCollaborationCreatorContentDetailsResponseDataCreatorContentDetail
  from ..models.get_open_collaboration_creator_content_details_response_data_product import GetOpenCollaborationCreatorContentDetailsResponseDataProduct





T = TypeVar("T", bound="GetOpenCollaborationCreatorContentDetailsResponseData")



@_attrs_define
class GetOpenCollaborationCreatorContentDetailsResponseData:
    """ 
        Attributes:
            next_page_token (str | Unset): Pagination token for the next page. Pass this value as `page_token` in the next
                request. An empty token means there are no more results.
            total_count (int | Unset): Total count of creators that satisfy all the input search conditions.
            creator_content_details (list[GetOpenCollaborationCreatorContentDetailsResponseDataCreatorContentDetail] |
                Unset): Creator profiles, content counts, and promotion details for the specified product.
            product (GetOpenCollaborationCreatorContentDetailsResponseDataProduct | Unset):
     """

    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    creator_content_details: list[GetOpenCollaborationCreatorContentDetailsResponseDataCreatorContentDetail] | Unset = UNSET
    product: GetOpenCollaborationCreatorContentDetailsResponseDataProduct | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_open_collaboration_creator_content_details_response_data_creator_content_detail import GetOpenCollaborationCreatorContentDetailsResponseDataCreatorContentDetail # noqa: PLC0415
        from ..models.get_open_collaboration_creator_content_details_response_data_product import GetOpenCollaborationCreatorContentDetailsResponseDataProduct # noqa: PLC0415
        next_page_token = self.next_page_token

        total_count = self.total_count

        creator_content_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creator_content_details, Unset):
            creator_content_details = []
            for creator_content_details_item_data in self.creator_content_details:
                creator_content_details_item = creator_content_details_item_data.to_dict()
                creator_content_details.append(creator_content_details_item)



        product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if creator_content_details is not UNSET:
            field_dict["creator_content_details"] = creator_content_details
        if product is not UNSET:
            field_dict["product"] = product

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_open_collaboration_creator_content_details_response_data_creator_content_detail import GetOpenCollaborationCreatorContentDetailsResponseDataCreatorContentDetail # noqa: PLC0415
        from ..models.get_open_collaboration_creator_content_details_response_data_product import GetOpenCollaborationCreatorContentDetailsResponseDataProduct # noqa: PLC0415
        d = dict(src_dict)
        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        _creator_content_details = d.pop("creator_content_details", UNSET)
        creator_content_details: list[GetOpenCollaborationCreatorContentDetailsResponseDataCreatorContentDetail] | Unset = UNSET
        if _creator_content_details is not UNSET:
            creator_content_details = []
            for creator_content_details_item_data in _creator_content_details:
                creator_content_details_item = GetOpenCollaborationCreatorContentDetailsResponseDataCreatorContentDetail.from_dict(creator_content_details_item_data)



                creator_content_details.append(creator_content_details_item)


        _product = d.pop("product", UNSET)
        product: GetOpenCollaborationCreatorContentDetailsResponseDataProduct | Unset
        if isinstance(_product,  Unset):
            product = UNSET
        else:
            product = GetOpenCollaborationCreatorContentDetailsResponseDataProduct.from_dict(_product)




        get_open_collaboration_creator_content_details_response_data = cls(
            next_page_token=next_page_token,
            total_count=total_count,
            creator_content_details=creator_content_details,
            product=product,
        )


        get_open_collaboration_creator_content_details_response_data.additional_properties = d
        return get_open_collaboration_creator_content_details_response_data

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
