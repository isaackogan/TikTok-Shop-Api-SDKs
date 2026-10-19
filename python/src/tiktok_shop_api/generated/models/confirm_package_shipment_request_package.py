from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.confirm_package_shipment_request_package_tcw_warehouse_type import (
    ConfirmPackageShipmentRequestPackageTcwWarehouseType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.confirm_package_shipment_request_package_dimension import (
        ConfirmPackageShipmentRequestPackageDimension,
    )
    from ..models.confirm_package_shipment_request_package_sku import ConfirmPackageShipmentRequestPackageSku
    from ..models.confirm_package_shipment_request_package_weight import ConfirmPackageShipmentRequestPackageWeight


T = TypeVar("T", bound="ConfirmPackageShipmentRequestPackage")


@_attrs_define
class ConfirmPackageShipmentRequestPackage:
    """
    Attributes:
        id (str): Package ID. The value must be a non-zero base-10 integer string no longer than 40 UTF-8 bytes.
        wms_order_id (str): Warehouse Management System order number
        time_zone (str): The warehouse time zone
        ship_time_millis (int): Time when the order is shipped out of the warehouse (Unix timestamp in milliseconds)
        create_time_millis (int): Time when warehouse receives the order (Unix timestamp in milliseconds)
        handover_time_millis (int): Time when the order is handed over to the shipping provider (Unix timestamp in
            milliseconds)
        shipping_provider_id (str): Shipping service provider ID
        shipping_provider_name (str): Shipping service provider name
        tracking_number (str): Tracking number
        dimension (ConfirmPackageShipmentRequestPackageDimension):
        skus (list[ConfirmPackageShipmentRequestPackageSku]): List of order SKUs in the package. Provide at least one
            SKU.
        provider_warehouse_code (str | Unset): Warehouse code. Maximum: 40 UTF-8 bytes.
        shipping_origin_city (str | Unset): Origin city name for the shipment
        weight (ConfirmPackageShipmentRequestPackageWeight | Unset):
        provider_warehouse_name (str | Unset): Warehouse name
        tcw_warehouse_type (ConfirmPackageShipmentRequestPackageTcwWarehouseType | Unset): TikTok warehouse type
            Possible values:
            - STANDARD: Standard warehouse that has not been specifically certified by TikTok
            - TIKTOK_CERTIFIED_WAREHOUSE_FULFILLMENT: TikTok certified warehouse usually offering better service levels.
            Certified warehouses are required to meet fulfillment timeline standards set by TikTok
    """

    id: str
    wms_order_id: str
    time_zone: str
    ship_time_millis: int
    create_time_millis: int
    handover_time_millis: int
    shipping_provider_id: str
    shipping_provider_name: str
    tracking_number: str
    dimension: ConfirmPackageShipmentRequestPackageDimension
    skus: list[ConfirmPackageShipmentRequestPackageSku]
    provider_warehouse_code: str | Unset = UNSET
    shipping_origin_city: str | Unset = UNSET
    weight: ConfirmPackageShipmentRequestPackageWeight | Unset = UNSET
    provider_warehouse_name: str | Unset = UNSET
    tcw_warehouse_type: ConfirmPackageShipmentRequestPackageTcwWarehouseType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        wms_order_id = self.wms_order_id

        time_zone = self.time_zone

        ship_time_millis = self.ship_time_millis

        create_time_millis = self.create_time_millis

        handover_time_millis = self.handover_time_millis

        shipping_provider_id = self.shipping_provider_id

        shipping_provider_name = self.shipping_provider_name

        tracking_number = self.tracking_number

        dimension = self.dimension.to_dict()

        skus = []
        for skus_item_data in self.skus:
            skus_item = skus_item_data.to_dict()
            skus.append(skus_item)

        provider_warehouse_code = self.provider_warehouse_code

        shipping_origin_city = self.shipping_origin_city

        weight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()

        provider_warehouse_name = self.provider_warehouse_name

        tcw_warehouse_type: str | Unset = UNSET
        if not isinstance(self.tcw_warehouse_type, Unset):
            tcw_warehouse_type = self.tcw_warehouse_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "wms_order_id": wms_order_id,
                "time_zone": time_zone,
                "ship_time_millis": ship_time_millis,
                "create_time_millis": create_time_millis,
                "handover_time_millis": handover_time_millis,
                "shipping_provider_id": shipping_provider_id,
                "shipping_provider_name": shipping_provider_name,
                "tracking_number": tracking_number,
                "dimension": dimension,
                "skus": skus,
            }
        )
        if provider_warehouse_code is not UNSET:
            field_dict["provider_warehouse_code"] = provider_warehouse_code
        if shipping_origin_city is not UNSET:
            field_dict["shipping_origin_city"] = shipping_origin_city
        if weight is not UNSET:
            field_dict["weight"] = weight
        if provider_warehouse_name is not UNSET:
            field_dict["provider_warehouse_name"] = provider_warehouse_name
        if tcw_warehouse_type is not UNSET:
            field_dict["tcw_warehouse_type"] = tcw_warehouse_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.confirm_package_shipment_request_package_dimension import (
            ConfirmPackageShipmentRequestPackageDimension,  # noqa: PLC0415
        )
        from ..models.confirm_package_shipment_request_package_sku import (
            ConfirmPackageShipmentRequestPackageSku,  # noqa: PLC0415
        )
        from ..models.confirm_package_shipment_request_package_weight import (
            ConfirmPackageShipmentRequestPackageWeight,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        wms_order_id = d.pop("wms_order_id")

        time_zone = d.pop("time_zone")

        ship_time_millis = d.pop("ship_time_millis")

        create_time_millis = d.pop("create_time_millis")

        handover_time_millis = d.pop("handover_time_millis")

        shipping_provider_id = d.pop("shipping_provider_id")

        shipping_provider_name = d.pop("shipping_provider_name")

        tracking_number = d.pop("tracking_number")

        dimension = ConfirmPackageShipmentRequestPackageDimension.from_dict(d.pop("dimension"))

        skus = []
        _skus = d.pop("skus")
        for skus_item_data in _skus:
            skus_item = ConfirmPackageShipmentRequestPackageSku.from_dict(skus_item_data)

            skus.append(skus_item)

        provider_warehouse_code = d.pop("provider_warehouse_code", UNSET)

        shipping_origin_city = d.pop("shipping_origin_city", UNSET)

        _weight = d.pop("weight", UNSET)
        weight: ConfirmPackageShipmentRequestPackageWeight | Unset
        if isinstance(_weight, Unset):
            weight = UNSET
        else:
            weight = ConfirmPackageShipmentRequestPackageWeight.from_dict(_weight)

        provider_warehouse_name = d.pop("provider_warehouse_name", UNSET)

        _tcw_warehouse_type = d.pop("tcw_warehouse_type", UNSET)
        tcw_warehouse_type: ConfirmPackageShipmentRequestPackageTcwWarehouseType | Unset
        if isinstance(_tcw_warehouse_type, Unset):
            tcw_warehouse_type = UNSET
        else:
            tcw_warehouse_type = ConfirmPackageShipmentRequestPackageTcwWarehouseType(_tcw_warehouse_type)

        confirm_package_shipment_request_package = cls(
            id=id,
            wms_order_id=wms_order_id,
            time_zone=time_zone,
            ship_time_millis=ship_time_millis,
            create_time_millis=create_time_millis,
            handover_time_millis=handover_time_millis,
            shipping_provider_id=shipping_provider_id,
            shipping_provider_name=shipping_provider_name,
            tracking_number=tracking_number,
            dimension=dimension,
            skus=skus,
            provider_warehouse_code=provider_warehouse_code,
            shipping_origin_city=shipping_origin_city,
            weight=weight,
            provider_warehouse_name=provider_warehouse_name,
            tcw_warehouse_type=tcw_warehouse_type,
        )

        confirm_package_shipment_request_package.additional_properties = d
        return confirm_package_shipment_request_package

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
