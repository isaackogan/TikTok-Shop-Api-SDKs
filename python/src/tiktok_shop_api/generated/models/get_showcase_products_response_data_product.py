from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_showcase_products_response_data_product_addition import (
        GetShowcaseProductsResponseDataProductAddition,
    )
    from ..models.get_showcase_products_response_data_product_collaboration import (
        GetShowcaseProductsResponseDataProductCollaboration,
    )
    from ..models.get_showcase_products_response_data_product_commission import (
        GetShowcaseProductsResponseDataProductCommission,
    )
    from ..models.get_showcase_products_response_data_product_main_image import (
        GetShowcaseProductsResponseDataProductMainImage,
    )
    from ..models.get_showcase_products_response_data_product_price import GetShowcaseProductsResponseDataProductPrice
    from ..models.get_showcase_products_response_data_product_status import GetShowcaseProductsResponseDataProductStatus
    from ..models.shop import Shop


T = TypeVar("T", bound="GetShowcaseProductsResponseDataProduct")


@_attrs_define
class GetShowcaseProductsResponseDataProduct:
    """
    Attributes:
        id (str | Unset): The product's product ID
        shop (Shop | Unset):
        addition (GetShowcaseProductsResponseDataProductAddition | Unset):
        price (GetShowcaseProductsResponseDataProductPrice | Unset):
        title (str | Unset): The product's display title.
        main_images (list[GetShowcaseProductsResponseDataProductMainImage] | Unset): A list of product images.
        status (GetShowcaseProductsResponseDataProductStatus | Unset):
        source (str | Unset): The product source. This is an enumerated type with values:
            - THIRD_PARTY
            - AFFILIATE
            - TIKTOK_STORE
        detail_link (str | Unset): The product detail page URL.
        third_party_link (str | Unset): The off-TikTok Shop product detail page URL.
        sale_regions (list[str] | Unset): A list of regions in which the product is offered for sale.
        commission (GetShowcaseProductsResponseDataProductCommission | Unset):
        collaboration (GetShowcaseProductsResponseDataProductCollaboration | Unset):
    """

    id: str | Unset = UNSET
    shop: Shop | Unset = UNSET
    addition: GetShowcaseProductsResponseDataProductAddition | Unset = UNSET
    price: GetShowcaseProductsResponseDataProductPrice | Unset = UNSET
    title: str | Unset = UNSET
    main_images: list[GetShowcaseProductsResponseDataProductMainImage] | Unset = UNSET
    status: GetShowcaseProductsResponseDataProductStatus | Unset = UNSET
    source: str | Unset = UNSET
    detail_link: str | Unset = UNSET
    third_party_link: str | Unset = UNSET
    sale_regions: list[str] | Unset = UNSET
    commission: GetShowcaseProductsResponseDataProductCommission | Unset = UNSET
    collaboration: GetShowcaseProductsResponseDataProductCollaboration | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        shop: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shop, Unset):
            shop = self.shop.to_dict()

        addition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.addition, Unset):
            addition = self.addition.to_dict()

        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        title = self.title

        main_images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.main_images, Unset):
            main_images = []
            for main_images_item_data in self.main_images:
                main_images_item = main_images_item_data.to_dict()
                main_images.append(main_images_item)

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        source = self.source

        detail_link = self.detail_link

        third_party_link = self.third_party_link

        sale_regions: list[str] | Unset = UNSET
        if not isinstance(self.sale_regions, Unset):
            sale_regions = self.sale_regions

        commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commission, Unset):
            commission = self.commission.to_dict()

        collaboration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.collaboration, Unset):
            collaboration = self.collaboration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if shop is not UNSET:
            field_dict["shop"] = shop
        if addition is not UNSET:
            field_dict["addition"] = addition
        if price is not UNSET:
            field_dict["price"] = price
        if title is not UNSET:
            field_dict["title"] = title
        if main_images is not UNSET:
            field_dict["main_images"] = main_images
        if status is not UNSET:
            field_dict["status"] = status
        if source is not UNSET:
            field_dict["source"] = source
        if detail_link is not UNSET:
            field_dict["detail_link"] = detail_link
        if third_party_link is not UNSET:
            field_dict["third_party_link"] = third_party_link
        if sale_regions is not UNSET:
            field_dict["sale_regions"] = sale_regions
        if commission is not UNSET:
            field_dict["commission"] = commission
        if collaboration is not UNSET:
            field_dict["collaboration"] = collaboration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_showcase_products_response_data_product_addition import (
            GetShowcaseProductsResponseDataProductAddition,  # noqa: PLC0415
        )
        from ..models.get_showcase_products_response_data_product_collaboration import (
            GetShowcaseProductsResponseDataProductCollaboration,  # noqa: PLC0415
        )
        from ..models.get_showcase_products_response_data_product_commission import (
            GetShowcaseProductsResponseDataProductCommission,  # noqa: PLC0415
        )
        from ..models.get_showcase_products_response_data_product_main_image import (
            GetShowcaseProductsResponseDataProductMainImage,  # noqa: PLC0415
        )
        from ..models.get_showcase_products_response_data_product_price import (
            GetShowcaseProductsResponseDataProductPrice,  # noqa: PLC0415
        )
        from ..models.get_showcase_products_response_data_product_status import (
            GetShowcaseProductsResponseDataProductStatus,  # noqa: PLC0415
        )
        from ..models.shop import Shop  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _shop = d.pop("shop", UNSET)
        shop: Shop | Unset
        if isinstance(_shop, Unset):
            shop = UNSET
        else:
            shop = Shop.from_dict(_shop)

        _addition = d.pop("addition", UNSET)
        addition: GetShowcaseProductsResponseDataProductAddition | Unset
        if isinstance(_addition, Unset):
            addition = UNSET
        else:
            addition = GetShowcaseProductsResponseDataProductAddition.from_dict(_addition)

        _price = d.pop("price", UNSET)
        price: GetShowcaseProductsResponseDataProductPrice | Unset
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = GetShowcaseProductsResponseDataProductPrice.from_dict(_price)

        title = d.pop("title", UNSET)

        _main_images = d.pop("main_images", UNSET)
        main_images: list[GetShowcaseProductsResponseDataProductMainImage] | Unset = UNSET
        if _main_images is not UNSET:
            main_images = []
            for main_images_item_data in _main_images:
                main_images_item = GetShowcaseProductsResponseDataProductMainImage.from_dict(main_images_item_data)

                main_images.append(main_images_item)

        _status = d.pop("status", UNSET)
        status: GetShowcaseProductsResponseDataProductStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GetShowcaseProductsResponseDataProductStatus.from_dict(_status)

        source = d.pop("source", UNSET)

        detail_link = d.pop("detail_link", UNSET)

        third_party_link = d.pop("third_party_link", UNSET)

        sale_regions = cast(list[str], d.pop("sale_regions", UNSET))

        _commission = d.pop("commission", UNSET)
        commission: GetShowcaseProductsResponseDataProductCommission | Unset
        if isinstance(_commission, Unset):
            commission = UNSET
        else:
            commission = GetShowcaseProductsResponseDataProductCommission.from_dict(_commission)

        _collaboration = d.pop("collaboration", UNSET)
        collaboration: GetShowcaseProductsResponseDataProductCollaboration | Unset
        if isinstance(_collaboration, Unset):
            collaboration = UNSET
        else:
            collaboration = GetShowcaseProductsResponseDataProductCollaboration.from_dict(_collaboration)

        get_showcase_products_response_data_product = cls(
            id=id,
            shop=shop,
            addition=addition,
            price=price,
            title=title,
            main_images=main_images,
            status=status,
            source=source,
            detail_link=detail_link,
            third_party_link=third_party_link,
            sale_regions=sale_regions,
            commission=commission,
            collaboration=collaboration,
        )

        get_showcase_products_response_data_product.additional_properties = d
        return get_showcase_products_response_data_product

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
