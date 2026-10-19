from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_eligible_shipping_services_response_data_dimension import (
        GetEligibleShippingServicesResponseDataDimension,
    )
    from ..models.get_eligible_shipping_services_response_data_shipping_service import (
        GetEligibleShippingServicesResponseDataShippingService,
    )
    from ..models.get_eligible_shipping_services_response_data_weight import (
        GetEligibleShippingServicesResponseDataWeight,
    )


T = TypeVar("T", bound="GetEligibleShippingServicesResponseData")


@_attrs_define
class GetEligibleShippingServicesResponseData:
    """
    Attributes:
        order_id (str | Unset): TikTok Shop order ID
        order_line_id (list[str] | Unset): Line item ID list
        weight (GetEligibleShippingServicesResponseDataWeight | Unset):
        shipping_services (list[GetEligibleShippingServicesResponseDataShippingService] | Unset): The shipping services
            available for the order.
        dimension (GetEligibleShippingServicesResponseDataDimension | Unset):
    """

    order_id: str | Unset = UNSET
    order_line_id: list[str] | Unset = UNSET
    weight: GetEligibleShippingServicesResponseDataWeight | Unset = UNSET
    shipping_services: list[GetEligibleShippingServicesResponseDataShippingService] | Unset = UNSET
    dimension: GetEligibleShippingServicesResponseDataDimension | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        order_line_id: list[str] | Unset = UNSET
        if not isinstance(self.order_line_id, Unset):
            order_line_id = self.order_line_id

        weight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()

        shipping_services: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shipping_services, Unset):
            shipping_services = []
            for shipping_services_item_data in self.shipping_services:
                shipping_services_item = shipping_services_item_data.to_dict()
                shipping_services.append(shipping_services_item)

        dimension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dimension, Unset):
            dimension = self.dimension.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id
        if weight is not UNSET:
            field_dict["weight"] = weight
        if shipping_services is not UNSET:
            field_dict["shipping_services"] = shipping_services
        if dimension is not UNSET:
            field_dict["dimension"] = dimension

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_eligible_shipping_services_response_data_dimension import (
            GetEligibleShippingServicesResponseDataDimension,  # noqa: PLC0415
        )
        from ..models.get_eligible_shipping_services_response_data_shipping_service import (
            GetEligibleShippingServicesResponseDataShippingService,  # noqa: PLC0415
        )
        from ..models.get_eligible_shipping_services_response_data_weight import (
            GetEligibleShippingServicesResponseDataWeight,  # noqa: PLC0415
        )

        d = dict(src_dict)
        order_id = d.pop("order_id", UNSET)

        order_line_id = cast(list[str], d.pop("order_line_id", UNSET))

        _weight = d.pop("weight", UNSET)
        weight: GetEligibleShippingServicesResponseDataWeight | Unset
        if isinstance(_weight, Unset):
            weight = UNSET
        else:
            weight = GetEligibleShippingServicesResponseDataWeight.from_dict(_weight)

        _shipping_services = d.pop("shipping_services", UNSET)
        shipping_services: list[GetEligibleShippingServicesResponseDataShippingService] | Unset = UNSET
        if _shipping_services is not UNSET:
            shipping_services = []
            for shipping_services_item_data in _shipping_services:
                shipping_services_item = GetEligibleShippingServicesResponseDataShippingService.from_dict(
                    shipping_services_item_data
                )

                shipping_services.append(shipping_services_item)

        _dimension = d.pop("dimension", UNSET)
        dimension: GetEligibleShippingServicesResponseDataDimension | Unset
        if isinstance(_dimension, Unset):
            dimension = UNSET
        else:
            dimension = GetEligibleShippingServicesResponseDataDimension.from_dict(_dimension)

        get_eligible_shipping_services_response_data = cls(
            order_id=order_id,
            order_line_id=order_line_id,
            weight=weight,
            shipping_services=shipping_services,
            dimension=dimension,
        )

        get_eligible_shipping_services_response_data.additional_properties = d
        return get_eligible_shipping_services_response_data

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
