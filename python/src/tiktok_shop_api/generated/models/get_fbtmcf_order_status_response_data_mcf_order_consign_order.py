from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_fbtmcf_order_status_response_data_mcf_order_consign_order_good import GetFBTMCFOrderStatusResponseDataMcfOrderConsignOrderGood
  from ..models.shipping_provider import ShippingProvider





T = TypeVar("T", bound="GetFBTMCFOrderStatusResponseDataMcfOrderConsignOrder")



@_attrs_define
class GetFBTMCFOrderStatusResponseDataMcfOrderConsignOrder:
    """ 
        Attributes:
            id (str | Unset): `consign order` unique id
            goods (list[GetFBTMCFOrderStatusResponseDataMcfOrderConsignOrderGood] | Unset): The goods id and quantity in
                this consign order.
            tracking_number (None | str | Unset): The tracking number of this consign order. If the order has not yet been
                handed over to the logistics carrier, this field may be a null value.
            carrier (None | str | Unset): The shipping carrier of this consign order. If the order has not yet been handed
                over to the logistics carrier, this field may be a null value.
            status (str | Unset): The status of the consign order.

                Possible values:
                - **PENDING** - The order is pending warehouse processing.
                - **HANDLE_BY_WAREHOUSE** - The order is being processed by the warehouse.
                - **SHIPPED** - The order has shipped from the warehouse.
                - **HANDOVER** - The logistics carrier has received the order and it is in transit.
                - **CLOSED** - The order is closed.
                - **LOST** - The order is lost.
                - **DAMAGE** - The order is damaged.
                - **RETURNED** - The order was returned.
                - **SCRAP** - The order was scrapped.
                - **UNKNOWN** - The consign-order status or shipping-exception subtype is unknown.
                - **COMPLETED** - The order is complete.
                - **ABNORMAL** - An issue prevents the order from being fulfilled.
            is_platform_closed (bool | Unset): Indicates who canceled the consign order when `status` is `CLOSED`. `true`
                means the FBT platform canceled the order; `false` means it was canceled through your OMS.
            issue (str | Unset): This field displays the reason for order stalling. When a `consign order` is in an abnormal
                status (such as **ABNORMAL**, **LOST**, etc.), specific issue reasons will be shown here.
            shipping_provider (None | ShippingProvider | Unset): The shipping carrier detailed informatioin of this consign
                order. If the order has not yet been handed over to the logistics carrier, this field may be a null value.
     """

    id: str | Unset = UNSET
    goods: list[GetFBTMCFOrderStatusResponseDataMcfOrderConsignOrderGood] | Unset = UNSET
    tracking_number: None | str | Unset = UNSET
    carrier: None | str | Unset = UNSET
    status: str | Unset = UNSET
    is_platform_closed: bool | Unset = UNSET
    issue: str | Unset = UNSET
    shipping_provider: None | ShippingProvider | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_fbtmcf_order_status_response_data_mcf_order_consign_order_good import GetFBTMCFOrderStatusResponseDataMcfOrderConsignOrderGood # noqa: PLC0415
        from ..models.shipping_provider import ShippingProvider # noqa: PLC0415
        id = self.id

        goods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.goods, Unset):
            goods = []
            for goods_item_data in self.goods:
                goods_item = goods_item_data.to_dict()
                goods.append(goods_item)



        tracking_number: None | str | Unset
        if isinstance(self.tracking_number, Unset):
            tracking_number = UNSET
        else:
            tracking_number = self.tracking_number

        carrier: None | str | Unset
        if isinstance(self.carrier, Unset):
            carrier = UNSET
        else:
            carrier = self.carrier

        status = self.status

        is_platform_closed = self.is_platform_closed

        issue = self.issue

        shipping_provider: dict[str, Any] | None | Unset
        if isinstance(self.shipping_provider, Unset):
            shipping_provider = UNSET
        elif isinstance(self.shipping_provider, ShippingProvider):
            shipping_provider = self.shipping_provider.to_dict()
        else:
            shipping_provider = self.shipping_provider


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if goods is not UNSET:
            field_dict["goods"] = goods
        if tracking_number is not UNSET:
            field_dict["tracking_number"] = tracking_number
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if status is not UNSET:
            field_dict["status"] = status
        if is_platform_closed is not UNSET:
            field_dict["is_platform_closed"] = is_platform_closed
        if issue is not UNSET:
            field_dict["issue"] = issue
        if shipping_provider is not UNSET:
            field_dict["shipping_provider"] = shipping_provider

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_fbtmcf_order_status_response_data_mcf_order_consign_order_good import GetFBTMCFOrderStatusResponseDataMcfOrderConsignOrderGood # noqa: PLC0415
        from ..models.shipping_provider import ShippingProvider # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _goods = d.pop("goods", UNSET)
        goods: list[GetFBTMCFOrderStatusResponseDataMcfOrderConsignOrderGood] | Unset = UNSET
        if _goods is not UNSET:
            goods = []
            for goods_item_data in _goods:
                goods_item = GetFBTMCFOrderStatusResponseDataMcfOrderConsignOrderGood.from_dict(goods_item_data)



                goods.append(goods_item)


        def _parse_tracking_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tracking_number = _parse_tracking_number(d.pop("tracking_number", UNSET))


        def _parse_carrier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        carrier = _parse_carrier(d.pop("carrier", UNSET))


        status = d.pop("status", UNSET)

        is_platform_closed = d.pop("is_platform_closed", UNSET)

        issue = d.pop("issue", UNSET)

        def _parse_shipping_provider(data: object) -> None | ShippingProvider | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shipping_provider_type_0 = ShippingProvider.from_dict(data)



                return shipping_provider_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ShippingProvider | Unset, data)

        shipping_provider = _parse_shipping_provider(d.pop("shipping_provider", UNSET))


        get_fbtmcf_order_status_response_data_mcf_order_consign_order = cls(
            id=id,
            goods=goods,
            tracking_number=tracking_number,
            carrier=carrier,
            status=status,
            is_platform_closed=is_platform_closed,
            issue=issue,
            shipping_provider=shipping_provider,
        )


        get_fbtmcf_order_status_response_data_mcf_order_consign_order.additional_properties = d
        return get_fbtmcf_order_status_response_data_mcf_order_consign_order

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
