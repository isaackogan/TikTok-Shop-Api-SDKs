from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_fbtmcf_order_status_webhook_data_mcf_order_consign_order_good import (
        GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrderGood,
    )
    from ..models.get_fbtmcf_order_status_webhook_data_mcf_order_consign_order_shipping_provider import (
        GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrderShippingProvider,
    )


T = TypeVar("T", bound="GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrder")


@_attrs_define
class GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrder:
    """
    Attributes:
        id (str | Unset): `consign order` unique id
        tracking_number (None | str | Unset): The tracking number of this consign order. If the order has not yet been
            handed over to the logistics carrier, this field may be a null value.
        status (str | Unset): The status of this consign order

             Possible Status Enumerations
             1. **SHIPPED** - Order has been shipped out from the warehouse
             2. **HANDOVER** - Order has been received by the logistics carrier and is in transit
             3. **CLOSED** - Order has been closed
             4. **LOST** - Order is lost
             5. **DAMAGE** - Order is damaged
             6. **COMPLETED** - Order has been completed
             7. **ABNORMAL** - There is an issue related to this order and cannot be fulfilled.
        goods (list[GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrderGood] | Unset): The goods id and quantity in this
            consign order.
        is_platform_closed (str | Unset): This field indicates whether a consign order has been canceled by the FBT
            platform. If the value is true, it means the order has been canceled by the platform; if it is false, it means
            the order has been canceled by your OMS.
        issue (str | Unset): This field displays the reason for order stalling. When a `consign order` is in an abnormal
            status (such as ABNORMAL, LOST, etc.), specific issue reasons will be shown here.
        shipping_provider (GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrderShippingProvider | None | Unset): The
            shipping carrier detailed information of this consign order. If the order has not yet been handed over to the
            logistics carrier, this field may be a null value.
    """

    id: str | Unset = UNSET
    tracking_number: None | str | Unset = UNSET
    status: str | Unset = UNSET
    goods: list[GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrderGood] | Unset = UNSET
    is_platform_closed: str | Unset = UNSET
    issue: str | Unset = UNSET
    shipping_provider: GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrderShippingProvider | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_fbtmcf_order_status_webhook_data_mcf_order_consign_order_shipping_provider import (
            GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrderShippingProvider,  # noqa: PLC0415
        )

        id = self.id

        tracking_number: None | str | Unset
        if isinstance(self.tracking_number, Unset):
            tracking_number = UNSET
        else:
            tracking_number = self.tracking_number

        status = self.status

        goods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.goods, Unset):
            goods = []
            for goods_item_data in self.goods:
                goods_item = goods_item_data.to_dict()
                goods.append(goods_item)

        is_platform_closed = self.is_platform_closed

        issue = self.issue

        shipping_provider: dict[str, Any] | None | Unset
        if isinstance(self.shipping_provider, Unset):
            shipping_provider = UNSET
        elif isinstance(self.shipping_provider, GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrderShippingProvider):
            shipping_provider = self.shipping_provider.to_dict()
        else:
            shipping_provider = self.shipping_provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tracking_number is not UNSET:
            field_dict["tracking_number"] = tracking_number
        if status is not UNSET:
            field_dict["status"] = status
        if goods is not UNSET:
            field_dict["goods"] = goods
        if is_platform_closed is not UNSET:
            field_dict["is_platform_closed"] = is_platform_closed
        if issue is not UNSET:
            field_dict["issue"] = issue
        if shipping_provider is not UNSET:
            field_dict["shipping_provider"] = shipping_provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_fbtmcf_order_status_webhook_data_mcf_order_consign_order_good import (
            GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrderGood,  # noqa: PLC0415
        )
        from ..models.get_fbtmcf_order_status_webhook_data_mcf_order_consign_order_shipping_provider import (
            GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrderShippingProvider,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_tracking_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tracking_number = _parse_tracking_number(d.pop("tracking_number", UNSET))

        status = d.pop("status", UNSET)

        _goods = d.pop("goods", UNSET)
        goods: list[GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrderGood] | Unset = UNSET
        if _goods is not UNSET:
            goods = []
            for goods_item_data in _goods:
                goods_item = GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrderGood.from_dict(goods_item_data)

                goods.append(goods_item)

        is_platform_closed = d.pop("is_platform_closed", UNSET)

        issue = d.pop("issue", UNSET)

        def _parse_shipping_provider(
            data: object,
        ) -> GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrderShippingProvider | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shipping_provider_type_0 = (
                    GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrderShippingProvider.from_dict(data)
                )

                return shipping_provider_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrderShippingProvider | None | Unset, data)

        shipping_provider = _parse_shipping_provider(d.pop("shipping_provider", UNSET))

        get_fbtmcf_order_status_webhook_data_mcf_order_consign_order = cls(
            id=id,
            tracking_number=tracking_number,
            status=status,
            goods=goods,
            is_platform_closed=is_platform_closed,
            issue=issue,
            shipping_provider=shipping_provider,
        )

        get_fbtmcf_order_status_webhook_data_mcf_order_consign_order.additional_properties = d
        return get_fbtmcf_order_status_webhook_data_mcf_order_consign_order

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
