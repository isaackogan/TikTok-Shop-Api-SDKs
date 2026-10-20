from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.avatar import Avatar
  from ..models.get_live_room_gmv_and_order_trends_response_data_gmv_trend_performance_data_point_gmv import GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv
  from ..models.get_marketplace_creator_performance_response_data_creator_avg_commission_rate_range import GetMarketplaceCreatorPerformanceResponseDataCreatorAvgCommissionRateRange
  from ..models.get_marketplace_creator_performance_response_data_creator_avg_gmv_per_buyer import GetMarketplaceCreatorPerformanceResponseDataCreatorAvgGmvPerBuyer
  from ..models.get_marketplace_creator_performance_response_data_creator_avg_gmv_per_buyer_range import GetMarketplaceCreatorPerformanceResponseDataCreatorAvgGmvPerBuyerRange
  from ..models.get_marketplace_creator_performance_response_data_creator_category_gmv_distribution import GetMarketplaceCreatorPerformanceResponseDataCreatorCategoryGmvDistribution
  from ..models.get_marketplace_creator_performance_response_data_creator_content_gmv_distribution import GetMarketplaceCreatorPerformanceResponseDataCreatorContentGmvDistribution
  from ..models.get_marketplace_creator_performance_response_data_creator_creator_profile import GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfile
  from ..models.get_marketplace_creator_performance_response_data_creator_follower_age import GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerAge
  from ..models.get_marketplace_creator_performance_response_data_creator_follower_gender import GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerGender
  from ..models.get_marketplace_creator_performance_response_data_creator_follower_location import GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerLocation
  from ..models.get_marketplace_creator_performance_response_data_creator_gpm import GetMarketplaceCreatorPerformanceResponseDataCreatorGpm
  from ..models.get_marketplace_creator_performance_response_data_creator_gpm_range import GetMarketplaceCreatorPerformanceResponseDataCreatorGpmRange
  from ..models.get_marketplace_creator_performance_response_data_creator_live_gmv import GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGmv
  from ..models.get_marketplace_creator_performance_response_data_creator_live_gpm import GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGpm
  from ..models.get_marketplace_creator_performance_response_data_creator_live_gpm_range import GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGpmRange
  from ..models.get_marketplace_creator_performance_response_data_creator_product_original_price_range import GetMarketplaceCreatorPerformanceResponseDataCreatorProductOriginalPriceRange
  from ..models.get_marketplace_creator_performance_response_data_creator_video_gpm import GetMarketplaceCreatorPerformanceResponseDataCreatorVideoGpm
  from ..models.get_marketplace_creator_performance_response_data_creator_video_gpm_range import GetMarketplaceCreatorPerformanceResponseDataCreatorVideoGpmRange
  from ..models.gmv_range import GmvRange
  from ..models.units_sold_range import UnitsSoldRange
  from ..models.video_gmv import VideoGmv





T = TypeVar("T", bound="GetMarketplaceCreatorPerformanceResponseDataCreator")



@_attrs_define
class GetMarketplaceCreatorPerformanceResponseDataCreator:
    """ 
        Attributes:
            username (str | Unset): TikTok user name.
            nickname (str | Unset): TikTok nickname.
            avatar (Avatar | Unset):
            selection_region (str | Unset): The region where the creator selects products to promote.
            bio_description (str | Unset): The biography description associated with the creator.
            follower_count (int | Unset): The creator's follower count.
            profile_tt_uri (str | Unset): The deep-link URI for the creator's TikTok profile.
            category_ids (list[str] | Unset): A list of category identifiers associated with the products for which the
                creator has created posts.
            top_collaborated_brand_ids (list[str] | Unset): A list of the top 10 brands with which the creator has
                previously collaborated.
            brand_collaboration_count (int | Unset): The total number of brands with which the creator has previously
                collaborated.
            units_sold (int | Unset): The total number of units sold. Units are indexed to SKU. Note that if the creator has
                not given permission for precise data sharing, this property will not be present.
            units_sold_range (UnitsSoldRange | Unset):
            gmv (GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv | Unset):
            video_gmv (VideoGmv | Unset):
            live_gmv (GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGmv | Unset):
            gmv_range (GmvRange | Unset):
            ec_live_engagement_rate (str | Unset): E-commerce live stream engagement rate in hundredths of a percent. For
                example, `6000` is 60%.
            category_gmv_distribution (list[GetMarketplaceCreatorPerformanceResponseDataCreatorCategoryGmvDistribution] |
                Unset): GMV distribution by category.
            content_gmv_distribution (list[GetMarketplaceCreatorPerformanceResponseDataCreatorContentGmvDistribution] |
                Unset): GMV associated with creator content by content type.
            product_original_price_range (GetMarketplaceCreatorPerformanceResponseDataCreatorProductOriginalPriceRange |
                Unset):
            gpm (GetMarketplaceCreatorPerformanceResponseDataCreatorGpm | Unset):
            live_gpm (GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGpm | Unset):
            video_gpm (GetMarketplaceCreatorPerformanceResponseDataCreatorVideoGpm | Unset):
            gpm_range (GetMarketplaceCreatorPerformanceResponseDataCreatorGpmRange | Unset):
            video_gpm_range (GetMarketplaceCreatorPerformanceResponseDataCreatorVideoGpmRange | Unset):
            live_gpm_range (GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGpmRange | Unset):
            promoted_product_num (int | Unset): The number of products promoted by the creator in the last 30 days.
            ec_live_count (int | Unset): The number of e-commerce livestreams associated with the creator in the last 30
                days.
            ec_video_count (int | Unset): The number of e-commerce video posts associated with the creator in the last 30
                days.
            avg_ec_video_play_count (int | Unset): The average number of number of e-commerce video plays.
            avg_commission_rate (int | Unset): The average commission rate in hundredths of a percent. Note that if the
                creator has not given permission for precise data sharing, these properties will not be present.
            avg_commission_rate_range (GetMarketplaceCreatorPerformanceResponseDataCreatorAvgCommissionRateRange | Unset):
            avg_gmv_per_buyer (GetMarketplaceCreatorPerformanceResponseDataCreatorAvgGmvPerBuyer | Unset):
            avg_gmv_per_buyer_range (GetMarketplaceCreatorPerformanceResponseDataCreatorAvgGmvPerBuyerRange | Unset):
            avg_ec_live_view_count (int | Unset): Average live stream views with promoted products.
            avg_ec_live_like_count (int | Unset): Average e-commerce live stream likes.
            avg_ec_live_comment_count (int | Unset): Average e-commerce live stream comments.
            avg_ec_live_share_count (int | Unset): Average e-commerce live stream shares.
            avg_ec_video_like_count (int | Unset): Average e-commerce video likes.
            avg_ec_video_comment_count (int | Unset): Average e-commerce video comments.
            avg_ec_video_share_count (int | Unset): Average e-commerce video shares.
            follower_location (list[GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerLocation] | Unset): A list of
                key–value pairs representing the distribution of followers by location.
            follower_age (list[GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerAge] | Unset): A list of key–value
                pairs representing the distribution of followers by age range.
            follower_gender (list[GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerGender] | Unset): A list of
                key–value pairs representing the distribution of followers by gender.
            pps (str | Unset): Promotion Performance Score (PPS)
                The score reflects the quality of a creator's shoppable content and product selection over the past 90 days. A
                high score may indicate a better shopping experience, with fewer potential refunds or negative reviews.
            rating (str | Unset): Rating from sellers who worked with this creator
            ec_video_engagement_rate (str | Unset): The number of post engagements (likes, shares, and comments) divided by
                the total video views averaged across the videos in the last 30 days.
                For example, 3000 stands for 0.3 or 30%
            post_rate (str | Unset): The projected rate at which a creator is likely to post a shoppable video or LIVE after
                receiving a sample.
                For example, 3000 stands for 0.3 or 30%
            creator_profile (GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfile | Unset):
     """

    username: str | Unset = UNSET
    nickname: str | Unset = UNSET
    avatar: Avatar | Unset = UNSET
    selection_region: str | Unset = UNSET
    bio_description: str | Unset = UNSET
    follower_count: int | Unset = UNSET
    profile_tt_uri: str | Unset = UNSET
    category_ids: list[str] | Unset = UNSET
    top_collaborated_brand_ids: list[str] | Unset = UNSET
    brand_collaboration_count: int | Unset = UNSET
    units_sold: int | Unset = UNSET
    units_sold_range: UnitsSoldRange | Unset = UNSET
    gmv: GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv | Unset = UNSET
    video_gmv: VideoGmv | Unset = UNSET
    live_gmv: GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGmv | Unset = UNSET
    gmv_range: GmvRange | Unset = UNSET
    ec_live_engagement_rate: str | Unset = UNSET
    category_gmv_distribution: list[GetMarketplaceCreatorPerformanceResponseDataCreatorCategoryGmvDistribution] | Unset = UNSET
    content_gmv_distribution: list[GetMarketplaceCreatorPerformanceResponseDataCreatorContentGmvDistribution] | Unset = UNSET
    product_original_price_range: GetMarketplaceCreatorPerformanceResponseDataCreatorProductOriginalPriceRange | Unset = UNSET
    gpm: GetMarketplaceCreatorPerformanceResponseDataCreatorGpm | Unset = UNSET
    live_gpm: GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGpm | Unset = UNSET
    video_gpm: GetMarketplaceCreatorPerformanceResponseDataCreatorVideoGpm | Unset = UNSET
    gpm_range: GetMarketplaceCreatorPerformanceResponseDataCreatorGpmRange | Unset = UNSET
    video_gpm_range: GetMarketplaceCreatorPerformanceResponseDataCreatorVideoGpmRange | Unset = UNSET
    live_gpm_range: GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGpmRange | Unset = UNSET
    promoted_product_num: int | Unset = UNSET
    ec_live_count: int | Unset = UNSET
    ec_video_count: int | Unset = UNSET
    avg_ec_video_play_count: int | Unset = UNSET
    avg_commission_rate: int | Unset = UNSET
    avg_commission_rate_range: GetMarketplaceCreatorPerformanceResponseDataCreatorAvgCommissionRateRange | Unset = UNSET
    avg_gmv_per_buyer: GetMarketplaceCreatorPerformanceResponseDataCreatorAvgGmvPerBuyer | Unset = UNSET
    avg_gmv_per_buyer_range: GetMarketplaceCreatorPerformanceResponseDataCreatorAvgGmvPerBuyerRange | Unset = UNSET
    avg_ec_live_view_count: int | Unset = UNSET
    avg_ec_live_like_count: int | Unset = UNSET
    avg_ec_live_comment_count: int | Unset = UNSET
    avg_ec_live_share_count: int | Unset = UNSET
    avg_ec_video_like_count: int | Unset = UNSET
    avg_ec_video_comment_count: int | Unset = UNSET
    avg_ec_video_share_count: int | Unset = UNSET
    follower_location: list[GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerLocation] | Unset = UNSET
    follower_age: list[GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerAge] | Unset = UNSET
    follower_gender: list[GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerGender] | Unset = UNSET
    pps: str | Unset = UNSET
    rating: str | Unset = UNSET
    ec_video_engagement_rate: str | Unset = UNSET
    post_rate: str | Unset = UNSET
    creator_profile: GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfile | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.avatar import Avatar # noqa: PLC0415
        from ..models.get_live_room_gmv_and_order_trends_response_data_gmv_trend_performance_data_point_gmv import GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_avg_commission_rate_range import GetMarketplaceCreatorPerformanceResponseDataCreatorAvgCommissionRateRange # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_avg_gmv_per_buyer import GetMarketplaceCreatorPerformanceResponseDataCreatorAvgGmvPerBuyer # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_avg_gmv_per_buyer_range import GetMarketplaceCreatorPerformanceResponseDataCreatorAvgGmvPerBuyerRange # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_category_gmv_distribution import GetMarketplaceCreatorPerformanceResponseDataCreatorCategoryGmvDistribution # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_content_gmv_distribution import GetMarketplaceCreatorPerformanceResponseDataCreatorContentGmvDistribution # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_creator_profile import GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfile # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_follower_age import GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerAge # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_follower_gender import GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerGender # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_follower_location import GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerLocation # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_gpm import GetMarketplaceCreatorPerformanceResponseDataCreatorGpm # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_gpm_range import GetMarketplaceCreatorPerformanceResponseDataCreatorGpmRange # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_live_gmv import GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGmv # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_live_gpm import GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGpm # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_live_gpm_range import GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGpmRange # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_product_original_price_range import GetMarketplaceCreatorPerformanceResponseDataCreatorProductOriginalPriceRange # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_video_gpm import GetMarketplaceCreatorPerformanceResponseDataCreatorVideoGpm # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_video_gpm_range import GetMarketplaceCreatorPerformanceResponseDataCreatorVideoGpmRange # noqa: PLC0415
        from ..models.gmv_range import GmvRange # noqa: PLC0415
        from ..models.units_sold_range import UnitsSoldRange # noqa: PLC0415
        from ..models.video_gmv import VideoGmv # noqa: PLC0415
        username = self.username

        nickname = self.nickname

        avatar: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        selection_region = self.selection_region

        bio_description = self.bio_description

        follower_count = self.follower_count

        profile_tt_uri = self.profile_tt_uri

        category_ids: list[str] | Unset = UNSET
        if not isinstance(self.category_ids, Unset):
            category_ids = self.category_ids



        top_collaborated_brand_ids: list[str] | Unset = UNSET
        if not isinstance(self.top_collaborated_brand_ids, Unset):
            top_collaborated_brand_ids = self.top_collaborated_brand_ids



        brand_collaboration_count = self.brand_collaboration_count

        units_sold = self.units_sold

        units_sold_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.units_sold_range, Unset):
            units_sold_range = self.units_sold_range.to_dict()

        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        video_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video_gmv, Unset):
            video_gmv = self.video_gmv.to_dict()

        live_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_gmv, Unset):
            live_gmv = self.live_gmv.to_dict()

        gmv_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv_range, Unset):
            gmv_range = self.gmv_range.to_dict()

        ec_live_engagement_rate = self.ec_live_engagement_rate

        category_gmv_distribution: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.category_gmv_distribution, Unset):
            category_gmv_distribution = []
            for category_gmv_distribution_item_data in self.category_gmv_distribution:
                category_gmv_distribution_item = category_gmv_distribution_item_data.to_dict()
                category_gmv_distribution.append(category_gmv_distribution_item)



        content_gmv_distribution: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content_gmv_distribution, Unset):
            content_gmv_distribution = []
            for content_gmv_distribution_item_data in self.content_gmv_distribution:
                content_gmv_distribution_item = content_gmv_distribution_item_data.to_dict()
                content_gmv_distribution.append(content_gmv_distribution_item)



        product_original_price_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_original_price_range, Unset):
            product_original_price_range = self.product_original_price_range.to_dict()

        gpm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gpm, Unset):
            gpm = self.gpm.to_dict()

        live_gpm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_gpm, Unset):
            live_gpm = self.live_gpm.to_dict()

        video_gpm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video_gpm, Unset):
            video_gpm = self.video_gpm.to_dict()

        gpm_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gpm_range, Unset):
            gpm_range = self.gpm_range.to_dict()

        video_gpm_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video_gpm_range, Unset):
            video_gpm_range = self.video_gpm_range.to_dict()

        live_gpm_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_gpm_range, Unset):
            live_gpm_range = self.live_gpm_range.to_dict()

        promoted_product_num = self.promoted_product_num

        ec_live_count = self.ec_live_count

        ec_video_count = self.ec_video_count

        avg_ec_video_play_count = self.avg_ec_video_play_count

        avg_commission_rate = self.avg_commission_rate

        avg_commission_rate_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avg_commission_rate_range, Unset):
            avg_commission_rate_range = self.avg_commission_rate_range.to_dict()

        avg_gmv_per_buyer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avg_gmv_per_buyer, Unset):
            avg_gmv_per_buyer = self.avg_gmv_per_buyer.to_dict()

        avg_gmv_per_buyer_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avg_gmv_per_buyer_range, Unset):
            avg_gmv_per_buyer_range = self.avg_gmv_per_buyer_range.to_dict()

        avg_ec_live_view_count = self.avg_ec_live_view_count

        avg_ec_live_like_count = self.avg_ec_live_like_count

        avg_ec_live_comment_count = self.avg_ec_live_comment_count

        avg_ec_live_share_count = self.avg_ec_live_share_count

        avg_ec_video_like_count = self.avg_ec_video_like_count

        avg_ec_video_comment_count = self.avg_ec_video_comment_count

        avg_ec_video_share_count = self.avg_ec_video_share_count

        follower_location: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.follower_location, Unset):
            follower_location = []
            for follower_location_item_data in self.follower_location:
                follower_location_item = follower_location_item_data.to_dict()
                follower_location.append(follower_location_item)



        follower_age: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.follower_age, Unset):
            follower_age = []
            for follower_age_item_data in self.follower_age:
                follower_age_item = follower_age_item_data.to_dict()
                follower_age.append(follower_age_item)



        follower_gender: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.follower_gender, Unset):
            follower_gender = []
            for follower_gender_item_data in self.follower_gender:
                follower_gender_item = follower_gender_item_data.to_dict()
                follower_gender.append(follower_gender_item)



        pps = self.pps

        rating = self.rating

        ec_video_engagement_rate = self.ec_video_engagement_rate

        post_rate = self.post_rate

        creator_profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator_profile, Unset):
            creator_profile = self.creator_profile.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if username is not UNSET:
            field_dict["username"] = username
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if selection_region is not UNSET:
            field_dict["selection_region"] = selection_region
        if bio_description is not UNSET:
            field_dict["bio_description"] = bio_description
        if follower_count is not UNSET:
            field_dict["follower_count"] = follower_count
        if profile_tt_uri is not UNSET:
            field_dict["profile_tt_uri"] = profile_tt_uri
        if category_ids is not UNSET:
            field_dict["category_ids"] = category_ids
        if top_collaborated_brand_ids is not UNSET:
            field_dict["top_collaborated_brand_ids"] = top_collaborated_brand_ids
        if brand_collaboration_count is not UNSET:
            field_dict["brand_collaboration_count"] = brand_collaboration_count
        if units_sold is not UNSET:
            field_dict["units_sold"] = units_sold
        if units_sold_range is not UNSET:
            field_dict["units_sold_range"] = units_sold_range
        if gmv is not UNSET:
            field_dict["gmv"] = gmv
        if video_gmv is not UNSET:
            field_dict["video_gmv"] = video_gmv
        if live_gmv is not UNSET:
            field_dict["live_gmv"] = live_gmv
        if gmv_range is not UNSET:
            field_dict["gmv_range"] = gmv_range
        if ec_live_engagement_rate is not UNSET:
            field_dict["ec_live_engagement_rate"] = ec_live_engagement_rate
        if category_gmv_distribution is not UNSET:
            field_dict["category_gmv_distribution"] = category_gmv_distribution
        if content_gmv_distribution is not UNSET:
            field_dict["content_gmv_distribution"] = content_gmv_distribution
        if product_original_price_range is not UNSET:
            field_dict["product_original_price_range"] = product_original_price_range
        if gpm is not UNSET:
            field_dict["gpm"] = gpm
        if live_gpm is not UNSET:
            field_dict["live_gpm"] = live_gpm
        if video_gpm is not UNSET:
            field_dict["video_gpm"] = video_gpm
        if gpm_range is not UNSET:
            field_dict["gpm_range"] = gpm_range
        if video_gpm_range is not UNSET:
            field_dict["video_gpm_range"] = video_gpm_range
        if live_gpm_range is not UNSET:
            field_dict["live_gpm_range"] = live_gpm_range
        if promoted_product_num is not UNSET:
            field_dict["promoted_product_num"] = promoted_product_num
        if ec_live_count is not UNSET:
            field_dict["ec_live_count"] = ec_live_count
        if ec_video_count is not UNSET:
            field_dict["ec_video_count"] = ec_video_count
        if avg_ec_video_play_count is not UNSET:
            field_dict["avg_ec_video_play_count"] = avg_ec_video_play_count
        if avg_commission_rate is not UNSET:
            field_dict["avg_commission_rate"] = avg_commission_rate
        if avg_commission_rate_range is not UNSET:
            field_dict["avg_commission_rate_range"] = avg_commission_rate_range
        if avg_gmv_per_buyer is not UNSET:
            field_dict["avg_gmv_per_buyer"] = avg_gmv_per_buyer
        if avg_gmv_per_buyer_range is not UNSET:
            field_dict["avg_gmv_per_buyer_range"] = avg_gmv_per_buyer_range
        if avg_ec_live_view_count is not UNSET:
            field_dict["avg_ec_live_view_count"] = avg_ec_live_view_count
        if avg_ec_live_like_count is not UNSET:
            field_dict["avg_ec_live_like_count"] = avg_ec_live_like_count
        if avg_ec_live_comment_count is not UNSET:
            field_dict["avg_ec_live_comment_count"] = avg_ec_live_comment_count
        if avg_ec_live_share_count is not UNSET:
            field_dict["avg_ec_live_share_count"] = avg_ec_live_share_count
        if avg_ec_video_like_count is not UNSET:
            field_dict["avg_ec_video_like_count"] = avg_ec_video_like_count
        if avg_ec_video_comment_count is not UNSET:
            field_dict["avg_ec_video_comment_count"] = avg_ec_video_comment_count
        if avg_ec_video_share_count is not UNSET:
            field_dict["avg_ec_video_share_count"] = avg_ec_video_share_count
        if follower_location is not UNSET:
            field_dict["follower_location"] = follower_location
        if follower_age is not UNSET:
            field_dict["follower_age"] = follower_age
        if follower_gender is not UNSET:
            field_dict["follower_gender"] = follower_gender
        if pps is not UNSET:
            field_dict["pps"] = pps
        if rating is not UNSET:
            field_dict["rating"] = rating
        if ec_video_engagement_rate is not UNSET:
            field_dict["ec_video_engagement_rate"] = ec_video_engagement_rate
        if post_rate is not UNSET:
            field_dict["post_rate"] = post_rate
        if creator_profile is not UNSET:
            field_dict["creator_profile"] = creator_profile

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.avatar import Avatar # noqa: PLC0415
        from ..models.get_live_room_gmv_and_order_trends_response_data_gmv_trend_performance_data_point_gmv import GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_avg_commission_rate_range import GetMarketplaceCreatorPerformanceResponseDataCreatorAvgCommissionRateRange # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_avg_gmv_per_buyer import GetMarketplaceCreatorPerformanceResponseDataCreatorAvgGmvPerBuyer # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_avg_gmv_per_buyer_range import GetMarketplaceCreatorPerformanceResponseDataCreatorAvgGmvPerBuyerRange # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_category_gmv_distribution import GetMarketplaceCreatorPerformanceResponseDataCreatorCategoryGmvDistribution # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_content_gmv_distribution import GetMarketplaceCreatorPerformanceResponseDataCreatorContentGmvDistribution # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_creator_profile import GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfile # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_follower_age import GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerAge # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_follower_gender import GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerGender # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_follower_location import GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerLocation # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_gpm import GetMarketplaceCreatorPerformanceResponseDataCreatorGpm # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_gpm_range import GetMarketplaceCreatorPerformanceResponseDataCreatorGpmRange # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_live_gmv import GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGmv # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_live_gpm import GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGpm # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_live_gpm_range import GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGpmRange # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_product_original_price_range import GetMarketplaceCreatorPerformanceResponseDataCreatorProductOriginalPriceRange # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_video_gpm import GetMarketplaceCreatorPerformanceResponseDataCreatorVideoGpm # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_video_gpm_range import GetMarketplaceCreatorPerformanceResponseDataCreatorVideoGpmRange # noqa: PLC0415
        from ..models.gmv_range import GmvRange # noqa: PLC0415
        from ..models.units_sold_range import UnitsSoldRange # noqa: PLC0415
        from ..models.video_gmv import VideoGmv # noqa: PLC0415
        d = dict(src_dict)
        username = d.pop("username", UNSET)

        nickname = d.pop("nickname", UNSET)

        _avatar = d.pop("avatar", UNSET)
        avatar: Avatar | Unset
        if isinstance(_avatar,  Unset):
            avatar = UNSET
        else:
            avatar = Avatar.from_dict(_avatar)




        selection_region = d.pop("selection_region", UNSET)

        bio_description = d.pop("bio_description", UNSET)

        follower_count = d.pop("follower_count", UNSET)

        profile_tt_uri = d.pop("profile_tt_uri", UNSET)

        category_ids = cast(list[str], d.pop("category_ids", UNSET))


        top_collaborated_brand_ids = cast(list[str], d.pop("top_collaborated_brand_ids", UNSET))


        brand_collaboration_count = d.pop("brand_collaboration_count", UNSET)

        units_sold = d.pop("units_sold", UNSET)

        _units_sold_range = d.pop("units_sold_range", UNSET)
        units_sold_range: UnitsSoldRange | Unset
        if isinstance(_units_sold_range,  Unset):
            units_sold_range = UNSET
        else:
            units_sold_range = UnitsSoldRange.from_dict(_units_sold_range)




        _gmv = d.pop("gmv", UNSET)
        gmv: GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv | Unset
        if isinstance(_gmv,  Unset):
            gmv = UNSET
        else:
            gmv = GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv.from_dict(_gmv)




        _video_gmv = d.pop("video_gmv", UNSET)
        video_gmv: VideoGmv | Unset
        if isinstance(_video_gmv,  Unset):
            video_gmv = UNSET
        else:
            video_gmv = VideoGmv.from_dict(_video_gmv)




        _live_gmv = d.pop("live_gmv", UNSET)
        live_gmv: GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGmv | Unset
        if isinstance(_live_gmv,  Unset):
            live_gmv = UNSET
        else:
            live_gmv = GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGmv.from_dict(_live_gmv)




        _gmv_range = d.pop("gmv_range", UNSET)
        gmv_range: GmvRange | Unset
        if isinstance(_gmv_range,  Unset):
            gmv_range = UNSET
        else:
            gmv_range = GmvRange.from_dict(_gmv_range)




        ec_live_engagement_rate = d.pop("ec_live_engagement_rate", UNSET)

        _category_gmv_distribution = d.pop("category_gmv_distribution", UNSET)
        category_gmv_distribution: list[GetMarketplaceCreatorPerformanceResponseDataCreatorCategoryGmvDistribution] | Unset = UNSET
        if _category_gmv_distribution is not UNSET:
            category_gmv_distribution = []
            for category_gmv_distribution_item_data in _category_gmv_distribution:
                category_gmv_distribution_item = GetMarketplaceCreatorPerformanceResponseDataCreatorCategoryGmvDistribution.from_dict(category_gmv_distribution_item_data)



                category_gmv_distribution.append(category_gmv_distribution_item)


        _content_gmv_distribution = d.pop("content_gmv_distribution", UNSET)
        content_gmv_distribution: list[GetMarketplaceCreatorPerformanceResponseDataCreatorContentGmvDistribution] | Unset = UNSET
        if _content_gmv_distribution is not UNSET:
            content_gmv_distribution = []
            for content_gmv_distribution_item_data in _content_gmv_distribution:
                content_gmv_distribution_item = GetMarketplaceCreatorPerformanceResponseDataCreatorContentGmvDistribution.from_dict(content_gmv_distribution_item_data)



                content_gmv_distribution.append(content_gmv_distribution_item)


        _product_original_price_range = d.pop("product_original_price_range", UNSET)
        product_original_price_range: GetMarketplaceCreatorPerformanceResponseDataCreatorProductOriginalPriceRange | Unset
        if isinstance(_product_original_price_range,  Unset):
            product_original_price_range = UNSET
        else:
            product_original_price_range = GetMarketplaceCreatorPerformanceResponseDataCreatorProductOriginalPriceRange.from_dict(_product_original_price_range)




        _gpm = d.pop("gpm", UNSET)
        gpm: GetMarketplaceCreatorPerformanceResponseDataCreatorGpm | Unset
        if isinstance(_gpm,  Unset):
            gpm = UNSET
        else:
            gpm = GetMarketplaceCreatorPerformanceResponseDataCreatorGpm.from_dict(_gpm)




        _live_gpm = d.pop("live_gpm", UNSET)
        live_gpm: GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGpm | Unset
        if isinstance(_live_gpm,  Unset):
            live_gpm = UNSET
        else:
            live_gpm = GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGpm.from_dict(_live_gpm)




        _video_gpm = d.pop("video_gpm", UNSET)
        video_gpm: GetMarketplaceCreatorPerformanceResponseDataCreatorVideoGpm | Unset
        if isinstance(_video_gpm,  Unset):
            video_gpm = UNSET
        else:
            video_gpm = GetMarketplaceCreatorPerformanceResponseDataCreatorVideoGpm.from_dict(_video_gpm)




        _gpm_range = d.pop("gpm_range", UNSET)
        gpm_range: GetMarketplaceCreatorPerformanceResponseDataCreatorGpmRange | Unset
        if isinstance(_gpm_range,  Unset):
            gpm_range = UNSET
        else:
            gpm_range = GetMarketplaceCreatorPerformanceResponseDataCreatorGpmRange.from_dict(_gpm_range)




        _video_gpm_range = d.pop("video_gpm_range", UNSET)
        video_gpm_range: GetMarketplaceCreatorPerformanceResponseDataCreatorVideoGpmRange | Unset
        if isinstance(_video_gpm_range,  Unset):
            video_gpm_range = UNSET
        else:
            video_gpm_range = GetMarketplaceCreatorPerformanceResponseDataCreatorVideoGpmRange.from_dict(_video_gpm_range)




        _live_gpm_range = d.pop("live_gpm_range", UNSET)
        live_gpm_range: GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGpmRange | Unset
        if isinstance(_live_gpm_range,  Unset):
            live_gpm_range = UNSET
        else:
            live_gpm_range = GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGpmRange.from_dict(_live_gpm_range)




        promoted_product_num = d.pop("promoted_product_num", UNSET)

        ec_live_count = d.pop("ec_live_count", UNSET)

        ec_video_count = d.pop("ec_video_count", UNSET)

        avg_ec_video_play_count = d.pop("avg_ec_video_play_count", UNSET)

        avg_commission_rate = d.pop("avg_commission_rate", UNSET)

        _avg_commission_rate_range = d.pop("avg_commission_rate_range", UNSET)
        avg_commission_rate_range: GetMarketplaceCreatorPerformanceResponseDataCreatorAvgCommissionRateRange | Unset
        if isinstance(_avg_commission_rate_range,  Unset):
            avg_commission_rate_range = UNSET
        else:
            avg_commission_rate_range = GetMarketplaceCreatorPerformanceResponseDataCreatorAvgCommissionRateRange.from_dict(_avg_commission_rate_range)




        _avg_gmv_per_buyer = d.pop("avg_gmv_per_buyer", UNSET)
        avg_gmv_per_buyer: GetMarketplaceCreatorPerformanceResponseDataCreatorAvgGmvPerBuyer | Unset
        if isinstance(_avg_gmv_per_buyer,  Unset):
            avg_gmv_per_buyer = UNSET
        else:
            avg_gmv_per_buyer = GetMarketplaceCreatorPerformanceResponseDataCreatorAvgGmvPerBuyer.from_dict(_avg_gmv_per_buyer)




        _avg_gmv_per_buyer_range = d.pop("avg_gmv_per_buyer_range", UNSET)
        avg_gmv_per_buyer_range: GetMarketplaceCreatorPerformanceResponseDataCreatorAvgGmvPerBuyerRange | Unset
        if isinstance(_avg_gmv_per_buyer_range,  Unset):
            avg_gmv_per_buyer_range = UNSET
        else:
            avg_gmv_per_buyer_range = GetMarketplaceCreatorPerformanceResponseDataCreatorAvgGmvPerBuyerRange.from_dict(_avg_gmv_per_buyer_range)




        avg_ec_live_view_count = d.pop("avg_ec_live_view_count", UNSET)

        avg_ec_live_like_count = d.pop("avg_ec_live_like_count", UNSET)

        avg_ec_live_comment_count = d.pop("avg_ec_live_comment_count", UNSET)

        avg_ec_live_share_count = d.pop("avg_ec_live_share_count", UNSET)

        avg_ec_video_like_count = d.pop("avg_ec_video_like_count", UNSET)

        avg_ec_video_comment_count = d.pop("avg_ec_video_comment_count", UNSET)

        avg_ec_video_share_count = d.pop("avg_ec_video_share_count", UNSET)

        _follower_location = d.pop("follower_location", UNSET)
        follower_location: list[GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerLocation] | Unset = UNSET
        if _follower_location is not UNSET:
            follower_location = []
            for follower_location_item_data in _follower_location:
                follower_location_item = GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerLocation.from_dict(follower_location_item_data)



                follower_location.append(follower_location_item)


        _follower_age = d.pop("follower_age", UNSET)
        follower_age: list[GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerAge] | Unset = UNSET
        if _follower_age is not UNSET:
            follower_age = []
            for follower_age_item_data in _follower_age:
                follower_age_item = GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerAge.from_dict(follower_age_item_data)



                follower_age.append(follower_age_item)


        _follower_gender = d.pop("follower_gender", UNSET)
        follower_gender: list[GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerGender] | Unset = UNSET
        if _follower_gender is not UNSET:
            follower_gender = []
            for follower_gender_item_data in _follower_gender:
                follower_gender_item = GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerGender.from_dict(follower_gender_item_data)



                follower_gender.append(follower_gender_item)


        pps = d.pop("pps", UNSET)

        rating = d.pop("rating", UNSET)

        ec_video_engagement_rate = d.pop("ec_video_engagement_rate", UNSET)

        post_rate = d.pop("post_rate", UNSET)

        _creator_profile = d.pop("creator_profile", UNSET)
        creator_profile: GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfile | Unset
        if isinstance(_creator_profile,  Unset):
            creator_profile = UNSET
        else:
            creator_profile = GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfile.from_dict(_creator_profile)




        get_marketplace_creator_performance_response_data_creator = cls(
            username=username,
            nickname=nickname,
            avatar=avatar,
            selection_region=selection_region,
            bio_description=bio_description,
            follower_count=follower_count,
            profile_tt_uri=profile_tt_uri,
            category_ids=category_ids,
            top_collaborated_brand_ids=top_collaborated_brand_ids,
            brand_collaboration_count=brand_collaboration_count,
            units_sold=units_sold,
            units_sold_range=units_sold_range,
            gmv=gmv,
            video_gmv=video_gmv,
            live_gmv=live_gmv,
            gmv_range=gmv_range,
            ec_live_engagement_rate=ec_live_engagement_rate,
            category_gmv_distribution=category_gmv_distribution,
            content_gmv_distribution=content_gmv_distribution,
            product_original_price_range=product_original_price_range,
            gpm=gpm,
            live_gpm=live_gpm,
            video_gpm=video_gpm,
            gpm_range=gpm_range,
            video_gpm_range=video_gpm_range,
            live_gpm_range=live_gpm_range,
            promoted_product_num=promoted_product_num,
            ec_live_count=ec_live_count,
            ec_video_count=ec_video_count,
            avg_ec_video_play_count=avg_ec_video_play_count,
            avg_commission_rate=avg_commission_rate,
            avg_commission_rate_range=avg_commission_rate_range,
            avg_gmv_per_buyer=avg_gmv_per_buyer,
            avg_gmv_per_buyer_range=avg_gmv_per_buyer_range,
            avg_ec_live_view_count=avg_ec_live_view_count,
            avg_ec_live_like_count=avg_ec_live_like_count,
            avg_ec_live_comment_count=avg_ec_live_comment_count,
            avg_ec_live_share_count=avg_ec_live_share_count,
            avg_ec_video_like_count=avg_ec_video_like_count,
            avg_ec_video_comment_count=avg_ec_video_comment_count,
            avg_ec_video_share_count=avg_ec_video_share_count,
            follower_location=follower_location,
            follower_age=follower_age,
            follower_gender=follower_gender,
            pps=pps,
            rating=rating,
            ec_video_engagement_rate=ec_video_engagement_rate,
            post_rate=post_rate,
            creator_profile=creator_profile,
        )


        get_marketplace_creator_performance_response_data_creator.additional_properties = d
        return get_marketplace_creator_performance_response_data_creator

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
