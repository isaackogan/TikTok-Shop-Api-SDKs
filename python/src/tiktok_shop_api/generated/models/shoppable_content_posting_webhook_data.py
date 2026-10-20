from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.shoppable_content_posting_webhook_data_event import ShoppableContentPostingWebhookDataEvent





T = TypeVar("T", bound="ShoppableContentPostingWebhookData")



@_attrs_define
class ShoppableContentPostingWebhookData:
    """ 
        Attributes:
            product_id (str | Unset): ID of the product promoted in the creator's video.
            event (ShoppableContentPostingWebhookDataEvent | Unset):
     """

    product_id: str | Unset = UNSET
    event: ShoppableContentPostingWebhookDataEvent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.shoppable_content_posting_webhook_data_event import ShoppableContentPostingWebhookDataEvent # noqa: PLC0415
        product_id = self.product_id

        event: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if event is not UNSET:
            field_dict["event"] = event

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shoppable_content_posting_webhook_data_event import ShoppableContentPostingWebhookDataEvent # noqa: PLC0415
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        _event = d.pop("event", UNSET)
        event: ShoppableContentPostingWebhookDataEvent | Unset
        if isinstance(_event,  Unset):
            event = UNSET
        else:
            event = ShoppableContentPostingWebhookDataEvent.from_dict(_event)




        shoppable_content_posting_webhook_data = cls(
            product_id=product_id,
            event=event,
        )


        shoppable_content_posting_webhook_data.additional_properties = d
        return shoppable_content_posting_webhook_data

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
