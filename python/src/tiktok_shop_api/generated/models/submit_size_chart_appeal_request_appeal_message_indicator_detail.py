from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.submit_size_chart_appeal_request_appeal_message_indicator_detail_indicator_type import SubmitSizeChartAppealRequestAppealMessageIndicatorDetailIndicatorType






T = TypeVar("T", bound="SubmitSizeChartAppealRequestAppealMessageIndicatorDetail")



@_attrs_define
class SubmitSizeChartAppealRequestAppealMessageIndicatorDetail:
    """ 
        Attributes:
            indicator_type (SubmitSizeChartAppealRequestAppealMessageIndicatorDetailIndicatorType): The target
                indicator_type to appeal of this field.
                Possible values:
                - REQUIRED_DIMENSION：Does the size chart include all required dimensions?
                - CONTAINS_ALL_SALE_PROPERTY：Does the size chart cover all sales attributes?""
                - VALUE_RANGE_OUT_OF_RANGE：Are the value ranges in the size chart valid?
     """

    indicator_type: SubmitSizeChartAppealRequestAppealMessageIndicatorDetailIndicatorType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        indicator_type = self.indicator_type.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "indicator_type": indicator_type,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        indicator_type = SubmitSizeChartAppealRequestAppealMessageIndicatorDetailIndicatorType(d.pop("indicator_type"))




        submit_size_chart_appeal_request_appeal_message_indicator_detail = cls(
            indicator_type=indicator_type,
        )


        submit_size_chart_appeal_request_appeal_message_indicator_detail.additional_properties = d
        return submit_size_chart_appeal_request_appeal_message_indicator_detail

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
