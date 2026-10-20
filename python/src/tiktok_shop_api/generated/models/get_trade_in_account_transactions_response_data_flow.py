from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_trade_in_account_transactions_response_data_flow_amount import (
        GetTradeInAccountTransactionsResponseDataFlowAmount,
    )


T = TypeVar("T", bound="GetTradeInAccountTransactionsResponseDataFlow")


@_attrs_define
class GetTradeInAccountTransactionsResponseDataFlow:
    """
    Attributes:
        amount (GetTradeInAccountTransactionsResponseDataFlowAmount | Unset):
        create_time (datetime.datetime | Unset): The time when the account transaction was created, in RFC 3339 format.
        direction (str | Unset): The direction of the account transaction.
            - IN: Funds credited to the supplier's account.
            - OUT: Funds debited from the supplier's account.
        origin_transaction_id (str | Unset): The original account transaction ID associated with a reversed transaction.
            This field is returned only for a REVERSE transaction when available.
        reference_id (str | Unset): The TradeIn business order ID associated with the account transaction.
        transaction_id (str | Unset): The unique ID of the account transaction.
        type_ (str | Unset): The TradeIn business transaction type.
            - RECHARGE: Funds credited through a recharge.
            - WITHDRAW: Funds debited through a payout.
            - REVERSE: Funds returned after a payout reversal.
    """

    amount: GetTradeInAccountTransactionsResponseDataFlowAmount | Unset = UNSET
    create_time: datetime.datetime | Unset = UNSET
    direction: str | Unset = UNSET
    origin_transaction_id: str | Unset = UNSET
    reference_id: str | Unset = UNSET
    transaction_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        direction = self.direction

        origin_transaction_id = self.origin_transaction_id

        reference_id = self.reference_id

        transaction_id = self.transaction_id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if direction is not UNSET:
            field_dict["direction"] = direction
        if origin_transaction_id is not UNSET:
            field_dict["origin_transaction_id"] = origin_transaction_id
        if reference_id is not UNSET:
            field_dict["reference_id"] = reference_id
        if transaction_id is not UNSET:
            field_dict["transaction_id"] = transaction_id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_trade_in_account_transactions_response_data_flow_amount import (
            GetTradeInAccountTransactionsResponseDataFlowAmount,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _amount = d.pop("amount", UNSET)
        amount: GetTradeInAccountTransactionsResponseDataFlowAmount | Unset
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = GetTradeInAccountTransactionsResponseDataFlowAmount.from_dict(_amount)

        _create_time = d.pop("create_time", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        direction = d.pop("direction", UNSET)

        origin_transaction_id = d.pop("origin_transaction_id", UNSET)

        reference_id = d.pop("reference_id", UNSET)

        transaction_id = d.pop("transaction_id", UNSET)

        type_ = d.pop("type", UNSET)

        get_trade_in_account_transactions_response_data_flow = cls(
            amount=amount,
            create_time=create_time,
            direction=direction,
            origin_transaction_id=origin_transaction_id,
            reference_id=reference_id,
            transaction_id=transaction_id,
            type_=type_,
        )

        get_trade_in_account_transactions_response_data_flow.additional_properties = d
        return get_trade_in_account_transactions_response_data_flow

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
