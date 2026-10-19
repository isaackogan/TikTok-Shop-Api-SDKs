from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_return_response_data_return_status import CreateReturnResponseDataReturnStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateReturnResponseData")


@_attrs_define
class CreateReturnResponseData:
    """
    Attributes:
        return_id (str | Unset): The identifier of a specific return request.
        return_status (CreateReturnResponseDataReturnStatus | Unset): Return status, available values:
            - RETURN_OR_REFUND_REQUEST_PENDING: Request is pending, needs to be approved by seller or platform
            - REFUND_OR_RETURN_REQUEST_REJECT: Seller rejected the request
            - AWAITING_BUYER_SHIP: Waiting buyer to ship items to seller, if exceed the deadline, request will be closed by
            platform
            - BUYER_SHIPPED_ITEM: Buyer has shipped items to seller.
            - REJECT_RECEIVE_PACKAGE: Seller reject return package
            - RETURN_OR_REFUND_REQUEST_SUCCESS: The refund/return request is successful, buyer will be refunded.
            - RETURN_OR_REFUND_REQUEST_CANCEL: The request has been cancelled by buyer or system
            - RETURN_OR_REFUND_REQUEST_COMPLETE: The request is successful, and the amount has been refunded.
    """

    return_id: str | Unset = UNSET
    return_status: CreateReturnResponseDataReturnStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return_id = self.return_id

        return_status: str | Unset = UNSET
        if not isinstance(self.return_status, Unset):
            return_status = self.return_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if return_id is not UNSET:
            field_dict["return_id"] = return_id
        if return_status is not UNSET:
            field_dict["return_status"] = return_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        return_id = d.pop("return_id", UNSET)

        _return_status = d.pop("return_status", UNSET)
        return_status: CreateReturnResponseDataReturnStatus | Unset
        if isinstance(_return_status, Unset):
            return_status = UNSET
        else:
            return_status = CreateReturnResponseDataReturnStatus(_return_status)

        create_return_response_data = cls(
            return_id=return_id,
            return_status=return_status,
        )

        create_return_response_data.additional_properties = d
        return create_return_response_data

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
