from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_price import ActivityPrice
    from ..models.get_activity_response_data_product_sku import GetActivityResponseDataProductSku


T = TypeVar("T", bound="GetActivityResponseDataProduct")


@_attrs_define
class GetActivityResponseDataProduct:
    """
    Attributes:
        id (str | Unset): TikTok Shop Product ID.
        activity_price (ActivityPrice | Unset):
        quantity_limit (int | Unset): The quantity limit of the products involved in the activity. The range is `[1,
            99]`, or `-1` for unlimited.
        quantity_per_user (int | Unset): Limit of product purchase per buyer. The range is `[1, 99]`, or `-1` for
            unlimited.
        discount (str | Unset): Discount value. If the product is 10% off, the value is `10`. Available only if
            `activity_type==DIRECT_DISCOUNT` and `product_level==PRODUCT`.
        skus (list[GetActivityResponseDataProductSku] | Unset): Available only if `product_level==VARIATION`.
        used_quantity (int | Unset): The quantity of products that have already taken effect in the activity.
    """

    id: str | Unset = UNSET
    activity_price: ActivityPrice | Unset = UNSET
    quantity_limit: int | Unset = UNSET
    quantity_per_user: int | Unset = UNSET
    discount: str | Unset = UNSET
    skus: list[GetActivityResponseDataProductSku] | Unset = UNSET
    used_quantity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        activity_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activity_price, Unset):
            activity_price = self.activity_price.to_dict()

        quantity_limit = self.quantity_limit

        quantity_per_user = self.quantity_per_user

        discount = self.discount

        skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skus, Unset):
            skus = []
            for skus_item_data in self.skus:
                skus_item = skus_item_data.to_dict()
                skus.append(skus_item)

        used_quantity = self.used_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if activity_price is not UNSET:
            field_dict["activity_price"] = activity_price
        if quantity_limit is not UNSET:
            field_dict["quantity_limit"] = quantity_limit
        if quantity_per_user is not UNSET:
            field_dict["quantity_per_user"] = quantity_per_user
        if discount is not UNSET:
            field_dict["discount"] = discount
        if skus is not UNSET:
            field_dict["skus"] = skus
        if used_quantity is not UNSET:
            field_dict["used_quantity"] = used_quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_price import ActivityPrice  # noqa: PLC0415
        from ..models.get_activity_response_data_product_sku import GetActivityResponseDataProductSku  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _activity_price = d.pop("activity_price", UNSET)
        activity_price: ActivityPrice | Unset
        if isinstance(_activity_price, Unset):
            activity_price = UNSET
        else:
            activity_price = ActivityPrice.from_dict(_activity_price)

        quantity_limit = d.pop("quantity_limit", UNSET)

        quantity_per_user = d.pop("quantity_per_user", UNSET)

        discount = d.pop("discount", UNSET)

        _skus = d.pop("skus", UNSET)
        skus: list[GetActivityResponseDataProductSku] | Unset = UNSET
        if _skus is not UNSET:
            skus = []
            for skus_item_data in _skus:
                skus_item = GetActivityResponseDataProductSku.from_dict(skus_item_data)

                skus.append(skus_item)

        used_quantity = d.pop("used_quantity", UNSET)

        get_activity_response_data_product = cls(
            id=id,
            activity_price=activity_price,
            quantity_limit=quantity_limit,
            quantity_per_user=quantity_per_user,
            discount=discount,
            skus=skus,
            used_quantity=used_quantity,
        )

        get_activity_response_data_product.additional_properties = d
        return get_activity_response_data_product

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
