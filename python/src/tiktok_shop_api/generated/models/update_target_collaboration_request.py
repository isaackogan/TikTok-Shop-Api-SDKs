from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.free_sample_rule import FreeSampleRule
  from ..models.update_target_collaboration_request_product import UpdateTargetCollaborationRequestProduct
  from ..models.update_target_collaboration_request_seller_contact_info import UpdateTargetCollaborationRequestSellerContactInfo





T = TypeVar("T", bound="UpdateTargetCollaborationRequest")



@_attrs_define
class UpdateTargetCollaborationRequest:
    """ 
        Attributes:
            name (str): The name of the target collaboration.
            end_time (str): The end time of the target collaboration, as a Unix timestamp in seconds.
            products (list[UpdateTargetCollaborationRequestProduct]): The information about the products provided by the
                seller for target collaboration with creators in the target collaboration.
                The maximum number of products is 100.
                When a product is deleted from the product list, if the deleted product has been added to the showcase by the
                creator, it will take effect at 0:00 the next day, otherwise it will take effect immediately.
            creator_user_open_ids (list[str]): The list of Creators' TikTok User Open IDs invited in the target
                collaboration. The maximum number of creators is 50. [More
                details](https://partner.tiktokshop.com/docv2/page/3obfokj6)
            seller_contact_info (UpdateTargetCollaborationRequestSellerContactInfo):
            free_sample_rule (FreeSampleRule):
     """

    name: str
    end_time: str
    products: list[UpdateTargetCollaborationRequestProduct]
    creator_user_open_ids: list[str]
    seller_contact_info: UpdateTargetCollaborationRequestSellerContactInfo
    free_sample_rule: FreeSampleRule
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.free_sample_rule import FreeSampleRule # noqa: PLC0415
        from ..models.update_target_collaboration_request_product import UpdateTargetCollaborationRequestProduct # noqa: PLC0415
        from ..models.update_target_collaboration_request_seller_contact_info import UpdateTargetCollaborationRequestSellerContactInfo # noqa: PLC0415
        name = self.name

        end_time = self.end_time

        products = []
        for products_item_data in self.products:
            products_item = products_item_data.to_dict()
            products.append(products_item)



        creator_user_open_ids = self.creator_user_open_ids



        seller_contact_info = self.seller_contact_info.to_dict()

        free_sample_rule = self.free_sample_rule.to_dict()


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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.free_sample_rule import FreeSampleRule # noqa: PLC0415
        from ..models.update_target_collaboration_request_product import UpdateTargetCollaborationRequestProduct # noqa: PLC0415
        from ..models.update_target_collaboration_request_seller_contact_info import UpdateTargetCollaborationRequestSellerContactInfo # noqa: PLC0415
        d = dict(src_dict)
        name = d.pop("name")

        end_time = d.pop("end_time")

        products = []
        _products = d.pop("products")
        for products_item_data in (_products):
            products_item = UpdateTargetCollaborationRequestProduct.from_dict(products_item_data)



            products.append(products_item)


        creator_user_open_ids = cast(list[str], d.pop("creator_user_open_ids"))


        seller_contact_info = UpdateTargetCollaborationRequestSellerContactInfo.from_dict(d.pop("seller_contact_info"))




        free_sample_rule = FreeSampleRule.from_dict(d.pop("free_sample_rule"))




        update_target_collaboration_request = cls(
            name=name,
            end_time=end_time,
            products=products,
            creator_user_open_ids=creator_user_open_ids,
            seller_contact_info=seller_contact_info,
            free_sample_rule=free_sample_rule,
        )


        update_target_collaboration_request.additional_properties = d
        return update_target_collaboration_request

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
