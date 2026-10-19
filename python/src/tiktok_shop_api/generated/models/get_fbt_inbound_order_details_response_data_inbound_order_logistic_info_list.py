from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_fbt_inbound_order_details_response_data_inbound_order_logistic_info_list_provider_name import (
    GetFBTInboundOrderDetailsResponseDataInboundOrderLogisticInfoListProviderName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetFBTInboundOrderDetailsResponseDataInboundOrderLogisticInfoList")


@_attrs_define
class GetFBTInboundOrderDetailsResponseDataInboundOrderLogisticInfoList:
    """
    Attributes:
        provider_name (GetFBTInboundOrderDetailsResponseDataInboundOrderLogisticInfoListProviderName | Unset): Name of
            the logistics service provider

            Possible values:
            * `FEDEX` (Federal Express)
            * `UPS` (United Parcel Service)
            * `DHL` (DHL Express)
            * `USPS` (United States Postal Service)
            * `OTHER` (All other logistics providers)
        waybill_number (str | Unset): The tracking number for the current inbound shipment with the carrier.
        related_number (str | Unset): Carton number tied to the logistics information.
    """

    provider_name: GetFBTInboundOrderDetailsResponseDataInboundOrderLogisticInfoListProviderName | Unset = UNSET
    waybill_number: str | Unset = UNSET
    related_number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_name: str | Unset = UNSET
        if not isinstance(self.provider_name, Unset):
            provider_name = self.provider_name.value

        waybill_number = self.waybill_number

        related_number = self.related_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider_name is not UNSET:
            field_dict["provider_name"] = provider_name
        if waybill_number is not UNSET:
            field_dict["waybill_number"] = waybill_number
        if related_number is not UNSET:
            field_dict["related_number"] = related_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _provider_name = d.pop("provider_name", UNSET)
        provider_name: GetFBTInboundOrderDetailsResponseDataInboundOrderLogisticInfoListProviderName | Unset
        if isinstance(_provider_name, Unset):
            provider_name = UNSET
        else:
            provider_name = GetFBTInboundOrderDetailsResponseDataInboundOrderLogisticInfoListProviderName(
                _provider_name
            )

        waybill_number = d.pop("waybill_number", UNSET)

        related_number = d.pop("related_number", UNSET)

        get_fbt_inbound_order_details_response_data_inbound_order_logistic_info_list = cls(
            provider_name=provider_name,
            waybill_number=waybill_number,
            related_number=related_number,
        )

        get_fbt_inbound_order_details_response_data_inbound_order_logistic_info_list.additional_properties = d
        return get_fbt_inbound_order_details_response_data_inbound_order_logistic_info_list

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
