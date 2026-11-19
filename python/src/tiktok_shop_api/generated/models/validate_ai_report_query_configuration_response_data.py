from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ValidateAIReportQueryConfigurationResponseData")



@_attrs_define
class ValidateAIReportQueryConfigurationResponseData:
    """ 
        Attributes:
            is_valid (bool | Unset): Whether the accepted request passed the business configuration checks. True means the
                checked combination passed; false means it was rejected, with reason_code and reason_message. This field is part
                of a successful validation response (code=0); malformed parameters or unknown catalog codes instead return a
                nonzero response code.
            reason_code (str | Unset): Reason the configuration was rejected. Returned when is_valid is false. Possible
                values: INVALID_METRIC: A metric code is not supported. Select a code from the catalog. DISABLED_METRIC: A
                selected metric is currently unavailable. Remove it or choose another metric. EMPTY_METRICS: No metrics were
                selected. Include at least one metric code. INVALID_DIMENSION: A dimension code is not supported. Select a code
                from the catalog. DUPLICATE_GROUP_BY: A grouping dimension appears more than once. Include each grouping
                dimension only once. INVALID_TIME_RANGE: The date range is invalid. Check the date format and the order of the
                start and end dates. INVALID_ORDER_BY: A sort rule is invalid. Use a selected metric, a selected dimension or
                time with a supported sort order. INVALID_QUERY_CONFIG: The query configuration is invalid. Review
                reason_message and correct the configuration. DIMENSION_CONFLICT: The selected metrics and dimensions cannot be
                combined. Choose a combination supported by the query rules. FILTER_REQUIRED: A required dimension filter is
                missing. Add a filter required by the matching rule group. TIME_LOOKBACK: The requested dates fall outside the
                supported lookback range. Choose a more recent date range. TIME_WINDOW: The date range exceeds the allowed
                number of days. Shorten the range. METRIC_DIM_BLOCKED: A selected metric prohibits a grouping or filter
                dimension. Remove the prohibited combination. INVALID_DETAIL_FIELD: A detail field code is not supported. Select
                a detail field from the catalog. DETAIL_FIELD_UNAVAILABLE: A detail field is unavailable for this configuration.
                Check the supported fields and required grouping dimensions. EXTERNAL_LIMIT_EXCEEDED: The selection exceeds an
                allowed limit. Reduce the number of selected items as described in reason_message. UNKNOWN_REASON: Validation
                was rejected for a reason not covered by the other codes. Use reason_message to identify the issue.
            reason_message (str | Unset): Explanation of why the query configuration was rejected and how to correct it.
                Returned when is_valid is false.
     """

    is_valid: bool | Unset = UNSET
    reason_code: str | Unset = UNSET
    reason_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        is_valid = self.is_valid

        reason_code = self.reason_code

        reason_message = self.reason_message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if is_valid is not UNSET:
            field_dict["is_valid"] = is_valid
        if reason_code is not UNSET:
            field_dict["reason_code"] = reason_code
        if reason_message is not UNSET:
            field_dict["reason_message"] = reason_message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_valid = d.pop("is_valid", UNSET)

        reason_code = d.pop("reason_code", UNSET)

        reason_message = d.pop("reason_message", UNSET)

        validate_ai_report_query_configuration_response_data = cls(
            is_valid=is_valid,
            reason_code=reason_code,
            reason_message=reason_message,
        )


        validate_ai_report_query_configuration_response_data.additional_properties = d
        return validate_ai_report_query_configuration_response_data

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
