from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.partial_edit_product_request_pod_info_pod_template_surface_custom_area_image_area_default_image import PartialEditProductRequestPodInfoPodTemplateSurfaceCustomAreaImageAreaDefaultImage





T = TypeVar("T", bound="PartialEditProductRequestPodInfoPodTemplateSurfaceCustomAreaImageArea")



@_attrs_define
class PartialEditProductRequestPodInfoPodTemplateSurfaceCustomAreaImageArea:
    """ 
        Attributes:
            default_image (PartialEditProductRequestPodInfoPodTemplateSurfaceCustomAreaImageAreaDefaultImage | Unset):
            min_height (int | Unset): The minimum required height, in pixels, for an image uploaded by the consumer.
            min_width (int | Unset): The minimum required width, in pixels, for an image uploaded by the consumer.
     """

    default_image: PartialEditProductRequestPodInfoPodTemplateSurfaceCustomAreaImageAreaDefaultImage | Unset = UNSET
    min_height: int | Unset = UNSET
    min_width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.partial_edit_product_request_pod_info_pod_template_surface_custom_area_image_area_default_image import PartialEditProductRequestPodInfoPodTemplateSurfaceCustomAreaImageAreaDefaultImage # noqa: PLC0415
        default_image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_image, Unset):
            default_image = self.default_image.to_dict()

        min_height = self.min_height

        min_width = self.min_width


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if default_image is not UNSET:
            field_dict["default_image"] = default_image
        if min_height is not UNSET:
            field_dict["min_height"] = min_height
        if min_width is not UNSET:
            field_dict["min_width"] = min_width

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partial_edit_product_request_pod_info_pod_template_surface_custom_area_image_area_default_image import PartialEditProductRequestPodInfoPodTemplateSurfaceCustomAreaImageAreaDefaultImage # noqa: PLC0415
        d = dict(src_dict)
        _default_image = d.pop("default_image", UNSET)
        default_image: PartialEditProductRequestPodInfoPodTemplateSurfaceCustomAreaImageAreaDefaultImage | Unset
        if isinstance(_default_image,  Unset):
            default_image = UNSET
        else:
            default_image = PartialEditProductRequestPodInfoPodTemplateSurfaceCustomAreaImageAreaDefaultImage.from_dict(_default_image)




        min_height = d.pop("min_height", UNSET)

        min_width = d.pop("min_width", UNSET)

        partial_edit_product_request_pod_info_pod_template_surface_custom_area_image_area = cls(
            default_image=default_image,
            min_height=min_height,
            min_width=min_width,
        )


        partial_edit_product_request_pod_info_pod_template_surface_custom_area_image_area.additional_properties = d
        return partial_edit_product_request_pod_info_pod_template_surface_custom_area_image_area

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
