from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.shoppable_content_posting_webhook_data_event_scene import ShoppableContentPostingWebhookDataEventScene
from ..models.shoppable_content_posting_webhook_data_event_type import ShoppableContentPostingWebhookDataEventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShoppableContentPostingWebhookDataEvent")


@_attrs_define
class ShoppableContentPostingWebhookDataEvent:
    """
    Attributes:
        type_ (ShoppableContentPostingWebhookDataEventType | Unset): The action which the creator takes to the product
            promoted in the video or live stream. The possible enumerations are:

             * `ADD`: Add the product.
             * `UPDATE`: Update the product.
             * `REMOVE`: Remove the product.
        scene (ShoppableContentPostingWebhookDataEventScene | Unset): The scene where the creator promotes the product.
            The possible enumerations are:

             * `VIDEO`: short video.
        content_id (str | Unset): The ID of the short video.
    """

    type_: ShoppableContentPostingWebhookDataEventType | Unset = UNSET
    scene: ShoppableContentPostingWebhookDataEventScene | Unset = UNSET
    content_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        scene: str | Unset = UNSET
        if not isinstance(self.scene, Unset):
            scene = self.scene.value

        content_id = self.content_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if scene is not UNSET:
            field_dict["scene"] = scene
        if content_id is not UNSET:
            field_dict["content_id"] = content_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: ShoppableContentPostingWebhookDataEventType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ShoppableContentPostingWebhookDataEventType(_type_)

        _scene = d.pop("scene", UNSET)
        scene: ShoppableContentPostingWebhookDataEventScene | Unset
        if isinstance(_scene, Unset):
            scene = UNSET
        else:
            scene = ShoppableContentPostingWebhookDataEventScene(_scene)

        content_id = d.pop("content_id", UNSET)

        shoppable_content_posting_webhook_data_event = cls(
            type_=type_,
            scene=scene,
            content_id=content_id,
        )

        shoppable_content_posting_webhook_data_event.additional_properties = d
        return shoppable_content_posting_webhook_data_event

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
