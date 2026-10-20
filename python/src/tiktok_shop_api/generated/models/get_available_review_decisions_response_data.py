from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_available_review_decisions_response_data_error import GetAvailableReviewDecisionsResponseDataError
  from ..models.get_available_review_decisions_response_data_line_item import GetAvailableReviewDecisionsResponseDataLineItem





T = TypeVar("T", bound="GetAvailableReviewDecisionsResponseData")



@_attrs_define
class GetAvailableReviewDecisionsResponseData:
    """ 
        Attributes:
            line_items (list[GetAvailableReviewDecisionsResponseDataLineItem] | Unset): Line items to which the returned
                decisions apply. Decision details apply to each line item individually. For example, a partial refund amount of
                1.00 for each of three line items results in a total of 3.00; use the `currency` returned with the amount range
                rather than assuming a currency.
            request_log_id (str | Unset): The log id of this request, used for troubleshooting with TikTok Shop support.
            errors (list[GetAvailableReviewDecisionsResponseDataError] | Unset): Lists errors for partially failed requests.
                For example, if a request reviews multiple orders or items and only some fail, individual error details are
                returned here.
                **IMPORTANT**: Partial failures still return a top-level success code (0), so clients must also check this field
                to detect partial errors. For complete failures (e.g. validation errors), the top-level response code and
                message will indicate a failure, but this field will remain empty.
     """

    line_items: list[GetAvailableReviewDecisionsResponseDataLineItem] | Unset = UNSET
    request_log_id: str | Unset = UNSET
    errors: list[GetAvailableReviewDecisionsResponseDataError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_available_review_decisions_response_data_error import GetAvailableReviewDecisionsResponseDataError # noqa: PLC0415
        from ..models.get_available_review_decisions_response_data_line_item import GetAvailableReviewDecisionsResponseDataLineItem # noqa: PLC0415
        line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)



        request_log_id = self.request_log_id

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if line_items is not UNSET:
            field_dict["line_items"] = line_items
        if request_log_id is not UNSET:
            field_dict["request_log_id"] = request_log_id
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_available_review_decisions_response_data_error import GetAvailableReviewDecisionsResponseDataError # noqa: PLC0415
        from ..models.get_available_review_decisions_response_data_line_item import GetAvailableReviewDecisionsResponseDataLineItem # noqa: PLC0415
        d = dict(src_dict)
        _line_items = d.pop("line_items", UNSET)
        line_items: list[GetAvailableReviewDecisionsResponseDataLineItem] | Unset = UNSET
        if _line_items is not UNSET:
            line_items = []
            for line_items_item_data in _line_items:
                line_items_item = GetAvailableReviewDecisionsResponseDataLineItem.from_dict(line_items_item_data)



                line_items.append(line_items_item)


        request_log_id = d.pop("request_log_id", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[GetAvailableReviewDecisionsResponseDataError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = GetAvailableReviewDecisionsResponseDataError.from_dict(errors_item_data)



                errors.append(errors_item)


        get_available_review_decisions_response_data = cls(
            line_items=line_items,
            request_log_id=request_log_id,
            errors=errors,
        )


        get_available_review_decisions_response_data.additional_properties = d
        return get_available_review_decisions_response_data

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
