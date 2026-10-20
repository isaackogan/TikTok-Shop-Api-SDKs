from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_trade_in_account_transactions_response_data_flow import GetTradeInAccountTransactionsResponseDataFlow





T = TypeVar("T", bound="GetTradeInAccountTransactionsResponseData")



@_attrs_define
class GetTradeInAccountTransactionsResponseData:
    """ 
        Attributes:
            flows (list[GetTradeInAccountTransactionsResponseDataFlow] | Unset): The TradeIn account transactions that match
                the query conditions. An empty array is returned when no transaction matches.
            has_more (bool | Unset): Whether more account transactions are available.
            next_page_token (str | Unset): An opaque token used to retrieve the next page. The value is empty when no more
                account transactions are available.
            total_count (int | Unset): The total number of account transactions that match the query conditions.
     """

    flows: list[GetTradeInAccountTransactionsResponseDataFlow] | Unset = UNSET
    has_more: bool | Unset = UNSET
    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_trade_in_account_transactions_response_data_flow import GetTradeInAccountTransactionsResponseDataFlow # noqa: PLC0415
        flows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.flows, Unset):
            flows = []
            for flows_item_data in self.flows:
                flows_item = flows_item_data.to_dict()
                flows.append(flows_item)



        has_more = self.has_more

        next_page_token = self.next_page_token

        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if flows is not UNSET:
            field_dict["flows"] = flows
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_trade_in_account_transactions_response_data_flow import GetTradeInAccountTransactionsResponseDataFlow # noqa: PLC0415
        d = dict(src_dict)
        _flows = d.pop("flows", UNSET)
        flows: list[GetTradeInAccountTransactionsResponseDataFlow] | Unset = UNSET
        if _flows is not UNSET:
            flows = []
            for flows_item_data in _flows:
                flows_item = GetTradeInAccountTransactionsResponseDataFlow.from_dict(flows_item_data)



                flows.append(flows_item)


        has_more = d.pop("has_more", UNSET)

        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        get_trade_in_account_transactions_response_data = cls(
            flows=flows,
            has_more=has_more,
            next_page_token=next_page_token,
            total_count=total_count,
        )


        get_trade_in_account_transactions_response_data.additional_properties = d
        return get_trade_in_account_transactions_response_data

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
