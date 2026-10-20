from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_global_product_request_sku_sale_price_region import EditGlobalProductRequestSkuSalePriceRegion

T = TypeVar("T", bound="EditGlobalProductRequestSkuSalePrice")


@_attrs_define
class EditGlobalProductRequestSkuSalePrice:
    """
    Attributes:
        region (EditGlobalProductRequestSkuSalePriceRegion): The market for which this local display price applies.
            Possible values:
            - AT: Austria
            - BE: Belgium
            - CZ: Czech Republic
            - DE: Germany
            - ES: Spain
            - FR: France
            - GB: United Kingdom
            - GR: Greece
            - HU: Hungary
            - ID: Indonesia
            - IE: Ireland
            - IT: Italy
            - JP: Japan
            - MY: Malaysia
            - NL: Netherlands (NL)
            - PH: Philippines
            - PO: Poland
            - PT: Portugal
            - SG: Singapore
            - TH: Thailand
            - US: United States
            - VN: Vietnam
            - MX: Mexico
        amount (str): The price amount.
            Refer to [Product Pricing](https://partner.tiktokshop.com/docv2/page/67e1288d76cfee049d9af858) for the allowed
            price ranges in each market.
    """

    region: EditGlobalProductRequestSkuSalePriceRegion
    amount: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region = self.region.value

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "region": region,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        region = EditGlobalProductRequestSkuSalePriceRegion(d.pop("region"))

        amount = d.pop("amount")

        edit_global_product_request_sku_sale_price = cls(
            region=region,
            amount=amount,
        )

        edit_global_product_request_sku_sale_price.additional_properties = d
        return edit_global_product_request_sku_sale_price

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
