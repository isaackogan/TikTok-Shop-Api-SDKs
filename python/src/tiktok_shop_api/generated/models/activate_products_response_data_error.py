from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.activate_products_response_data_error_detail import ActivateProductsResponseDataErrorDetail





T = TypeVar("T", bound="ActivateProductsResponseDataError")



@_attrs_define
class ActivateProductsResponseDataError:
    """ 
        Attributes:
            code (int | Unset): The main error code.
            message (str | Unset): The main error message.
            detail (ActivateProductsResponseDataErrorDetail | Unset):
     """

    code: int | Unset = UNSET
    message: str | Unset = UNSET
    detail: ActivateProductsResponseDataErrorDetail | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.activate_products_response_data_error_detail import ActivateProductsResponseDataErrorDetail # noqa: PLC0415
        code = self.code

        message = self.message

        detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.detail, Unset):
            detail = self.detail.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activate_products_response_data_error_detail import ActivateProductsResponseDataErrorDetail # noqa: PLC0415
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        _detail = d.pop("detail", UNSET)
        detail: ActivateProductsResponseDataErrorDetail | Unset
        if isinstance(_detail,  Unset):
            detail = UNSET
        else:
            detail = ActivateProductsResponseDataErrorDetail.from_dict(_detail)




        activate_products_response_data_error = cls(
            code=code,
            message=message,
            detail=detail,
        )


        activate_products_response_data_error.additional_properties = d
        return activate_products_response_data_error

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
