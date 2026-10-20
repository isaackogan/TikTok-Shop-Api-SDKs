from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.search_return_merchandise_authorizations_request_filter_statuses_item import SearchReturnMerchandiseAuthorizationsRequestFilterStatusesItem
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.time import Time





T = TypeVar("T", bound="SearchReturnMerchandiseAuthorizationsRequestFilter")



@_attrs_define
class SearchReturnMerchandiseAuthorizationsRequestFilter:
    """ 
        Attributes:
            rma_ids (list[str] | Unset): Restricts results to the specified RMA records. Each RMA ID must be a base-10
                integer string that fits in a signed 64-bit integer.
            package_ids (list[str] | Unset): Restricts results to the specified packages. Each package ID must be a base-10
                integer string that fits in a signed 64-bit integer.
            statuses (list[SearchReturnMerchandiseAuthorizationsRequestFilterStatusesItem] | Unset): Restricts results to
                the specified RMA data statuses.
                Possible values:
                - `INIT`
                - `AWAITING_BUYER_RETURN`
                - `RETURN_IN_TRANSIT`
                - `PENDING_PACKAGE_REVIEW`
                - `PACKAGE_REVIEW_COMPLETED`
            aftersales_request_ids (list[str] | Unset): Restricts results to the specified aftersales requests. Each ID must
                be a base-10 integer string that fits in a signed 64-bit integer.
            main_order_ids (list[str] | Unset): Restricts results to the specified main (forward) order IDs.
            time (Time | Unset):
     """

    rma_ids: list[str] | Unset = UNSET
    package_ids: list[str] | Unset = UNSET
    statuses: list[SearchReturnMerchandiseAuthorizationsRequestFilterStatusesItem] | Unset = UNSET
    aftersales_request_ids: list[str] | Unset = UNSET
    main_order_ids: list[str] | Unset = UNSET
    time: Time | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.time import Time # noqa: PLC0415
        rma_ids: list[str] | Unset = UNSET
        if not isinstance(self.rma_ids, Unset):
            rma_ids = self.rma_ids



        package_ids: list[str] | Unset = UNSET
        if not isinstance(self.package_ids, Unset):
            package_ids = self.package_ids



        statuses: list[str] | Unset = UNSET
        if not isinstance(self.statuses, Unset):
            statuses = []
            for statuses_item_data in self.statuses:
                statuses_item = statuses_item_data.value
                statuses.append(statuses_item)



        aftersales_request_ids: list[str] | Unset = UNSET
        if not isinstance(self.aftersales_request_ids, Unset):
            aftersales_request_ids = self.aftersales_request_ids



        main_order_ids: list[str] | Unset = UNSET
        if not isinstance(self.main_order_ids, Unset):
            main_order_ids = self.main_order_ids



        time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rma_ids is not UNSET:
            field_dict["rma_ids"] = rma_ids
        if package_ids is not UNSET:
            field_dict["package_ids"] = package_ids
        if statuses is not UNSET:
            field_dict["statuses"] = statuses
        if aftersales_request_ids is not UNSET:
            field_dict["aftersales_request_ids"] = aftersales_request_ids
        if main_order_ids is not UNSET:
            field_dict["main_order_ids"] = main_order_ids
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.time import Time # noqa: PLC0415
        d = dict(src_dict)
        rma_ids = cast(list[str], d.pop("rma_ids", UNSET))


        package_ids = cast(list[str], d.pop("package_ids", UNSET))


        _statuses = d.pop("statuses", UNSET)
        statuses: list[SearchReturnMerchandiseAuthorizationsRequestFilterStatusesItem] | Unset = UNSET
        if _statuses is not UNSET:
            statuses = []
            for statuses_item_data in _statuses:
                statuses_item = SearchReturnMerchandiseAuthorizationsRequestFilterStatusesItem(statuses_item_data)



                statuses.append(statuses_item)


        aftersales_request_ids = cast(list[str], d.pop("aftersales_request_ids", UNSET))


        main_order_ids = cast(list[str], d.pop("main_order_ids", UNSET))


        _time = d.pop("time", UNSET)
        time: Time | Unset
        if isinstance(_time,  Unset):
            time = UNSET
        else:
            time = Time.from_dict(_time)




        search_return_merchandise_authorizations_request_filter = cls(
            rma_ids=rma_ids,
            package_ids=package_ids,
            statuses=statuses,
            aftersales_request_ids=aftersales_request_ids,
            main_order_ids=main_order_ids,
            time=time,
        )


        search_return_merchandise_authorizations_request_filter.additional_properties = d
        return search_return_merchandise_authorizations_request_filter

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
