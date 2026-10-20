from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.area_placement import AreaPlacement
  from ..models.get_product_response_data_pod_info_pod_template_surface_custom_area_image_area import GetProductResponseDataPodInfoPodTemplateSurfaceCustomAreaImageArea
  from ..models.text_area import TextArea





T = TypeVar("T", bound="GetProductResponseDataPodInfoPodTemplateSurfaceCustomArea")



@_attrs_define
class GetProductResponseDataPodInfoPodTemplateSurfaceCustomArea:
    """ 
        Attributes:
            area_name (str | Unset): The name of the customizable area.
            area_placement (AreaPlacement | Unset):
            area_type (str | Unset): The type of the customizable area. Enum values: `TEXT`, `IMAGE`.
            external_area_id (str | Unset): The seller-defined external identifier of the customizable area, used for
                mapping with the seller's own system.
            image_area (GetProductResponseDataPodInfoPodTemplateSurfaceCustomAreaImageArea | Unset):
            is_required (bool | Unset): Specifies whether the consumer must provide customization content for this area. If
                set to `false`, the default content or base product version may be used.
            text_area (TextArea | Unset):
     """

    area_name: str | Unset = UNSET
    area_placement: AreaPlacement | Unset = UNSET
    area_type: str | Unset = UNSET
    external_area_id: str | Unset = UNSET
    image_area: GetProductResponseDataPodInfoPodTemplateSurfaceCustomAreaImageArea | Unset = UNSET
    is_required: bool | Unset = UNSET
    text_area: TextArea | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.area_placement import AreaPlacement # noqa: PLC0415
        from ..models.get_product_response_data_pod_info_pod_template_surface_custom_area_image_area import GetProductResponseDataPodInfoPodTemplateSurfaceCustomAreaImageArea # noqa: PLC0415
        from ..models.text_area import TextArea # noqa: PLC0415
        area_name = self.area_name

        area_placement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.area_placement, Unset):
            area_placement = self.area_placement.to_dict()

        area_type = self.area_type

        external_area_id = self.external_area_id

        image_area: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image_area, Unset):
            image_area = self.image_area.to_dict()

        is_required = self.is_required

        text_area: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_area, Unset):
            text_area = self.text_area.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if area_name is not UNSET:
            field_dict["area_name"] = area_name
        if area_placement is not UNSET:
            field_dict["area_placement"] = area_placement
        if area_type is not UNSET:
            field_dict["area_type"] = area_type
        if external_area_id is not UNSET:
            field_dict["external_area_id"] = external_area_id
        if image_area is not UNSET:
            field_dict["image_area"] = image_area
        if is_required is not UNSET:
            field_dict["is_required"] = is_required
        if text_area is not UNSET:
            field_dict["text_area"] = text_area

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.area_placement import AreaPlacement # noqa: PLC0415
        from ..models.get_product_response_data_pod_info_pod_template_surface_custom_area_image_area import GetProductResponseDataPodInfoPodTemplateSurfaceCustomAreaImageArea # noqa: PLC0415
        from ..models.text_area import TextArea # noqa: PLC0415
        d = dict(src_dict)
        area_name = d.pop("area_name", UNSET)

        _area_placement = d.pop("area_placement", UNSET)
        area_placement: AreaPlacement | Unset
        if isinstance(_area_placement,  Unset):
            area_placement = UNSET
        else:
            area_placement = AreaPlacement.from_dict(_area_placement)




        area_type = d.pop("area_type", UNSET)

        external_area_id = d.pop("external_area_id", UNSET)

        _image_area = d.pop("image_area", UNSET)
        image_area: GetProductResponseDataPodInfoPodTemplateSurfaceCustomAreaImageArea | Unset
        if isinstance(_image_area,  Unset):
            image_area = UNSET
        else:
            image_area = GetProductResponseDataPodInfoPodTemplateSurfaceCustomAreaImageArea.from_dict(_image_area)




        is_required = d.pop("is_required", UNSET)

        _text_area = d.pop("text_area", UNSET)
        text_area: TextArea | Unset
        if isinstance(_text_area,  Unset):
            text_area = UNSET
        else:
            text_area = TextArea.from_dict(_text_area)




        get_product_response_data_pod_info_pod_template_surface_custom_area = cls(
            area_name=area_name,
            area_placement=area_placement,
            area_type=area_type,
            external_area_id=external_area_id,
            image_area=image_area,
            is_required=is_required,
            text_area=text_area,
        )


        get_product_response_data_pod_info_pod_template_surface_custom_area.additional_properties = d
        return get_product_response_data_pod_info_pod_template_surface_custom_area

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
