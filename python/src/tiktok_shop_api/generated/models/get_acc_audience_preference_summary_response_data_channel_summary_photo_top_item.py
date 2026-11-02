from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.get_acc_audience_preference_summary_response_data_channel_summary_photo_top_item_post_image import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryPhotoTopItemPostImage
  from ..models.linked_product import LinkedProduct
  from ..models.stat import Stat





T = TypeVar("T", bound="GetACCAudiencePreferenceSummaryResponseDataChannelSummaryPhotoTopItem")



@_attrs_define
class GetACCAudiencePreferenceSummaryResponseDataChannelSummaryPhotoTopItem:
    """ 
        Attributes:
            image_urls (list[str] | Unset): URLs of images in the photo post. The cover image URL can be returned when no
                other image URLs are available.
            linked_products (list[LinkedProduct] | Unset): Products linked to the photo post, when provided.
            photo_id (str | Unset): ID of the photo post.
            photo_title (str | Unset): Title of the photo post.
            post_images (list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryPhotoTopItemPostImage] | Unset):
                Image metadata for the images in the photo post.
            publish_time (datetime.date | Unset): Publication date of the photo post, in YYYY-MM-DD format (UTC).
            seller_own_avatar_url (str | Unset): URL of the content author's avatar.
            seller_own_id (str | Unset): ID of the content author.
            seller_own_name (str | Unset): Display name of the content author.
            stats (Stat | Unset):
     """

    image_urls: list[str] | Unset = UNSET
    linked_products: list[LinkedProduct] | Unset = UNSET
    photo_id: str | Unset = UNSET
    photo_title: str | Unset = UNSET
    post_images: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryPhotoTopItemPostImage] | Unset = UNSET
    publish_time: datetime.date | Unset = UNSET
    seller_own_avatar_url: str | Unset = UNSET
    seller_own_id: str | Unset = UNSET
    seller_own_name: str | Unset = UNSET
    stats: Stat | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary_photo_top_item_post_image import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryPhotoTopItemPostImage # noqa: PLC0415
        from ..models.linked_product import LinkedProduct # noqa: PLC0415
        from ..models.stat import Stat # noqa: PLC0415
        image_urls: list[str] | Unset = UNSET
        if not isinstance(self.image_urls, Unset):
            image_urls = self.image_urls



        linked_products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_products, Unset):
            linked_products = []
            for linked_products_item_data in self.linked_products:
                linked_products_item = linked_products_item_data.to_dict()
                linked_products.append(linked_products_item)



        photo_id = self.photo_id

        photo_title = self.photo_title

        post_images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.post_images, Unset):
            post_images = []
            for post_images_item_data in self.post_images:
                post_images_item = post_images_item_data.to_dict()
                post_images.append(post_images_item)



        publish_time: str | Unset = UNSET
        if not isinstance(self.publish_time, Unset):
            publish_time = self.publish_time.isoformat()

        seller_own_avatar_url = self.seller_own_avatar_url

        seller_own_id = self.seller_own_id

        seller_own_name = self.seller_own_name

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if image_urls is not UNSET:
            field_dict["image_urls"] = image_urls
        if linked_products is not UNSET:
            field_dict["linked_products"] = linked_products
        if photo_id is not UNSET:
            field_dict["photo_id"] = photo_id
        if photo_title is not UNSET:
            field_dict["photo_title"] = photo_title
        if post_images is not UNSET:
            field_dict["post_images"] = post_images
        if publish_time is not UNSET:
            field_dict["publish_time"] = publish_time
        if seller_own_avatar_url is not UNSET:
            field_dict["seller_own_avatar_url"] = seller_own_avatar_url
        if seller_own_id is not UNSET:
            field_dict["seller_own_id"] = seller_own_id
        if seller_own_name is not UNSET:
            field_dict["seller_own_name"] = seller_own_name
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary_photo_top_item_post_image import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryPhotoTopItemPostImage # noqa: PLC0415
        from ..models.linked_product import LinkedProduct # noqa: PLC0415
        from ..models.stat import Stat # noqa: PLC0415
        d = dict(src_dict)
        image_urls = cast(list[str], d.pop("image_urls", UNSET))


        _linked_products = d.pop("linked_products", UNSET)
        linked_products: list[LinkedProduct] | Unset = UNSET
        if _linked_products is not UNSET:
            linked_products = []
            for linked_products_item_data in _linked_products:
                linked_products_item = LinkedProduct.from_dict(linked_products_item_data)



                linked_products.append(linked_products_item)


        photo_id = d.pop("photo_id", UNSET)

        photo_title = d.pop("photo_title", UNSET)

        _post_images = d.pop("post_images", UNSET)
        post_images: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryPhotoTopItemPostImage] | Unset = UNSET
        if _post_images is not UNSET:
            post_images = []
            for post_images_item_data in _post_images:
                post_images_item = GetACCAudiencePreferenceSummaryResponseDataChannelSummaryPhotoTopItemPostImage.from_dict(post_images_item_data)



                post_images.append(post_images_item)


        _publish_time = d.pop("publish_time", UNSET)
        publish_time: datetime.date | Unset
        if isinstance(_publish_time,  Unset):
            publish_time = UNSET
        else:
            publish_time = datetime.date.fromisoformat(_publish_time)




        seller_own_avatar_url = d.pop("seller_own_avatar_url", UNSET)

        seller_own_id = d.pop("seller_own_id", UNSET)

        seller_own_name = d.pop("seller_own_name", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: Stat | Unset
        if isinstance(_stats,  Unset):
            stats = UNSET
        else:
            stats = Stat.from_dict(_stats)




        get_acc_audience_preference_summary_response_data_channel_summary_photo_top_item = cls(
            image_urls=image_urls,
            linked_products=linked_products,
            photo_id=photo_id,
            photo_title=photo_title,
            post_images=post_images,
            publish_time=publish_time,
            seller_own_avatar_url=seller_own_avatar_url,
            seller_own_id=seller_own_id,
            seller_own_name=seller_own_name,
            stats=stats,
        )


        get_acc_audience_preference_summary_response_data_channel_summary_photo_top_item.additional_properties = d
        return get_acc_audience_preference_summary_response_data_channel_summary_photo_top_item

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
