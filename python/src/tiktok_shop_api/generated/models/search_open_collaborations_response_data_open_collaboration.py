from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_open_collaborations_response_data_open_collaboration_current_commission import SearchOpenCollaborationsResponseDataOpenCollaborationCurrentCommission
  from ..models.search_open_collaborations_response_data_open_collaboration_product import SearchOpenCollaborationsResponseDataOpenCollaborationProduct





T = TypeVar("T", bound="SearchOpenCollaborationsResponseDataOpenCollaboration")



@_attrs_define
class SearchOpenCollaborationsResponseDataOpenCollaboration:
    """ 
        Attributes:
            id (str | Unset): The open collaboration id
            status (str | Unset): Status of open collaboration.
                Field values:
                - NORMAL：NORMAL means the current open collaboration status is normal and in effect.
                - TERMINATING: TERMINATING means that the merchant has removed open collaboration and the open collaboration
                will expire soon. The expiration time can be found at the end_time of current_commission.
                The open collaborations which were removed and expired will not be returned in the response.
            current_commission (SearchOpenCollaborationsResponseDataOpenCollaborationCurrentCommission | Unset):
            showcase_creator_count (int | Unset): This field indicates the number of creators who added the product to the
                showcase from open collaboration.
            content_creator_count (int | Unset): This field indicates the number of creators who posted the LIve or Video
                from open collaboration.
            product (SearchOpenCollaborationsResponseDataOpenCollaborationProduct | Unset):
     """

    id: str | Unset = UNSET
    status: str | Unset = UNSET
    current_commission: SearchOpenCollaborationsResponseDataOpenCollaborationCurrentCommission | Unset = UNSET
    showcase_creator_count: int | Unset = UNSET
    content_creator_count: int | Unset = UNSET
    product: SearchOpenCollaborationsResponseDataOpenCollaborationProduct | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_open_collaborations_response_data_open_collaboration_current_commission import SearchOpenCollaborationsResponseDataOpenCollaborationCurrentCommission # noqa: PLC0415
        from ..models.search_open_collaborations_response_data_open_collaboration_product import SearchOpenCollaborationsResponseDataOpenCollaborationProduct # noqa: PLC0415
        id = self.id

        status = self.status

        current_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current_commission, Unset):
            current_commission = self.current_commission.to_dict()

        showcase_creator_count = self.showcase_creator_count

        content_creator_count = self.content_creator_count

        product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if current_commission is not UNSET:
            field_dict["current_commission"] = current_commission
        if showcase_creator_count is not UNSET:
            field_dict["showcase_creator_count"] = showcase_creator_count
        if content_creator_count is not UNSET:
            field_dict["content_creator_count"] = content_creator_count
        if product is not UNSET:
            field_dict["product"] = product

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_open_collaborations_response_data_open_collaboration_current_commission import SearchOpenCollaborationsResponseDataOpenCollaborationCurrentCommission # noqa: PLC0415
        from ..models.search_open_collaborations_response_data_open_collaboration_product import SearchOpenCollaborationsResponseDataOpenCollaborationProduct # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        _current_commission = d.pop("current_commission", UNSET)
        current_commission: SearchOpenCollaborationsResponseDataOpenCollaborationCurrentCommission | Unset
        if isinstance(_current_commission,  Unset):
            current_commission = UNSET
        else:
            current_commission = SearchOpenCollaborationsResponseDataOpenCollaborationCurrentCommission.from_dict(_current_commission)




        showcase_creator_count = d.pop("showcase_creator_count", UNSET)

        content_creator_count = d.pop("content_creator_count", UNSET)

        _product = d.pop("product", UNSET)
        product: SearchOpenCollaborationsResponseDataOpenCollaborationProduct | Unset
        if isinstance(_product,  Unset):
            product = UNSET
        else:
            product = SearchOpenCollaborationsResponseDataOpenCollaborationProduct.from_dict(_product)




        search_open_collaborations_response_data_open_collaboration = cls(
            id=id,
            status=status,
            current_commission=current_commission,
            showcase_creator_count=showcase_creator_count,
            content_creator_count=content_creator_count,
            product=product,
        )


        search_open_collaborations_response_data_open_collaboration.additional_properties = d
        return search_open_collaborations_response_data_open_collaboration

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
