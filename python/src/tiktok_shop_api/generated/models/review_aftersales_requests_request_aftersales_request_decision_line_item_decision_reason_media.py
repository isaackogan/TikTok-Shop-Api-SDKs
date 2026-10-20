from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionReasonMedia")



@_attrs_define
class ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionReasonMedia:
    """ 
        Attributes:
            uri (str | Unset): Image URI obtained from the [Upload Product
                Image](https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22) API.
            mime_type (str | Unset): MIME type of the media (such as image/jpeg).
     """

    uri: str | Unset = UNSET
    mime_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        uri = self.uri

        mime_type = self.mime_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if uri is not UNSET:
            field_dict["uri"] = uri
        if mime_type is not UNSET:
            field_dict["mime_type"] = mime_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uri = d.pop("uri", UNSET)

        mime_type = d.pop("mime_type", UNSET)

        review_aftersales_requests_request_aftersales_request_decision_line_item_decision_reason_media = cls(
            uri=uri,
            mime_type=mime_type,
        )


        review_aftersales_requests_request_aftersales_request_decision_line_item_decision_reason_media.additional_properties = d
        return review_aftersales_requests_request_aftersales_request_decision_line_item_decision_reason_media

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
