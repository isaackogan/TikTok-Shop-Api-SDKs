from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_fbt_inbound_order_details_response_data_inbound_order_carton_detail import (
        GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetail,
    )
    from ..models.get_fbt_inbound_order_details_response_data_inbound_order_inbound_goods_lot_receive_item_detail import (
        GetFBTInboundOrderDetailsResponseDataInboundOrderInboundGoodsLotReceiveItemDetail,
    )
    from ..models.get_fbt_inbound_order_details_response_data_inbound_order_logistic_info_list import (
        GetFBTInboundOrderDetailsResponseDataInboundOrderLogisticInfoList,
    )
    from ..models.get_fbt_inbound_order_details_response_data_inbound_order_merchant import (
        GetFBTInboundOrderDetailsResponseDataInboundOrderMerchant,
    )
    from ..models.get_fbt_inbound_order_details_response_data_inbound_order_status_log import (
        GetFBTInboundOrderDetailsResponseDataInboundOrderStatusLog,
    )
    from ..models.get_fbt_inbound_order_details_response_data_inbound_order_warehouse import (
        GetFBTInboundOrderDetailsResponseDataInboundOrderWarehouse,
    )


T = TypeVar("T", bound="GetFBTInboundOrderDetailsResponseDataInboundOrder")


@_attrs_define
class GetFBTInboundOrderDetailsResponseDataInboundOrder:
    """
    Attributes:
        order_id (str | Unset): The numeric identifier for inbound order in Fulfilled by TikTok system.
        order_id_string (str | Unset): The string identifier for inbound order in Fulfilled by TikTok system.
        order_plan_id (str | Unset): Plan identifier for the inbound order.
        merchant (GetFBTInboundOrderDetailsResponseDataInboundOrderMerchant | Unset):
        create_time (int | Unset): Unix seconds timestamp when the inbound order was created.
        ship_time (int | Unset): Unix seconds timestamp when the inbound order was shipped.
        expected_arrival_time (int | Unset): Unix seconds timestamp of the expected arrival time provided by merchant.
        actual_arrival_time (int | Unset): Unix seconds timestamp of the actual arrival time of the inbound order.
        warehouse (GetFBTInboundOrderDetailsResponseDataInboundOrderWarehouse | Unset):
        status_logs (list[GetFBTInboundOrderDetailsResponseDataInboundOrderStatusLog] | Unset): Inbound order operation-
            history entries derived from at most 200 source status records. This list may be incomplete, and this operation
            does not provide a cursor for retrieving additional status records.
        logistic_info_list (list[GetFBTInboundOrderDetailsResponseDataInboundOrderLogisticInfoList] | Unset): List of
            logistics information tied to the order. Only populated for small-parcel inbound orders.
        carton_details (list[GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetail] | Unset): Detailed carton
            information for the inbound order. Only populated if `include_carton_details` is passed as true in the request.
        inbound_goods_lot_receive_item_details
            (list[GetFBTInboundOrderDetailsResponseDataInboundOrderInboundGoodsLotReceiveItemDetail] | Unset): A detailed
            breakdown of planned versus actual receiving information, segmented by item, lot number, and expiration date.
    """

    order_id: str | Unset = UNSET
    order_id_string: str | Unset = UNSET
    order_plan_id: str | Unset = UNSET
    merchant: GetFBTInboundOrderDetailsResponseDataInboundOrderMerchant | Unset = UNSET
    create_time: int | Unset = UNSET
    ship_time: int | Unset = UNSET
    expected_arrival_time: int | Unset = UNSET
    actual_arrival_time: int | Unset = UNSET
    warehouse: GetFBTInboundOrderDetailsResponseDataInboundOrderWarehouse | Unset = UNSET
    status_logs: list[GetFBTInboundOrderDetailsResponseDataInboundOrderStatusLog] | Unset = UNSET
    logistic_info_list: list[GetFBTInboundOrderDetailsResponseDataInboundOrderLogisticInfoList] | Unset = UNSET
    carton_details: list[GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetail] | Unset = UNSET
    inbound_goods_lot_receive_item_details: (
        list[GetFBTInboundOrderDetailsResponseDataInboundOrderInboundGoodsLotReceiveItemDetail] | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        order_id_string = self.order_id_string

        order_plan_id = self.order_plan_id

        merchant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        create_time = self.create_time

        ship_time = self.ship_time

        expected_arrival_time = self.expected_arrival_time

        actual_arrival_time = self.actual_arrival_time

        warehouse: dict[str, Any] | Unset = UNSET
        if not isinstance(self.warehouse, Unset):
            warehouse = self.warehouse.to_dict()

        status_logs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.status_logs, Unset):
            status_logs = []
            for status_logs_item_data in self.status_logs:
                status_logs_item = status_logs_item_data.to_dict()
                status_logs.append(status_logs_item)

        logistic_info_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.logistic_info_list, Unset):
            logistic_info_list = []
            for logistic_info_list_item_data in self.logistic_info_list:
                logistic_info_list_item = logistic_info_list_item_data.to_dict()
                logistic_info_list.append(logistic_info_list_item)

        carton_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.carton_details, Unset):
            carton_details = []
            for carton_details_item_data in self.carton_details:
                carton_details_item = carton_details_item_data.to_dict()
                carton_details.append(carton_details_item)

        inbound_goods_lot_receive_item_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inbound_goods_lot_receive_item_details, Unset):
            inbound_goods_lot_receive_item_details = []
            for inbound_goods_lot_receive_item_details_item_data in self.inbound_goods_lot_receive_item_details:
                inbound_goods_lot_receive_item_details_item = inbound_goods_lot_receive_item_details_item_data.to_dict()
                inbound_goods_lot_receive_item_details.append(inbound_goods_lot_receive_item_details_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if order_id_string is not UNSET:
            field_dict["order_id_string"] = order_id_string
        if order_plan_id is not UNSET:
            field_dict["order_plan_id"] = order_plan_id
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if ship_time is not UNSET:
            field_dict["ship_time"] = ship_time
        if expected_arrival_time is not UNSET:
            field_dict["expected_arrival_time"] = expected_arrival_time
        if actual_arrival_time is not UNSET:
            field_dict["actual_arrival_time"] = actual_arrival_time
        if warehouse is not UNSET:
            field_dict["warehouse"] = warehouse
        if status_logs is not UNSET:
            field_dict["status_logs"] = status_logs
        if logistic_info_list is not UNSET:
            field_dict["logistic_info_list"] = logistic_info_list
        if carton_details is not UNSET:
            field_dict["carton_details"] = carton_details
        if inbound_goods_lot_receive_item_details is not UNSET:
            field_dict["inbound_goods_lot_receive_item_details"] = inbound_goods_lot_receive_item_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_fbt_inbound_order_details_response_data_inbound_order_carton_detail import (
            GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetail,  # noqa: PLC0415
        )
        from ..models.get_fbt_inbound_order_details_response_data_inbound_order_inbound_goods_lot_receive_item_detail import (
            GetFBTInboundOrderDetailsResponseDataInboundOrderInboundGoodsLotReceiveItemDetail,  # noqa: PLC0415
        )
        from ..models.get_fbt_inbound_order_details_response_data_inbound_order_logistic_info_list import (
            GetFBTInboundOrderDetailsResponseDataInboundOrderLogisticInfoList,  # noqa: PLC0415
        )
        from ..models.get_fbt_inbound_order_details_response_data_inbound_order_merchant import (
            GetFBTInboundOrderDetailsResponseDataInboundOrderMerchant,  # noqa: PLC0415
        )
        from ..models.get_fbt_inbound_order_details_response_data_inbound_order_status_log import (
            GetFBTInboundOrderDetailsResponseDataInboundOrderStatusLog,  # noqa: PLC0415
        )
        from ..models.get_fbt_inbound_order_details_response_data_inbound_order_warehouse import (
            GetFBTInboundOrderDetailsResponseDataInboundOrderWarehouse,  # noqa: PLC0415
        )

        d = dict(src_dict)
        order_id = d.pop("order_id", UNSET)

        order_id_string = d.pop("order_id_string", UNSET)

        order_plan_id = d.pop("order_plan_id", UNSET)

        _merchant = d.pop("merchant", UNSET)
        merchant: GetFBTInboundOrderDetailsResponseDataInboundOrderMerchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = GetFBTInboundOrderDetailsResponseDataInboundOrderMerchant.from_dict(_merchant)

        create_time = d.pop("create_time", UNSET)

        ship_time = d.pop("ship_time", UNSET)

        expected_arrival_time = d.pop("expected_arrival_time", UNSET)

        actual_arrival_time = d.pop("actual_arrival_time", UNSET)

        _warehouse = d.pop("warehouse", UNSET)
        warehouse: GetFBTInboundOrderDetailsResponseDataInboundOrderWarehouse | Unset
        if isinstance(_warehouse, Unset):
            warehouse = UNSET
        else:
            warehouse = GetFBTInboundOrderDetailsResponseDataInboundOrderWarehouse.from_dict(_warehouse)

        _status_logs = d.pop("status_logs", UNSET)
        status_logs: list[GetFBTInboundOrderDetailsResponseDataInboundOrderStatusLog] | Unset = UNSET
        if _status_logs is not UNSET:
            status_logs = []
            for status_logs_item_data in _status_logs:
                status_logs_item = GetFBTInboundOrderDetailsResponseDataInboundOrderStatusLog.from_dict(
                    status_logs_item_data
                )

                status_logs.append(status_logs_item)

        _logistic_info_list = d.pop("logistic_info_list", UNSET)
        logistic_info_list: list[GetFBTInboundOrderDetailsResponseDataInboundOrderLogisticInfoList] | Unset = UNSET
        if _logistic_info_list is not UNSET:
            logistic_info_list = []
            for logistic_info_list_item_data in _logistic_info_list:
                logistic_info_list_item = GetFBTInboundOrderDetailsResponseDataInboundOrderLogisticInfoList.from_dict(
                    logistic_info_list_item_data
                )

                logistic_info_list.append(logistic_info_list_item)

        _carton_details = d.pop("carton_details", UNSET)
        carton_details: list[GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetail] | Unset = UNSET
        if _carton_details is not UNSET:
            carton_details = []
            for carton_details_item_data in _carton_details:
                carton_details_item = GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetail.from_dict(
                    carton_details_item_data
                )

                carton_details.append(carton_details_item)

        _inbound_goods_lot_receive_item_details = d.pop("inbound_goods_lot_receive_item_details", UNSET)
        inbound_goods_lot_receive_item_details: (
            list[GetFBTInboundOrderDetailsResponseDataInboundOrderInboundGoodsLotReceiveItemDetail] | Unset
        ) = UNSET
        if _inbound_goods_lot_receive_item_details is not UNSET:
            inbound_goods_lot_receive_item_details = []
            for inbound_goods_lot_receive_item_details_item_data in _inbound_goods_lot_receive_item_details:
                inbound_goods_lot_receive_item_details_item = (
                    GetFBTInboundOrderDetailsResponseDataInboundOrderInboundGoodsLotReceiveItemDetail.from_dict(
                        inbound_goods_lot_receive_item_details_item_data
                    )
                )

                inbound_goods_lot_receive_item_details.append(inbound_goods_lot_receive_item_details_item)

        get_fbt_inbound_order_details_response_data_inbound_order = cls(
            order_id=order_id,
            order_id_string=order_id_string,
            order_plan_id=order_plan_id,
            merchant=merchant,
            create_time=create_time,
            ship_time=ship_time,
            expected_arrival_time=expected_arrival_time,
            actual_arrival_time=actual_arrival_time,
            warehouse=warehouse,
            status_logs=status_logs,
            logistic_info_list=logistic_info_list,
            carton_details=carton_details,
            inbound_goods_lot_receive_item_details=inbound_goods_lot_receive_item_details,
        )

        get_fbt_inbound_order_details_response_data_inbound_order.additional_properties = d
        return get_fbt_inbound_order_details_response_data_inbound_order

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
