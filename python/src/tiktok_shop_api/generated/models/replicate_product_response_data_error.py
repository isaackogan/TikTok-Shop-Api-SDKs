from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.replicate_product_response_data_error_detail import ReplicateProductResponseDataErrorDetail


T = TypeVar("T", bound="ReplicateProductResponseDataError")


@_attrs_define
class ReplicateProductResponseDataError:
    """
    Attributes:
        code (int | Unset): The error code.
        detail (ReplicateProductResponseDataErrorDetail | Unset):
        message (str | Unset): The error message.
    """

    code: int | Unset = UNSET
    detail: ReplicateProductResponseDataErrorDetail | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.detail, Unset):
            detail = self.detail.to_dict()

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if detail is not UNSET:
            field_dict["detail"] = detail
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.replicate_product_response_data_error_detail import (
            ReplicateProductResponseDataErrorDetail,  # noqa: PLC0415
        )

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        _detail = d.pop("detail", UNSET)
        detail: ReplicateProductResponseDataErrorDetail | Unset
        if isinstance(_detail, Unset):
            detail = UNSET
        else:
            detail = ReplicateProductResponseDataErrorDetail.from_dict(_detail)

        message = d.pop("message", UNSET)

        replicate_product_response_data_error = cls(
            code=code,
            detail=detail,
            message=message,
        )

        replicate_product_response_data_error.additional_properties = d
        return replicate_product_response_data_error

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
