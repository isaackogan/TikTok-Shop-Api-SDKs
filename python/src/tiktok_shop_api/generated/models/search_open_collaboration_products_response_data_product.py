from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_chain import CategoryChain
    from ..models.commission import Commission
    from ..models.original_price import OriginalPrice
    from ..models.sales_price import SalesPrice
    from ..models.shop import Shop


T = TypeVar("T", bound="SearchOpenCollaborationProductsResponseDataProduct")


@_attrs_define
class SearchOpenCollaborationProductsResponseDataProduct:
    """
    Attributes:
        shop (Shop | Unset):
        id (str | Unset): The product identifier.
        has_inventory (bool | Unset): Set to `true` if there are more than zero units of the product in inventory. Set
            to `false` if there are zero units in inventory.
        units_sold (int | Unset): Total number of units sold. Units are indexed to SKU. Note that if the creator has not
            given permission for precise data sharing, this property will not be present.
        title (str | Unset): The product name.
        sale_region (str | Unset): The region where the product is offered for sale.
        main_image_url (str | Unset): The product image URL.
        detail_link (str | Unset): The URL for the product's detail page.
        original_price (OriginalPrice | Unset):
        category_chains (list[CategoryChain] | Unset): A list of categories associated with the product. Maximum length
            of the list is `3` categories.
        commission (Commission | Unset):
        sales_price (SalesPrice | Unset):
    """

    shop: Shop | Unset = UNSET
    id: str | Unset = UNSET
    has_inventory: bool | Unset = UNSET
    units_sold: int | Unset = UNSET
    title: str | Unset = UNSET
    sale_region: str | Unset = UNSET
    main_image_url: str | Unset = UNSET
    detail_link: str | Unset = UNSET
    original_price: OriginalPrice | Unset = UNSET
    category_chains: list[CategoryChain] | Unset = UNSET
    commission: Commission | Unset = UNSET
    sales_price: SalesPrice | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shop: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shop, Unset):
            shop = self.shop.to_dict()

        id = self.id

        has_inventory = self.has_inventory

        units_sold = self.units_sold

        title = self.title

        sale_region = self.sale_region

        main_image_url = self.main_image_url

        detail_link = self.detail_link

        original_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.original_price, Unset):
            original_price = self.original_price.to_dict()

        category_chains: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.category_chains, Unset):
            category_chains = []
            for category_chains_item_data in self.category_chains:
                category_chains_item = category_chains_item_data.to_dict()
                category_chains.append(category_chains_item)

        commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commission, Unset):
            commission = self.commission.to_dict()

        sales_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sales_price, Unset):
            sales_price = self.sales_price.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shop is not UNSET:
            field_dict["shop"] = shop
        if id is not UNSET:
            field_dict["id"] = id
        if has_inventory is not UNSET:
            field_dict["has_inventory"] = has_inventory
        if units_sold is not UNSET:
            field_dict["units_sold"] = units_sold
        if title is not UNSET:
            field_dict["title"] = title
        if sale_region is not UNSET:
            field_dict["sale_region"] = sale_region
        if main_image_url is not UNSET:
            field_dict["main_image_url"] = main_image_url
        if detail_link is not UNSET:
            field_dict["detail_link"] = detail_link
        if original_price is not UNSET:
            field_dict["original_price"] = original_price
        if category_chains is not UNSET:
            field_dict["category_chains"] = category_chains
        if commission is not UNSET:
            field_dict["commission"] = commission
        if sales_price is not UNSET:
            field_dict["sales_price"] = sales_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_chain import CategoryChain  # noqa: PLC0415
        from ..models.commission import Commission  # noqa: PLC0415
        from ..models.original_price import OriginalPrice  # noqa: PLC0415
        from ..models.sales_price import SalesPrice  # noqa: PLC0415
        from ..models.shop import Shop  # noqa: PLC0415

        d = dict(src_dict)
        _shop = d.pop("shop", UNSET)
        shop: Shop | Unset
        if isinstance(_shop, Unset):
            shop = UNSET
        else:
            shop = Shop.from_dict(_shop)

        id = d.pop("id", UNSET)

        has_inventory = d.pop("has_inventory", UNSET)

        units_sold = d.pop("units_sold", UNSET)

        title = d.pop("title", UNSET)

        sale_region = d.pop("sale_region", UNSET)

        main_image_url = d.pop("main_image_url", UNSET)

        detail_link = d.pop("detail_link", UNSET)

        _original_price = d.pop("original_price", UNSET)
        original_price: OriginalPrice | Unset
        if isinstance(_original_price, Unset):
            original_price = UNSET
        else:
            original_price = OriginalPrice.from_dict(_original_price)

        _category_chains = d.pop("category_chains", UNSET)
        category_chains: list[CategoryChain] | Unset = UNSET
        if _category_chains is not UNSET:
            category_chains = []
            for category_chains_item_data in _category_chains:
                category_chains_item = CategoryChain.from_dict(category_chains_item_data)

                category_chains.append(category_chains_item)

        _commission = d.pop("commission", UNSET)
        commission: Commission | Unset
        if isinstance(_commission, Unset):
            commission = UNSET
        else:
            commission = Commission.from_dict(_commission)

        _sales_price = d.pop("sales_price", UNSET)
        sales_price: SalesPrice | Unset
        if isinstance(_sales_price, Unset):
            sales_price = UNSET
        else:
            sales_price = SalesPrice.from_dict(_sales_price)

        search_open_collaboration_products_response_data_product = cls(
            shop=shop,
            id=id,
            has_inventory=has_inventory,
            units_sold=units_sold,
            title=title,
            sale_region=sale_region,
            main_image_url=main_image_url,
            detail_link=detail_link,
            original_price=original_price,
            category_chains=category_chains,
            commission=commission,
            sales_price=sales_price,
        )

        search_open_collaboration_products_response_data_product.additional_properties = d
        return search_open_collaboration_products_response_data_product

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
