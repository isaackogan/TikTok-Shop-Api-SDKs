from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_product_response_data_pod_info_pod_template_surface_background_image import (
        GetProductResponseDataPodInfoPodTemplateSurfaceBackgroundImage,
    )
    from ..models.get_product_response_data_pod_info_pod_template_surface_custom_area import (
        GetProductResponseDataPodInfoPodTemplateSurfaceCustomArea,
    )
    from ..models.get_product_response_data_pod_info_pod_template_surface_mask_image import (
        GetProductResponseDataPodInfoPodTemplateSurfaceMaskImage,
    )


T = TypeVar("T", bound="GetProductResponseDataPodInfoPodTemplateSurface")


@_attrs_define
class GetProductResponseDataPodInfoPodTemplateSurface:
    """
    Attributes:
        background_image (GetProductResponseDataPodInfoPodTemplateSurfaceBackgroundImage | Unset):
        custom_areas (list[GetProductResponseDataPodInfoPodTemplateSurfaceCustomArea] | Unset): A list of customizable
            areas on this surface. The order of the elements represents the layer order to be used when rendering the final
            customization preview. A surface can contain up to 10 customization areas.
        external_surface_id (str | Unset): The seller-defined external identifier of the customizable surface, used for
            mapping with the seller's own system.
        mask_image (GetProductResponseDataPodInfoPodTemplateSurfaceMaskImage | Unset):
        surface_name (str | Unset): The name of the customizable surface, for example, `Front Side` or `Back Side`.
    """

    background_image: GetProductResponseDataPodInfoPodTemplateSurfaceBackgroundImage | Unset = UNSET
    custom_areas: list[GetProductResponseDataPodInfoPodTemplateSurfaceCustomArea] | Unset = UNSET
    external_surface_id: str | Unset = UNSET
    mask_image: GetProductResponseDataPodInfoPodTemplateSurfaceMaskImage | Unset = UNSET
    surface_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        background_image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_image, Unset):
            background_image = self.background_image.to_dict()

        custom_areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_areas, Unset):
            custom_areas = []
            for custom_areas_item_data in self.custom_areas:
                custom_areas_item = custom_areas_item_data.to_dict()
                custom_areas.append(custom_areas_item)

        external_surface_id = self.external_surface_id

        mask_image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mask_image, Unset):
            mask_image = self.mask_image.to_dict()

        surface_name = self.surface_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if background_image is not UNSET:
            field_dict["background_image"] = background_image
        if custom_areas is not UNSET:
            field_dict["custom_areas"] = custom_areas
        if external_surface_id is not UNSET:
            field_dict["external_surface_id"] = external_surface_id
        if mask_image is not UNSET:
            field_dict["mask_image"] = mask_image
        if surface_name is not UNSET:
            field_dict["surface_name"] = surface_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_product_response_data_pod_info_pod_template_surface_background_image import (
            GetProductResponseDataPodInfoPodTemplateSurfaceBackgroundImage,  # noqa: PLC0415
        )
        from ..models.get_product_response_data_pod_info_pod_template_surface_custom_area import (
            GetProductResponseDataPodInfoPodTemplateSurfaceCustomArea,  # noqa: PLC0415
        )
        from ..models.get_product_response_data_pod_info_pod_template_surface_mask_image import (
            GetProductResponseDataPodInfoPodTemplateSurfaceMaskImage,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _background_image = d.pop("background_image", UNSET)
        background_image: GetProductResponseDataPodInfoPodTemplateSurfaceBackgroundImage | Unset
        if isinstance(_background_image, Unset):
            background_image = UNSET
        else:
            background_image = GetProductResponseDataPodInfoPodTemplateSurfaceBackgroundImage.from_dict(
                _background_image
            )

        _custom_areas = d.pop("custom_areas", UNSET)
        custom_areas: list[GetProductResponseDataPodInfoPodTemplateSurfaceCustomArea] | Unset = UNSET
        if _custom_areas is not UNSET:
            custom_areas = []
            for custom_areas_item_data in _custom_areas:
                custom_areas_item = GetProductResponseDataPodInfoPodTemplateSurfaceCustomArea.from_dict(
                    custom_areas_item_data
                )

                custom_areas.append(custom_areas_item)

        external_surface_id = d.pop("external_surface_id", UNSET)

        _mask_image = d.pop("mask_image", UNSET)
        mask_image: GetProductResponseDataPodInfoPodTemplateSurfaceMaskImage | Unset
        if isinstance(_mask_image, Unset):
            mask_image = UNSET
        else:
            mask_image = GetProductResponseDataPodInfoPodTemplateSurfaceMaskImage.from_dict(_mask_image)

        surface_name = d.pop("surface_name", UNSET)

        get_product_response_data_pod_info_pod_template_surface = cls(
            background_image=background_image,
            custom_areas=custom_areas,
            external_surface_id=external_surface_id,
            mask_image=mask_image,
            surface_name=surface_name,
        )

        get_product_response_data_pod_info_pod_template_surface.additional_properties = d
        return get_product_response_data_pod_info_pod_template_surface

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
