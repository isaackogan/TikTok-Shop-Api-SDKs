from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.check_creator_outreach_eligibility_response_data_creator_eligibility_result import CheckCreatorOutreachEligibilityResponseDataCreatorEligibilityResult





T = TypeVar("T", bound="CheckCreatorOutreachEligibilityResponseData")



@_attrs_define
class CheckCreatorOutreachEligibilityResponseData:
    """ 
        Attributes:
            creator_eligibility_results (list[CheckCreatorOutreachEligibilityResponseDataCreatorEligibilityResult] | Unset):
                Per-creator raw connection and quota eligibility facts.
            ineligible_creator_levels (list[int] | Unset): Creator levels that prevent quota consumption for the full
                requested batch. This is an empty array when no creator level prevents quota consumption.
            is_batch_quota_consumable (bool | Unset): Whether quota can be consumed for the full requested creator batch.
     """

    creator_eligibility_results: list[CheckCreatorOutreachEligibilityResponseDataCreatorEligibilityResult] | Unset = UNSET
    ineligible_creator_levels: list[int] | Unset = UNSET
    is_batch_quota_consumable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.check_creator_outreach_eligibility_response_data_creator_eligibility_result import CheckCreatorOutreachEligibilityResponseDataCreatorEligibilityResult # noqa: PLC0415
        creator_eligibility_results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creator_eligibility_results, Unset):
            creator_eligibility_results = []
            for creator_eligibility_results_item_data in self.creator_eligibility_results:
                creator_eligibility_results_item = creator_eligibility_results_item_data.to_dict()
                creator_eligibility_results.append(creator_eligibility_results_item)



        ineligible_creator_levels: list[int] | Unset = UNSET
        if not isinstance(self.ineligible_creator_levels, Unset):
            ineligible_creator_levels = self.ineligible_creator_levels



        is_batch_quota_consumable = self.is_batch_quota_consumable


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if creator_eligibility_results is not UNSET:
            field_dict["creator_eligibility_results"] = creator_eligibility_results
        if ineligible_creator_levels is not UNSET:
            field_dict["ineligible_creator_levels"] = ineligible_creator_levels
        if is_batch_quota_consumable is not UNSET:
            field_dict["is_batch_quota_consumable"] = is_batch_quota_consumable

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_creator_outreach_eligibility_response_data_creator_eligibility_result import CheckCreatorOutreachEligibilityResponseDataCreatorEligibilityResult # noqa: PLC0415
        d = dict(src_dict)
        _creator_eligibility_results = d.pop("creator_eligibility_results", UNSET)
        creator_eligibility_results: list[CheckCreatorOutreachEligibilityResponseDataCreatorEligibilityResult] | Unset = UNSET
        if _creator_eligibility_results is not UNSET:
            creator_eligibility_results = []
            for creator_eligibility_results_item_data in _creator_eligibility_results:
                creator_eligibility_results_item = CheckCreatorOutreachEligibilityResponseDataCreatorEligibilityResult.from_dict(creator_eligibility_results_item_data)



                creator_eligibility_results.append(creator_eligibility_results_item)


        ineligible_creator_levels = cast(list[int], d.pop("ineligible_creator_levels", UNSET))


        is_batch_quota_consumable = d.pop("is_batch_quota_consumable", UNSET)

        check_creator_outreach_eligibility_response_data = cls(
            creator_eligibility_results=creator_eligibility_results,
            ineligible_creator_levels=ineligible_creator_levels,
            is_batch_quota_consumable=is_batch_quota_consumable,
        )


        check_creator_outreach_eligibility_response_data.additional_properties = d
        return check_creator_outreach_eligibility_response_data

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
