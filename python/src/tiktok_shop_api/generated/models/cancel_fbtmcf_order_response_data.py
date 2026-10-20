from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cancel_fbtmcf_order_response_data_mcf_order import CancelFBTMCFOrderResponseDataMcfOrder





T = TypeVar("T", bound="CancelFBTMCFOrderResponseData")



@_attrs_define
class CancelFBTMCFOrderResponseData:
    """ 
        Attributes:
            mcf_order (CancelFBTMCFOrderResponseDataMcfOrder | Unset):
     """

    mcf_order: CancelFBTMCFOrderResponseDataMcfOrder | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cancel_fbtmcf_order_response_data_mcf_order import CancelFBTMCFOrderResponseDataMcfOrder # noqa: PLC0415
        mcf_order: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mcf_order, Unset):
            mcf_order = self.mcf_order.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if mcf_order is not UNSET:
            field_dict["mcf_order"] = mcf_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cancel_fbtmcf_order_response_data_mcf_order import CancelFBTMCFOrderResponseDataMcfOrder # noqa: PLC0415
        d = dict(src_dict)
        _mcf_order = d.pop("mcf_order", UNSET)
        mcf_order: CancelFBTMCFOrderResponseDataMcfOrder | Unset
        if isinstance(_mcf_order,  Unset):
            mcf_order = UNSET
        else:
            mcf_order = CancelFBTMCFOrderResponseDataMcfOrder.from_dict(_mcf_order)




        cancel_fbtmcf_order_response_data = cls(
            mcf_order=mcf_order,
        )


        cancel_fbtmcf_order_response_data.additional_properties = d
        return cancel_fbtmcf_order_response_data

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
