from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.search_returns_request_arbitration_status_item import SearchReturnsRequestArbitrationStatusItem
from ..models.search_returns_request_return_status_item import SearchReturnsRequestReturnStatusItem
from ..models.search_returns_request_return_types_item import SearchReturnsRequestReturnTypesItem
from ..models.search_returns_request_seller_proposed_return_type_item import SearchReturnsRequestSellerProposedReturnTypeItem
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SearchReturnsRequest")



@_attrs_define
class SearchReturnsRequest:
    """ 
        Attributes:
            return_ids (list[str] | Unset): List of return IDs. Each ID must be a base-10 integer string that fits in a
                signed 64-bit integer.
            order_ids (list[str] | Unset): List of TikTok Shop order IDs. Each ID must be a base-10 integer string that fits
                in a signed 64-bit integer.
            buyer_user_ids (list[str] | Unset): List of TikTok Shop buyer user IDs. Each ID must be a base-10 integer string
                that fits in a signed 64-bit integer.
            return_types (list[SearchReturnsRequestReturnTypesItem] | Unset): List of return types.
                Available values:
                - `REFUND`
                - `RETURN_AND_REFUND`
                - `REPLACEMENT`
                - `EXCHANGE`
            return_status (list[SearchReturnsRequestReturnStatusItem] | Unset): List of return status.
                Available values:
                - `RETURN_OR_REFUND_REQUEST_PENDING`: Buyer has initiated a return or refund request. The request is pending
                review by seller or system.
                - `REFUND_OR_RETURN_REQUEST_REJECT`: The return or refund request was rejected.
                - `AWAITING_BUYER_SHIP`: The return request was approved. The seller is waiting for the buyer to ship the
                approved items to the seller. If the buyer doesn't ship the items to the seller before the deadline, the
                platform will close the request.
                - `BUYER_SHIPPED_ITEM`: Buyer has shipped the approved items to seller.
                - `REJECT_RECEIVE_PACKAGE`: Seller inspected the returned items and rejected the return request.
                - `RETURN_OR_REFUND_REQUEST_SUCCESS`: The return/refund request was successful. The buyer will be refunded.
                - `RETURN_OR_REFUND_REQUEST_CANCEL`: The request has been cancelled by the buyer or system.
                - `RETURN_OR_REFUND_REQUEST_COMPLETE`: The return/refund was processed successfully. The buyer has been
                refunded.
                - `REPLACEMENT_REQUEST_PENDING`: Buyer has initiated a replacement request. The request is pending review by
                seller.
                - `REPLACEMENT_REQUEST_REJECT`: Seller reject the buyer replacement request.
                - `REPLACEMENT_REQUEST_REFUND_SUCCESS`: Buyer's replacement request was resolved by refund due to insufficient
                inventory.
                - `REPLACEMENT_REQUEST_CANCEL`: Buyer canceled the replacement request.
                - `REPLACEMENT_REQUEST_COMPLETE`: Seller has approved the buyer's replacement request, platform will generate a
                new order for seller to fulfill.
                - `AWAITING_BUYER_RESPONSE`: Seller offer another return type to the buyer, and waiting buyer response. Seller
                proposed return type can check the `seller_proposed_return_type`.
                - `EXCHANGE_REQUEST_PENDING`: Buyer has initiated an exchange request. The request is pending review by seller.
                - `EXCHANGE_REQUEST_REFUND_SUCCESS`: Buyer's exchange request was resolved by refund due to insufficient
                inventory.
                - `EXCHANGE_REQUEST_CANCEL`: Buyer canceled the exchange request.
                - `EXCHANGE_REQUEST_COMPLETE`: Seller has approved the buyer's exchange request, platform will generate a new
                order for seller to fulfill.
            seller_proposed_return_type (list[SearchReturnsRequestSellerProposedReturnTypeItem] | Unset): List of seller
                proposed return types.
                Available values:
                - `PARTIAL_REFUND`
            create_time_ge (int | Unset): Filter returns to show only those that are created on or after the specified date
                and time. Unix timestamp.

                Note:
                `create_time_ge` and `create_time_le` together constitute the creation time filter condition.
                - If `create_time_ge` is filled but `create_time_le` is empty, `create_time_le` will default to the current
                time.
                - If `create_time_lt` is filled but `create_time_ge` is empty, `create_time_ge` will default to the earliest
                shop time.
            arbitration_status (list[SearchReturnsRequestArbitrationStatusItem] | Unset): List of arbitration statuses.
                Available values:
                - `IN_PROGRESS`: The TikTok Shop platform operator is processing arbitration. Platform may request additional
                information from the seller.
                - `SUPPORT_BUYER`: The platform operator supports buyer.
                - `SUPPORT_SELLER`: The platform operator supports seller.
                - `CLOSED`: Arbitration is closed.
            update_time_ge (int | Unset): Filter returns to show only those that are updated on or after the specified date
                and time. Unix timestamp.

                Note:
                `update_time_ge` and `update_time_le` together define the update time filter condition.
                - If `update_time_ge` is filled but `update_time_le` is empty, `update_time_le` will default to the current
                time.
                - If `update_time_lt` is filled but `update_time_ge` is empty, `update_time_ge` will default to the earliest
                shop time.
            update_time_lt (int | Unset): Filter returns to those updated before the specified time. Provide a Unix
                timestamp in seconds.
            locale (str | Unset): The BCP-47 locale codes for displaying the returns, delimited by commas. Default: `en`
                Refer to [Locale codes](678e3a47bae28f030a8c7523) for the list of supported locale codes.
            create_time_lt (int | Unset): Filter returns to those created before the specified time. Provide a Unix
                timestamp in seconds.
     """

    return_ids: list[str] | Unset = UNSET
    order_ids: list[str] | Unset = UNSET
    buyer_user_ids: list[str] | Unset = UNSET
    return_types: list[SearchReturnsRequestReturnTypesItem] | Unset = UNSET
    return_status: list[SearchReturnsRequestReturnStatusItem] | Unset = UNSET
    seller_proposed_return_type: list[SearchReturnsRequestSellerProposedReturnTypeItem] | Unset = UNSET
    create_time_ge: int | Unset = UNSET
    arbitration_status: list[SearchReturnsRequestArbitrationStatusItem] | Unset = UNSET
    update_time_ge: int | Unset = UNSET
    update_time_lt: int | Unset = UNSET
    locale: str | Unset = UNSET
    create_time_lt: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        return_ids: list[str] | Unset = UNSET
        if not isinstance(self.return_ids, Unset):
            return_ids = self.return_ids



        order_ids: list[str] | Unset = UNSET
        if not isinstance(self.order_ids, Unset):
            order_ids = self.order_ids



        buyer_user_ids: list[str] | Unset = UNSET
        if not isinstance(self.buyer_user_ids, Unset):
            buyer_user_ids = self.buyer_user_ids



        return_types: list[str] | Unset = UNSET
        if not isinstance(self.return_types, Unset):
            return_types = []
            for return_types_item_data in self.return_types:
                return_types_item = return_types_item_data.value
                return_types.append(return_types_item)



        return_status: list[str] | Unset = UNSET
        if not isinstance(self.return_status, Unset):
            return_status = []
            for return_status_item_data in self.return_status:
                return_status_item = return_status_item_data.value
                return_status.append(return_status_item)



        seller_proposed_return_type: list[str] | Unset = UNSET
        if not isinstance(self.seller_proposed_return_type, Unset):
            seller_proposed_return_type = []
            for seller_proposed_return_type_item_data in self.seller_proposed_return_type:
                seller_proposed_return_type_item = seller_proposed_return_type_item_data.value
                seller_proposed_return_type.append(seller_proposed_return_type_item)



        create_time_ge = self.create_time_ge

        arbitration_status: list[str] | Unset = UNSET
        if not isinstance(self.arbitration_status, Unset):
            arbitration_status = []
            for arbitration_status_item_data in self.arbitration_status:
                arbitration_status_item = arbitration_status_item_data.value
                arbitration_status.append(arbitration_status_item)



        update_time_ge = self.update_time_ge

        update_time_lt = self.update_time_lt

        locale = self.locale

        create_time_lt = self.create_time_lt


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if return_ids is not UNSET:
            field_dict["return_ids"] = return_ids
        if order_ids is not UNSET:
            field_dict["order_ids"] = order_ids
        if buyer_user_ids is not UNSET:
            field_dict["buyer_user_ids"] = buyer_user_ids
        if return_types is not UNSET:
            field_dict["return_types"] = return_types
        if return_status is not UNSET:
            field_dict["return_status"] = return_status
        if seller_proposed_return_type is not UNSET:
            field_dict["seller_proposed_return_type"] = seller_proposed_return_type
        if create_time_ge is not UNSET:
            field_dict["create_time_ge"] = create_time_ge
        if arbitration_status is not UNSET:
            field_dict["arbitration_status"] = arbitration_status
        if update_time_ge is not UNSET:
            field_dict["update_time_ge"] = update_time_ge
        if update_time_lt is not UNSET:
            field_dict["update_time_lt"] = update_time_lt
        if locale is not UNSET:
            field_dict["locale"] = locale
        if create_time_lt is not UNSET:
            field_dict["create_time_lt"] = create_time_lt

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        return_ids = cast(list[str], d.pop("return_ids", UNSET))


        order_ids = cast(list[str], d.pop("order_ids", UNSET))


        buyer_user_ids = cast(list[str], d.pop("buyer_user_ids", UNSET))


        _return_types = d.pop("return_types", UNSET)
        return_types: list[SearchReturnsRequestReturnTypesItem] | Unset = UNSET
        if _return_types is not UNSET:
            return_types = []
            for return_types_item_data in _return_types:
                return_types_item = SearchReturnsRequestReturnTypesItem(return_types_item_data)



                return_types.append(return_types_item)


        _return_status = d.pop("return_status", UNSET)
        return_status: list[SearchReturnsRequestReturnStatusItem] | Unset = UNSET
        if _return_status is not UNSET:
            return_status = []
            for return_status_item_data in _return_status:
                return_status_item = SearchReturnsRequestReturnStatusItem(return_status_item_data)



                return_status.append(return_status_item)


        _seller_proposed_return_type = d.pop("seller_proposed_return_type", UNSET)
        seller_proposed_return_type: list[SearchReturnsRequestSellerProposedReturnTypeItem] | Unset = UNSET
        if _seller_proposed_return_type is not UNSET:
            seller_proposed_return_type = []
            for seller_proposed_return_type_item_data in _seller_proposed_return_type:
                seller_proposed_return_type_item = SearchReturnsRequestSellerProposedReturnTypeItem(seller_proposed_return_type_item_data)



                seller_proposed_return_type.append(seller_proposed_return_type_item)


        create_time_ge = d.pop("create_time_ge", UNSET)

        _arbitration_status = d.pop("arbitration_status", UNSET)
        arbitration_status: list[SearchReturnsRequestArbitrationStatusItem] | Unset = UNSET
        if _arbitration_status is not UNSET:
            arbitration_status = []
            for arbitration_status_item_data in _arbitration_status:
                arbitration_status_item = SearchReturnsRequestArbitrationStatusItem(arbitration_status_item_data)



                arbitration_status.append(arbitration_status_item)


        update_time_ge = d.pop("update_time_ge", UNSET)

        update_time_lt = d.pop("update_time_lt", UNSET)

        locale = d.pop("locale", UNSET)

        create_time_lt = d.pop("create_time_lt", UNSET)

        search_returns_request = cls(
            return_ids=return_ids,
            order_ids=order_ids,
            buyer_user_ids=buyer_user_ids,
            return_types=return_types,
            return_status=return_status,
            seller_proposed_return_type=seller_proposed_return_type,
            create_time_ge=create_time_ge,
            arbitration_status=arbitration_status,
            update_time_ge=update_time_ge,
            update_time_lt=update_time_lt,
            locale=locale,
            create_time_lt=create_time_lt,
        )


        search_returns_request.additional_properties = d
        return search_returns_request

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
