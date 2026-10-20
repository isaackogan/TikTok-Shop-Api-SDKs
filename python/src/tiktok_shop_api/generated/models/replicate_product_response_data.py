from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.replicate_product_response_data_error import ReplicateProductResponseDataError





T = TypeVar("T", bound="ReplicateProductResponseData")



@_attrs_define
class ReplicateProductResponseData:
    """ 
        Attributes:
            errors (list[ReplicateProductResponseDataError] | Unset): The pre-submission validation errors for target
                markets. When this list is non-empty, asynchronous replication is not submitted. Use each item's `detail.region`
                to identify the affected target market.
     """

    errors: list[ReplicateProductResponseDataError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.replicate_product_response_data_error import ReplicateProductResponseDataError # noqa: PLC0415
        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.replicate_product_response_data_error import ReplicateProductResponseDataError # noqa: PLC0415
        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[ReplicateProductResponseDataError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ReplicateProductResponseDataError.from_dict(errors_item_data)



                errors.append(errors_item)


        replicate_product_response_data = cls(
            errors=errors,
        )


        replicate_product_response_data.additional_properties = d
        return replicate_product_response_data

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
