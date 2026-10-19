from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delete_global_products_response_data_error_detail import DeleteGlobalProductsResponseDataErrorDetail


T = TypeVar("T", bound="DeleteGlobalProductsResponseDataError")


@_attrs_define
class DeleteGlobalProductsResponseDataError:
    """
    Attributes:
        message (str | Unset): The error message.
        code (int | Unset): The error code.
        detail (DeleteGlobalProductsResponseDataErrorDetail | Unset):
    """

    message: str | Unset = UNSET
    code: int | Unset = UNSET
    detail: DeleteGlobalProductsResponseDataErrorDetail | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        code = self.code

        detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.detail, Unset):
            detail = self.detail.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if code is not UNSET:
            field_dict["code"] = code
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delete_global_products_response_data_error_detail import (
            DeleteGlobalProductsResponseDataErrorDetail,  # noqa: PLC0415
        )

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        code = d.pop("code", UNSET)

        _detail = d.pop("detail", UNSET)
        detail: DeleteGlobalProductsResponseDataErrorDetail | Unset
        if isinstance(_detail, Unset):
            detail = UNSET
        else:
            detail = DeleteGlobalProductsResponseDataErrorDetail.from_dict(_detail)

        delete_global_products_response_data_error = cls(
            message=message,
            code=code,
            detail=detail,
        )

        delete_global_products_response_data_error.additional_properties = d
        return delete_global_products_response_data_error

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
