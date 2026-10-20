from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.local_gmv import LocalGmv
  from ..models.local_unit_price import LocalUnitPrice





T = TypeVar("T", bound="GetLiveRoomProductStatsResponseDataProductStat")



@_attrs_define
class GetLiveRoomProductStatsResponseDataProductStat:
    """ 
        Attributes:
            main_image_url (str | Unset): The main image of product URL
            product_id (str | Unset): Unique ID for each product
            is_live (bool | Unset): If the item is currently on sale in the livestream room
            click_through_rate (str | Unset): The ratio of product clicks to product impressions
            sellable_region (str | Unset): The region where products sells
            created_order_count (int | Unset): The number of orders created for this product by users from the livestream
            exposure_count (int | Unset): The number of impressions of this product, including in the product list and
                product cards
            total_click_count (int | Unset): The total number of times the product was clicked from this livestream,
                including from the product list and product card
            local_gmv (LocalGmv | Unset):
            product_name (str | Unset): The display name of the product in the live room product stats list.
            local_unit_price (LocalUnitPrice | Unset):
            paid_order_count (int | Unset): The number of SKU orders created and paid by users for this product from the
                livestream room
            inventory_left_count (int | Unset): The remaining inventory of the product
            inventory_consumption_count (int | Unset): The number of product units sold
            created_order_user_count (int | Unset): Number of unique users who created orders for this product
            paid_user_count (int | Unset): Number of unique users who paid orders for this product
            click_order_rate (str | Unset): Product paid SKU orders/Product clicks
     """

    main_image_url: str | Unset = UNSET
    product_id: str | Unset = UNSET
    is_live: bool | Unset = UNSET
    click_through_rate: str | Unset = UNSET
    sellable_region: str | Unset = UNSET
    created_order_count: int | Unset = UNSET
    exposure_count: int | Unset = UNSET
    total_click_count: int | Unset = UNSET
    local_gmv: LocalGmv | Unset = UNSET
    product_name: str | Unset = UNSET
    local_unit_price: LocalUnitPrice | Unset = UNSET
    paid_order_count: int | Unset = UNSET
    inventory_left_count: int | Unset = UNSET
    inventory_consumption_count: int | Unset = UNSET
    created_order_user_count: int | Unset = UNSET
    paid_user_count: int | Unset = UNSET
    click_order_rate: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.local_gmv import LocalGmv # noqa: PLC0415
        from ..models.local_unit_price import LocalUnitPrice # noqa: PLC0415
        main_image_url = self.main_image_url

        product_id = self.product_id

        is_live = self.is_live

        click_through_rate = self.click_through_rate

        sellable_region = self.sellable_region

        created_order_count = self.created_order_count

        exposure_count = self.exposure_count

        total_click_count = self.total_click_count

        local_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.local_gmv, Unset):
            local_gmv = self.local_gmv.to_dict()

        product_name = self.product_name

        local_unit_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.local_unit_price, Unset):
            local_unit_price = self.local_unit_price.to_dict()

        paid_order_count = self.paid_order_count

        inventory_left_count = self.inventory_left_count

        inventory_consumption_count = self.inventory_consumption_count

        created_order_user_count = self.created_order_user_count

        paid_user_count = self.paid_user_count

        click_order_rate = self.click_order_rate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if main_image_url is not UNSET:
            field_dict["main_image_url"] = main_image_url
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if is_live is not UNSET:
            field_dict["is_live"] = is_live
        if click_through_rate is not UNSET:
            field_dict["click_through_rate"] = click_through_rate
        if sellable_region is not UNSET:
            field_dict["sellable_region"] = sellable_region
        if created_order_count is not UNSET:
            field_dict["created_order_count"] = created_order_count
        if exposure_count is not UNSET:
            field_dict["exposure_count"] = exposure_count
        if total_click_count is not UNSET:
            field_dict["total_click_count"] = total_click_count
        if local_gmv is not UNSET:
            field_dict["local_gmv"] = local_gmv
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if local_unit_price is not UNSET:
            field_dict["local_unit_price"] = local_unit_price
        if paid_order_count is not UNSET:
            field_dict["paid_order_count"] = paid_order_count
        if inventory_left_count is not UNSET:
            field_dict["inventory_left_count"] = inventory_left_count
        if inventory_consumption_count is not UNSET:
            field_dict["inventory_consumption_count"] = inventory_consumption_count
        if created_order_user_count is not UNSET:
            field_dict["created_order_user_count"] = created_order_user_count
        if paid_user_count is not UNSET:
            field_dict["paid_user_count"] = paid_user_count
        if click_order_rate is not UNSET:
            field_dict["click_order_rate"] = click_order_rate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.local_gmv import LocalGmv # noqa: PLC0415
        from ..models.local_unit_price import LocalUnitPrice # noqa: PLC0415
        d = dict(src_dict)
        main_image_url = d.pop("main_image_url", UNSET)

        product_id = d.pop("product_id", UNSET)

        is_live = d.pop("is_live", UNSET)

        click_through_rate = d.pop("click_through_rate", UNSET)

        sellable_region = d.pop("sellable_region", UNSET)

        created_order_count = d.pop("created_order_count", UNSET)

        exposure_count = d.pop("exposure_count", UNSET)

        total_click_count = d.pop("total_click_count", UNSET)

        _local_gmv = d.pop("local_gmv", UNSET)
        local_gmv: LocalGmv | Unset
        if isinstance(_local_gmv,  Unset):
            local_gmv = UNSET
        else:
            local_gmv = LocalGmv.from_dict(_local_gmv)




        product_name = d.pop("product_name", UNSET)

        _local_unit_price = d.pop("local_unit_price", UNSET)
        local_unit_price: LocalUnitPrice | Unset
        if isinstance(_local_unit_price,  Unset):
            local_unit_price = UNSET
        else:
            local_unit_price = LocalUnitPrice.from_dict(_local_unit_price)




        paid_order_count = d.pop("paid_order_count", UNSET)

        inventory_left_count = d.pop("inventory_left_count", UNSET)

        inventory_consumption_count = d.pop("inventory_consumption_count", UNSET)

        created_order_user_count = d.pop("created_order_user_count", UNSET)

        paid_user_count = d.pop("paid_user_count", UNSET)

        click_order_rate = d.pop("click_order_rate", UNSET)

        get_live_room_product_stats_response_data_product_stat = cls(
            main_image_url=main_image_url,
            product_id=product_id,
            is_live=is_live,
            click_through_rate=click_through_rate,
            sellable_region=sellable_region,
            created_order_count=created_order_count,
            exposure_count=exposure_count,
            total_click_count=total_click_count,
            local_gmv=local_gmv,
            product_name=product_name,
            local_unit_price=local_unit_price,
            paid_order_count=paid_order_count,
            inventory_left_count=inventory_left_count,
            inventory_consumption_count=inventory_consumption_count,
            created_order_user_count=created_order_user_count,
            paid_user_count=paid_user_count,
            click_order_rate=click_order_rate,
        )


        get_live_room_product_stats_response_data_product_stat.additional_properties = d
        return get_live_room_product_stats_response_data_product_stat

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
