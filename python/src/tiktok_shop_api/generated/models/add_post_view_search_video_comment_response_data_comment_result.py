from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AddPostViewSearchVideoCommentResponseDataCommentResult")



@_attrs_define
class AddPostViewSearchVideoCommentResponseDataCommentResult:
    """ 
        Attributes:
            comment_id (str | Unset): Unique comment id.
            error_code (str | Unset): Omitted on success. Possible values: COMMENT_PUBLISH_FAILED: publication could not be
                confirmed; inspect recent comments without automatically resubmitting. COMMENT_PUBLISHER_USER_ID_REQUIRED:
                author resolution failed; contact support with the request log ID. VIDEO_RELATION_LOCK_LOST: the outcome is
                uncertain; do not automatically resubmit. OPERATION_UNCONFIRMED: no more specific public reason is available;
                inspect recent comments and contact support with the request log ID without automatically retrying.
            error_message (str | Unset): Human-readable failure explanation and suggested action. Omitted on success. Use
                error_code for programmatic decisions.
            status (str | Unset): Business result: UNSPECIFIED means no known outcome; SUCCEEDED means completed;
                PARTIAL_FAILED means some changes failed; FAILED means the requested change failed.
     """

    comment_id: str | Unset = UNSET
    error_code: str | Unset = UNSET
    error_message: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        comment_id = self.comment_id

        error_code = self.error_code

        error_message = self.error_message

        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if comment_id is not UNSET:
            field_dict["comment_id"] = comment_id
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
        comment_id = d.pop("comment_id", UNSET)

        error_code = d.pop("error_code", UNSET)

        error_message = d.pop("error_message", UNSET)

        status = d.pop("status", UNSET)

        add_post_view_search_video_comment_response_data_comment_result = cls(
            comment_id=comment_id,
            error_code=error_code,
            error_message=error_message,
            status=status,
        )


        add_post_view_search_video_comment_response_data_comment_result.additional_properties = d
        return add_post_view_search_video_comment_response_data_comment_result

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
