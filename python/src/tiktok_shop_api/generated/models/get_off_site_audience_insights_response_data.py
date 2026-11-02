from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_off_site_audience_insights_response_data_age import GetOffSiteAudienceInsightsResponseDataAge
  from ..models.get_off_site_audience_insights_response_data_consumption_level import GetOffSiteAudienceInsightsResponseDataConsumptionLevel
  from ..models.get_off_site_audience_insights_response_data_followed_shop import GetOffSiteAudienceInsightsResponseDataFollowedShop
  from ..models.get_off_site_audience_insights_response_data_gender import GetOffSiteAudienceInsightsResponseDataGender
  from ..models.get_off_site_audience_insights_response_data_persona import GetOffSiteAudienceInsightsResponseDataPersona
  from ..models.get_off_site_audience_insights_response_data_region import GetOffSiteAudienceInsightsResponseDataRegion
  from ..models.get_off_site_audience_insights_response_data_top_favorite_content import GetOffSiteAudienceInsightsResponseDataTopFavoriteContent
  from ..models.get_off_site_audience_insights_response_data_top_purchase_category_preference import GetOffSiteAudienceInsightsResponseDataTopPurchaseCategoryPreference





T = TypeVar("T", bound="GetOffSiteAudienceInsightsResponseData")



@_attrs_define
class GetOffSiteAudienceInsightsResponseData:
    """ 
        Attributes:
            age (list[GetOffSiteAudienceInsightsResponseDataAge] | Unset): Age-group distribution, ordered by descending
                TikTok Shop customer count. Empty labels and `Unknown` are excluded.
            consumption_level (list[GetOffSiteAudienceInsightsResponseDataConsumptionLevel] | Unset): Consumption-level
                distribution, ordered by descending TikTok Shop customer count. Empty labels and `Unknown` are excluded.
            followed_shop (list[GetOffSiteAudienceInsightsResponseDataFollowedShop] | Unset): Distribution by shop-follow
                status, ordered by descending TikTok Shop customer count. Empty labels and `Unknown` are excluded.
            gender (list[GetOffSiteAudienceInsightsResponseDataGender] | Unset): Gender distribution, ordered by descending
                TikTok Shop customer count. Empty labels and `Unknown` are excluded.
            personas (list[GetOffSiteAudienceInsightsResponseDataPersona] | Unset): Audience persona distribution, ordered
                by descending TikTok Shop customer count. Empty labels and `Unknown` are excluded; `OTHERS` is also excluded
                regardless of case. The number of returned persona labels is not fixed at eight.
            region (list[GetOffSiteAudienceInsightsResponseDataRegion] | Unset): City distribution, ordered by descending
                TikTok Shop customer count. At most 10 entries are returned: the top 10 labels are selected before empty labels
                and `Unknown` are removed.
            top_favorite_content (list[GetOffSiteAudienceInsightsResponseDataTopFavoriteContent] | Unset): Content-interest
                distribution, ordered by descending TikTok Shop customer count. At most 10 entries are returned: the top 10
                labels are selected before empty labels and `Unknown` are removed.
            top_purchase_category_preferences (list[GetOffSiteAudienceInsightsResponseDataTopPurchaseCategoryPreference] |
                Unset): Level-2 purchase-category distribution, ordered by descending TikTok Shop customer count. At most 10
                entries are returned; categories are selected before label filtering, so fewer than 10 entries may be returned.
     """

    age: list[GetOffSiteAudienceInsightsResponseDataAge] | Unset = UNSET
    consumption_level: list[GetOffSiteAudienceInsightsResponseDataConsumptionLevel] | Unset = UNSET
    followed_shop: list[GetOffSiteAudienceInsightsResponseDataFollowedShop] | Unset = UNSET
    gender: list[GetOffSiteAudienceInsightsResponseDataGender] | Unset = UNSET
    personas: list[GetOffSiteAudienceInsightsResponseDataPersona] | Unset = UNSET
    region: list[GetOffSiteAudienceInsightsResponseDataRegion] | Unset = UNSET
    top_favorite_content: list[GetOffSiteAudienceInsightsResponseDataTopFavoriteContent] | Unset = UNSET
    top_purchase_category_preferences: list[GetOffSiteAudienceInsightsResponseDataTopPurchaseCategoryPreference] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_off_site_audience_insights_response_data_age import GetOffSiteAudienceInsightsResponseDataAge # noqa: PLC0415
        from ..models.get_off_site_audience_insights_response_data_consumption_level import GetOffSiteAudienceInsightsResponseDataConsumptionLevel # noqa: PLC0415
        from ..models.get_off_site_audience_insights_response_data_followed_shop import GetOffSiteAudienceInsightsResponseDataFollowedShop # noqa: PLC0415
        from ..models.get_off_site_audience_insights_response_data_gender import GetOffSiteAudienceInsightsResponseDataGender # noqa: PLC0415
        from ..models.get_off_site_audience_insights_response_data_persona import GetOffSiteAudienceInsightsResponseDataPersona # noqa: PLC0415
        from ..models.get_off_site_audience_insights_response_data_region import GetOffSiteAudienceInsightsResponseDataRegion # noqa: PLC0415
        from ..models.get_off_site_audience_insights_response_data_top_favorite_content import GetOffSiteAudienceInsightsResponseDataTopFavoriteContent # noqa: PLC0415
        from ..models.get_off_site_audience_insights_response_data_top_purchase_category_preference import GetOffSiteAudienceInsightsResponseDataTopPurchaseCategoryPreference # noqa: PLC0415
        age: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.age, Unset):
            age = []
            for age_item_data in self.age:
                age_item = age_item_data.to_dict()
                age.append(age_item)



        consumption_level: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.consumption_level, Unset):
            consumption_level = []
            for consumption_level_item_data in self.consumption_level:
                consumption_level_item = consumption_level_item_data.to_dict()
                consumption_level.append(consumption_level_item)



        followed_shop: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.followed_shop, Unset):
            followed_shop = []
            for followed_shop_item_data in self.followed_shop:
                followed_shop_item = followed_shop_item_data.to_dict()
                followed_shop.append(followed_shop_item)



        gender: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gender, Unset):
            gender = []
            for gender_item_data in self.gender:
                gender_item = gender_item_data.to_dict()
                gender.append(gender_item)



        personas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.personas, Unset):
            personas = []
            for personas_item_data in self.personas:
                personas_item = personas_item_data.to_dict()
                personas.append(personas_item)



        region: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = []
            for region_item_data in self.region:
                region_item = region_item_data.to_dict()
                region.append(region_item)



        top_favorite_content: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_favorite_content, Unset):
            top_favorite_content = []
            for top_favorite_content_item_data in self.top_favorite_content:
                top_favorite_content_item = top_favorite_content_item_data.to_dict()
                top_favorite_content.append(top_favorite_content_item)



        top_purchase_category_preferences: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_purchase_category_preferences, Unset):
            top_purchase_category_preferences = []
            for top_purchase_category_preferences_item_data in self.top_purchase_category_preferences:
                top_purchase_category_preferences_item = top_purchase_category_preferences_item_data.to_dict()
                top_purchase_category_preferences.append(top_purchase_category_preferences_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if age is not UNSET:
            field_dict["age"] = age
        if consumption_level is not UNSET:
            field_dict["consumption_level"] = consumption_level
        if followed_shop is not UNSET:
            field_dict["followed_shop"] = followed_shop
        if gender is not UNSET:
            field_dict["gender"] = gender
        if personas is not UNSET:
            field_dict["personas"] = personas
        if region is not UNSET:
            field_dict["region"] = region
        if top_favorite_content is not UNSET:
            field_dict["top_favorite_content"] = top_favorite_content
        if top_purchase_category_preferences is not UNSET:
            field_dict["top_purchase_category_preferences"] = top_purchase_category_preferences

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_off_site_audience_insights_response_data_age import GetOffSiteAudienceInsightsResponseDataAge # noqa: PLC0415
        from ..models.get_off_site_audience_insights_response_data_consumption_level import GetOffSiteAudienceInsightsResponseDataConsumptionLevel # noqa: PLC0415
        from ..models.get_off_site_audience_insights_response_data_followed_shop import GetOffSiteAudienceInsightsResponseDataFollowedShop # noqa: PLC0415
        from ..models.get_off_site_audience_insights_response_data_gender import GetOffSiteAudienceInsightsResponseDataGender # noqa: PLC0415
        from ..models.get_off_site_audience_insights_response_data_persona import GetOffSiteAudienceInsightsResponseDataPersona # noqa: PLC0415
        from ..models.get_off_site_audience_insights_response_data_region import GetOffSiteAudienceInsightsResponseDataRegion # noqa: PLC0415
        from ..models.get_off_site_audience_insights_response_data_top_favorite_content import GetOffSiteAudienceInsightsResponseDataTopFavoriteContent # noqa: PLC0415
        from ..models.get_off_site_audience_insights_response_data_top_purchase_category_preference import GetOffSiteAudienceInsightsResponseDataTopPurchaseCategoryPreference # noqa: PLC0415
        d = dict(src_dict)
        _age = d.pop("age", UNSET)
        age: list[GetOffSiteAudienceInsightsResponseDataAge] | Unset = UNSET
        if _age is not UNSET:
            age = []
            for age_item_data in _age:
                age_item = GetOffSiteAudienceInsightsResponseDataAge.from_dict(age_item_data)



                age.append(age_item)


        _consumption_level = d.pop("consumption_level", UNSET)
        consumption_level: list[GetOffSiteAudienceInsightsResponseDataConsumptionLevel] | Unset = UNSET
        if _consumption_level is not UNSET:
            consumption_level = []
            for consumption_level_item_data in _consumption_level:
                consumption_level_item = GetOffSiteAudienceInsightsResponseDataConsumptionLevel.from_dict(consumption_level_item_data)



                consumption_level.append(consumption_level_item)


        _followed_shop = d.pop("followed_shop", UNSET)
        followed_shop: list[GetOffSiteAudienceInsightsResponseDataFollowedShop] | Unset = UNSET
        if _followed_shop is not UNSET:
            followed_shop = []
            for followed_shop_item_data in _followed_shop:
                followed_shop_item = GetOffSiteAudienceInsightsResponseDataFollowedShop.from_dict(followed_shop_item_data)



                followed_shop.append(followed_shop_item)


        _gender = d.pop("gender", UNSET)
        gender: list[GetOffSiteAudienceInsightsResponseDataGender] | Unset = UNSET
        if _gender is not UNSET:
            gender = []
            for gender_item_data in _gender:
                gender_item = GetOffSiteAudienceInsightsResponseDataGender.from_dict(gender_item_data)



                gender.append(gender_item)


        _personas = d.pop("personas", UNSET)
        personas: list[GetOffSiteAudienceInsightsResponseDataPersona] | Unset = UNSET
        if _personas is not UNSET:
            personas = []
            for personas_item_data in _personas:
                personas_item = GetOffSiteAudienceInsightsResponseDataPersona.from_dict(personas_item_data)



                personas.append(personas_item)


        _region = d.pop("region", UNSET)
        region: list[GetOffSiteAudienceInsightsResponseDataRegion] | Unset = UNSET
        if _region is not UNSET:
            region = []
            for region_item_data in _region:
                region_item = GetOffSiteAudienceInsightsResponseDataRegion.from_dict(region_item_data)



                region.append(region_item)


        _top_favorite_content = d.pop("top_favorite_content", UNSET)
        top_favorite_content: list[GetOffSiteAudienceInsightsResponseDataTopFavoriteContent] | Unset = UNSET
        if _top_favorite_content is not UNSET:
            top_favorite_content = []
            for top_favorite_content_item_data in _top_favorite_content:
                top_favorite_content_item = GetOffSiteAudienceInsightsResponseDataTopFavoriteContent.from_dict(top_favorite_content_item_data)



                top_favorite_content.append(top_favorite_content_item)


        _top_purchase_category_preferences = d.pop("top_purchase_category_preferences", UNSET)
        top_purchase_category_preferences: list[GetOffSiteAudienceInsightsResponseDataTopPurchaseCategoryPreference] | Unset = UNSET
        if _top_purchase_category_preferences is not UNSET:
            top_purchase_category_preferences = []
            for top_purchase_category_preferences_item_data in _top_purchase_category_preferences:
                top_purchase_category_preferences_item = GetOffSiteAudienceInsightsResponseDataTopPurchaseCategoryPreference.from_dict(top_purchase_category_preferences_item_data)



                top_purchase_category_preferences.append(top_purchase_category_preferences_item)


        get_off_site_audience_insights_response_data = cls(
            age=age,
            consumption_level=consumption_level,
            followed_shop=followed_shop,
            gender=gender,
            personas=personas,
            region=region,
            top_favorite_content=top_favorite_content,
            top_purchase_category_preferences=top_purchase_category_preferences,
        )


        get_off_site_audience_insights_response_data.additional_properties = d
        return get_off_site_audience_insights_response_data

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
