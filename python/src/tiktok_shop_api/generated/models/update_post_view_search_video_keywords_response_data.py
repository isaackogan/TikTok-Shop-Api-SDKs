from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_post_view_search_video_keywords_response_data_keyword_result import UpdatePostViewSearchVideoKeywordsResponseDataKeywordResult





T = TypeVar("T", bound="UpdatePostViewSearchVideoKeywordsResponseData")



@_attrs_define
class UpdatePostViewSearchVideoKeywordsResponseData:
    """ 
        Attributes:
            keyword_result (UpdatePostViewSearchVideoKeywordsResponseDataKeywordResult | Unset):
            request_id (str | Unset): Server-generated submission identifier, in openapi-<UUID v4> format. A new value is
                generated for every invocation; it is not an idempotency key. Distinct from the request log ID in the response
                envelope.
     """

    keyword_result: UpdatePostViewSearchVideoKeywordsResponseDataKeywordResult | Unset = UNSET
    request_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_post_view_search_video_keywords_response_data_keyword_result import UpdatePostViewSearchVideoKeywordsResponseDataKeywordResult # noqa: PLC0415
        keyword_result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.keyword_result, Unset):
            keyword_result = self.keyword_result.to_dict()

        request_id = self.request_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if keyword_result is not UNSET:
            field_dict["keyword_result"] = keyword_result
        if request_id is not UNSET:
            field_dict["request_id"] = request_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_post_view_search_video_keywords_response_data_keyword_result import UpdatePostViewSearchVideoKeywordsResponseDataKeywordResult # noqa: PLC0415
        d = dict(src_dict)
        _keyword_result = d.pop("keyword_result", UNSET)
        keyword_result: UpdatePostViewSearchVideoKeywordsResponseDataKeywordResult | Unset
        if isinstance(_keyword_result,  Unset):
            keyword_result = UNSET
        else:
            keyword_result = UpdatePostViewSearchVideoKeywordsResponseDataKeywordResult.from_dict(_keyword_result)




        request_id = d.pop("request_id", UNSET)

        update_post_view_search_video_keywords_response_data = cls(
            keyword_result=keyword_result,
            request_id=request_id,
        )


        update_post_view_search_video_keywords_response_data.additional_properties = d
        return update_post_view_search_video_keywords_response_data

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
