from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.search_global_products_request_status import SearchGlobalProductsRequestStatus
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SearchGlobalProductsRequest")



@_attrs_define
class SearchGlobalProductsRequest:
    """ 
        Attributes:
            status (SearchGlobalProductsRequestStatus | Unset): Filter global products by their status.
                Possible values:
                - PUBLISHED
                - UNPUBLISHED
                - DRAFT
                - DELETED
            seller_skus (list[str] | Unset): A Seller SKU used to filter global products. Provide no more than one Seller
                SKU. The API returns global products that include the specified Seller SKU.
            create_time_ge (int | Unset): Filter global products to show only those that are created on or after the
                specified date and time. Unix timestamp in seconds.

                **Note**:
                The "create_time_ge" and "create_time_le" together constitute the creation time filter condition.
                - If "create_time_ge" is filled but "create_time_le" is empty, "create_time_le" will default to the current
                time.
                - If "create_time_le" is filled but "create_time_ge" is empty, "create_time_ge" will default to the earliest
                shop time.
            create_time_le (int | Unset): Filter global products to show only those that are created on or before the
                specified date and time. Unix timestamp in seconds.
                Refer to notes in "create_time_ge" for more usage information.
            update_time_ge (int | Unset): Filter global products to show only those that are updated on or after the
                specified date and time. Unix timestamp in seconds.

                **Note**:
                The fields "update_time_ge" and "update_time_le" together define the update time filter condition.
                - If "update_time_ge" is filled but "update_time_le" is empty, "update_time_le" will default to the current
                time.
                - If "update_time_le" is filled but "update_time_ge" is empty, "update_time_ge" will default to the earliest
                shop time.
            update_time_le (int | Unset): Filter global products to show only those that are updated on or before the
                specified date and time. Unix timestamp in seconds.
                Refer to notes in `update_time_ge` for more usage information.
     """

    status: SearchGlobalProductsRequestStatus | Unset = UNSET
    seller_skus: list[str] | Unset = UNSET
    create_time_ge: int | Unset = UNSET
    create_time_le: int | Unset = UNSET
    update_time_ge: int | Unset = UNSET
    update_time_le: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        seller_skus: list[str] | Unset = UNSET
        if not isinstance(self.seller_skus, Unset):
            seller_skus = self.seller_skus



        create_time_ge = self.create_time_ge

        create_time_le = self.create_time_le

        update_time_ge = self.update_time_ge

        update_time_le = self.update_time_le


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if status is not UNSET:
            field_dict["status"] = status
        if seller_skus is not UNSET:
            field_dict["seller_skus"] = seller_skus
        if create_time_ge is not UNSET:
            field_dict["create_time_ge"] = create_time_ge
        if create_time_le is not UNSET:
            field_dict["create_time_le"] = create_time_le
        if update_time_ge is not UNSET:
            field_dict["update_time_ge"] = update_time_ge
        if update_time_le is not UNSET:
            field_dict["update_time_le"] = update_time_le

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: SearchGlobalProductsRequestStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = SearchGlobalProductsRequestStatus(_status)




        seller_skus = cast(list[str], d.pop("seller_skus", UNSET))


        create_time_ge = d.pop("create_time_ge", UNSET)

        create_time_le = d.pop("create_time_le", UNSET)

        update_time_ge = d.pop("update_time_ge", UNSET)

        update_time_le = d.pop("update_time_le", UNSET)

        search_global_products_request = cls(
            status=status,
            seller_skus=seller_skus,
            create_time_ge=create_time_ge,
            create_time_le=create_time_le,
            update_time_ge=update_time_ge,
            update_time_le=update_time_le,
        )


        search_global_products_request.additional_properties = d
        return search_global_products_request

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
