from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.combined_sku import CombinedSku
    from ..models.create_product_request_sku_price import CreateProductRequestSkuPrice
    from ..models.create_product_request_sku_sales_attribute import CreateProductRequestSkuSalesAttribute
    from ..models.external_list_price import ExternalListPrice
    from ..models.fee import Fee
    from ..models.identifier_code import IdentifierCode
    from ..models.inventory import Inventory
    from ..models.list_price import ListPrice
    from ..models.pre_sale import PreSale
    from ..models.sku_dimension import SkuDimension
    from ..models.sku_weight import SkuWeight


T = TypeVar("T", bound="CreateProductRequestSku")


@_attrs_define
class CreateProductRequestSku:
    """
    Attributes:
        inventory (list[Inventory]): SKU inventory information.
        price (CreateProductRequestSkuPrice):
        sales_attributes (list[CreateProductRequestSkuSalesAttribute] | Unset): A list of attributes  (e.g. size, color,
            length) that define each variant of a product.

            **Note**:
            - You can omit this object if there is only 1 SKU. Otherwise, this is **required**.
            - You can only have up to 3 types of sales attributes per product.
            - Each SKU must include the same number and type of sales attributes. For example, you cannot have one SKU that
            has only a Color attribute, while another SKU has both Color and Size attributes.
            - Provide either a built-in ID or a custom name; if both are provided, the ID takes priority.
            - The `id/name` and `value_id/value_name` pairs must be unique in each SKU. For example, you cannot repeat
            `"name": "Color"`, `"value_name": "Red"` in different SKUs.
        seller_sku (str | Unset): An internal code/name for managing SKUs, not visible to buyers.
            Valid length:
            - DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: 6-50 characters
            - Other regions: 1-50 characters
            Format:
            - DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: Use alphabets, numbers, hyphens (-), or underscores (_) only
            - Other regions: Text without spaces
        external_sku_id (str | Unset): An external identifier used in an external ecommerce platform. This is used to
            associate the SKU between TikTok Shop and the external ecommerce platform.
            Max length: 999 characters
        identifier_code (IdentifierCode | Unset):
        combined_skus (list[CombinedSku] | Unset): If this SKU belongs to a virtual bundle, this object contains the
            list of individual SKUs that form the bundle (e.g. gift basket, starter pack).
        sku_unit_count (str | Unset): The total quantity/volume of the product represented by the SKU.
            For example, if the SKU represents 500ml of water, this value would be 500 if the unit type is defined as ml.
            Valid range: [0.01, 99,999.9999]
            Applicable only for the EU market.

            **Note**:
            - This is mainly used to calculate the unit price of the SKU, and is required only if you wish to display the
            unit price to facilitate easier price comparisons across different products and packaging sizes.
            - Unit price = Selling price/(SKU unit count/base unit count). Therefore if you want to obtain the unit price,
            you would also need to define the "base unit count" and the "unit type" product attributes. Retrieve the
            relevant information for these product attributes by using the [Get Attributes
            API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8). The unit price would then be returned
            in the [Get Product API](https://partner.tiktokshop.com/docv2/page/6509d85b4a0bb702c057fdda).
        external_urls (list[str] | Unset): A list of URLs for third-party product listing pages where consumers can
            place orders. Add this property if you have products listed on third-party sites other than TikTok Shop and
            would like to map them.
            Max string length: 500
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
        pre_sale (PreSale | Unset):
        list_price (ListPrice | Unset):
        external_list_prices (list[ExternalListPrice] | Unset): The SKU list price (e.g. MSRP, RRP) or original price
            information on external ecommerce platforms.
            Applicable only for selected sellers in the US market.

            **Note**: This value may appear as the strikethrough price on the product page. However, whether the
            strikethrough price is shown and the amount shown are subject to the audit team's review and decision based on
            various pricing information.
        fees (list[Fee] | Unset): The fees required for this product based on TikTok Shop policies. Fees are required
            only for certain product categories, retrieve the requirements from the [Get Category Rules
            API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9).
        sku_dimensions (SkuDimension | Unset):
        sku_weight (SkuWeight | Unset):
    """

    inventory: list[Inventory]
    price: CreateProductRequestSkuPrice
    sales_attributes: list[CreateProductRequestSkuSalesAttribute] | Unset = UNSET
    seller_sku: str | Unset = UNSET
    external_sku_id: str | Unset = UNSET
    identifier_code: IdentifierCode | Unset = UNSET
    combined_skus: list[CombinedSku] | Unset = UNSET
    sku_unit_count: str | Unset = UNSET
    external_urls: list[str] | Unset = UNSET
    extra_identifier_codes: list[str] | Unset = UNSET
    pre_sale: PreSale | Unset = UNSET
    list_price: ListPrice | Unset = UNSET
    external_list_prices: list[ExternalListPrice] | Unset = UNSET
    fees: list[Fee] | Unset = UNSET
    sku_dimensions: SkuDimension | Unset = UNSET
    sku_weight: SkuWeight | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inventory = []
        for inventory_item_data in self.inventory:
            inventory_item = inventory_item_data.to_dict()
            inventory.append(inventory_item)

        price = self.price.to_dict()

        sales_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sales_attributes, Unset):
            sales_attributes = []
            for sales_attributes_item_data in self.sales_attributes:
                sales_attributes_item = sales_attributes_item_data.to_dict()
                sales_attributes.append(sales_attributes_item)

        seller_sku = self.seller_sku

        external_sku_id = self.external_sku_id

        identifier_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier_code, Unset):
            identifier_code = self.identifier_code.to_dict()

        combined_skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.combined_skus, Unset):
            combined_skus = []
            for combined_skus_item_data in self.combined_skus:
                combined_skus_item = combined_skus_item_data.to_dict()
                combined_skus.append(combined_skus_item)

        sku_unit_count = self.sku_unit_count

        external_urls: list[str] | Unset = UNSET
        if not isinstance(self.external_urls, Unset):
            external_urls = self.external_urls

        extra_identifier_codes: list[str] | Unset = UNSET
        if not isinstance(self.extra_identifier_codes, Unset):
            extra_identifier_codes = self.extra_identifier_codes

        pre_sale: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pre_sale, Unset):
            pre_sale = self.pre_sale.to_dict()

        list_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.list_price, Unset):
            list_price = self.list_price.to_dict()

        external_list_prices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.external_list_prices, Unset):
            external_list_prices = []
            for external_list_prices_item_data in self.external_list_prices:
                external_list_prices_item = external_list_prices_item_data.to_dict()
                external_list_prices.append(external_list_prices_item)

        fees: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fees, Unset):
            fees = []
            for fees_item_data in self.fees:
                fees_item = fees_item_data.to_dict()
                fees.append(fees_item)

        sku_dimensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sku_dimensions, Unset):
            sku_dimensions = self.sku_dimensions.to_dict()

        sku_weight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sku_weight, Unset):
            sku_weight = self.sku_weight.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inventory": inventory,
                "price": price,
            }
        )
        if sales_attributes is not UNSET:
            field_dict["sales_attributes"] = sales_attributes
        if seller_sku is not UNSET:
            field_dict["seller_sku"] = seller_sku
        if external_sku_id is not UNSET:
            field_dict["external_sku_id"] = external_sku_id
        if identifier_code is not UNSET:
            field_dict["identifier_code"] = identifier_code
        if combined_skus is not UNSET:
            field_dict["combined_skus"] = combined_skus
        if sku_unit_count is not UNSET:
            field_dict["sku_unit_count"] = sku_unit_count
        if external_urls is not UNSET:
            field_dict["external_urls"] = external_urls
        if extra_identifier_codes is not UNSET:
            field_dict["extra_identifier_codes"] = extra_identifier_codes
        if pre_sale is not UNSET:
            field_dict["pre_sale"] = pre_sale
        if list_price is not UNSET:
            field_dict["list_price"] = list_price
        if external_list_prices is not UNSET:
            field_dict["external_list_prices"] = external_list_prices
        if fees is not UNSET:
            field_dict["fees"] = fees
        if sku_dimensions is not UNSET:
            field_dict["sku_dimensions"] = sku_dimensions
        if sku_weight is not UNSET:
            field_dict["sku_weight"] = sku_weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.combined_sku import CombinedSku  # noqa: PLC0415
        from ..models.create_product_request_sku_price import CreateProductRequestSkuPrice  # noqa: PLC0415
        from ..models.create_product_request_sku_sales_attribute import (
            CreateProductRequestSkuSalesAttribute,  # noqa: PLC0415
        )
        from ..models.external_list_price import ExternalListPrice  # noqa: PLC0415
        from ..models.fee import Fee  # noqa: PLC0415
        from ..models.identifier_code import IdentifierCode  # noqa: PLC0415
        from ..models.inventory import Inventory  # noqa: PLC0415
        from ..models.list_price import ListPrice  # noqa: PLC0415
        from ..models.pre_sale import PreSale  # noqa: PLC0415
        from ..models.sku_dimension import SkuDimension  # noqa: PLC0415
        from ..models.sku_weight import SkuWeight  # noqa: PLC0415

        d = dict(src_dict)
        inventory = []
        _inventory = d.pop("inventory")
        for inventory_item_data in _inventory:
            inventory_item = Inventory.from_dict(inventory_item_data)

            inventory.append(inventory_item)

        price = CreateProductRequestSkuPrice.from_dict(d.pop("price"))

        _sales_attributes = d.pop("sales_attributes", UNSET)
        sales_attributes: list[CreateProductRequestSkuSalesAttribute] | Unset = UNSET
        if _sales_attributes is not UNSET:
            sales_attributes = []
            for sales_attributes_item_data in _sales_attributes:
                sales_attributes_item = CreateProductRequestSkuSalesAttribute.from_dict(sales_attributes_item_data)

                sales_attributes.append(sales_attributes_item)

        seller_sku = d.pop("seller_sku", UNSET)

        external_sku_id = d.pop("external_sku_id", UNSET)

        _identifier_code = d.pop("identifier_code", UNSET)
        identifier_code: IdentifierCode | Unset
        if isinstance(_identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = IdentifierCode.from_dict(_identifier_code)

        _combined_skus = d.pop("combined_skus", UNSET)
        combined_skus: list[CombinedSku] | Unset = UNSET
        if _combined_skus is not UNSET:
            combined_skus = []
            for combined_skus_item_data in _combined_skus:
                combined_skus_item = CombinedSku.from_dict(combined_skus_item_data)

                combined_skus.append(combined_skus_item)

        sku_unit_count = d.pop("sku_unit_count", UNSET)

        external_urls = cast(list[str], d.pop("external_urls", UNSET))

        extra_identifier_codes = cast(list[str], d.pop("extra_identifier_codes", UNSET))

        _pre_sale = d.pop("pre_sale", UNSET)
        pre_sale: PreSale | Unset
        if isinstance(_pre_sale, Unset):
            pre_sale = UNSET
        else:
            pre_sale = PreSale.from_dict(_pre_sale)

        _list_price = d.pop("list_price", UNSET)
        list_price: ListPrice | Unset
        if isinstance(_list_price, Unset):
            list_price = UNSET
        else:
            list_price = ListPrice.from_dict(_list_price)

        _external_list_prices = d.pop("external_list_prices", UNSET)
        external_list_prices: list[ExternalListPrice] | Unset = UNSET
        if _external_list_prices is not UNSET:
            external_list_prices = []
            for external_list_prices_item_data in _external_list_prices:
                external_list_prices_item = ExternalListPrice.from_dict(external_list_prices_item_data)

                external_list_prices.append(external_list_prices_item)

        _fees = d.pop("fees", UNSET)
        fees: list[Fee] | Unset = UNSET
        if _fees is not UNSET:
            fees = []
            for fees_item_data in _fees:
                fees_item = Fee.from_dict(fees_item_data)

                fees.append(fees_item)

        _sku_dimensions = d.pop("sku_dimensions", UNSET)
        sku_dimensions: SkuDimension | Unset
        if isinstance(_sku_dimensions, Unset):
            sku_dimensions = UNSET
        else:
            sku_dimensions = SkuDimension.from_dict(_sku_dimensions)

        _sku_weight = d.pop("sku_weight", UNSET)
        sku_weight: SkuWeight | Unset
        if isinstance(_sku_weight, Unset):
            sku_weight = UNSET
        else:
            sku_weight = SkuWeight.from_dict(_sku_weight)

        create_product_request_sku = cls(
            inventory=inventory,
            price=price,
            sales_attributes=sales_attributes,
            seller_sku=seller_sku,
            external_sku_id=external_sku_id,
            identifier_code=identifier_code,
            combined_skus=combined_skus,
            sku_unit_count=sku_unit_count,
            external_urls=external_urls,
            extra_identifier_codes=extra_identifier_codes,
            pre_sale=pre_sale,
            list_price=list_price,
            external_list_prices=external_list_prices,
            fees=fees,
            sku_dimensions=sku_dimensions,
            sku_weight=sku_weight,
        )

        create_product_request_sku.additional_properties = d
        return create_product_request_sku

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
