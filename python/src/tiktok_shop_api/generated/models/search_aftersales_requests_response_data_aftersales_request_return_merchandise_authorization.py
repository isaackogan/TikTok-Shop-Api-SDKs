from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line_item import LineItem


T = TypeVar("T", bound="SearchAftersalesRequestsResponseDataAftersalesRequestReturnMerchandiseAuthorization")


@_attrs_define
class SearchAftersalesRequestsResponseDataAftersalesRequestReturnMerchandiseAuthorization:
    """
    Attributes:
        id (str | Unset): Unique identifier for this RMA data.
        package_id (str | Unset): Identifier of the associated physical return package.
        aftersales_request_id (str | Unset): Identifier of the parent aftersales request.
        status (str | Unset): The current state of this RMA data.
            Possible values:
            - `INIT`
            - `AWAITING_BUYER_RETURN`
            - `RETURN_IN_TRANSIT`
            - `PENDING_PACKAGE_REVIEW`
            - `PACKAGE_REVIEW_COMPLETED`
        line_items (list[LineItem] | Unset): List of items associated with this return merchandise authorization (RMA).
    """

    id: str | Unset = UNSET
    package_id: str | Unset = UNSET
    aftersales_request_id: str | Unset = UNSET
    status: str | Unset = UNSET
    line_items: list[LineItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        package_id = self.package_id

        aftersales_request_id = self.aftersales_request_id

        status = self.status

        line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if package_id is not UNSET:
            field_dict["package_id"] = package_id
        if aftersales_request_id is not UNSET:
            field_dict["aftersales_request_id"] = aftersales_request_id
        if status is not UNSET:
            field_dict["status"] = status
        if line_items is not UNSET:
            field_dict["line_items"] = line_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.line_item import LineItem  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        package_id = d.pop("package_id", UNSET)

        aftersales_request_id = d.pop("aftersales_request_id", UNSET)

        status = d.pop("status", UNSET)

        _line_items = d.pop("line_items", UNSET)
        line_items: list[LineItem] | Unset = UNSET
        if _line_items is not UNSET:
            line_items = []
            for line_items_item_data in _line_items:
                line_items_item = LineItem.from_dict(line_items_item_data)

                line_items.append(line_items_item)

        search_aftersales_requests_response_data_aftersales_request_return_merchandise_authorization = cls(
            id=id,
            package_id=package_id,
            aftersales_request_id=aftersales_request_id,
            status=status,
            line_items=line_items,
        )

        search_aftersales_requests_response_data_aftersales_request_return_merchandise_authorization.additional_properties = d
        return search_aftersales_requests_response_data_aftersales_request_return_merchandise_authorization

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
