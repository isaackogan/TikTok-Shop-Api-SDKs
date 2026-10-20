from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_payments_response_data_payment_amount import GetPaymentsResponseDataPaymentAmount
    from ..models.get_payments_response_data_payment_payment_amount_before_exchange import (
        GetPaymentsResponseDataPaymentPaymentAmountBeforeExchange,
    )
    from ..models.get_payments_response_data_payment_settlement_amount import (
        GetPaymentsResponseDataPaymentSettlementAmount,
    )


T = TypeVar("T", bound="GetPaymentsResponseDataPayment")


@_attrs_define
class GetPaymentsResponseDataPayment:
    """
    Attributes:
        create_time (int | Unset): The time when the payment was initiated in TikTok Shop, as a Unix timestamp in
            seconds.
        id (str | Unset): The payment ID.
        status (str | Unset): The payment status, indicating whether payment has been transferred to the seller's bank
            account.
            Possible values:
            - PAID: Payment has been transferred to the seller.
            - FAILED: Payment transfer failed.
            - PROCESSING: Payment is currently being processed.
        amount (GetPaymentsResponseDataPaymentAmount | Unset):
        settlement_amount (GetPaymentsResponseDataPaymentSettlementAmount | Unset):
        payment_amount_before_exchange (GetPaymentsResponseDataPaymentPaymentAmountBeforeExchange | Unset):
        exchange_rate (str | Unset): The exchange rate, displayed with six decimal places.
        paid_time (int | Unset): The time when payment processing finished in TikTok Shop, as a Unix timestamp in
            seconds. Returns `0` when no finish time is available.
        bank_account (str | Unset): The seller's bank account number masked, revealing only the last 4 digits for
            privacy.
    """

    create_time: int | Unset = UNSET
    id: str | Unset = UNSET
    status: str | Unset = UNSET
    amount: GetPaymentsResponseDataPaymentAmount | Unset = UNSET
    settlement_amount: GetPaymentsResponseDataPaymentSettlementAmount | Unset = UNSET
    payment_amount_before_exchange: GetPaymentsResponseDataPaymentPaymentAmountBeforeExchange | Unset = UNSET
    exchange_rate: str | Unset = UNSET
    paid_time: int | Unset = UNSET
    bank_account: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_time = self.create_time

        id = self.id

        status = self.status

        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        settlement_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settlement_amount, Unset):
            settlement_amount = self.settlement_amount.to_dict()

        payment_amount_before_exchange: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payment_amount_before_exchange, Unset):
            payment_amount_before_exchange = self.payment_amount_before_exchange.to_dict()

        exchange_rate = self.exchange_rate

        paid_time = self.paid_time

        bank_account = self.bank_account

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if amount is not UNSET:
            field_dict["amount"] = amount
        if settlement_amount is not UNSET:
            field_dict["settlement_amount"] = settlement_amount
        if payment_amount_before_exchange is not UNSET:
            field_dict["payment_amount_before_exchange"] = payment_amount_before_exchange
        if exchange_rate is not UNSET:
            field_dict["exchange_rate"] = exchange_rate
        if paid_time is not UNSET:
            field_dict["paid_time"] = paid_time
        if bank_account is not UNSET:
            field_dict["bank_account"] = bank_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_payments_response_data_payment_amount import (
            GetPaymentsResponseDataPaymentAmount,  # noqa: PLC0415
        )
        from ..models.get_payments_response_data_payment_payment_amount_before_exchange import (
            GetPaymentsResponseDataPaymentPaymentAmountBeforeExchange,  # noqa: PLC0415
        )
        from ..models.get_payments_response_data_payment_settlement_amount import (
            GetPaymentsResponseDataPaymentSettlementAmount,  # noqa: PLC0415
        )

        d = dict(src_dict)
        create_time = d.pop("create_time", UNSET)

        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        _amount = d.pop("amount", UNSET)
        amount: GetPaymentsResponseDataPaymentAmount | Unset
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = GetPaymentsResponseDataPaymentAmount.from_dict(_amount)

        _settlement_amount = d.pop("settlement_amount", UNSET)
        settlement_amount: GetPaymentsResponseDataPaymentSettlementAmount | Unset
        if isinstance(_settlement_amount, Unset):
            settlement_amount = UNSET
        else:
            settlement_amount = GetPaymentsResponseDataPaymentSettlementAmount.from_dict(_settlement_amount)

        _payment_amount_before_exchange = d.pop("payment_amount_before_exchange", UNSET)
        payment_amount_before_exchange: GetPaymentsResponseDataPaymentPaymentAmountBeforeExchange | Unset
        if isinstance(_payment_amount_before_exchange, Unset):
            payment_amount_before_exchange = UNSET
        else:
            payment_amount_before_exchange = GetPaymentsResponseDataPaymentPaymentAmountBeforeExchange.from_dict(
                _payment_amount_before_exchange
            )

        exchange_rate = d.pop("exchange_rate", UNSET)

        paid_time = d.pop("paid_time", UNSET)

        bank_account = d.pop("bank_account", UNSET)

        get_payments_response_data_payment = cls(
            create_time=create_time,
            id=id,
            status=status,
            amount=amount,
            settlement_amount=settlement_amount,
            payment_amount_before_exchange=payment_amount_before_exchange,
            exchange_rate=exchange_rate,
            paid_time=paid_time,
            bank_account=bank_account,
        )

        get_payments_response_data_payment.additional_properties = d
        return get_payments_response_data_payment

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
