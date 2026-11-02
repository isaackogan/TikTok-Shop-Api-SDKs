from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_acc_audience_overview_response_data_key_metric_acc import GetACCAudienceOverviewResponseDataKeyMetricAcc
  from ..models.get_acc_audience_overview_response_data_key_metric_awareness import GetACCAudienceOverviewResponseDataKeyMetricAwareness
  from ..models.get_acc_audience_overview_response_data_key_metric_consideration import GetACCAudienceOverviewResponseDataKeyMetricConsideration
  from ..models.get_acc_audience_overview_response_data_key_metric_conversion import GetACCAudienceOverviewResponseDataKeyMetricConversion
  from ..models.get_acc_audience_overview_response_data_key_metric_new_conversion import GetACCAudienceOverviewResponseDataKeyMetricNewConversion
  from ..models.get_acc_audience_overview_response_data_key_metric_repeat_conversion import GetACCAudienceOverviewResponseDataKeyMetricRepeatConversion





T = TypeVar("T", bound="GetACCAudienceOverviewResponseDataKeyMetric")



@_attrs_define
class GetACCAudienceOverviewResponseDataKeyMetric:
    """ 
        Attributes:
            acc (GetACCAudienceOverviewResponseDataKeyMetricAcc | Unset):
            awareness (GetACCAudienceOverviewResponseDataKeyMetricAwareness | Unset):
            consideration (GetACCAudienceOverviewResponseDataKeyMetricConsideration | Unset):
            conversion (GetACCAudienceOverviewResponseDataKeyMetricConversion | Unset):
            new_conversion (GetACCAudienceOverviewResponseDataKeyMetricNewConversion | Unset):
            repeat_conversion (GetACCAudienceOverviewResponseDataKeyMetricRepeatConversion | Unset):
     """

    acc: GetACCAudienceOverviewResponseDataKeyMetricAcc | Unset = UNSET
    awareness: GetACCAudienceOverviewResponseDataKeyMetricAwareness | Unset = UNSET
    consideration: GetACCAudienceOverviewResponseDataKeyMetricConsideration | Unset = UNSET
    conversion: GetACCAudienceOverviewResponseDataKeyMetricConversion | Unset = UNSET
    new_conversion: GetACCAudienceOverviewResponseDataKeyMetricNewConversion | Unset = UNSET
    repeat_conversion: GetACCAudienceOverviewResponseDataKeyMetricRepeatConversion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_acc_audience_overview_response_data_key_metric_acc import GetACCAudienceOverviewResponseDataKeyMetricAcc # noqa: PLC0415
        from ..models.get_acc_audience_overview_response_data_key_metric_awareness import GetACCAudienceOverviewResponseDataKeyMetricAwareness # noqa: PLC0415
        from ..models.get_acc_audience_overview_response_data_key_metric_consideration import GetACCAudienceOverviewResponseDataKeyMetricConsideration # noqa: PLC0415
        from ..models.get_acc_audience_overview_response_data_key_metric_conversion import GetACCAudienceOverviewResponseDataKeyMetricConversion # noqa: PLC0415
        from ..models.get_acc_audience_overview_response_data_key_metric_new_conversion import GetACCAudienceOverviewResponseDataKeyMetricNewConversion # noqa: PLC0415
        from ..models.get_acc_audience_overview_response_data_key_metric_repeat_conversion import GetACCAudienceOverviewResponseDataKeyMetricRepeatConversion # noqa: PLC0415
        acc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.acc, Unset):
            acc = self.acc.to_dict()

        awareness: dict[str, Any] | Unset = UNSET
        if not isinstance(self.awareness, Unset):
            awareness = self.awareness.to_dict()

        consideration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.consideration, Unset):
            consideration = self.consideration.to_dict()

        conversion: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conversion, Unset):
            conversion = self.conversion.to_dict()

        new_conversion: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_conversion, Unset):
            new_conversion = self.new_conversion.to_dict()

        repeat_conversion: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repeat_conversion, Unset):
            repeat_conversion = self.repeat_conversion.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if acc is not UNSET:
            field_dict["acc"] = acc
        if awareness is not UNSET:
            field_dict["awareness"] = awareness
        if consideration is not UNSET:
            field_dict["consideration"] = consideration
        if conversion is not UNSET:
            field_dict["conversion"] = conversion
        if new_conversion is not UNSET:
            field_dict["new_conversion"] = new_conversion
        if repeat_conversion is not UNSET:
            field_dict["repeat_conversion"] = repeat_conversion

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_acc_audience_overview_response_data_key_metric_acc import GetACCAudienceOverviewResponseDataKeyMetricAcc # noqa: PLC0415
        from ..models.get_acc_audience_overview_response_data_key_metric_awareness import GetACCAudienceOverviewResponseDataKeyMetricAwareness # noqa: PLC0415
        from ..models.get_acc_audience_overview_response_data_key_metric_consideration import GetACCAudienceOverviewResponseDataKeyMetricConsideration # noqa: PLC0415
        from ..models.get_acc_audience_overview_response_data_key_metric_conversion import GetACCAudienceOverviewResponseDataKeyMetricConversion # noqa: PLC0415
        from ..models.get_acc_audience_overview_response_data_key_metric_new_conversion import GetACCAudienceOverviewResponseDataKeyMetricNewConversion # noqa: PLC0415
        from ..models.get_acc_audience_overview_response_data_key_metric_repeat_conversion import GetACCAudienceOverviewResponseDataKeyMetricRepeatConversion # noqa: PLC0415
        d = dict(src_dict)
        _acc = d.pop("acc", UNSET)
        acc: GetACCAudienceOverviewResponseDataKeyMetricAcc | Unset
        if isinstance(_acc,  Unset):
            acc = UNSET
        else:
            acc = GetACCAudienceOverviewResponseDataKeyMetricAcc.from_dict(_acc)




        _awareness = d.pop("awareness", UNSET)
        awareness: GetACCAudienceOverviewResponseDataKeyMetricAwareness | Unset
        if isinstance(_awareness,  Unset):
            awareness = UNSET
        else:
            awareness = GetACCAudienceOverviewResponseDataKeyMetricAwareness.from_dict(_awareness)




        _consideration = d.pop("consideration", UNSET)
        consideration: GetACCAudienceOverviewResponseDataKeyMetricConsideration | Unset
        if isinstance(_consideration,  Unset):
            consideration = UNSET
        else:
            consideration = GetACCAudienceOverviewResponseDataKeyMetricConsideration.from_dict(_consideration)




        _conversion = d.pop("conversion", UNSET)
        conversion: GetACCAudienceOverviewResponseDataKeyMetricConversion | Unset
        if isinstance(_conversion,  Unset):
            conversion = UNSET
        else:
            conversion = GetACCAudienceOverviewResponseDataKeyMetricConversion.from_dict(_conversion)




        _new_conversion = d.pop("new_conversion", UNSET)
        new_conversion: GetACCAudienceOverviewResponseDataKeyMetricNewConversion | Unset
        if isinstance(_new_conversion,  Unset):
            new_conversion = UNSET
        else:
            new_conversion = GetACCAudienceOverviewResponseDataKeyMetricNewConversion.from_dict(_new_conversion)




        _repeat_conversion = d.pop("repeat_conversion", UNSET)
        repeat_conversion: GetACCAudienceOverviewResponseDataKeyMetricRepeatConversion | Unset
        if isinstance(_repeat_conversion,  Unset):
            repeat_conversion = UNSET
        else:
            repeat_conversion = GetACCAudienceOverviewResponseDataKeyMetricRepeatConversion.from_dict(_repeat_conversion)




        get_acc_audience_overview_response_data_key_metric = cls(
            acc=acc,
            awareness=awareness,
            consideration=consideration,
            conversion=conversion,
            new_conversion=new_conversion,
            repeat_conversion=repeat_conversion,
        )


        get_acc_audience_overview_response_data_key_metric.additional_properties = d
        return get_acc_audience_overview_response_data_key_metric

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
