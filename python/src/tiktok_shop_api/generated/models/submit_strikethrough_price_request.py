from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.submit_strikethrough_price_request_sku import SubmitStrikethroughPriceRequestSku


T = TypeVar("T", bound="SubmitStrikethroughPriceRequest")


@_attrs_define
class SubmitStrikethroughPriceRequest:
    """
    Attributes:
        external_product_id (str): An external product identifier used on an external ecommerce platform. This value
            must match the `external_product_id` used when the product was created.
        skus (list[SubmitStrikethroughPriceRequestSku]): A list of SKUs whose external pricing information is submitted
            for verification. All SKU IDs must belong to the product identified by `product_id`.
    """

    external_product_id: str
    skus: list[SubmitStrikethroughPriceRequestSku]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_product_id = self.external_product_id

        skus = []
        for skus_item_data in self.skus:
            skus_item = skus_item_data.to_dict()
            skus.append(skus_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_product_id": external_product_id,
                "skus": skus,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_strikethrough_price_request_sku import SubmitStrikethroughPriceRequestSku  # noqa: PLC0415

        d = dict(src_dict)
        external_product_id = d.pop("external_product_id")

        skus = []
        _skus = d.pop("skus")
        for skus_item_data in _skus:
            skus_item = SubmitStrikethroughPriceRequestSku.from_dict(skus_item_data)

            skus.append(skus_item)

        submit_strikethrough_price_request = cls(
            external_product_id=external_product_id,
            skus=skus,
        )

        submit_strikethrough_price_request.additional_properties = d
        return submit_strikethrough_price_request

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
