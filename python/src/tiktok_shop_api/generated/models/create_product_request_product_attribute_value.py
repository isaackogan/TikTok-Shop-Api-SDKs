from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_standard_info import MetricStandardInfo


T = TypeVar("T", bound="CreateProductRequestProductAttributeValue")


@_attrs_define
class CreateProductRequestProductAttributeValue:
    """
    Attributes:
        id (str | Unset): The ID of a built-in product attribute value, retrieved from the [Get Attributes
            API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8).
        name (str | Unset): A self-defined custom product attribute value if the built-in values do not satisfy your
            needs. The system will auto-generate an ID after listing.

            **Note**:
            - No duplicates allowed under the same attribute.
            - Max length: 2000 characters
        metric_standard_info (MetricStandardInfo | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    metric_standard_info: MetricStandardInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        metric_standard_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metric_standard_info, Unset):
            metric_standard_info = self.metric_standard_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if metric_standard_info is not UNSET:
            field_dict["metric_standard_info"] = metric_standard_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metric_standard_info import MetricStandardInfo  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _metric_standard_info = d.pop("metric_standard_info", UNSET)
        metric_standard_info: MetricStandardInfo | Unset
        if isinstance(_metric_standard_info, Unset):
            metric_standard_info = UNSET
        else:
            metric_standard_info = MetricStandardInfo.from_dict(_metric_standard_info)

        create_product_request_product_attribute_value = cls(
            id=id,
            name=name,
            metric_standard_info=metric_standard_info,
        )

        create_product_request_product_attribute_value.additional_properties = d
        return create_product_request_product_attribute_value

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
