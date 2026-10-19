from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partial_edit_product_request_pod_info_pod_template_surface import (
        PartialEditProductRequestPodInfoPodTemplateSurface,
    )


T = TypeVar("T", bound="PartialEditProductRequestPodInfoPodTemplate")


@_attrs_define
class PartialEditProductRequestPodInfoPodTemplate:
    """
    Attributes:
        pod_template_id (str | Unset): The unique identifier of the POD customization template. This field is generated
            by the system and is not required when creating a new template.
        remark (str | Unset): Optional notes or instructions for this customization template. These notes may be used to
            remind consumers about customization requirements on the customization page.
        sku_ids (list[str] | Unset): A list of product SKU IDs associated with this customization template. The same SKU
            cannot be associated with more than one template.
        surfaces (list[PartialEditProductRequestPodInfoPodTemplateSurface] | Unset): A list of customizable product
            surfaces under this template, such as the front side, back side, collar, or sleeve. A template can contain up to
            10 surfaces.
        template_name (str | Unset): The name of the customization template, used by the seller for internal management.
    """

    pod_template_id: str | Unset = UNSET
    remark: str | Unset = UNSET
    sku_ids: list[str] | Unset = UNSET
    surfaces: list[PartialEditProductRequestPodInfoPodTemplateSurface] | Unset = UNSET
    template_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pod_template_id = self.pod_template_id

        remark = self.remark

        sku_ids: list[str] | Unset = UNSET
        if not isinstance(self.sku_ids, Unset):
            sku_ids = self.sku_ids

        surfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.surfaces, Unset):
            surfaces = []
            for surfaces_item_data in self.surfaces:
                surfaces_item = surfaces_item_data.to_dict()
                surfaces.append(surfaces_item)

        template_name = self.template_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pod_template_id is not UNSET:
            field_dict["pod_template_id"] = pod_template_id
        if remark is not UNSET:
            field_dict["remark"] = remark
        if sku_ids is not UNSET:
            field_dict["sku_ids"] = sku_ids
        if surfaces is not UNSET:
            field_dict["surfaces"] = surfaces
        if template_name is not UNSET:
            field_dict["template_name"] = template_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partial_edit_product_request_pod_info_pod_template_surface import (
            PartialEditProductRequestPodInfoPodTemplateSurface,  # noqa: PLC0415
        )

        d = dict(src_dict)
        pod_template_id = d.pop("pod_template_id", UNSET)

        remark = d.pop("remark", UNSET)

        sku_ids = cast(list[str], d.pop("sku_ids", UNSET))

        _surfaces = d.pop("surfaces", UNSET)
        surfaces: list[PartialEditProductRequestPodInfoPodTemplateSurface] | Unset = UNSET
        if _surfaces is not UNSET:
            surfaces = []
            for surfaces_item_data in _surfaces:
                surfaces_item = PartialEditProductRequestPodInfoPodTemplateSurface.from_dict(surfaces_item_data)

                surfaces.append(surfaces_item)

        template_name = d.pop("template_name", UNSET)

        partial_edit_product_request_pod_info_pod_template = cls(
            pod_template_id=pod_template_id,
            remark=remark,
            sku_ids=sku_ids,
            surfaces=surfaces,
            template_name=template_name,
        )

        partial_edit_product_request_pod_info_pod_template.additional_properties = d
        return partial_edit_product_request_pod_info_pod_template

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
