from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fulfillment_type import FulfillmentType


T = TypeVar("T", bound="GetProductResponseDataSkuPreSale")


@_attrs_define
class GetProductResponseDataSkuPreSale:
    """
    Attributes:
        fulfillment_type (FulfillmentType | Unset):
        type_ (str | Unset): The type of pre-sale.
            Possible values based on the region:
            **US**
            - `PRE_ORDER`: The product is not yet available or released. Fulfillment can be extended by specifying a
            **release date**.
            - `MADE_TO_ORDER`: The product is produced only after the order is received. Fulfillment can be extended by
            specifying a **duration**.
            - `CUSTOM`: The product requires a fulfillment timeline that exceeds the standard due to other factors.
            Fulfillment can be extended by specifying a **duration**.

            **UK, EU, SEA, JP, and LATAM**
            - `PRE_ORDER`: The product is not yet available or released. Fulfillment can be extended by specifying a
            **duration**.
    """

    fulfillment_type: FulfillmentType | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fulfillment_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fulfillment_type, Unset):
            fulfillment_type = self.fulfillment_type.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fulfillment_type is not UNSET:
            field_dict["fulfillment_type"] = fulfillment_type
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fulfillment_type import FulfillmentType  # noqa: PLC0415

        d = dict(src_dict)
        _fulfillment_type = d.pop("fulfillment_type", UNSET)
        fulfillment_type: FulfillmentType | Unset
        if isinstance(_fulfillment_type, Unset):
            fulfillment_type = UNSET
        else:
            fulfillment_type = FulfillmentType.from_dict(_fulfillment_type)

        type_ = d.pop("type", UNSET)

        get_product_response_data_sku_pre_sale = cls(
            fulfillment_type=fulfillment_type,
            type_=type_,
        )

        get_product_response_data_sku_pre_sale.additional_properties = d
        return get_product_response_data_sku_pre_sale

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
