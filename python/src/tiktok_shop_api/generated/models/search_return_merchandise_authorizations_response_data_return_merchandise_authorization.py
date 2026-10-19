from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_return_merchandise_authorizations_response_data_return_merchandise_authorization_status import (
    SearchReturnMerchandiseAuthorizationsResponseDataReturnMerchandiseAuthorizationStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line_item import LineItem
    from ..models.sku_return_request import SkuReturnRequest


T = TypeVar("T", bound="SearchReturnMerchandiseAuthorizationsResponseDataReturnMerchandiseAuthorization")


@_attrs_define
class SearchReturnMerchandiseAuthorizationsResponseDataReturnMerchandiseAuthorization:
    """
    Attributes:
        id (str | Unset): Unique identifier for this RMA data.
        package_id (str | Unset): Identifier of the associated physical return package.
        aftersales_request_id (str | Unset): Identifier of the parent aftersales request.
        status (SearchReturnMerchandiseAuthorizationsResponseDataReturnMerchandiseAuthorizationStatus | Unset): The
            current state of this RMA data.
            Possible values:
            - `INIT`
            - `AWAITING_BUYER_RETURN`
            - `RETURN_IN_TRANSIT`
            - `PENDING_PACKAGE_REVIEW`
            - `PACKAGE_REVIEW_COMPLETED`
        line_items (list[LineItem] | Unset): Item units expected in this return package. This field is returned only
            when `LINE_ITEMS` is included in `whitelisted_data_fields` and matching item data is available.
        sku_return_requests (list[SkuReturnRequest] | Unset): SKU-level sub return requests associated with this RMA.
            This field is returned only when `SKU_RETURN_REQUESTS` is included in `whitelisted_data_fields` and matching
            data is available.
    """

    id: str | Unset = UNSET
    package_id: str | Unset = UNSET
    aftersales_request_id: str | Unset = UNSET
    status: SearchReturnMerchandiseAuthorizationsResponseDataReturnMerchandiseAuthorizationStatus | Unset = UNSET
    line_items: list[LineItem] | Unset = UNSET
    sku_return_requests: list[SkuReturnRequest] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        package_id = self.package_id

        aftersales_request_id = self.aftersales_request_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)

        sku_return_requests: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sku_return_requests, Unset):
            sku_return_requests = []
            for sku_return_requests_item_data in self.sku_return_requests:
                sku_return_requests_item = sku_return_requests_item_data.to_dict()
                sku_return_requests.append(sku_return_requests_item)

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
        if sku_return_requests is not UNSET:
            field_dict["sku_return_requests"] = sku_return_requests

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.line_item import LineItem  # noqa: PLC0415
        from ..models.sku_return_request import SkuReturnRequest  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        package_id = d.pop("package_id", UNSET)

        aftersales_request_id = d.pop("aftersales_request_id", UNSET)

        _status = d.pop("status", UNSET)
        status: SearchReturnMerchandiseAuthorizationsResponseDataReturnMerchandiseAuthorizationStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SearchReturnMerchandiseAuthorizationsResponseDataReturnMerchandiseAuthorizationStatus(_status)

        _line_items = d.pop("line_items", UNSET)
        line_items: list[LineItem] | Unset = UNSET
        if _line_items is not UNSET:
            line_items = []
            for line_items_item_data in _line_items:
                line_items_item = LineItem.from_dict(line_items_item_data)

                line_items.append(line_items_item)

        _sku_return_requests = d.pop("sku_return_requests", UNSET)
        sku_return_requests: list[SkuReturnRequest] | Unset = UNSET
        if _sku_return_requests is not UNSET:
            sku_return_requests = []
            for sku_return_requests_item_data in _sku_return_requests:
                sku_return_requests_item = SkuReturnRequest.from_dict(sku_return_requests_item_data)

                sku_return_requests.append(sku_return_requests_item)

        search_return_merchandise_authorizations_response_data_return_merchandise_authorization = cls(
            id=id,
            package_id=package_id,
            aftersales_request_id=aftersales_request_id,
            status=status,
            line_items=line_items,
            sku_return_requests=sku_return_requests,
        )

        search_return_merchandise_authorizations_response_data_return_merchandise_authorization.additional_properties = d
        return search_return_merchandise_authorizations_response_data_return_merchandise_authorization

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
