from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_warehouse_list_response_data_warehouse_address import GetWarehouseListResponseDataWarehouseAddress





T = TypeVar("T", bound="GetWarehouseListResponseDataWarehouse")



@_attrs_define
class GetWarehouseListResponseDataWarehouse:
    """ 
        Attributes:
            id (str | Unset): The warehouse ID, a unique and immutable primary key, used for all warehouse logistics.
            entity_id (str | Unset): The warehouse entity ID, used to associate physical information of a warehouse,
                different warehouses may be associated with the same entity.
            name (str | Unset): Warehouse name. This name is not unique across the TikTok Shop system.
            effect_status (str | Unset): Indicates whether inventory at the warehouse is available for sale.
                Possible values:
                - `ENABLED`: All products in stock are available for sale.
                - `DISABLED`: All products in stock are unavailable for sale.
                - `RESTRICTED`: The warehouse is in holiday mode or order limit mode, so all products in stock are unavailable
                for sale.

                The seller can enable holiday mode in Seller Center when the seller cannot fulfill orders from the warehouse.
                Order limit mode is applied when TikTok Shop limits the order volume that can be fulfilled by the warehouse
                because of policy violations.
            type_ (str | Unset): Possible values:
                - SALES_WAREHOUSE: Warehouse for shipping products.
                - RETURN_WAREHOUSE: Warehouse for receiving returned products.
                You can have the same warehouse for both shipping and receiving returns, but they will have different warehouse
                IDs with the same address.
            sub_type (str | Unset): Possible values:
                - DOMESTIC_WAREHOUSE: The warehouse is in the same country as the target market and the seller.
                - CB_OVERSEA_WAREHOUSE: For cross-border sellers, a local warehouse in the target market.
                - CB_DIRECT_SHIPPING_WAREHOUSE: For cross-border sellers, a warehouse in the seller's base country, e.g.,
                Mainland China or Hong Kong.
            is_default (bool | Unset): The default warehouse.  If a product is listed with no designated warehouse, the
                default warehouse will be used.
            address (GetWarehouseListResponseDataWarehouseAddress | Unset):
     """

    id: str | Unset = UNSET
    entity_id: str | Unset = UNSET
    name: str | Unset = UNSET
    effect_status: str | Unset = UNSET
    type_: str | Unset = UNSET
    sub_type: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    address: GetWarehouseListResponseDataWarehouseAddress | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_warehouse_list_response_data_warehouse_address import GetWarehouseListResponseDataWarehouseAddress # noqa: PLC0415
        id = self.id

        entity_id = self.entity_id

        name = self.name

        effect_status = self.effect_status

        type_ = self.type_

        sub_type = self.sub_type

        is_default = self.is_default

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if name is not UNSET:
            field_dict["name"] = name
        if effect_status is not UNSET:
            field_dict["effect_status"] = effect_status
        if type_ is not UNSET:
            field_dict["type"] = type_
        if sub_type is not UNSET:
            field_dict["sub_type"] = sub_type
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_warehouse_list_response_data_warehouse_address import GetWarehouseListResponseDataWarehouseAddress # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        entity_id = d.pop("entity_id", UNSET)

        name = d.pop("name", UNSET)

        effect_status = d.pop("effect_status", UNSET)

        type_ = d.pop("type", UNSET)

        sub_type = d.pop("sub_type", UNSET)

        is_default = d.pop("is_default", UNSET)

        _address = d.pop("address", UNSET)
        address: GetWarehouseListResponseDataWarehouseAddress | Unset
        if isinstance(_address,  Unset):
            address = UNSET
        else:
            address = GetWarehouseListResponseDataWarehouseAddress.from_dict(_address)




        get_warehouse_list_response_data_warehouse = cls(
            id=id,
            entity_id=entity_id,
            name=name,
            effect_status=effect_status,
            type_=type_,
            sub_type=sub_type,
            is_default=is_default,
            address=address,
        )


        get_warehouse_list_response_data_warehouse.additional_properties = d
        return get_warehouse_list_response_data_warehouse

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
