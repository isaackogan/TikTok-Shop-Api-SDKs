from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.confirm_inbound_method_request_inbound_method import ConfirmInboundMethodRequestInboundMethod
from typing import cast

if TYPE_CHECKING:
  from ..models.estimate_arrival_time import EstimateArrivalTime





T = TypeVar("T", bound="ConfirmInboundMethodRequest")



@_attrs_define
class ConfirmInboundMethodRequest:
    """ 
        Attributes:
            plan_id (str): Identifier of the FBT inbound plan whose warehouse placement option is being confirmed.
            placement_option_id (str): Placement option id. A placement option represents the shipment splits and
                destinations.
            inbound_method (ConfirmInboundMethodRequestInboundMethod): **Possible values:**
                * `D2FC` (Direct to fulfillment center, may be split into multiple shipments)
                * `ONE_HUB` (Single destination, includes fee)
            estimate_arrival_time (EstimateArrivalTime):
     """

    plan_id: str
    placement_option_id: str
    inbound_method: ConfirmInboundMethodRequestInboundMethod
    estimate_arrival_time: EstimateArrivalTime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.estimate_arrival_time import EstimateArrivalTime # noqa: PLC0415
        plan_id = self.plan_id

        placement_option_id = self.placement_option_id

        inbound_method = self.inbound_method.value

        estimate_arrival_time = self.estimate_arrival_time.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "plan_id": plan_id,
            "placement_option_id": placement_option_id,
            "inbound_method": inbound_method,
            "estimate_arrival_time": estimate_arrival_time,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.estimate_arrival_time import EstimateArrivalTime # noqa: PLC0415
        d = dict(src_dict)
        plan_id = d.pop("plan_id")

        placement_option_id = d.pop("placement_option_id")

        inbound_method = ConfirmInboundMethodRequestInboundMethod(d.pop("inbound_method"))




        estimate_arrival_time = EstimateArrivalTime.from_dict(d.pop("estimate_arrival_time"))




        confirm_inbound_method_request = cls(
            plan_id=plan_id,
            placement_option_id=placement_option_id,
            inbound_method=inbound_method,
            estimate_arrival_time=estimate_arrival_time,
        )


        confirm_inbound_method_request.additional_properties = d
        return confirm_inbound_method_request

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
