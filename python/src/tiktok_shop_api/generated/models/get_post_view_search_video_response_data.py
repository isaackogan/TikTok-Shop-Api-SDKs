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
  from ..models.get_post_view_search_video_response_data_comment import GetPostViewSearchVideoResponseDataComment
  from ..models.get_post_view_search_video_response_data_product import GetPostViewSearchVideoResponseDataProduct
  from ..models.get_post_view_search_video_response_data_video import GetPostViewSearchVideoResponseDataVideo





T = TypeVar("T", bound="GetPostViewSearchVideoResponseData")



@_attrs_define
class GetPostViewSearchVideoResponseData:
    """ 
        Attributes:
            video (GetPostViewSearchVideoResponseDataVideo):
            comments (list[GetPostViewSearchVideoResponseDataComment] | Unset): Business policy permits access only to the
                latest 50 comments created through this tool by the video author for one video. Earlier comments are outside the
                API access scope; pagination is not supported. Newest first; unknown timestamps sort last. Self-posted videos
                only; omitted for creator videos. Empty when no matching comments are returned.
            end_date (datetime.date | Unset): Effective inclusive end date.
            keywords (list[str] | Unset): Currently configured keywords; empty when none are configured.
            products (list[GetPostViewSearchVideoResponseDataProduct] | Unset): Currently associated products; empty when
                none are configured.
            start_date (datetime.date | Unset): Effective inclusive start date.
     """

    video: GetPostViewSearchVideoResponseDataVideo
    comments: list[GetPostViewSearchVideoResponseDataComment] | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    keywords: list[str] | Unset = UNSET
    products: list[GetPostViewSearchVideoResponseDataProduct] | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_post_view_search_video_response_data_comment import GetPostViewSearchVideoResponseDataComment # noqa: PLC0415
        from ..models.get_post_view_search_video_response_data_product import GetPostViewSearchVideoResponseDataProduct # noqa: PLC0415
        from ..models.get_post_view_search_video_response_data_video import GetPostViewSearchVideoResponseDataVideo # noqa: PLC0415
        video = self.video.to_dict()

        comments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()
                comments.append(comments_item)



        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        keywords: list[str] | Unset = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords



        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)



        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "video": video,
        })
        if comments is not UNSET:
            field_dict["comments"] = comments
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if products is not UNSET:
            field_dict["products"] = products
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_post_view_search_video_response_data_comment import GetPostViewSearchVideoResponseDataComment # noqa: PLC0415
        from ..models.get_post_view_search_video_response_data_product import GetPostViewSearchVideoResponseDataProduct # noqa: PLC0415
        from ..models.get_post_view_search_video_response_data_video import GetPostViewSearchVideoResponseDataVideo # noqa: PLC0415
        d = dict(src_dict)
        video = GetPostViewSearchVideoResponseDataVideo.from_dict(d.pop("video"))




        _comments = d.pop("comments", UNSET)
        comments: list[GetPostViewSearchVideoResponseDataComment] | Unset = UNSET
        if _comments is not UNSET:
            comments = []
            for comments_item_data in _comments:
                comments_item = GetPostViewSearchVideoResponseDataComment.from_dict(comments_item_data)



                comments.append(comments_item)


        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date,  Unset):
            end_date = UNSET
        else:
            end_date = datetime.date.fromisoformat(_end_date)




        keywords = cast(list[str], d.pop("keywords", UNSET))


        _products = d.pop("products", UNSET)
        products: list[GetPostViewSearchVideoResponseDataProduct] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = GetPostViewSearchVideoResponseDataProduct.from_dict(products_item_data)



                products.append(products_item)


        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)




        get_post_view_search_video_response_data = cls(
            video=video,
            comments=comments,
            end_date=end_date,
            keywords=keywords,
            products=products,
            start_date=start_date,
        )


        get_post_view_search_video_response_data.additional_properties = d
        return get_post_view_search_video_response_data

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
