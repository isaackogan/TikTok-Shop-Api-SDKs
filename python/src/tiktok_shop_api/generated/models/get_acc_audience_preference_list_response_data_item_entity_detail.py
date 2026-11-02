from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="GetACCAudiencePreferenceListResponseDataItemEntityDetail")



@_attrs_define
class GetACCAudiencePreferenceListResponseDataItemEntityDetail:
    """ 
        Attributes:
            creator_id (str | Unset): ID of the creator of the video or photo post, when available. Applies to `VIDEO` and
                `PHOTO`.
            creator_name (str | Unset): Display name of the creator of the video or photo post, when available. Applies to
                `VIDEO` and `PHOTO`.
            l2_category_id (str | Unset): Second-level category ID of the ranked product. Applies to `PRODUCT`.
            l3_category_id (str | Unset): Third-level category identifier associated with this ranking entry. Applies to
                `PRODUCT`. A value of `-1` denotes the default third-level category selection.
            live_start_time (datetime.date | Unset): UTC calendar date on which the live stream started, in `YYYY-MM-DD`
                format, when available. Applies to `LIVE`.
            post_time (datetime.date | Unset): UTC publication date of the video or photo post, in `YYYY-MM-DD` format, when
                available. Applies to `VIDEO` and `PHOTO`.
            product_url (str | Unset): Link to the ranked product, when available. Applies to `PRODUCT`.
            replay_url (str | Unset): Link to the live stream replay, when available. Applies to `LIVE`.
     """

    creator_id: str | Unset = UNSET
    creator_name: str | Unset = UNSET
    l2_category_id: str | Unset = UNSET
    l3_category_id: str | Unset = UNSET
    live_start_time: datetime.date | Unset = UNSET
    post_time: datetime.date | Unset = UNSET
    product_url: str | Unset = UNSET
    replay_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        creator_id = self.creator_id

        creator_name = self.creator_name

        l2_category_id = self.l2_category_id

        l3_category_id = self.l3_category_id

        live_start_time: str | Unset = UNSET
        if not isinstance(self.live_start_time, Unset):
            live_start_time = self.live_start_time.isoformat()

        post_time: str | Unset = UNSET
        if not isinstance(self.post_time, Unset):
            post_time = self.post_time.isoformat()

        product_url = self.product_url

        replay_url = self.replay_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if creator_id is not UNSET:
            field_dict["creator_id"] = creator_id
        if creator_name is not UNSET:
            field_dict["creator_name"] = creator_name
        if l2_category_id is not UNSET:
            field_dict["l2_category_id"] = l2_category_id
        if l3_category_id is not UNSET:
            field_dict["l3_category_id"] = l3_category_id
        if live_start_time is not UNSET:
            field_dict["live_start_time"] = live_start_time
        if post_time is not UNSET:
            field_dict["post_time"] = post_time
        if product_url is not UNSET:
            field_dict["product_url"] = product_url
        if replay_url is not UNSET:
            field_dict["replay_url"] = replay_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator_id = d.pop("creator_id", UNSET)

        creator_name = d.pop("creator_name", UNSET)

        l2_category_id = d.pop("l2_category_id", UNSET)

        l3_category_id = d.pop("l3_category_id", UNSET)

        _live_start_time = d.pop("live_start_time", UNSET)
        live_start_time: datetime.date | Unset
        if isinstance(_live_start_time,  Unset):
            live_start_time = UNSET
        else:
            live_start_time = datetime.date.fromisoformat(_live_start_time)




        _post_time = d.pop("post_time", UNSET)
        post_time: datetime.date | Unset
        if isinstance(_post_time,  Unset):
            post_time = UNSET
        else:
            post_time = datetime.date.fromisoformat(_post_time)




        product_url = d.pop("product_url", UNSET)

        replay_url = d.pop("replay_url", UNSET)

        get_acc_audience_preference_list_response_data_item_entity_detail = cls(
            creator_id=creator_id,
            creator_name=creator_name,
            l2_category_id=l2_category_id,
            l3_category_id=l3_category_id,
            live_start_time=live_start_time,
            post_time=post_time,
            product_url=product_url,
            replay_url=replay_url,
        )


        get_acc_audience_preference_list_response_data_item_entity_detail.additional_properties = d
        return get_acc_audience_preference_list_response_data_item_entity_detail

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
