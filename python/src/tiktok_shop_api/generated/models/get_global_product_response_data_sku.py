from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_global_product_response_data_sku_inventory import GetGlobalProductResponseDataSkuInventory
    from ..models.get_global_product_response_data_sku_price import GetGlobalProductResponseDataSkuPrice
    from ..models.get_global_product_response_data_sku_sales_attribute import (
        GetGlobalProductResponseDataSkuSalesAttribute,
    )
    from ..models.identifier_code import IdentifierCode


T = TypeVar("T", bound="GetGlobalProductResponseDataSku")


@_attrs_define
class GetGlobalProductResponseDataSku:
    """
    Attributes:
        id (str | Unset): The global SKU ID in TikTok Shop.
        seller_sku (str | Unset): An internal code/name for managing SKUs, not visible to buyers.
        price (GetGlobalProductResponseDataSkuPrice | Unset):
        global_quantity (int | Unset): The total SKU inventory quantity across all shops globally.

            The inventory for each local shop is automatically calculated when a product is first published. After
            publishing, this global quantity cannot be manually changed. You can only modify the inventory quantity in each
            local shop.
        identifier_code (IdentifierCode | Unset):
        sales_attributes (list[GetGlobalProductResponseDataSkuSalesAttribute] | Unset): A list of attributes  (e.g.
            size, color, length) that define each variant of a product.
        inventory (list[GetGlobalProductResponseDataSkuInventory] | Unset): SKU inventory information per warehouse.
        sku_unit_count (str | Unset): The total quantity/volume of the product represented by the SKU.
            For example, if the SKU represents 500ml of water, this value would be 500 if the unit type is defined as ml.
            Applicable only for the EU market.

            **Note**:
            - This is mainly used to calculate the unit price of the SKU, and is required only if you wish to display the
            unit price to facilitate easier price comparisons across different products and packaging sizes.
            - Unit price = Selling price/(SKU unit count/base unit count). Therefore if you want to obtain the unit price,
            you would also need to define the "base unit count" and the "unit type" product attributes. Retrieve the
            relevant information for these product attributes by using the [Get Global Attributes
            API](650a0483c16ffe02b8dfc80a).
        extra_identifier_codes (list[str] | Unset): A list of up to 10 additional identifier codes if the SKU belongs to
            a virtual bundle (containing multiple individual SKUs).

            **Note**: Applicable only for the EU market.
        external_global_sku_id (str | Unset): An external identifier used in an external ecommerce platform. This is
            used to associate the SKU between TikTok Shop and the external ecommerce platform.
    """

    id: str | Unset = UNSET
    seller_sku: str | Unset = UNSET
    price: GetGlobalProductResponseDataSkuPrice | Unset = UNSET
    global_quantity: int | Unset = UNSET
    identifier_code: IdentifierCode | Unset = UNSET
    sales_attributes: list[GetGlobalProductResponseDataSkuSalesAttribute] | Unset = UNSET
    inventory: list[GetGlobalProductResponseDataSkuInventory] | Unset = UNSET
    sku_unit_count: str | Unset = UNSET
    extra_identifier_codes: list[str] | Unset = UNSET
    external_global_sku_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        seller_sku = self.seller_sku

        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        global_quantity = self.global_quantity

        identifier_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier_code, Unset):
            identifier_code = self.identifier_code.to_dict()

        sales_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sales_attributes, Unset):
            sales_attributes = []
            for sales_attributes_item_data in self.sales_attributes:
                sales_attributes_item = sales_attributes_item_data.to_dict()
                sales_attributes.append(sales_attributes_item)

        inventory: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inventory, Unset):
            inventory = []
            for inventory_item_data in self.inventory:
                inventory_item = inventory_item_data.to_dict()
                inventory.append(inventory_item)

        sku_unit_count = self.sku_unit_count

        extra_identifier_codes: list[str] | Unset = UNSET
        if not isinstance(self.extra_identifier_codes, Unset):
            extra_identifier_codes = self.extra_identifier_codes

        external_global_sku_id = self.external_global_sku_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if seller_sku is not UNSET:
            field_dict["seller_sku"] = seller_sku
        if price is not UNSET:
            field_dict["price"] = price
        if global_quantity is not UNSET:
            field_dict["global_quantity"] = global_quantity
        if identifier_code is not UNSET:
            field_dict["identifier_code"] = identifier_code
        if sales_attributes is not UNSET:
            field_dict["sales_attributes"] = sales_attributes
        if inventory is not UNSET:
            field_dict["inventory"] = inventory
        if sku_unit_count is not UNSET:
            field_dict["sku_unit_count"] = sku_unit_count
        if extra_identifier_codes is not UNSET:
            field_dict["extra_identifier_codes"] = extra_identifier_codes
        if external_global_sku_id is not UNSET:
            field_dict["external_global_sku_id"] = external_global_sku_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_global_product_response_data_sku_inventory import (
            GetGlobalProductResponseDataSkuInventory,  # noqa: PLC0415
        )
        from ..models.get_global_product_response_data_sku_price import (
            GetGlobalProductResponseDataSkuPrice,  # noqa: PLC0415
        )
        from ..models.get_global_product_response_data_sku_sales_attribute import (
            GetGlobalProductResponseDataSkuSalesAttribute,  # noqa: PLC0415
        )
        from ..models.identifier_code import IdentifierCode  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        seller_sku = d.pop("seller_sku", UNSET)

        _price = d.pop("price", UNSET)
        price: GetGlobalProductResponseDataSkuPrice | Unset
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = GetGlobalProductResponseDataSkuPrice.from_dict(_price)

        global_quantity = d.pop("global_quantity", UNSET)

        _identifier_code = d.pop("identifier_code", UNSET)
        identifier_code: IdentifierCode | Unset
        if isinstance(_identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = IdentifierCode.from_dict(_identifier_code)

        _sales_attributes = d.pop("sales_attributes", UNSET)
        sales_attributes: list[GetGlobalProductResponseDataSkuSalesAttribute] | Unset = UNSET
        if _sales_attributes is not UNSET:
            sales_attributes = []
            for sales_attributes_item_data in _sales_attributes:
                sales_attributes_item = GetGlobalProductResponseDataSkuSalesAttribute.from_dict(
                    sales_attributes_item_data
                )

                sales_attributes.append(sales_attributes_item)

        _inventory = d.pop("inventory", UNSET)
        inventory: list[GetGlobalProductResponseDataSkuInventory] | Unset = UNSET
        if _inventory is not UNSET:
            inventory = []
            for inventory_item_data in _inventory:
                inventory_item = GetGlobalProductResponseDataSkuInventory.from_dict(inventory_item_data)

                inventory.append(inventory_item)

        sku_unit_count = d.pop("sku_unit_count", UNSET)

        extra_identifier_codes = cast(list[str], d.pop("extra_identifier_codes", UNSET))

        external_global_sku_id = d.pop("external_global_sku_id", UNSET)

        get_global_product_response_data_sku = cls(
            id=id,
            seller_sku=seller_sku,
            price=price,
            global_quantity=global_quantity,
            identifier_code=identifier_code,
            sales_attributes=sales_attributes,
            inventory=inventory,
            sku_unit_count=sku_unit_count,
            extra_identifier_codes=extra_identifier_codes,
            external_global_sku_id=external_global_sku_id,
        )

        get_global_product_response_data_sku.additional_properties = d
        return get_global_product_response_data_sku

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
