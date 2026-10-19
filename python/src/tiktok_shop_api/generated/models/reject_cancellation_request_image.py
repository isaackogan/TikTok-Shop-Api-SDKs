from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RejectCancellationRequestImage")


@_attrs_define
class RejectCancellationRequestImage:
    """
    Attributes:
        image_id (str): Image ID.
        mime_type (str | Unset): MIME type.
        height (int | Unset): Image height.
            Unit: px
        width (int | Unset): Image width.
            Unit: px
    """

    image_id: str
    mime_type: str | Unset = UNSET
    height: int | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_id = self.image_id

        mime_type = self.mime_type

        height = self.height

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image_id": image_id,
            }
        )
        if mime_type is not UNSET:
            field_dict["mime_type"] = mime_type
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_id = d.pop("image_id")

        mime_type = d.pop("mime_type", UNSET)

        height = d.pop("height", UNSET)

        width = d.pop("width", UNSET)

        reject_cancellation_request_image = cls(
            image_id=image_id,
            mime_type=mime_type,
            height=height,
            width=width,
        )

        reject_cancellation_request_image.additional_properties = d
        return reject_cancellation_request_image

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
