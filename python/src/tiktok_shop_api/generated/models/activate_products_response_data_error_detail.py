from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.activate_products_response_data_error_detail_extra_error import ActivateProductsResponseDataErrorDetailExtraError





T = TypeVar("T", bound="ActivateProductsResponseDataErrorDetail")



@_attrs_define
class ActivateProductsResponseDataErrorDetail:
    """ 
        Attributes:
            product_id (str | Unset): The ID of the product that could not be activated.
            extra_errors (list[ActivateProductsResponseDataErrorDetailExtraError] | Unset): A list of further nested errors
                or issues related to the main error.
     """

    product_id: str | Unset = UNSET
    extra_errors: list[ActivateProductsResponseDataErrorDetailExtraError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.activate_products_response_data_error_detail_extra_error import ActivateProductsResponseDataErrorDetailExtraError # noqa: PLC0415
        product_id = self.product_id

        extra_errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.extra_errors, Unset):
            extra_errors = []
            for extra_errors_item_data in self.extra_errors:
                extra_errors_item = extra_errors_item_data.to_dict()
                extra_errors.append(extra_errors_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if extra_errors is not UNSET:
            field_dict["extra_errors"] = extra_errors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activate_products_response_data_error_detail_extra_error import ActivateProductsResponseDataErrorDetailExtraError # noqa: PLC0415
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        _extra_errors = d.pop("extra_errors", UNSET)
        extra_errors: list[ActivateProductsResponseDataErrorDetailExtraError] | Unset = UNSET
        if _extra_errors is not UNSET:
            extra_errors = []
            for extra_errors_item_data in _extra_errors:
                extra_errors_item = ActivateProductsResponseDataErrorDetailExtraError.from_dict(extra_errors_item_data)



                extra_errors.append(extra_errors_item)


        activate_products_response_data_error_detail = cls(
            product_id=product_id,
            extra_errors=extra_errors,
        )


        activate_products_response_data_error_detail.additional_properties = d
        return activate_products_response_data_error_detail

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
