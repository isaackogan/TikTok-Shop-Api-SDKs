from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GenerateGeneralSharingLinksResponseDataSharingLink")



@_attrs_define
class GenerateGeneralSharingLinksResponseDataSharingLink:
    """ 
        Attributes:
            material_id (str | Unset): Material ID.
            sharing_link (str | Unset): This is the product promotion link that agencies can share with collaborated
                creators. Creators can copy/paste this link into the web browser.
                After you have the links, add the following request parameters and their corresponding values to the end of the
                link URL. When a user places an order using this link, the resulting e-commerce order will carry these
                parameters as part of its information:
                - event_id: Unique event id for each click
                - publisher_id: The unique publish_id assigned by CJ
                Nice to have
                - publisher_name: From CJ publisher profile.
                - device_type: 1-mobile, 2-desktop.
                - device_id: The clicks from the same device id can be aggregated as UV.
                - referrer_src: The URL of the webpage that a user came from before landing on the current share link.
            deep_link (str | Unset): A product promotion app deep link that opens the corresponding TikTok Shop product
                detail page. It is returned for `PRODUCT` requests that use the TikTok Shop link type and is omitted when
                `link_type` is `TOKO`. Agencies can share this link with collaborated creators, and creators can share it with
                users. Use `one_link` for the HTTPS link that can be opened in a web browser.

                To enable attribution, replace the `o_event_id` placeholder in the returned `deep_link` URL with a developer-
                generated unique ID for each click. Do not URL-encode or URL-decode the returned link. If a user places an order
                through this link, the resulting e-commerce order carries the event ID for tracking.
            one_link (str | Unset): A product promotion one-link that opens the corresponding TikTok Shop product detail
                page. It is returned for `PRODUCT` requests that use the TikTok Shop link type and is omitted when `link_type`
                is `TOKO`. Agencies can share this link with collaborated creators, and creators can copy and paste it into a
                web browser or share it with users.

                To enable attribution, replace the `o_event_id` placeholder in the returned `one_link` URL with a developer-
                generated unique ID for each click. Do not URL-encode or URL-decode the returned link. If a user places an order
                through this link, the resulting e-commerce order carries the event ID for tracking. If the user does not have
                TikTok installed, the link redirects the user to the app store to install TikTok.
     """

    material_id: str | Unset = UNSET
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

        generate_general_sharing_links_response_data_sharing_link = cls(
            material_id=material_id,
            sharing_link=sharing_link,
            deep_link=deep_link,
            one_link=one_link,
        )


        generate_general_sharing_links_response_data_sharing_link.additional_properties = d
        return generate_general_sharing_links_response_data_sharing_link

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
