from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextArea")


@_attrs_define
class TextArea:
    """
    Attributes:
        align_type (str | Unset): The text alignment type. Enum values: `LEFT`, `CENTER`, `RIGHT`.
        colors (list[str] | Unset): A list of text colors available for consumers to choose from, using hexadecimal
            color values such as `#FFFFFF`.
        default_text (str | Unset): Optional default text displayed in this area. If the consumer does not customize
            this area, the default text may be used.
        fonts (list[str] | Unset): A list of font keys available for consumers to choose from, based on the platform-
            supported font library.
        max_text_length (int | Unset): The maximum number of characters allowed for consumer text input.
    """

    align_type: str | Unset = UNSET
    colors: list[str] | Unset = UNSET
    default_text: str | Unset = UNSET
    fonts: list[str] | Unset = UNSET
    max_text_length: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        align_type = self.align_type

        colors: list[str] | Unset = UNSET
        if not isinstance(self.colors, Unset):
            colors = self.colors

        default_text = self.default_text

        fonts: list[str] | Unset = UNSET
        if not isinstance(self.fonts, Unset):
            fonts = self.fonts

        max_text_length = self.max_text_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if align_type is not UNSET:
            field_dict["align_type"] = align_type
        if colors is not UNSET:
            field_dict["colors"] = colors
        if default_text is not UNSET:
            field_dict["default_text"] = default_text
        if fonts is not UNSET:
            field_dict["fonts"] = fonts
        if max_text_length is not UNSET:
            field_dict["max_text_length"] = max_text_length

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        align_type = d.pop("align_type", UNSET)

        colors = cast(list[str], d.pop("colors", UNSET))

        default_text = d.pop("default_text", UNSET)

        fonts = cast(list[str], d.pop("fonts", UNSET))

        max_text_length = d.pop("max_text_length", UNSET)

        text_area = cls(
            align_type=align_type,
            colors=colors,
            default_text=default_text,
            fonts=fonts,
            max_text_length=max_text_length,
        )

        text_area.additional_properties = d
        return text_area

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
