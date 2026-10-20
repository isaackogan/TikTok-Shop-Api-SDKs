from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_global_product_request_sku_inventory import CreateGlobalProductRequestSkuInventory
  from ..models.create_global_product_request_sku_price import CreateGlobalProductRequestSkuPrice
  from ..models.create_global_product_request_sku_sales_attribute import CreateGlobalProductRequestSkuSalesAttribute
  from ..models.identifier_code import IdentifierCode
  from ..models.partial_edit_global_product_request_sku_sale_price import PartialEditGlobalProductRequestSkuSalePrice





T = TypeVar("T", bound="PartialEditGlobalProductRequestSku")



@_attrs_define
class PartialEditGlobalProductRequestSku:
    """ 
        Attributes:
            id (str | Unset): The global SKU ID in TikTok Shop. One product can contain multiple SKU IDs.

                **Note**:
                - To edit an existing SKU, include its SKU ID.
                - Any existing SKU IDs not listed here will result in the deletion of those SKUs. For example, if this product
                contains 5 SKUs and you only provide 2 SKU IDs, the remaining 3 will be deleted.
                - To create new SKUs, leave the SKU ID blank and complete the other fields.
            global_quantity (int | Unset): The total SKU inventory quantity across all shops globally.

                The inventory for each local shop is automatically calculated when a product is first published. After
                publishing, this global quantity cannot be manually changed. You can only modify the inventory quantity in each
                local shop.
            seller_sku (str | Unset): An internal code/name for managing SKUs, not visible to buyers.
                - Valid length: 1-50 characters
                - Format: Text without spaces
            price (CreateGlobalProductRequestSkuPrice | Unset):
            sales_attributes (list[CreateGlobalProductRequestSkuSalesAttribute] | Unset): A list of attributes  (e.g. size,
                color, length) that define each variant of a product.

                **Note**:
                - You must retain at least 1 sales attribute, deleting all existing sales attributes is not allowed.
                - You can only have up to 3 types of sales attributes per product.
                - Each SKU must include the same number and type of sales attributes. For example, you cannot have one SKU that
                has only a Color attribute, while another SKU has both Color and Size attributes.
                - Provide either a built-in ID or a custom name; if both are provided, the ID takes priority.
                - The `id/name` and `value_id/value_name` pairs must be unique in each SKU. For example, you cannot repeat
                `"name": "Color"`, `"value_name": "Red"` in different SKUs.
            inventory (list[CreateGlobalProductRequestSkuInventory] | Unset): SKU inventory information per warehouse.
                If multi-warehouse is enabled in Seller Center, you must provide the inventory details for each warehouse.
                Max count: 50

                **Note**: `global_quantity` will not take effect if inventory details are provided for each warehouse.
            identifier_code (IdentifierCode | Unset):
            sku_unit_count (str | Unset): The total quantity/volume of the product represented by the SKU.
                For example, if the SKU represents 500ml of water, this value would be 500 if the unit type is defined as ml.
                Valid range: [0.01, 99,999.9999]
                Applicable only for the EU market.

                **Note**:
                - This is mainly used to calculate the unit price of the SKU, and is required only if you wish to display the
                unit price to facilitate easier price comparisons across different products and packaging sizes.
                - Unit price = Selling price/(SKU unit count/base unit count). Therefore if you want to obtain the unit price,
                you would also need to define the "base unit count" and the "unit type" product attributes. Retrieve the
                relevant information for these product attributes by using the [Get Global Attributes
                API](https://partner.tiktokshop.com/docv2/page/650a0483c16ffe02b8dfc80a). The unit price would then be returned
                in the [Get Global Product API](https://partner.tiktokshop.com/docv2/page/6509e2b0bace3e02b7490c96).
            extra_identifier_codes (list[str] | Unset): If the SKU belongs to a virtual bundle (containing multiple
                individual SKUs), you can add up to 10 additional identifier codes here for the SKUs included in the bundle.

                **Format**:
                GTIN: 14 digits
                EAN: 8, 13, or 14 digits
                UPC: 12 digits
                ISBN: 13 digits, or 9 digits ending in capital `X`

                **Note**:
                - Applicable only for the EU market.
                - The identifier code must be unique for each SKU, with no repetition allowed.
            external_global_sku_id (str | Unset): An external identifier used in an external ecommerce platform. This is
                used to associate the global SKU between TikTok Shop and the external ecommerce platform.
                Max length: 999 characters
            sale_prices (list[PartialEditGlobalProductRequestSkuSalePrice] | Unset): The SKU's **local display price** shown
                on the product page before any discounts.

                **Note**:
                -  Required for JP and US shops using China warehouses, optional for others.
                - This is the definitive final price shown on the product page, all other prices will be ignored.
     """

    id: str | Unset = UNSET
    global_quantity: int | Unset = UNSET
    seller_sku: str | Unset = UNSET
    price: CreateGlobalProductRequestSkuPrice | Unset = UNSET
    sales_attributes: list[CreateGlobalProductRequestSkuSalesAttribute] | Unset = UNSET
    inventory: list[CreateGlobalProductRequestSkuInventory] | Unset = UNSET
    identifier_code: IdentifierCode | Unset = UNSET
    sku_unit_count: str | Unset = UNSET
    extra_identifier_codes: list[str] | Unset = UNSET
    external_global_sku_id: str | Unset = UNSET
    sale_prices: list[PartialEditGlobalProductRequestSkuSalePrice] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_global_product_request_sku_inventory import CreateGlobalProductRequestSkuInventory # noqa: PLC0415
        from ..models.create_global_product_request_sku_price import CreateGlobalProductRequestSkuPrice # noqa: PLC0415
        from ..models.create_global_product_request_sku_sales_attribute import CreateGlobalProductRequestSkuSalesAttribute # noqa: PLC0415
        from ..models.identifier_code import IdentifierCode # noqa: PLC0415
        from ..models.partial_edit_global_product_request_sku_sale_price import PartialEditGlobalProductRequestSkuSalePrice # noqa: PLC0415
        id = self.id

        global_quantity = self.global_quantity

        seller_sku = self.seller_sku

        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

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



        identifier_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier_code, Unset):
            identifier_code = self.identifier_code.to_dict()

        sku_unit_count = self.sku_unit_count

        extra_identifier_codes: list[str] | Unset = UNSET
        if not isinstance(self.extra_identifier_codes, Unset):
            extra_identifier_codes = self.extra_identifier_codes



        external_global_sku_id = self.external_global_sku_id

        sale_prices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sale_prices, Unset):
            sale_prices = []
            for sale_prices_item_data in self.sale_prices:
                sale_prices_item = sale_prices_item_data.to_dict()
                sale_prices.append(sale_prices_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if global_quantity is not UNSET:
            field_dict["global_quantity"] = global_quantity
        if seller_sku is not UNSET:
            field_dict["seller_sku"] = seller_sku
        if price is not UNSET:
            field_dict["price"] = price
        if sales_attributes is not UNSET:
            field_dict["sales_attributes"] = sales_attributes
        if inventory is not UNSET:
            field_dict["inventory"] = inventory
        if identifier_code is not UNSET:
            field_dict["identifier_code"] = identifier_code
        if sku_unit_count is not UNSET:
            field_dict["sku_unit_count"] = sku_unit_count
        if extra_identifier_codes is not UNSET:
            field_dict["extra_identifier_codes"] = extra_identifier_codes
        if external_global_sku_id is not UNSET:
            field_dict["external_global_sku_id"] = external_global_sku_id
        if sale_prices is not UNSET:
            field_dict["sale_prices"] = sale_prices

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_global_product_request_sku_inventory import CreateGlobalProductRequestSkuInventory # noqa: PLC0415
        from ..models.create_global_product_request_sku_price import CreateGlobalProductRequestSkuPrice # noqa: PLC0415
        from ..models.create_global_product_request_sku_sales_attribute import CreateGlobalProductRequestSkuSalesAttribute # noqa: PLC0415
        from ..models.identifier_code import IdentifierCode # noqa: PLC0415
        from ..models.partial_edit_global_product_request_sku_sale_price import PartialEditGlobalProductRequestSkuSalePrice # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        global_quantity = d.pop("global_quantity", UNSET)

        seller_sku = d.pop("seller_sku", UNSET)

        _price = d.pop("price", UNSET)
        price: CreateGlobalProductRequestSkuPrice | Unset
        if isinstance(_price,  Unset):
            price = UNSET
        else:
            price = CreateGlobalProductRequestSkuPrice.from_dict(_price)




        _sales_attributes = d.pop("sales_attributes", UNSET)
        sales_attributes: list[CreateGlobalProductRequestSkuSalesAttribute] | Unset = UNSET
        if _sales_attributes is not UNSET:
            sales_attributes = []
            for sales_attributes_item_data in _sales_attributes:
                sales_attributes_item = CreateGlobalProductRequestSkuSalesAttribute.from_dict(sales_attributes_item_data)



                sales_attributes.append(sales_attributes_item)


        _inventory = d.pop("inventory", UNSET)
        inventory: list[CreateGlobalProductRequestSkuInventory] | Unset = UNSET
        if _inventory is not UNSET:
            inventory = []
            for inventory_item_data in _inventory:
                inventory_item = CreateGlobalProductRequestSkuInventory.from_dict(inventory_item_data)



                inventory.append(inventory_item)


        _identifier_code = d.pop("identifier_code", UNSET)
        identifier_code: IdentifierCode | Unset
        if isinstance(_identifier_code,  Unset):
            identifier_code = UNSET
        else:
            identifier_code = IdentifierCode.from_dict(_identifier_code)




        sku_unit_count = d.pop("sku_unit_count", UNSET)

        extra_identifier_codes = cast(list[str], d.pop("extra_identifier_codes", UNSET))


        external_global_sku_id = d.pop("external_global_sku_id", UNSET)

        _sale_prices = d.pop("sale_prices", UNSET)
        sale_prices: list[PartialEditGlobalProductRequestSkuSalePrice] | Unset = UNSET
        if _sale_prices is not UNSET:
            sale_prices = []
            for sale_prices_item_data in _sale_prices:
                sale_prices_item = PartialEditGlobalProductRequestSkuSalePrice.from_dict(sale_prices_item_data)



                sale_prices.append(sale_prices_item)


        partial_edit_global_product_request_sku = cls(
            id=id,
            global_quantity=global_quantity,
            seller_sku=seller_sku,
            price=price,
            sales_attributes=sales_attributes,
            inventory=inventory,
            identifier_code=identifier_code,
            sku_unit_count=sku_unit_count,
            extra_identifier_codes=extra_identifier_codes,
            external_global_sku_id=external_global_sku_id,
            sale_prices=sale_prices,
        )


        partial_edit_global_product_request_sku.additional_properties = d
        return partial_edit_global_product_request_sku

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
