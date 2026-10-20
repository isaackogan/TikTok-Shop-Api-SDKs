from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_first_mile_bundle_response_data_error import CreateFirstMileBundleResponseDataError





T = TypeVar("T", bound="CreateFirstMileBundleV2ResponseData")



@_attrs_define
class CreateFirstMileBundleV2ResponseData:
    """ 
        Attributes:
            first_mile_bundle_id (str | Unset): The ID of the first-mile bundle.
            url (str | Unset): The returned waybill link.
            errors (list[CreateFirstMileBundleResponseDataError] | Unset): Errors associated with requested orders. An entry
                can indicate that the requested order could not be resolved, or that a package associated with the order could
                not be included in the bundle. Multiple errors may be returned, including when the top-level `code` is `0`.
     """

    first_mile_bundle_id: str | Unset = UNSET
    url: str | Unset = UNSET
    errors: list[CreateFirstMileBundleResponseDataError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_first_mile_bundle_response_data_error import CreateFirstMileBundleResponseDataError # noqa: PLC0415
        first_mile_bundle_id = self.first_mile_bundle_id

        url = self.url

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
        if first_mile_bundle_id is not UNSET:
            field_dict["first_mile_bundle_id"] = first_mile_bundle_id
        if url is not UNSET:
            field_dict["url"] = url
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_first_mile_bundle_response_data_error import CreateFirstMileBundleResponseDataError # noqa: PLC0415
        d = dict(src_dict)
        first_mile_bundle_id = d.pop("first_mile_bundle_id", UNSET)

        url = d.pop("url", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[CreateFirstMileBundleResponseDataError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = CreateFirstMileBundleResponseDataError.from_dict(errors_item_data)



                errors.append(errors_item)


        create_first_mile_bundle_v2_response_data = cls(
            first_mile_bundle_id=first_mile_bundle_id,
            url=url,
            errors=errors,
        )


        create_first_mile_bundle_v2_response_data.additional_properties = d
        return create_first_mile_bundle_v2_response_data

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
