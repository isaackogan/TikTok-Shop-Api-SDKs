from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sku_img import SkuImg


T = TypeVar("T", bound="CreateGlobalProductRequestSkuSalesAttribute")


@_attrs_define
class CreateGlobalProductRequestSkuSalesAttribute:
    """
    Attributes:
        id (str | Unset): The ID of a built-in sales attribute, retrieved from [Get Global Attributes
            API](https://partner.tiktokshop.com/docv2/page/650a0483c16ffe02b8dfc80a).
        name (str | Unset): A self-defined custom sales attribute name if the built-in attributes do not satisfy your
            needs. TikTok Shop generates an ID when the global product is created and returns it in
            `data.global_skus[].sales_attributes[].id`.

            **Note**:
            - Do not include sensitive characters.
            - Max length: 20 characters
        value_id (str | Unset): The ID of a built-in sales attribute value, retrieved from the [Get Global Attributes
            API](https://partner.tiktokshop.com/docv2/page/650a0483c16ffe02b8dfc80a).
        value_name (str | Unset): A self-defined custom sales attribute value if the built-in values do not satisfy your
            needs. TikTok Shop generates an ID when the global product is created and returns it in
            `data.global_skus[].sales_attributes[].value_id`.

            **Note**:
            - No duplicates allowed under the same attribute.
            - Max length: 50 characters.
            - Supports only alphabets and numbers.
        sku_img (SkuImg | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    value_id: str | Unset = UNSET
    value_name: str | Unset = UNSET
    sku_img: SkuImg | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        value_id = self.value_id

        value_name = self.value_name

        sku_img: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sku_img, Unset):
            sku_img = self.sku_img.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if value_id is not UNSET:
            field_dict["value_id"] = value_id
        if value_name is not UNSET:
            field_dict["value_name"] = value_name
        if sku_img is not UNSET:
            field_dict["sku_img"] = sku_img

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sku_img import SkuImg  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        value_id = d.pop("value_id", UNSET)

        value_name = d.pop("value_name", UNSET)

        _sku_img = d.pop("sku_img", UNSET)
        sku_img: SkuImg | Unset
        if isinstance(_sku_img, Unset):
            sku_img = UNSET
        else:
            sku_img = SkuImg.from_dict(_sku_img)

        create_global_product_request_sku_sales_attribute = cls(
            id=id,
            name=name,
            value_id=value_id,
            value_name=value_name,
            sku_img=sku_img,
        )

        create_global_product_request_sku_sales_attribute.additional_properties = d
        return create_global_product_request_sku_sales_attribute

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
