from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.submit_size_chart_appeal_request_appeal_message_field_name import SubmitSizeChartAppealRequestAppealMessageFieldName
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.submit_size_chart_appeal_request_appeal_message_indicator_detail import SubmitSizeChartAppealRequestAppealMessageIndicatorDetail





T = TypeVar("T", bound="SubmitSizeChartAppealRequestAppealMessage")



@_attrs_define
class SubmitSizeChartAppealRequestAppealMessage:
    """ 
        Attributes:
            field_name (SubmitSizeChartAppealRequestAppealMessageFieldName): The target fields to appeal.
                Possible values:
                - APPEAL_MESSAGE_FIELD_SIZE_CHART
            indicator_details (list[SubmitSizeChartAppealRequestAppealMessageIndicatorDetail]): Indicator details of the
                products submitted for appeal
            size_chart_id (str | Unset): size_chart_id
            size_chart_image_uri (str | Unset): uri of size_chart_image
     """

    field_name: SubmitSizeChartAppealRequestAppealMessageFieldName
    indicator_details: list[SubmitSizeChartAppealRequestAppealMessageIndicatorDetail]
    size_chart_id: str | Unset = UNSET
    size_chart_image_uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.submit_size_chart_appeal_request_appeal_message_indicator_detail import SubmitSizeChartAppealRequestAppealMessageIndicatorDetail # noqa: PLC0415
        field_name = self.field_name.value

        indicator_details = []
        for indicator_details_item_data in self.indicator_details:
            indicator_details_item = indicator_details_item_data.to_dict()
            indicator_details.append(indicator_details_item)



        size_chart_id = self.size_chart_id

        size_chart_image_uri = self.size_chart_image_uri


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "field_name": field_name,
            "indicator_details": indicator_details,
        })
        if size_chart_id is not UNSET:
            field_dict["size_chart_id"] = size_chart_id
        if size_chart_image_uri is not UNSET:
            field_dict["size_chart_image_uri"] = size_chart_image_uri

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_size_chart_appeal_request_appeal_message_indicator_detail import SubmitSizeChartAppealRequestAppealMessageIndicatorDetail # noqa: PLC0415
        d = dict(src_dict)
        field_name = SubmitSizeChartAppealRequestAppealMessageFieldName(d.pop("field_name"))




        indicator_details = []
        _indicator_details = d.pop("indicator_details")
        for indicator_details_item_data in (_indicator_details):
            indicator_details_item = SubmitSizeChartAppealRequestAppealMessageIndicatorDetail.from_dict(indicator_details_item_data)



            indicator_details.append(indicator_details_item)


        size_chart_id = d.pop("size_chart_id", UNSET)

        size_chart_image_uri = d.pop("size_chart_image_uri", UNSET)

        submit_size_chart_appeal_request_appeal_message = cls(
            field_name=field_name,
            indicator_details=indicator_details,
            size_chart_id=size_chart_id,
            size_chart_image_uri=size_chart_image_uri,
        )


        submit_size_chart_appeal_request_appeal_message.additional_properties = d
        return submit_size_chart_appeal_request_appeal_message

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
