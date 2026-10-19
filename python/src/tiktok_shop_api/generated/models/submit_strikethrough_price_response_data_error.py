from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.submit_strikethrough_price_response_data_error_detail import (
        SubmitStrikethroughPriceResponseDataErrorDetail,
    )


T = TypeVar("T", bound="SubmitStrikethroughPriceResponseDataError")


@_attrs_define
class SubmitStrikethroughPriceResponseDataError:
    """
    Attributes:
        code (int): The stable business failure code for this SKU.
        detail (SubmitStrikethroughPriceResponseDataErrorDetail):
        message (str): A human-readable description of the failure and the action needed to correct it.
    """

    code: int
    detail: SubmitStrikethroughPriceResponseDataErrorDetail
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        detail = self.detail.to_dict()

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "detail": detail,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_strikethrough_price_response_data_error_detail import (
            SubmitStrikethroughPriceResponseDataErrorDetail,  # noqa: PLC0415
        )

        d = dict(src_dict)
        code = d.pop("code")

        detail = SubmitStrikethroughPriceResponseDataErrorDetail.from_dict(d.pop("detail"))

        message = d.pop("message")

        submit_strikethrough_price_response_data_error = cls(
            code=code,
            detail=detail,
            message=message,
        )

        submit_strikethrough_price_response_data_error.additional_properties = d
        return submit_strikethrough_price_response_data_error

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
