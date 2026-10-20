from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.delete_webhook_for_an_event_request_event_type import DeleteWebhookForAnEventRequestEventType






T = TypeVar("T", bound="DeleteWebhookForAnEventRequest")



@_attrs_define
class DeleteWebhookForAnEventRequest:
    """ 
        Attributes:
            event_type (DeleteWebhookForAnEventRequestEventType): The topic of the webhook event.
                Possible values:
                - `ORDER_STATUS_CHANGE`: Triggers on each order status update, from new order placement through all subsequent
                status changes. See [Order Status change](650300b8a57708028b430b4a).
                - `RECIPIENT_ADDRESS_UPDATE`: Triggers when the recipient's address is updated. See [Receipient address
                update](650301af5a12ff0294ea3bf9).
                - `PACKAGE_UPDATE`: Triggers when a package is updated (e.g., combined, split, or address changed). See [Package
                update](650955cabace3e02b73cc886).
                - `PRODUCT_STATUS_CHANGE`: Triggers when product audit results are updated. See [Product status
                change](650956aff1fd3102b90b6261).
                - `SELLER_DEAUTHORIZATION`: Triggers when a seller is deauthorized to inform developers and avoid
                misunderstandings about platform authorization issues. See [Seller deauthorization](65095746defece02be4d749d).
                - `UPCOMING_AUTHORIZATION_EXPIRATION`: Triggers 30 days before authorization expiration, with daily
                notifications at 0:00 until re-authorization is completed. See [Upcoming authorization
                expiration](6509579c0fcef602bf11312c).
                - `CANCELLATION_STATUS_CHANGE`: Triggers when an order's cancellation status changes. See [Cancellation status
                change](65030150746462028285f657).
                - `RETURN_STATUS_CHANGE`: Triggers when an order's return status changes. See [Return status
                change](65030162bb2a4d028d50cc51).
                - `NEW_CONVERSATION`: Triggers when a customer service agent joins or leaves a conversation. See [New
                conversation](6614330bfe9fdc02e002abfd).
                - `NEW_MESSAGE`: Triggers when a new message is sent in a customer service conversation. See [New
                Message](66143486ef8a1202dc323258).
                - `PRODUCT_INFORMATION_CHANGE`: Triggers when changes to a product's title, description, main images, or
                attributes go live. See [Product information change](65d6f41411a60f02dc1cf8bf).
                - `PRODUCT_CREATION`: Triggers when a new product is created. See [Product creation](663c98b566828e02e4515580).
                - `PRODUCT_CATEGORY_CHANGE`: Triggers when the category of a product is changed. See [Product category
                change](668764a371f16d02eef1f393).
                - `NEW_MESSAGE_LISTENER`: Triggers when a creator sends a message to the seller. See [New message
                listener](6790b76eb59cf9030997b783).
                - `INVOICE_STATUS_CHANGE`: Triggers when the status of an invoice upload changes after using the [POST Upload
                Invoice](67b542559a140004b343984f) endpoint. See [Invoice Status Change](67b68ca185619104a6772e5d).
                - `PRODUCT_AUDIT_STATUS_CHANGE`: Triggers when the product audit status changes. See [Product audit status
                change](67b5c6cba42623049abe5062).
                - `REVERSE_STATUS_UPDATE`: Triggers when buyer raises cancellation, refund only, or return & refund requests
                that need the seller to accept or reject. See [Reverse Status
                Update](https://partner.tiktokshop.com/doc/page/63fd7459715d622a338c5437).
     """

    event_type: DeleteWebhookForAnEventRequestEventType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "event_type": event_type,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_type = DeleteWebhookForAnEventRequestEventType(d.pop("event_type"))




        delete_webhook_for_an_event_request = cls(
            event_type=event_type,
        )


        delete_webhook_for_an_event_request.additional_properties = d
        return delete_webhook_for_an_event_request

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
