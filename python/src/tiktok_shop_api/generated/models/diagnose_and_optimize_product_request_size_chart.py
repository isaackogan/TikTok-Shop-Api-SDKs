from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diagnose_and_optimize_product_request_size_chart_image import (
        DiagnoseAndOptimizeProductRequestSizeChartImage,
    )
    from ..models.diagnose_and_optimize_product_request_size_chart_template import (
        DiagnoseAndOptimizeProductRequestSizeChartTemplate,
    )


T = TypeVar("T", bound="DiagnoseAndOptimizeProductRequestSizeChart")


@_attrs_define
class DiagnoseAndOptimizeProductRequestSizeChart:
    """
    Attributes:
        template (DiagnoseAndOptimizeProductRequestSizeChartTemplate | Unset):
        image (DiagnoseAndOptimizeProductRequestSizeChartImage | Unset):
    """

    template: DiagnoseAndOptimizeProductRequestSizeChartTemplate | Unset = UNSET
    image: DiagnoseAndOptimizeProductRequestSizeChartImage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template is not UNSET:
            field_dict["template"] = template
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diagnose_and_optimize_product_request_size_chart_image import (
            DiagnoseAndOptimizeProductRequestSizeChartImage,  # noqa: PLC0415
        )
        from ..models.diagnose_and_optimize_product_request_size_chart_template import (
            DiagnoseAndOptimizeProductRequestSizeChartTemplate,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _template = d.pop("template", UNSET)
        template: DiagnoseAndOptimizeProductRequestSizeChartTemplate | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = DiagnoseAndOptimizeProductRequestSizeChartTemplate.from_dict(_template)

        _image = d.pop("image", UNSET)
        image: DiagnoseAndOptimizeProductRequestSizeChartImage | Unset
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = DiagnoseAndOptimizeProductRequestSizeChartImage.from_dict(_image)

        diagnose_and_optimize_product_request_size_chart = cls(
            template=template,
            image=image,
        )

        diagnose_and_optimize_product_request_size_chart.additional_properties = d
        return diagnose_and_optimize_product_request_size_chart

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
