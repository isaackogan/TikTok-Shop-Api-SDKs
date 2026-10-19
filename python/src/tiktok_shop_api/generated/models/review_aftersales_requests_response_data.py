from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_available_review_decisions_response_data_error import GetAvailableReviewDecisionsResponseDataError


T = TypeVar("T", bound="ReviewAftersalesRequestsResponseData")


@_attrs_define
class ReviewAftersalesRequestsResponseData:
    """
    Attributes:
        errors (list[GetAvailableReviewDecisionsResponseDataError] | Unset): Lists errors for partially failed requests.
            For example, if a request reviews multiple orders or items and only some fail, individual error details are
            returned here.

            **IMPORTANT**: Partial failures still return a top-level success code (0), so clients must also check this field
            to detect partial errors. For complete failures (e.g. validation errors), the top-level response code and
            message will indicate a failure, but this field will remain empty.
    """

    errors: list[GetAvailableReviewDecisionsResponseDataError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_available_review_decisions_response_data_error import (
            GetAvailableReviewDecisionsResponseDataError,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[GetAvailableReviewDecisionsResponseDataError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = GetAvailableReviewDecisionsResponseDataError.from_dict(errors_item_data)

                errors.append(errors_item)

        review_aftersales_requests_response_data = cls(
            errors=errors,
        )

        review_aftersales_requests_response_data.additional_properties = d
        return review_aftersales_requests_response_data

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
