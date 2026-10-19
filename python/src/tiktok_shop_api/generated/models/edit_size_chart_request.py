from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.size_chart_data import SizeChartData


T = TypeVar("T", bound="EditSizeChartRequest")


@_attrs_define
class EditSizeChartRequest:
    """
    Attributes:
        size_chart_id (str): The ID of the seller-owned reusable size chart template to update.
        size_chart_data (SizeChartData):
        template_name (str | Unset): The new name of the size chart template. If omitted, the current name remains
            unchanged.
    """

    size_chart_id: str
    size_chart_data: SizeChartData
    template_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        size_chart_id = self.size_chart_id

        size_chart_data = self.size_chart_data.to_dict()

        template_name = self.template_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "size_chart_id": size_chart_id,
                "size_chart_data": size_chart_data,
            }
        )
        if template_name is not UNSET:
            field_dict["template_name"] = template_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.size_chart_data import SizeChartData  # noqa: PLC0415

        d = dict(src_dict)
        size_chart_id = d.pop("size_chart_id")

        size_chart_data = SizeChartData.from_dict(d.pop("size_chart_data"))

        template_name = d.pop("template_name", UNSET)

        edit_size_chart_request = cls(
            size_chart_id=size_chart_id,
            size_chart_data=size_chart_data,
            template_name=template_name,
        )

        edit_size_chart_request.additional_properties = d
        return edit_size_chart_request

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
