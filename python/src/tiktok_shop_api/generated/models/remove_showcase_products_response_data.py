from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoveShowcaseProductsResponseData")


@_attrs_define
class RemoveShowcaseProductsResponseData:
    """
    Attributes:
        code (int | Unset): The success or failure status code returned in API response.
        message (str | Unset): The success or failure messages are returned in API response. Reasons of failure will be
            described in the message.
        request_id (str | Unset): Every request generates a unique request_id for logging purposes.
    """

    code: int | Unset = UNSET
    message: str | Unset = UNSET
    request_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        request_id = self.request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if request_id is not UNSET:
            field_dict["request_id"] = request_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        request_id = d.pop("request_id", UNSET)

        remove_showcase_products_response_data = cls(
            code=code,
            message=message,
            request_id=request_id,
        )

        remove_showcase_products_response_data.additional_properties = d
        return remove_showcase_products_response_data

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
