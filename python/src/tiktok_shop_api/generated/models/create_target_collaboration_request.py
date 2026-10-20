from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_target_collaboration_request_product import CreateTargetCollaborationRequestProduct
  from ..models.free_sample_rule import FreeSampleRule
  from ..models.seller_contact_info import SellerContactInfo





T = TypeVar("T", bound="CreateTargetCollaborationRequest")



@_attrs_define
class CreateTargetCollaborationRequest:
    """ 
        Attributes:
            name (str): The name of the target collaboration.
            end_time (str): The date at which the target collaboration ends, in Unix epoch time.
            products (list[CreateTargetCollaborationRequestProduct]): A list of metadata and data for the products provided
                by the seller for target collaboration. Maximum length of the list is `100` products.
            creator_user_open_ids (list[str]): Maximum length of the list is `50` user open identifiers. Creator Open ID.
                [More details](https://partner.tiktokshop.com/docv2/page/3obfokj6)
            seller_contact_info (SellerContactInfo):
            free_sample_rule (FreeSampleRule):
            message (str | Unset): The message sent to creators associated with the target collaboration.
            preferred_content_type (str | Unset): preferred creator content type, "LIVE" or "VIDEO"
     """

    name: str
    end_time: str
    products: list[CreateTargetCollaborationRequestProduct]
    creator_user_open_ids: list[str]
    seller_contact_info: SellerContactInfo
    free_sample_rule: FreeSampleRule
    message: str | Unset = UNSET
    preferred_content_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_target_collaboration_request_product import CreateTargetCollaborationRequestProduct # noqa: PLC0415
        from ..models.free_sample_rule import FreeSampleRule # noqa: PLC0415
        from ..models.seller_contact_info import SellerContactInfo # noqa: PLC0415
        name = self.name

        end_time = self.end_time

        products = []
        for products_item_data in self.products:
            products_item = products_item_data.to_dict()
            products.append(products_item)



        creator_user_open_ids = self.creator_user_open_ids



        seller_contact_info = self.seller_contact_info.to_dict()

        free_sample_rule = self.free_sample_rule.to_dict()

        message = self.message

        preferred_content_type = self.preferred_content_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "end_time": end_time,
            "products": products,
            "creator_user_open_ids": creator_user_open_ids,
            "seller_contact_info": seller_contact_info,
            "free_sample_rule": free_sample_rule,
        })
        if message is not UNSET:
            field_dict["message"] = message
        if preferred_content_type is not UNSET:
            field_dict["preferred_content_type"] = preferred_content_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_target_collaboration_request_product import CreateTargetCollaborationRequestProduct # noqa: PLC0415
        from ..models.free_sample_rule import FreeSampleRule # noqa: PLC0415
        from ..models.seller_contact_info import SellerContactInfo # noqa: PLC0415
        d = dict(src_dict)
        name = d.pop("name")

        end_time = d.pop("end_time")

        products = []
        _products = d.pop("products")
        for products_item_data in (_products):
            products_item = CreateTargetCollaborationRequestProduct.from_dict(products_item_data)



            products.append(products_item)


        creator_user_open_ids = cast(list[str], d.pop("creator_user_open_ids"))


        seller_contact_info = SellerContactInfo.from_dict(d.pop("seller_contact_info"))




        free_sample_rule = FreeSampleRule.from_dict(d.pop("free_sample_rule"))




        message = d.pop("message", UNSET)

        preferred_content_type = d.pop("preferred_content_type", UNSET)

        create_target_collaboration_request = cls(
            name=name,
            end_time=end_time,
            products=products,
            creator_user_open_ids=creator_user_open_ids,
            seller_contact_info=seller_contact_info,
            free_sample_rule=free_sample_rule,
            message=message,
            preferred_content_type=preferred_content_type,
        )


        create_target_collaboration_request.additional_properties = d
        return create_target_collaboration_request

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
