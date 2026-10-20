from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_sps_overview_response_data_benefit import GetSPSOverviewResponseDataBenefit
    from ..models.get_sps_overview_response_data_dimension import GetSPSOverviewResponseDataDimension
    from ..models.get_sps_overview_response_data_primary_category import GetSPSOverviewResponseDataPrimaryCategory
    from ..models.get_sps_overview_response_data_top_issue import GetSPSOverviewResponseDataTopIssue


T = TypeVar("T", bound="GetSPSOverviewResponseData")


@_attrs_define
class GetSPSOverviewResponseData:
    """
    Attributes:
        benefits (list[GetSPSOverviewResponseDataBenefit] | Unset): Fixed complete set of benefits associated with the
            shop SPS score.
        dimensions (list[GetSPSOverviewResponseDataDimension] | Unset): Score details by SPS dimension.
        evaluate_duration_days (int | Unset): The number of days included in the score evaluation period.
        end_evaluation_time (int | Unset): The evaluation period end time. Unix timestamp in seconds.
        start_evaluation_time (int | Unset): The evaluation period start time. Unix timestamp in seconds.
        peer_percentile (str | Unset): The shop's percentile among peers, from 0 to 100.
        primary_category (GetSPSOverviewResponseDataPrimaryCategory | Unset):
        sps_score (str | Unset): The shop SPS score, from 0 to 5 with one decimal place.
        sps_tier (str | Unset): The SPS tier. Possible values include EXCELLENT, GOOD, POOR, CRITICAL and NIL.
        sps_tier_text (str | Unset): The SPS tier. Values like Excellent, Good, Normal, Attention.
        top_issues (GetSPSOverviewResponseDataTopIssue | Unset):
        update_time (int | Unset): The latest score refresh time. Unix timestamp in seconds.
    """

    benefits: list[GetSPSOverviewResponseDataBenefit] | Unset = UNSET
    dimensions: list[GetSPSOverviewResponseDataDimension] | Unset = UNSET
    evaluate_duration_days: int | Unset = UNSET
    end_evaluation_time: int | Unset = UNSET
    start_evaluation_time: int | Unset = UNSET
    peer_percentile: str | Unset = UNSET
    primary_category: GetSPSOverviewResponseDataPrimaryCategory | Unset = UNSET
    sps_score: str | Unset = UNSET
    sps_tier: str | Unset = UNSET
    sps_tier_text: str | Unset = UNSET
    top_issues: GetSPSOverviewResponseDataTopIssue | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        benefits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.benefits, Unset):
            benefits = []
            for benefits_item_data in self.benefits:
                benefits_item = benefits_item_data.to_dict()
                benefits.append(benefits_item)

        dimensions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = []
            for dimensions_item_data in self.dimensions:
                dimensions_item = dimensions_item_data.to_dict()
                dimensions.append(dimensions_item)

        evaluate_duration_days = self.evaluate_duration_days

        end_evaluation_time = self.end_evaluation_time

        start_evaluation_time = self.start_evaluation_time

        peer_percentile = self.peer_percentile

        primary_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary_category, Unset):
            primary_category = self.primary_category.to_dict()

        sps_score = self.sps_score

        sps_tier = self.sps_tier

        sps_tier_text = self.sps_tier_text

        top_issues: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top_issues, Unset):
            top_issues = self.top_issues.to_dict()

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if benefits is not UNSET:
            field_dict["benefits"] = benefits
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if evaluate_duration_days is not UNSET:
            field_dict["evaluate_duration_days"] = evaluate_duration_days
        if end_evaluation_time is not UNSET:
            field_dict["end_evaluation_time"] = end_evaluation_time
        if start_evaluation_time is not UNSET:
            field_dict["start_evaluation_time"] = start_evaluation_time
        if peer_percentile is not UNSET:
            field_dict["peer_percentile"] = peer_percentile
        if primary_category is not UNSET:
            field_dict["primary_category"] = primary_category
        if sps_score is not UNSET:
            field_dict["sps_score"] = sps_score
        if sps_tier is not UNSET:
            field_dict["sps_tier"] = sps_tier
        if sps_tier_text is not UNSET:
            field_dict["sps_tier_text"] = sps_tier_text
        if top_issues is not UNSET:
            field_dict["top_issues"] = top_issues
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_sps_overview_response_data_benefit import GetSPSOverviewResponseDataBenefit  # noqa: PLC0415
        from ..models.get_sps_overview_response_data_dimension import (
            GetSPSOverviewResponseDataDimension,  # noqa: PLC0415
        )
        from ..models.get_sps_overview_response_data_primary_category import (
            GetSPSOverviewResponseDataPrimaryCategory,  # noqa: PLC0415
        )
        from ..models.get_sps_overview_response_data_top_issue import (
            GetSPSOverviewResponseDataTopIssue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _benefits = d.pop("benefits", UNSET)
        benefits: list[GetSPSOverviewResponseDataBenefit] | Unset = UNSET
        if _benefits is not UNSET:
            benefits = []
            for benefits_item_data in _benefits:
                benefits_item = GetSPSOverviewResponseDataBenefit.from_dict(benefits_item_data)

                benefits.append(benefits_item)

        _dimensions = d.pop("dimensions", UNSET)
        dimensions: list[GetSPSOverviewResponseDataDimension] | Unset = UNSET
        if _dimensions is not UNSET:
            dimensions = []
            for dimensions_item_data in _dimensions:
                dimensions_item = GetSPSOverviewResponseDataDimension.from_dict(dimensions_item_data)

                dimensions.append(dimensions_item)

        evaluate_duration_days = d.pop("evaluate_duration_days", UNSET)

        end_evaluation_time = d.pop("end_evaluation_time", UNSET)

        start_evaluation_time = d.pop("start_evaluation_time", UNSET)

        peer_percentile = d.pop("peer_percentile", UNSET)

        _primary_category = d.pop("primary_category", UNSET)
        primary_category: GetSPSOverviewResponseDataPrimaryCategory | Unset
        if isinstance(_primary_category, Unset):
            primary_category = UNSET
        else:
            primary_category = GetSPSOverviewResponseDataPrimaryCategory.from_dict(_primary_category)

        sps_score = d.pop("sps_score", UNSET)

        sps_tier = d.pop("sps_tier", UNSET)

        sps_tier_text = d.pop("sps_tier_text", UNSET)

        _top_issues = d.pop("top_issues", UNSET)
        top_issues: GetSPSOverviewResponseDataTopIssue | Unset
        if isinstance(_top_issues, Unset):
            top_issues = UNSET
        else:
            top_issues = GetSPSOverviewResponseDataTopIssue.from_dict(_top_issues)

        update_time = d.pop("update_time", UNSET)

        get_sps_overview_response_data = cls(
            benefits=benefits,
            dimensions=dimensions,
            evaluate_duration_days=evaluate_duration_days,
            end_evaluation_time=end_evaluation_time,
            start_evaluation_time=start_evaluation_time,
            peer_percentile=peer_percentile,
            primary_category=primary_category,
            sps_score=sps_score,
            sps_tier=sps_tier,
            sps_tier_text=sps_tier_text,
            top_issues=top_issues,
            update_time=update_time,
        )

        get_sps_overview_response_data.additional_properties = d
        return get_sps_overview_response_data

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
