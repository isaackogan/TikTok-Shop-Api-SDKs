from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GeneratePublisherSharingLinksInBatchResponseDataSharingLink")



@_attrs_define
class GeneratePublisherSharingLinksInBatchResponseDataSharingLink:
    """ 
        Attributes:
            material_id (int | Unset): Material ID.
            sharing_link (str | Unset): This is the product promotion link that agencies can share with collaborated
                publishers. The publishers can post this link at their will.
            deep_link (str | Unset): A product promotion deep link that opens the corresponding TikTok Shop product detail
                page. Agencies can share this link with collaborated creators, and creators can copy/paste it into a web browser
                (or share it to users).
                If a user places an order via this link, the resulting e-commerce order will carry these parameter values for
                tracking.
            one_link (str | Unset): A product promotion one-link that opens the corresponding TikTok Shop product detail
                page. Agencies can share this link with collaborated creators, and creators can copy/paste it into a web browser
                (or share it to users).
                If a user places an order via this link, the resulting e-commerce order will carry these parameter values for
                tracking.
                If the user does not have TikTok installed on their phone, they will be redirected to the app store to install
                TikTok.
     """

    material_id: int | Unset = UNSET
    sharing_link: str | Unset = UNSET
    deep_link: str | Unset = UNSET
    one_link: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        material_id = self.material_id

        sharing_link = self.sharing_link

        deep_link = self.deep_link

        one_link = self.one_link


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if material_id is not UNSET:
            field_dict["material_id"] = material_id
        if sharing_link is not UNSET:
            field_dict["sharing_link"] = sharing_link
        if deep_link is not UNSET:
            field_dict["deep_link"] = deep_link
        if one_link is not UNSET:
            field_dict["one_link"] = one_link

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        material_id = d.pop("material_id", UNSET)

        sharing_link = d.pop("sharing_link", UNSET)

        deep_link = d.pop("deep_link", UNSET)

        one_link = d.pop("one_link", UNSET)

        generate_publisher_sharing_links_in_batch_response_data_sharing_link = cls(
            material_id=material_id,
            sharing_link=sharing_link,
            deep_link=deep_link,
            one_link=one_link,
        )


        generate_publisher_sharing_links_in_batch_response_data_sharing_link.additional_properties = d
        return generate_publisher_sharing_links_in_batch_response_data_sharing_link

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
