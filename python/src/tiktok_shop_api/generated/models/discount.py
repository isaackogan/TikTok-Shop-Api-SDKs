from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bxgy_discount import BxgyDiscount
    from ..models.discount_bmsm_discount import DiscountBmsmDiscount
    from ..models.gift_discount import GiftDiscount
    from ..models.shipping_discount import ShippingDiscount


T = TypeVar("T", bound="Discount")


@_attrs_define
class Discount:
    """
    Attributes:
        shipping_discount (ShippingDiscount | Unset):
        bmsm_discount (DiscountBmsmDiscount | Unset):
        gift_discount (GiftDiscount | Unset):
        bxgy_discount (BxgyDiscount | Unset):
    """

    shipping_discount: ShippingDiscount | Unset = UNSET
    bmsm_discount: DiscountBmsmDiscount | Unset = UNSET
    gift_discount: GiftDiscount | Unset = UNSET
    bxgy_discount: BxgyDiscount | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shipping_discount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shipping_discount, Unset):
            shipping_discount = self.shipping_discount.to_dict()

        bmsm_discount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bmsm_discount, Unset):
            bmsm_discount = self.bmsm_discount.to_dict()

        gift_discount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gift_discount, Unset):
            gift_discount = self.gift_discount.to_dict()

        bxgy_discount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bxgy_discount, Unset):
            bxgy_discount = self.bxgy_discount.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipping_discount is not UNSET:
            field_dict["shipping_discount"] = shipping_discount
        if bmsm_discount is not UNSET:
            field_dict["bmsm_discount"] = bmsm_discount
        if gift_discount is not UNSET:
            field_dict["gift_discount"] = gift_discount
        if bxgy_discount is not UNSET:
            field_dict["bxgy_discount"] = bxgy_discount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bxgy_discount import BxgyDiscount  # noqa: PLC0415
        from ..models.discount_bmsm_discount import DiscountBmsmDiscount  # noqa: PLC0415
        from ..models.gift_discount import GiftDiscount  # noqa: PLC0415
        from ..models.shipping_discount import ShippingDiscount  # noqa: PLC0415

        d = dict(src_dict)
        _shipping_discount = d.pop("shipping_discount", UNSET)
        shipping_discount: ShippingDiscount | Unset
        if isinstance(_shipping_discount, Unset):
            shipping_discount = UNSET
        else:
            shipping_discount = ShippingDiscount.from_dict(_shipping_discount)

        _bmsm_discount = d.pop("bmsm_discount", UNSET)
        bmsm_discount: DiscountBmsmDiscount | Unset
        if isinstance(_bmsm_discount, Unset):
            bmsm_discount = UNSET
        else:
            bmsm_discount = DiscountBmsmDiscount.from_dict(_bmsm_discount)

        _gift_discount = d.pop("gift_discount", UNSET)
        gift_discount: GiftDiscount | Unset
        if isinstance(_gift_discount, Unset):
            gift_discount = UNSET
        else:
            gift_discount = GiftDiscount.from_dict(_gift_discount)

        _bxgy_discount = d.pop("bxgy_discount", UNSET)
        bxgy_discount: BxgyDiscount | Unset
        if isinstance(_bxgy_discount, Unset):
            bxgy_discount = UNSET
        else:
            bxgy_discount = BxgyDiscount.from_dict(_bxgy_discount)

        discount = cls(
            shipping_discount=shipping_discount,
            bmsm_discount=bmsm_discount,
            gift_discount=gift_discount,
            bxgy_discount=bxgy_discount,
        )

        discount.additional_properties = d
        return discount

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
