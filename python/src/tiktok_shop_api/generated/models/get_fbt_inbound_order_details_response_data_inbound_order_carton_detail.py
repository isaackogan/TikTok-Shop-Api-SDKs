from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_fbt_inbound_order_details_response_data_inbound_order_carton_detail_carton_type import (
    GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailCartonType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_fbt_inbound_order_details_response_data_inbound_order_carton_detail_box_measurement import (
        GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailBoxMeasurement,
    )
    from ..models.get_fbt_inbound_order_details_response_data_inbound_order_carton_detail_item import (
        GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailItem,
    )


T = TypeVar("T", bound="GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetail")


@_attrs_define
class GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetail:
    """
    Attributes:
        carton_no (str | Unset): Carton number.
        carton_type (GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailCartonType | Unset): Whether this
            carton is single-SKU or multi-SKU.

            **Possible values:**
            * `SINGLE_SKU`
            * `MULTI_SKU`
        box_measurements (GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailBoxMeasurement | Unset):
        items (list[GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailItem] | Unset): List of items in this
            carton.
    """

    carton_no: str | Unset = UNSET
    carton_type: GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailCartonType | Unset = UNSET
    box_measurements: GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailBoxMeasurement | Unset = UNSET
    items: list[GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carton_no = self.carton_no

        carton_type: str | Unset = UNSET
        if not isinstance(self.carton_type, Unset):
            carton_type = self.carton_type.value

        box_measurements: dict[str, Any] | Unset = UNSET
        if not isinstance(self.box_measurements, Unset):
            box_measurements = self.box_measurements.to_dict()

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if carton_no is not UNSET:
            field_dict["carton_no"] = carton_no
        if carton_type is not UNSET:
            field_dict["carton_type"] = carton_type
        if box_measurements is not UNSET:
            field_dict["box_measurements"] = box_measurements
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_fbt_inbound_order_details_response_data_inbound_order_carton_detail_box_measurement import (
            GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailBoxMeasurement,  # noqa: PLC0415
        )
        from ..models.get_fbt_inbound_order_details_response_data_inbound_order_carton_detail_item import (
            GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        carton_no = d.pop("carton_no", UNSET)

        _carton_type = d.pop("carton_type", UNSET)
        carton_type: GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailCartonType | Unset
        if isinstance(_carton_type, Unset):
            carton_type = UNSET
        else:
            carton_type = GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailCartonType(_carton_type)

        _box_measurements = d.pop("box_measurements", UNSET)
        box_measurements: GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailBoxMeasurement | Unset
        if isinstance(_box_measurements, Unset):
            box_measurements = UNSET
        else:
            box_measurements = GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailBoxMeasurement.from_dict(
                _box_measurements
            )

        _items = d.pop("items", UNSET)
        items: list[GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailItem.from_dict(
                    items_item_data
                )

                items.append(items_item)

        get_fbt_inbound_order_details_response_data_inbound_order_carton_detail = cls(
            carton_no=carton_no,
            carton_type=carton_type,
            box_measurements=box_measurements,
            items=items,
        )

        get_fbt_inbound_order_details_response_data_inbound_order_carton_detail.additional_properties = d
        return get_fbt_inbound_order_details_response_data_inbound_order_carton_detail

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
