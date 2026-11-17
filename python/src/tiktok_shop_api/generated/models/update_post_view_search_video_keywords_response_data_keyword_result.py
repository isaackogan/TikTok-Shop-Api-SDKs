from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdatePostViewSearchVideoKeywordsResponseDataKeywordResult")



@_attrs_define
class UpdatePostViewSearchVideoKeywordsResponseDataKeywordResult:
    """ 
        Attributes:
            error_code (str | Unset): Omitted on success. Possible values: INVALID_FORMAT: remove surrounding whitespace,
                commas and control characters. SENSITIVE_KEYWORD: choose compliant keywords. TOO_MANY_KEYWORDS: use at most 5.
                VALIDATION_UNAVAILABLE: query current keywords before deciding to resubmit. KEYWORD_RELATION_UPDATE_FAILED and
                STALE_IDEMPOTENT_REPLAY: query and reconcile the complete keyword set before submitting again.
                VIDEO_RELATION_LOCK_LOST: the outcome is uncertain; query current state and do not automatically retry.
                OPERATION_UNCONFIRMED: no more specific public reason is available; check current state and contact support with
                the request log ID without automatically retrying.
            error_message (str | Unset): Human-readable failure explanation and suggested action. Omitted on success. Use
                error_code for programmatic decisions.
            status (str | Unset): Business result: UNSPECIFIED means no known outcome; SUCCEEDED means completed;
                PARTIAL_FAILED means some changes failed; FAILED means the requested change failed.
     """

    error_code: str | Unset = UNSET
    error_message: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        error_code = self.error_code

        error_message = self.error_message

        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error_code = d.pop("error_code", UNSET)

        error_message = d.pop("error_message", UNSET)

        status = d.pop("status", UNSET)

        update_post_view_search_video_keywords_response_data_keyword_result = cls(
            error_code=error_code,
            error_message=error_message,
            status=status,
        )


        update_post_view_search_video_keywords_response_data_keyword_result.additional_properties = d
        return update_post_view_search_video_keywords_response_data_keyword_result

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
