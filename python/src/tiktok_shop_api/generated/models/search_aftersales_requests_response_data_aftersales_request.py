from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_aftersales_requests_response_data_aftersales_request_status import (
    SearchAftersalesRequestsResponseDataAftersalesRequestStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line_item import LineItem
    from ..models.search_aftersales_requests_response_data_aftersales_request_return_merchandise_authorization import (
        SearchAftersalesRequestsResponseDataAftersalesRequestReturnMerchandiseAuthorization,
    )
    from ..models.sku_return_request import SkuReturnRequest


T = TypeVar("T", bound="SearchAftersalesRequestsResponseDataAftersalesRequest")


@_attrs_define
class SearchAftersalesRequestsResponseDataAftersalesRequest:
    """
    Attributes:
        id (str | Unset): Unique identifier for this aftersales request.
        line_items (list[LineItem] | Unset): List of items associated with this aftersales request. This field is
            returned only when `LINE_ITEMS` is included in `whitelisted_data_fields` and matching item data is available.
        status (SearchAftersalesRequestsResponseDataAftersalesRequestStatus | Unset): Current state of this aftersales
            request.
            Possible values:
            - `INIT`
            - `PENDING_REQUEST_REVIEW`
            - `REQUEST_REVIEW_COMPLETED`
        sku_return_requests (list[SkuReturnRequest] | Unset): SKU-level sub return requests associated with this
            aftersales request, also known as reverse orders or return requests. This field is returned only when
            `SKU_RETURN_REQUESTS` is included in `whitelisted_data_fields` and matching data is available.
        return_merchandise_authorizations
            (list[SearchAftersalesRequestsResponseDataAftersalesRequestReturnMerchandiseAuthorization] | Unset): Return
            merchandise authorization (RMA) records associated with this aftersales request. This field is returned only
            when `RETURN_MERCHANDISE_AUTHORIZATIONS` is included in `whitelisted_data_fields` and matching RMA data is
            available.
    """

    id: str | Unset = UNSET
    line_items: list[LineItem] | Unset = UNSET
    status: SearchAftersalesRequestsResponseDataAftersalesRequestStatus | Unset = UNSET
    sku_return_requests: list[SkuReturnRequest] | Unset = UNSET
    return_merchandise_authorizations: (
        list[SearchAftersalesRequestsResponseDataAftersalesRequestReturnMerchandiseAuthorization] | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        sku_return_requests: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sku_return_requests, Unset):
            sku_return_requests = []
            for sku_return_requests_item_data in self.sku_return_requests:
                sku_return_requests_item = sku_return_requests_item_data.to_dict()
                sku_return_requests.append(sku_return_requests_item)

        return_merchandise_authorizations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.return_merchandise_authorizations, Unset):
            return_merchandise_authorizations = []
            for return_merchandise_authorizations_item_data in self.return_merchandise_authorizations:
                return_merchandise_authorizations_item = return_merchandise_authorizations_item_data.to_dict()
                return_merchandise_authorizations.append(return_merchandise_authorizations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if line_items is not UNSET:
            field_dict["line_items"] = line_items
        if status is not UNSET:
            field_dict["status"] = status
        if sku_return_requests is not UNSET:
            field_dict["sku_return_requests"] = sku_return_requests
        if return_merchandise_authorizations is not UNSET:
            field_dict["return_merchandise_authorizations"] = return_merchandise_authorizations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.line_item import LineItem  # noqa: PLC0415
        from ..models.search_aftersales_requests_response_data_aftersales_request_return_merchandise_authorization import (
            SearchAftersalesRequestsResponseDataAftersalesRequestReturnMerchandiseAuthorization,  # noqa: PLC0415
        )
        from ..models.sku_return_request import SkuReturnRequest  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _line_items = d.pop("line_items", UNSET)
        line_items: list[LineItem] | Unset = UNSET
        if _line_items is not UNSET:
            line_items = []
            for line_items_item_data in _line_items:
                line_items_item = LineItem.from_dict(line_items_item_data)

                line_items.append(line_items_item)

        _status = d.pop("status", UNSET)
        status: SearchAftersalesRequestsResponseDataAftersalesRequestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SearchAftersalesRequestsResponseDataAftersalesRequestStatus(_status)

        _sku_return_requests = d.pop("sku_return_requests", UNSET)
        sku_return_requests: list[SkuReturnRequest] | Unset = UNSET
        if _sku_return_requests is not UNSET:
            sku_return_requests = []
            for sku_return_requests_item_data in _sku_return_requests:
                sku_return_requests_item = SkuReturnRequest.from_dict(sku_return_requests_item_data)

                sku_return_requests.append(sku_return_requests_item)

        _return_merchandise_authorizations = d.pop("return_merchandise_authorizations", UNSET)
        return_merchandise_authorizations: (
            list[SearchAftersalesRequestsResponseDataAftersalesRequestReturnMerchandiseAuthorization] | Unset
        ) = UNSET
        if _return_merchandise_authorizations is not UNSET:
            return_merchandise_authorizations = []
            for return_merchandise_authorizations_item_data in _return_merchandise_authorizations:
                return_merchandise_authorizations_item = (
                    SearchAftersalesRequestsResponseDataAftersalesRequestReturnMerchandiseAuthorization.from_dict(
                        return_merchandise_authorizations_item_data
                    )
                )

                return_merchandise_authorizations.append(return_merchandise_authorizations_item)

        search_aftersales_requests_response_data_aftersales_request = cls(
            id=id,
            line_items=line_items,
            status=status,
            sku_return_requests=sku_return_requests,
            return_merchandise_authorizations=return_merchandise_authorizations,
        )

        search_aftersales_requests_response_data_aftersales_request.additional_properties = d
        return search_aftersales_requests_response_data_aftersales_request

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
