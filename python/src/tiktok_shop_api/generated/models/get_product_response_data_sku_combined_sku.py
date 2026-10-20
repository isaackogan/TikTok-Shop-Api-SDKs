from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brand import Brand
    from ..models.get_product_response_data_sku_combined_sku_category import (
        GetProductResponseDataSkuCombinedSkuCategory,
    )
    from ..models.get_product_response_data_sku_combined_sku_inventory import (
        GetProductResponseDataSkuCombinedSkuInventory,
    )
    from ..models.get_product_response_data_sku_combined_sku_price import GetProductResponseDataSkuCombinedSkuPrice
    from ..models.get_product_response_data_sku_combined_sku_product_main_image import (
        GetProductResponseDataSkuCombinedSkuProductMainImage,
    )
    from ..models.get_product_response_data_sku_combined_sku_sales_attribute import (
        GetProductResponseDataSkuCombinedSkuSalesAttribute,
    )


T = TypeVar("T", bound="GetProductResponseDataSkuCombinedSku")


@_attrs_define
class GetProductResponseDataSkuCombinedSku:
    """
    Attributes:
        brand (Brand | Unset):
        categories (list[GetProductResponseDataSkuCombinedSkuCategory] | Unset): The category tree information of the
            source product included in the virtual bundle.
        combined_listing_not_live_reasons (list[str] | Unset): The reasons linked to the source product included in the
            virtual bundle that are keeping the virtual bundle status from being live.
            Possible values:
            - SUB_PRODUCT_DEACTIVATE: Indicate the source product has been deactivated.
            - SUB_PRODUCT_DELETE: Indicate the source product has been deleted.
            - SUB_PRODUCT_FROZEN: Indicate the source product has been frozen.
            - SUB_SKU_DELETE: Indicate the source SKU has been deleted.
            - SUB_PRODUCT_CATEGORY_FIRST_LEVEL_ERROR: Indicate the level one category of the virtual bundle does not match
            that of the source product.
            - SUB_PRODUCT_CATEGORY_OVER_RESTRICTION:  Indicate the level one category of the source product is not in the
            set of restricted categories.
        inventory (list[GetProductResponseDataSkuCombinedSkuInventory] | Unset): Source SKU inventory details.
        price (GetProductResponseDataSkuCombinedSkuPrice | Unset):
        product_id (str | Unset): The ID of the source product included in the virtual bundle.
        product_main_image (GetProductResponseDataSkuCombinedSkuProductMainImage | Unset):
        sales_attributes (list[GetProductResponseDataSkuCombinedSkuSalesAttribute] | Unset): A list of attributes  (e.g.
            size, color, length) that define the source SKU.
        seller_sku (str | Unset): An internal code/name for managing the source SKU, not visible to buyers.
        sku_count (int | Unset): The quantity of the source SKU included in the virtual bundle.
        sku_id (str | Unset): The ID of the source SKU included in the virtual bundle.
        title (str | Unset): The title of the source product included in the virtual bundle.
    """

    brand: Brand | Unset = UNSET
    categories: list[GetProductResponseDataSkuCombinedSkuCategory] | Unset = UNSET
    combined_listing_not_live_reasons: list[str] | Unset = UNSET
    inventory: list[GetProductResponseDataSkuCombinedSkuInventory] | Unset = UNSET
    price: GetProductResponseDataSkuCombinedSkuPrice | Unset = UNSET
    product_id: str | Unset = UNSET
    product_main_image: GetProductResponseDataSkuCombinedSkuProductMainImage | Unset = UNSET
    sales_attributes: list[GetProductResponseDataSkuCombinedSkuSalesAttribute] | Unset = UNSET
    seller_sku: str | Unset = UNSET
    sku_count: int | Unset = UNSET
    sku_id: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand: dict[str, Any] | Unset = UNSET
        if not isinstance(self.brand, Unset):
            brand = self.brand.to_dict()

        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        combined_listing_not_live_reasons: list[str] | Unset = UNSET
        if not isinstance(self.combined_listing_not_live_reasons, Unset):
            combined_listing_not_live_reasons = self.combined_listing_not_live_reasons

        inventory: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inventory, Unset):
            inventory = []
            for inventory_item_data in self.inventory:
                inventory_item = inventory_item_data.to_dict()
                inventory.append(inventory_item)

        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        product_id = self.product_id

        product_main_image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_main_image, Unset):
            product_main_image = self.product_main_image.to_dict()

        sales_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sales_attributes, Unset):
            sales_attributes = []
            for sales_attributes_item_data in self.sales_attributes:
                sales_attributes_item = sales_attributes_item_data.to_dict()
                sales_attributes.append(sales_attributes_item)

        seller_sku = self.seller_sku

        sku_count = self.sku_count

        sku_id = self.sku_id

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if brand is not UNSET:
            field_dict["brand"] = brand
        if categories is not UNSET:
            field_dict["categories"] = categories
        if combined_listing_not_live_reasons is not UNSET:
            field_dict["combined_listing_not_live_reasons"] = combined_listing_not_live_reasons
        if inventory is not UNSET:
            field_dict["inventory"] = inventory
        if price is not UNSET:
            field_dict["price"] = price
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_main_image is not UNSET:
            field_dict["product_main_image"] = product_main_image
        if sales_attributes is not UNSET:
            field_dict["sales_attributes"] = sales_attributes
        if seller_sku is not UNSET:
            field_dict["seller_sku"] = seller_sku
        if sku_count is not UNSET:
            field_dict["sku_count"] = sku_count
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brand import Brand  # noqa: PLC0415
        from ..models.get_product_response_data_sku_combined_sku_category import (
            GetProductResponseDataSkuCombinedSkuCategory,  # noqa: PLC0415
        )
        from ..models.get_product_response_data_sku_combined_sku_inventory import (
            GetProductResponseDataSkuCombinedSkuInventory,  # noqa: PLC0415
        )
        from ..models.get_product_response_data_sku_combined_sku_price import (
            GetProductResponseDataSkuCombinedSkuPrice,  # noqa: PLC0415
        )
        from ..models.get_product_response_data_sku_combined_sku_product_main_image import (
            GetProductResponseDataSkuCombinedSkuProductMainImage,  # noqa: PLC0415
        )
        from ..models.get_product_response_data_sku_combined_sku_sales_attribute import (
            GetProductResponseDataSkuCombinedSkuSalesAttribute,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _brand = d.pop("brand", UNSET)
        brand: Brand | Unset
        if isinstance(_brand, Unset):
            brand = UNSET
        else:
            brand = Brand.from_dict(_brand)

        _categories = d.pop("categories", UNSET)
        categories: list[GetProductResponseDataSkuCombinedSkuCategory] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = GetProductResponseDataSkuCombinedSkuCategory.from_dict(categories_item_data)

                categories.append(categories_item)

        combined_listing_not_live_reasons = cast(list[str], d.pop("combined_listing_not_live_reasons", UNSET))

        _inventory = d.pop("inventory", UNSET)
        inventory: list[GetProductResponseDataSkuCombinedSkuInventory] | Unset = UNSET
        if _inventory is not UNSET:
            inventory = []
            for inventory_item_data in _inventory:
                inventory_item = GetProductResponseDataSkuCombinedSkuInventory.from_dict(inventory_item_data)

                inventory.append(inventory_item)

        _price = d.pop("price", UNSET)
        price: GetProductResponseDataSkuCombinedSkuPrice | Unset
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = GetProductResponseDataSkuCombinedSkuPrice.from_dict(_price)

        product_id = d.pop("product_id", UNSET)

        _product_main_image = d.pop("product_main_image", UNSET)
        product_main_image: GetProductResponseDataSkuCombinedSkuProductMainImage | Unset
        if isinstance(_product_main_image, Unset):
            product_main_image = UNSET
        else:
            product_main_image = GetProductResponseDataSkuCombinedSkuProductMainImage.from_dict(_product_main_image)

        _sales_attributes = d.pop("sales_attributes", UNSET)
        sales_attributes: list[GetProductResponseDataSkuCombinedSkuSalesAttribute] | Unset = UNSET
        if _sales_attributes is not UNSET:
            sales_attributes = []
            for sales_attributes_item_data in _sales_attributes:
                sales_attributes_item = GetProductResponseDataSkuCombinedSkuSalesAttribute.from_dict(
                    sales_attributes_item_data
                )

                sales_attributes.append(sales_attributes_item)

        seller_sku = d.pop("seller_sku", UNSET)

        sku_count = d.pop("sku_count", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        title = d.pop("title", UNSET)

        get_product_response_data_sku_combined_sku = cls(
            brand=brand,
            categories=categories,
            combined_listing_not_live_reasons=combined_listing_not_live_reasons,
            inventory=inventory,
            price=price,
            product_id=product_id,
            product_main_image=product_main_image,
            sales_attributes=sales_attributes,
            seller_sku=seller_sku,
            sku_count=sku_count,
            sku_id=sku_id,
            title=title,
        )

        get_product_response_data_sku_combined_sku.additional_properties = d
        return get_product_response_data_sku_combined_sku

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
