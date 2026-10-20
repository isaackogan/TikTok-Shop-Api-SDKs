from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.external_order import ExternalOrder





T = TypeVar("T", bound="SearchOrdersByExternalOrderReferenceResponseDataOrder")



@_attrs_define
class SearchOrdersByExternalOrderReferenceResponseDataOrder:
    """ 
        Attributes:
            id (str | Unset): The unique identifier for a TikTok Shop order.
            external_order (ExternalOrder | Unset):
     """

    id: str | Unset = UNSET
    external_order: ExternalOrder | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.external_order import ExternalOrder # noqa: PLC0415
        id = self.id

        external_order: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_order, Unset):
            external_order = self.external_order.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if external_order is not UNSET:
            field_dict["external_order"] = external_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_order import ExternalOrder # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _external_order = d.pop("external_order", UNSET)
        external_order: ExternalOrder | Unset
        if isinstance(_external_order,  Unset):
            external_order = UNSET
        else:
            external_order = ExternalOrder.from_dict(_external_order)




        search_orders_by_external_order_reference_response_data_order = cls(
            id=id,
            external_order=external_order,
        )


        search_orders_by_external_order_reference_response_data_order.additional_properties = d
        return search_orders_by_external_order_reference_response_data_order

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
