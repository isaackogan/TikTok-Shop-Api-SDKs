from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.check_creator_sample_eligibility_response_data_label import CheckCreatorSampleEligibilityResponseDataLabel





T = TypeVar("T", bound="CheckCreatorSampleEligibilityResponseData")



@_attrs_define
class CheckCreatorSampleEligibilityResponseData:
    """ 
        Attributes:
            label (CheckCreatorSampleEligibilityResponseDataLabel | Unset):
     """

    label: CheckCreatorSampleEligibilityResponseDataLabel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.check_creator_sample_eligibility_response_data_label import CheckCreatorSampleEligibilityResponseDataLabel # noqa: PLC0415
        label: dict[str, Any] | Unset = UNSET
        if not isinstance(self.label, Unset):
            label = self.label.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_creator_sample_eligibility_response_data_label import CheckCreatorSampleEligibilityResponseDataLabel # noqa: PLC0415
        d = dict(src_dict)
        _label = d.pop("label", UNSET)
        label: CheckCreatorSampleEligibilityResponseDataLabel | Unset
        if isinstance(_label,  Unset):
            label = UNSET
        else:
            label = CheckCreatorSampleEligibilityResponseDataLabel.from_dict(_label)




        check_creator_sample_eligibility_response_data = cls(
            label=label,
        )


        check_creator_sample_eligibility_response_data.additional_properties = d
        return check_creator_sample_eligibility_response_data

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
