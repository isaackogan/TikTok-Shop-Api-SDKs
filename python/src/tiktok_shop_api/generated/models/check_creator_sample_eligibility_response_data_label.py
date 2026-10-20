from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.check_creator_sample_eligibility_response_data_label_sample_product import CheckCreatorSampleEligibilityResponseDataLabelSampleProduct





T = TypeVar("T", bound="CheckCreatorSampleEligibilityResponseDataLabel")



@_attrs_define
class CheckCreatorSampleEligibilityResponseDataLabel:
    """ 
        Attributes:
            can_apply (bool | Unset): Whether the authenticated creator can apply for a sample of the specified product.
            status (str | Unset): Status indicating whether the creator has applied for a free sample of the specified
                product.
                - UNKNOWN: The application status is unknown.
                - TO_APPLY: The creator has not applied for a free sample of the product.
                - ONGOING: The creator has applied for a free sample but has not completed sample fulfillment.
                - COMPLETE: The creator has applied for a free sample and completed sample fulfillment.
            application_id (str | Unset): Sample Application ID. only appear when the creator has already applied this
                product.
            reach_limit (bool | Unset): If the creator has reached the sample application upper limit.
            sample_product (CheckCreatorSampleEligibilityResponseDataLabelSampleProduct | Unset):
     """

    can_apply: bool | Unset = UNSET
    status: str | Unset = UNSET
    application_id: str | Unset = UNSET
    reach_limit: bool | Unset = UNSET
    sample_product: CheckCreatorSampleEligibilityResponseDataLabelSampleProduct | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.check_creator_sample_eligibility_response_data_label_sample_product import CheckCreatorSampleEligibilityResponseDataLabelSampleProduct # noqa: PLC0415
        can_apply = self.can_apply

        status = self.status

        application_id = self.application_id

        reach_limit = self.reach_limit

        sample_product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sample_product, Unset):
            sample_product = self.sample_product.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if can_apply is not UNSET:
            field_dict["can_apply"] = can_apply
        if status is not UNSET:
            field_dict["status"] = status
        if application_id is not UNSET:
            field_dict["application_id"] = application_id
        if reach_limit is not UNSET:
            field_dict["reach_limit"] = reach_limit
        if sample_product is not UNSET:
            field_dict["sample_product"] = sample_product

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_creator_sample_eligibility_response_data_label_sample_product import CheckCreatorSampleEligibilityResponseDataLabelSampleProduct # noqa: PLC0415
        d = dict(src_dict)
        can_apply = d.pop("can_apply", UNSET)

        status = d.pop("status", UNSET)

        application_id = d.pop("application_id", UNSET)

        reach_limit = d.pop("reach_limit", UNSET)

        _sample_product = d.pop("sample_product", UNSET)
        sample_product: CheckCreatorSampleEligibilityResponseDataLabelSampleProduct | Unset
        if isinstance(_sample_product,  Unset):
            sample_product = UNSET
        else:
            sample_product = CheckCreatorSampleEligibilityResponseDataLabelSampleProduct.from_dict(_sample_product)




        check_creator_sample_eligibility_response_data_label = cls(
            can_apply=can_apply,
            status=status,
            application_id=application_id,
            reach_limit=reach_limit,
            sample_product=sample_product,
        )


        check_creator_sample_eligibility_response_data_label.additional_properties = d
        return check_creator_sample_eligibility_response_data_label

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
