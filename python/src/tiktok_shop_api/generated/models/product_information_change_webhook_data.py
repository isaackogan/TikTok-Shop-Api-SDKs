from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.product_information_change_webhook_data_change_source import (
    ProductInformationChangeWebhookDataChangeSource,
)
from ..models.product_information_change_webhook_data_changed_fields_item import (
    ProductInformationChangeWebhookDataChangedFieldsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductInformationChangeWebhookData")


@_attrs_define
class ProductInformationChangeWebhookData:
    """
    Attributes:
        product_id (str | Unset): The ID of the product that's being changed.
        change_source (ProductInformationChangeWebhookDataChangeSource | Unset): The originating source of the change.
             Possible values:
             - `SELLER_CENTER`
             - `OPEN_API`
        changed_fields (list[ProductInformationChangeWebhookDataChangedFieldsItem] | Unset): The product properties that
            were changed.
             Possible values:
             - `title`: The product name was changed.
             - `description`: The product description was changed.
             - `main_images`: Product images that appear in the image gallery were added, removed, or changed.
             - `product_attributes`: Product attributes were added, removed, or edited.
             - `size_chart_image`: The size chart image was added, removed, or changed.
             - `size_chart_template`: The associated size chart template was removed or its details were edited, or a new
            size chart template was associated.
             - `others`: Other product properties not specified above were changed.
        update_time (int | Unset): The time when the change occurred. Unix timestamp.
    """

    product_id: str | Unset = UNSET
    change_source: ProductInformationChangeWebhookDataChangeSource | Unset = UNSET
    changed_fields: list[ProductInformationChangeWebhookDataChangedFieldsItem] | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        change_source: str | Unset = UNSET
        if not isinstance(self.change_source, Unset):
            change_source = self.change_source.value

        changed_fields: list[str] | Unset = UNSET
        if not isinstance(self.changed_fields, Unset):
            changed_fields = []
            for changed_fields_item_data in self.changed_fields:
                changed_fields_item = changed_fields_item_data.value
                changed_fields.append(changed_fields_item)

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if change_source is not UNSET:
            field_dict["change_source"] = change_source
        if changed_fields is not UNSET:
            field_dict["changed_fields"] = changed_fields
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        _change_source = d.pop("change_source", UNSET)
        change_source: ProductInformationChangeWebhookDataChangeSource | Unset
        if isinstance(_change_source, Unset):
            change_source = UNSET
        else:
            change_source = ProductInformationChangeWebhookDataChangeSource(_change_source)

        _changed_fields = d.pop("changed_fields", UNSET)
        changed_fields: list[ProductInformationChangeWebhookDataChangedFieldsItem] | Unset = UNSET
        if _changed_fields is not UNSET:
            changed_fields = []
            for changed_fields_item_data in _changed_fields:
                changed_fields_item = ProductInformationChangeWebhookDataChangedFieldsItem(changed_fields_item_data)

                changed_fields.append(changed_fields_item)

        update_time = d.pop("update_time", UNSET)

        product_information_change_webhook_data = cls(
            product_id=product_id,
            change_source=change_source,
            changed_fields=changed_fields,
            update_time=update_time,
        )

        product_information_change_webhook_data.additional_properties = d
        return product_information_change_webhook_data

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
