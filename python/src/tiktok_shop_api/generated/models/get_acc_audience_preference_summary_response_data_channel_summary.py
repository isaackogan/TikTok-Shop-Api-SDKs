from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_acc_audience_preference_summary_response_data_channel_summary_live_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryLiveTopItem
  from ..models.get_acc_audience_preference_summary_response_data_channel_summary_live_type_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryLiveTypeTopItem
  from ..models.get_acc_audience_preference_summary_response_data_channel_summary_photo_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryPhotoTopItem
  from ..models.get_acc_audience_preference_summary_response_data_channel_summary_product_category_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryProductCategoryTopItem
  from ..models.get_acc_audience_preference_summary_response_data_channel_summary_product_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryProductTopItem
  from ..models.get_acc_audience_preference_summary_response_data_channel_summary_seller_own_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummarySellerOwnTopItem
  from ..models.get_acc_audience_preference_summary_response_data_channel_summary_video_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryVideoTopItem





T = TypeVar("T", bound="GetACCAudiencePreferenceSummaryResponseDataChannelSummary")



@_attrs_define
class GetACCAudiencePreferenceSummaryResponseDataChannelSummary:
    """ 
        Attributes:
            channel (str | Unset): Channel represented by this summary: PRODUCT, LIVE, VIDEO, or PHOTO.
            live_top_items (list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryLiveTopItem] | Unset): Up to 3
                livestreams with the highest GMV for the selected audience, scope, and reporting window, in descending GMV
                order. Populated in the LIVE summary when data is available.
            live_type_top_items (list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryLiveTypeTopItem] | Unset): Up
                to 3 livestream types with the highest GMV for the selected audience, scope, and reporting window, in descending
                GMV order. Populated in the LIVE summary when data is available.
            photo_top_items (list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryPhotoTopItem] | Unset): Up to 3
                photo posts with the highest GMV for the selected audience, scope, and reporting window, in descending GMV
                order. Populated in the PHOTO summary when data is available.
            product_category_top_items
                (list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryProductCategoryTopItem] | Unset): Up to 3 level-2
                product categories with the highest GMV, in descending GMV order, in the PRODUCT summary. Each category includes
                its available level-3 children; the 3-category limit applies to level-2 entries.
            product_top_items (list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryProductTopItem] | Unset): Up to
                3 products with the highest GMV for the selected audience, scope, and reporting window, in descending GMV order.
                Populated in the PRODUCT summary when data is available.
            seller_own_top_items (list[GetACCAudiencePreferenceSummaryResponseDataChannelSummarySellerOwnTopItem] | Unset):
                Content-author preference summaries for the channel. This list can be empty.
            video_top_items (list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryVideoTopItem] | Unset): Up to 3
                videos with the highest GMV for the selected audience, scope, and reporting window, in descending GMV order.
                Populated in the VIDEO summary when data is available.
     """

    channel: str | Unset = UNSET
    live_top_items: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryLiveTopItem] | Unset = UNSET
    live_type_top_items: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryLiveTypeTopItem] | Unset = UNSET
    photo_top_items: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryPhotoTopItem] | Unset = UNSET
    product_category_top_items: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryProductCategoryTopItem] | Unset = UNSET
    product_top_items: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryProductTopItem] | Unset = UNSET
    seller_own_top_items: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummarySellerOwnTopItem] | Unset = UNSET
    video_top_items: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryVideoTopItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary_live_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryLiveTopItem # noqa: PLC0415
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary_live_type_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryLiveTypeTopItem # noqa: PLC0415
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary_photo_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryPhotoTopItem # noqa: PLC0415
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary_product_category_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryProductCategoryTopItem # noqa: PLC0415
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary_product_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryProductTopItem # noqa: PLC0415
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary_seller_own_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummarySellerOwnTopItem # noqa: PLC0415
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary_video_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryVideoTopItem # noqa: PLC0415
        channel = self.channel

        live_top_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.live_top_items, Unset):
            live_top_items = []
            for live_top_items_item_data in self.live_top_items:
                live_top_items_item = live_top_items_item_data.to_dict()
                live_top_items.append(live_top_items_item)



        live_type_top_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.live_type_top_items, Unset):
            live_type_top_items = []
            for live_type_top_items_item_data in self.live_type_top_items:
                live_type_top_items_item = live_type_top_items_item_data.to_dict()
                live_type_top_items.append(live_type_top_items_item)



        photo_top_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.photo_top_items, Unset):
            photo_top_items = []
            for photo_top_items_item_data in self.photo_top_items:
                photo_top_items_item = photo_top_items_item_data.to_dict()
                photo_top_items.append(photo_top_items_item)



        product_category_top_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_category_top_items, Unset):
            product_category_top_items = []
            for product_category_top_items_item_data in self.product_category_top_items:
                product_category_top_items_item = product_category_top_items_item_data.to_dict()
                product_category_top_items.append(product_category_top_items_item)



        product_top_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_top_items, Unset):
            product_top_items = []
            for product_top_items_item_data in self.product_top_items:
                product_top_items_item = product_top_items_item_data.to_dict()
                product_top_items.append(product_top_items_item)



        seller_own_top_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.seller_own_top_items, Unset):
            seller_own_top_items = []
            for seller_own_top_items_item_data in self.seller_own_top_items:
                seller_own_top_items_item = seller_own_top_items_item_data.to_dict()
                seller_own_top_items.append(seller_own_top_items_item)



        video_top_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.video_top_items, Unset):
            video_top_items = []
            for video_top_items_item_data in self.video_top_items:
                video_top_items_item = video_top_items_item_data.to_dict()
                video_top_items.append(video_top_items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if channel is not UNSET:
            field_dict["channel"] = channel
        if live_top_items is not UNSET:
            field_dict["live_top_items"] = live_top_items
        if live_type_top_items is not UNSET:
            field_dict["live_type_top_items"] = live_type_top_items
        if photo_top_items is not UNSET:
            field_dict["photo_top_items"] = photo_top_items
        if product_category_top_items is not UNSET:
            field_dict["product_category_top_items"] = product_category_top_items
        if product_top_items is not UNSET:
            field_dict["product_top_items"] = product_top_items
        if seller_own_top_items is not UNSET:
            field_dict["seller_own_top_items"] = seller_own_top_items
        if video_top_items is not UNSET:
            field_dict["video_top_items"] = video_top_items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary_live_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryLiveTopItem # noqa: PLC0415
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary_live_type_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryLiveTypeTopItem # noqa: PLC0415
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary_photo_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryPhotoTopItem # noqa: PLC0415
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary_product_category_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryProductCategoryTopItem # noqa: PLC0415
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary_product_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryProductTopItem # noqa: PLC0415
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary_seller_own_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummarySellerOwnTopItem # noqa: PLC0415
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary_video_top_item import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryVideoTopItem # noqa: PLC0415
        d = dict(src_dict)
        channel = d.pop("channel", UNSET)

        _live_top_items = d.pop("live_top_items", UNSET)
        live_top_items: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryLiveTopItem] | Unset = UNSET
        if _live_top_items is not UNSET:
            live_top_items = []
            for live_top_items_item_data in _live_top_items:
                live_top_items_item = GetACCAudiencePreferenceSummaryResponseDataChannelSummaryLiveTopItem.from_dict(live_top_items_item_data)



                live_top_items.append(live_top_items_item)


        _live_type_top_items = d.pop("live_type_top_items", UNSET)
        live_type_top_items: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryLiveTypeTopItem] | Unset = UNSET
        if _live_type_top_items is not UNSET:
            live_type_top_items = []
            for live_type_top_items_item_data in _live_type_top_items:
                live_type_top_items_item = GetACCAudiencePreferenceSummaryResponseDataChannelSummaryLiveTypeTopItem.from_dict(live_type_top_items_item_data)



                live_type_top_items.append(live_type_top_items_item)


        _photo_top_items = d.pop("photo_top_items", UNSET)
        photo_top_items: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryPhotoTopItem] | Unset = UNSET
        if _photo_top_items is not UNSET:
            photo_top_items = []
            for photo_top_items_item_data in _photo_top_items:
                photo_top_items_item = GetACCAudiencePreferenceSummaryResponseDataChannelSummaryPhotoTopItem.from_dict(photo_top_items_item_data)



                photo_top_items.append(photo_top_items_item)


        _product_category_top_items = d.pop("product_category_top_items", UNSET)
        product_category_top_items: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryProductCategoryTopItem] | Unset = UNSET
        if _product_category_top_items is not UNSET:
            product_category_top_items = []
            for product_category_top_items_item_data in _product_category_top_items:
                product_category_top_items_item = GetACCAudiencePreferenceSummaryResponseDataChannelSummaryProductCategoryTopItem.from_dict(product_category_top_items_item_data)



                product_category_top_items.append(product_category_top_items_item)


        _product_top_items = d.pop("product_top_items", UNSET)
        product_top_items: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryProductTopItem] | Unset = UNSET
        if _product_top_items is not UNSET:
            product_top_items = []
            for product_top_items_item_data in _product_top_items:
                product_top_items_item = GetACCAudiencePreferenceSummaryResponseDataChannelSummaryProductTopItem.from_dict(product_top_items_item_data)



                product_top_items.append(product_top_items_item)


        _seller_own_top_items = d.pop("seller_own_top_items", UNSET)
        seller_own_top_items: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummarySellerOwnTopItem] | Unset = UNSET
        if _seller_own_top_items is not UNSET:
            seller_own_top_items = []
            for seller_own_top_items_item_data in _seller_own_top_items:
                seller_own_top_items_item = GetACCAudiencePreferenceSummaryResponseDataChannelSummarySellerOwnTopItem.from_dict(seller_own_top_items_item_data)



                seller_own_top_items.append(seller_own_top_items_item)


        _video_top_items = d.pop("video_top_items", UNSET)
        video_top_items: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryVideoTopItem] | Unset = UNSET
        if _video_top_items is not UNSET:
            video_top_items = []
            for video_top_items_item_data in _video_top_items:
                video_top_items_item = GetACCAudiencePreferenceSummaryResponseDataChannelSummaryVideoTopItem.from_dict(video_top_items_item_data)



                video_top_items.append(video_top_items_item)


        get_acc_audience_preference_summary_response_data_channel_summary = cls(
            channel=channel,
            live_top_items=live_top_items,
            live_type_top_items=live_type_top_items,
            photo_top_items=photo_top_items,
            product_category_top_items=product_category_top_items,
            product_top_items=product_top_items,
            seller_own_top_items=seller_own_top_items,
            video_top_items=video_top_items,
        )


        get_acc_audience_preference_summary_response_data_channel_summary.additional_properties = d
        return get_acc_audience_preference_summary_response_data_channel_summary

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
