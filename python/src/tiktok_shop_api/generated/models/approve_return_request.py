from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.approve_return_request_decision import ApproveReturnRequestDecision
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.partial_refund import PartialRefund





T = TypeVar("T", bound="ApproveReturnRequest")



@_attrs_define
class ApproveReturnRequest:
    """ 
        Attributes:
            decision (ApproveReturnRequestDecision): Seller's decision for the return request, available values:
                - `APPROVE_REFUND`: seller approve a refund-only request
                - `APPROVE_RETURN`: seller approve the initial return-and-refund request
                - `APPROVE_RECEIVED_PACKAGE`: seller approve return-and-refund request after the buyer has already shipped or
                handed over the item.
                - `APPROVE_REPLACEMENT`: seller approve replacement request
                - `ISSUE_REPLACEMENT_REFUND`: seller decline the replacement request and directly refund the buyer instead.
                - `OFFER_PARTIAL_REFUND`: seller offers a partial refund amount to the buyer without requiring the item(s) to be
                returned.
                - `DIRECT_REFUND`: seller issues a returnless refund, meaning the buyer receives a full refund and keeps the
                item
            buyer_keep_item (bool | Unset): **Optional**. Use this field only when decision is set to `APPROVE_RETURN`. If
                set to `true`, the seller issues a returnless refund, which means the buyer receives a full refund and keeps the
                item. If set to `false` or omitted, the seller approves the return-and-refund flow and the buyer returns the
                item.
            partial_refund (PartialRefund | Unset):
     """

    decision: ApproveReturnRequestDecision
    buyer_keep_item: bool | Unset = UNSET
    partial_refund: PartialRefund | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.partial_refund import PartialRefund # noqa: PLC0415
        decision = self.decision.value

        buyer_keep_item = self.buyer_keep_item

        partial_refund: dict[str, Any] | Unset = UNSET
        if not isinstance(self.partial_refund, Unset):
            partial_refund = self.partial_refund.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "decision": decision,
        })
        if buyer_keep_item is not UNSET:
            field_dict["buyer_keep_item"] = buyer_keep_item
        if partial_refund is not UNSET:
            field_dict["partial_refund"] = partial_refund

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partial_refund import PartialRefund # noqa: PLC0415
        d = dict(src_dict)
        decision = ApproveReturnRequestDecision(d.pop("decision"))




        buyer_keep_item = d.pop("buyer_keep_item", UNSET)

        _partial_refund = d.pop("partial_refund", UNSET)
        partial_refund: PartialRefund | Unset
        if isinstance(_partial_refund,  Unset):
            partial_refund = UNSET
        else:
            partial_refund = PartialRefund.from_dict(_partial_refund)




        approve_return_request = cls(
            decision=decision,
            buyer_keep_item=buyer_keep_item,
            partial_refund=partial_refund,
        )


        approve_return_request.additional_properties = d
        return approve_return_request

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
