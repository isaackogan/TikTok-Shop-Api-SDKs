from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.attributed_gmv import AttributedGmv
  from ..models.get_shop_video_performance_list_response_data_video_creator import GetShopVideoPerformanceListResponseDataVideoCreator
  from ..models.get_shop_video_performance_list_response_data_video_product import GetShopVideoPerformanceListResponseDataVideoProduct
  from ..models.gmv import Gmv
  from ..models.gpm import Gpm
  from ..models.indirect_gmv import IndirectGmv





T = TypeVar("T", bound="GetShopVideoPerformanceListResponseDataVideo")



@_attrs_define
class GetShopVideoPerformanceListResponseDataVideo:
    """ 
        Attributes:
            advertisable (bool | Unset): Whether the video can be used for advertising.
            attributed_gmv (AttributedGmv | Unset):
            avg_customers (int | Unset): Daily average customers.
            click_through_rate (str | Unset): Ratio of product clicks to video views in raw decimal format.
            comments (int | Unset): Number of comments received by the video.
            creator (GetShopVideoPerformanceListResponseDataVideoCreator | Unset):
            ctor (str | Unset): Click-to-order rate in raw decimal format.
            duration (int | Unset): Video duration in seconds.
            gmv (Gmv | Unset):
            gpm (Gpm | Unset):
            hash_tags (list[str] | Unset): Hash tags of the video.
            id (str | Unset): The unique identifier of the video in the performance list.
            indirect_gmv (IndirectGmv | Unset):
            items_sold (int | Unset): Number of units sold from the video.
            likes (int | Unset): Number of likes received by the video.
            new_followers (int | Unset): Number of new followers attributed to the video.
            product_clicks (int | Unset): Number of product clicks from the video.
            product_impressions (int | Unset): Number of product impressions from the video.
            products (list[GetShopVideoPerformanceListResponseDataVideoProduct] | Unset): Products promoted in the video.
            review_type (str | Unset): Review classification of the video.
            shares (int | Unset): Number of times the video was shared.
            sku_orders (int | Unset): The total number of paid SKU orders placed directly from the current video.
            title (str | Unset): The title of the video.
            username (str | Unset): The username associated with the video.
            v_to_l_clicks (int | Unset): Number of clicks from the video to a LIVE session.
            v_to_l_rate (str | Unset): Rate of clicks from the video to a LIVE session in raw decimal format.
            video_finish_rate (str | Unset): Video completion rate in raw decimal format.
            video_post_time (str | Unset): Date and time when the video was posted.
            views (int | Unset): Number of video views during the selected time range.
     """

    advertisable: bool | Unset = UNSET
    attributed_gmv: AttributedGmv | Unset = UNSET
    avg_customers: int | Unset = UNSET
    click_through_rate: str | Unset = UNSET
    comments: int | Unset = UNSET
    creator: GetShopVideoPerformanceListResponseDataVideoCreator | Unset = UNSET
    ctor: str | Unset = UNSET
    duration: int | Unset = UNSET
    gmv: Gmv | Unset = UNSET
    gpm: Gpm | Unset = UNSET
    hash_tags: list[str] | Unset = UNSET
    id: str | Unset = UNSET
    indirect_gmv: IndirectGmv | Unset = UNSET
    items_sold: int | Unset = UNSET
    likes: int | Unset = UNSET
    new_followers: int | Unset = UNSET
    product_clicks: int | Unset = UNSET
    product_impressions: int | Unset = UNSET
    products: list[GetShopVideoPerformanceListResponseDataVideoProduct] | Unset = UNSET
    review_type: str | Unset = UNSET
    shares: int | Unset = UNSET
    sku_orders: int | Unset = UNSET
    title: str | Unset = UNSET
    username: str | Unset = UNSET
    v_to_l_clicks: int | Unset = UNSET
    v_to_l_rate: str | Unset = UNSET
    video_finish_rate: str | Unset = UNSET
    video_post_time: str | Unset = UNSET
    views: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.attributed_gmv import AttributedGmv # noqa: PLC0415
        from ..models.get_shop_video_performance_list_response_data_video_creator import GetShopVideoPerformanceListResponseDataVideoCreator # noqa: PLC0415
        from ..models.get_shop_video_performance_list_response_data_video_product import GetShopVideoPerformanceListResponseDataVideoProduct # noqa: PLC0415
        from ..models.gmv import Gmv # noqa: PLC0415
        from ..models.gpm import Gpm # noqa: PLC0415
        from ..models.indirect_gmv import IndirectGmv # noqa: PLC0415
        advertisable = self.advertisable

        attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributed_gmv, Unset):
            attributed_gmv = self.attributed_gmv.to_dict()

        avg_customers = self.avg_customers

        click_through_rate = self.click_through_rate

        comments = self.comments

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        ctor = self.ctor

        duration = self.duration

        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        gpm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gpm, Unset):
            gpm = self.gpm.to_dict()

        hash_tags: list[str] | Unset = UNSET
        if not isinstance(self.hash_tags, Unset):
            hash_tags = self.hash_tags



        id = self.id

        indirect_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.indirect_gmv, Unset):
            indirect_gmv = self.indirect_gmv.to_dict()

        items_sold = self.items_sold

        likes = self.likes

        new_followers = self.new_followers

        product_clicks = self.product_clicks

        product_impressions = self.product_impressions

        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)



        review_type = self.review_type

        shares = self.shares

        sku_orders = self.sku_orders

        title = self.title

        username = self.username

        v_to_l_clicks = self.v_to_l_clicks

        v_to_l_rate = self.v_to_l_rate

        video_finish_rate = self.video_finish_rate

        video_post_time = self.video_post_time

        views = self.views


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if advertisable is not UNSET:
            field_dict["advertisable"] = advertisable
        if attributed_gmv is not UNSET:
            field_dict["attributed_gmv"] = attributed_gmv
        if avg_customers is not UNSET:
            field_dict["avg_customers"] = avg_customers
        if click_through_rate is not UNSET:
            field_dict["click_through_rate"] = click_through_rate
        if comments is not UNSET:
            field_dict["comments"] = comments
        if creator is not UNSET:
            field_dict["creator"] = creator
        if ctor is not UNSET:
            field_dict["ctor"] = ctor
        if duration is not UNSET:
            field_dict["duration"] = duration
        if gmv is not UNSET:
            field_dict["gmv"] = gmv
        if gpm is not UNSET:
            field_dict["gpm"] = gpm
        if hash_tags is not UNSET:
            field_dict["hash_tags"] = hash_tags
        if id is not UNSET:
            field_dict["id"] = id
        if indirect_gmv is not UNSET:
            field_dict["indirect_gmv"] = indirect_gmv
        if items_sold is not UNSET:
            field_dict["items_sold"] = items_sold
        if likes is not UNSET:
            field_dict["likes"] = likes
        if new_followers is not UNSET:
            field_dict["new_followers"] = new_followers
        if product_clicks is not UNSET:
            field_dict["product_clicks"] = product_clicks
        if product_impressions is not UNSET:
            field_dict["product_impressions"] = product_impressions
        if products is not UNSET:
            field_dict["products"] = products
        if review_type is not UNSET:
            field_dict["review_type"] = review_type
        if shares is not UNSET:
            field_dict["shares"] = shares
        if sku_orders is not UNSET:
            field_dict["sku_orders"] = sku_orders
        if title is not UNSET:
            field_dict["title"] = title
        if username is not UNSET:
            field_dict["username"] = username
        if v_to_l_clicks is not UNSET:
            field_dict["v_to_l_clicks"] = v_to_l_clicks
        if v_to_l_rate is not UNSET:
            field_dict["v_to_l_rate"] = v_to_l_rate
        if video_finish_rate is not UNSET:
            field_dict["video_finish_rate"] = video_finish_rate
        if video_post_time is not UNSET:
            field_dict["video_post_time"] = video_post_time
        if views is not UNSET:
            field_dict["views"] = views

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attributed_gmv import AttributedGmv # noqa: PLC0415
        from ..models.get_shop_video_performance_list_response_data_video_creator import GetShopVideoPerformanceListResponseDataVideoCreator # noqa: PLC0415
        from ..models.get_shop_video_performance_list_response_data_video_product import GetShopVideoPerformanceListResponseDataVideoProduct # noqa: PLC0415
        from ..models.gmv import Gmv # noqa: PLC0415
        from ..models.gpm import Gpm # noqa: PLC0415
        from ..models.indirect_gmv import IndirectGmv # noqa: PLC0415
        d = dict(src_dict)
        advertisable = d.pop("advertisable", UNSET)

        _attributed_gmv = d.pop("attributed_gmv", UNSET)
        attributed_gmv: AttributedGmv | Unset
        if isinstance(_attributed_gmv,  Unset):
            attributed_gmv = UNSET
        else:
            attributed_gmv = AttributedGmv.from_dict(_attributed_gmv)




        avg_customers = d.pop("avg_customers", UNSET)

        click_through_rate = d.pop("click_through_rate", UNSET)

        comments = d.pop("comments", UNSET)

        _creator = d.pop("creator", UNSET)
        creator: GetShopVideoPerformanceListResponseDataVideoCreator | Unset
        if isinstance(_creator,  Unset):
            creator = UNSET
        else:
            creator = GetShopVideoPerformanceListResponseDataVideoCreator.from_dict(_creator)




        ctor = d.pop("ctor", UNSET)

        duration = d.pop("duration", UNSET)

        _gmv = d.pop("gmv", UNSET)
        gmv: Gmv | Unset
        if isinstance(_gmv,  Unset):
            gmv = UNSET
        else:
            gmv = Gmv.from_dict(_gmv)




        _gpm = d.pop("gpm", UNSET)
        gpm: Gpm | Unset
        if isinstance(_gpm,  Unset):
            gpm = UNSET
        else:
            gpm = Gpm.from_dict(_gpm)




        hash_tags = cast(list[str], d.pop("hash_tags", UNSET))


        id = d.pop("id", UNSET)

        _indirect_gmv = d.pop("indirect_gmv", UNSET)
        indirect_gmv: IndirectGmv | Unset
        if isinstance(_indirect_gmv,  Unset):
            indirect_gmv = UNSET
        else:
            indirect_gmv = IndirectGmv.from_dict(_indirect_gmv)




        items_sold = d.pop("items_sold", UNSET)

        likes = d.pop("likes", UNSET)

        new_followers = d.pop("new_followers", UNSET)

        product_clicks = d.pop("product_clicks", UNSET)

        product_impressions = d.pop("product_impressions", UNSET)

        _products = d.pop("products", UNSET)
        products: list[GetShopVideoPerformanceListResponseDataVideoProduct] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = GetShopVideoPerformanceListResponseDataVideoProduct.from_dict(products_item_data)



                products.append(products_item)


        review_type = d.pop("review_type", UNSET)

        shares = d.pop("shares", UNSET)

        sku_orders = d.pop("sku_orders", UNSET)

        title = d.pop("title", UNSET)

        username = d.pop("username", UNSET)

        v_to_l_clicks = d.pop("v_to_l_clicks", UNSET)

        v_to_l_rate = d.pop("v_to_l_rate", UNSET)

        video_finish_rate = d.pop("video_finish_rate", UNSET)

        video_post_time = d.pop("video_post_time", UNSET)

        views = d.pop("views", UNSET)

        get_shop_video_performance_list_response_data_video = cls(
            advertisable=advertisable,
            attributed_gmv=attributed_gmv,
            avg_customers=avg_customers,
            click_through_rate=click_through_rate,
            comments=comments,
            creator=creator,
            ctor=ctor,
            duration=duration,
            gmv=gmv,
            gpm=gpm,
            hash_tags=hash_tags,
            id=id,
            indirect_gmv=indirect_gmv,
            items_sold=items_sold,
            likes=likes,
            new_followers=new_followers,
            product_clicks=product_clicks,
            product_impressions=product_impressions,
            products=products,
            review_type=review_type,
            shares=shares,
            sku_orders=sku_orders,
            title=title,
            username=username,
            v_to_l_clicks=v_to_l_clicks,
            v_to_l_rate=v_to_l_rate,
            video_finish_rate=video_finish_rate,
            video_post_time=video_post_time,
            views=views,
        )


        get_shop_video_performance_list_response_data_video.additional_properties = d
        return get_shop_video_performance_list_response_data_video

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
