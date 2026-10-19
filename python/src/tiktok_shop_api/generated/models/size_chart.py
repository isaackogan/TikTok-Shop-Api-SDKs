from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image import Image
    from ..models.template import Template


T = TypeVar("T", bound="SizeChart")


@_attrs_define
class SizeChart:
    """
    Attributes:
        image (Image | Unset):
        template (Template | Unset):
    """

    image: Image | Unset = UNSET
    template: Template | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image is not UNSET:
            field_dict["image"] = image
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image import Image  # noqa: PLC0415
        from ..models.template import Template  # noqa: PLC0415

        d = dict(src_dict)
        _image = d.pop("image", UNSET)
        image: Image | Unset
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = Image.from_dict(_image)

        _template = d.pop("template", UNSET)
        template: Template | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = Template.from_dict(_template)

        size_chart = cls(
            image=image,
            template=template,
        )

        size_chart.additional_properties = d
        return size_chart

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
