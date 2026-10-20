from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SearchCreatorsInCreatorMarketplaceResponseDataCreatorCreatorProfile")



@_attrs_define
class SearchCreatorsInCreatorMarketplaceResponseDataCreatorCreatorProfile:
    """ 
        Attributes:
            is_official_recommend (bool | Unset): Creator has official recommend tag or not
            creator_bind_mcn_name (str | Unset): Creator bind MCN name
            is_fast_growing (bool | Unset): Creator has fast growing tag or not
            has_collaborated (bool | Unset): Has collaborated with this creator or not
            user_type_tag (list[int] | Unset): User type tag.
                Possible values:
                - 1: Privacy creator
                - 2: Carve-out creator
            has_invited_90d (bool | Unset): Has invited creaor before 90 days
            is_creator_blocked (bool | Unset): Is this creator blocked by shop or not
            pps_score (str | Unset): Creator promotion performance score(PPS).The score reflects the quality of a creator's
                shoppable content and product selection over the past 30 days. A high score may indicate a better shopping
                experience, with fewer potential refunds or negative reviews. e.g. 4.3/5.0
            is_eligible_flat_fee (bool | Unset): Is creator eligible for flat fee, only available for US local seller
            is_rising_star (bool | Unset): Creator has rising star tag or not
            creator_level (int | Unset): Creator level
     """

    is_official_recommend: bool | Unset = UNSET
    creator_bind_mcn_name: str | Unset = UNSET
    is_fast_growing: bool | Unset = UNSET
    has_collaborated: bool | Unset = UNSET
    user_type_tag: list[int] | Unset = UNSET
    has_invited_90d: bool | Unset = UNSET
    is_creator_blocked: bool | Unset = UNSET
    pps_score: str | Unset = UNSET
    is_eligible_flat_fee: bool | Unset = UNSET
    is_rising_star: bool | Unset = UNSET
    creator_level: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        is_official_recommend = self.is_official_recommend

        creator_bind_mcn_name = self.creator_bind_mcn_name

        is_fast_growing = self.is_fast_growing

        has_collaborated = self.has_collaborated

        user_type_tag: list[int] | Unset = UNSET
        if not isinstance(self.user_type_tag, Unset):
            user_type_tag = self.user_type_tag



        has_invited_90d = self.has_invited_90d

        is_creator_blocked = self.is_creator_blocked

        pps_score = self.pps_score

        is_eligible_flat_fee = self.is_eligible_flat_fee

        is_rising_star = self.is_rising_star

        creator_level = self.creator_level


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if is_official_recommend is not UNSET:
            field_dict["is_official_recommend"] = is_official_recommend
        if creator_bind_mcn_name is not UNSET:
            field_dict["creator_bind_mcn_name"] = creator_bind_mcn_name
        if is_fast_growing is not UNSET:
            field_dict["is_fast_growing"] = is_fast_growing
        if has_collaborated is not UNSET:
            field_dict["has_collaborated"] = has_collaborated
        if user_type_tag is not UNSET:
            field_dict["user_type_tag"] = user_type_tag
        if has_invited_90d is not UNSET:
            field_dict["has_invited_90d"] = has_invited_90d
        if is_creator_blocked is not UNSET:
            field_dict["is_creator_blocked"] = is_creator_blocked
        if pps_score is not UNSET:
            field_dict["pps_score"] = pps_score
        if is_eligible_flat_fee is not UNSET:
            field_dict["is_eligible_flat_fee"] = is_eligible_flat_fee
        if is_rising_star is not UNSET:
            field_dict["is_rising_star"] = is_rising_star
        if creator_level is not UNSET:
            field_dict["creator_level"] = creator_level

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_official_recommend = d.pop("is_official_recommend", UNSET)

        creator_bind_mcn_name = d.pop("creator_bind_mcn_name", UNSET)

        is_fast_growing = d.pop("is_fast_growing", UNSET)

        has_collaborated = d.pop("has_collaborated", UNSET)

        user_type_tag = cast(list[int], d.pop("user_type_tag", UNSET))


        has_invited_90d = d.pop("has_invited_90d", UNSET)

        is_creator_blocked = d.pop("is_creator_blocked", UNSET)

        pps_score = d.pop("pps_score", UNSET)

        is_eligible_flat_fee = d.pop("is_eligible_flat_fee", UNSET)

        is_rising_star = d.pop("is_rising_star", UNSET)

        creator_level = d.pop("creator_level", UNSET)

        search_creators_in_creator_marketplace_response_data_creator_creator_profile = cls(
            is_official_recommend=is_official_recommend,
            creator_bind_mcn_name=creator_bind_mcn_name,
            is_fast_growing=is_fast_growing,
            has_collaborated=has_collaborated,
            user_type_tag=user_type_tag,
            has_invited_90d=has_invited_90d,
            is_creator_blocked=is_creator_blocked,
            pps_score=pps_score,
            is_eligible_flat_fee=is_eligible_flat_fee,
            is_rising_star=is_rising_star,
            creator_level=creator_level,
        )


        search_creators_in_creator_marketplace_response_data_creator_creator_profile.additional_properties = d
        return search_creators_in_creator_marketplace_response_data_creator_creator_profile

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
