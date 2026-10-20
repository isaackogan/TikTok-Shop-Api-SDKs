from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_warehouse_delivery_options_response_data_delivery_option_dimension_limit import GetWarehouseDeliveryOptionsResponseDataDeliveryOptionDimensionLimit
  from ..models.get_warehouse_delivery_options_response_data_delivery_option_weight_limit import GetWarehouseDeliveryOptionsResponseDataDeliveryOptionWeightLimit





T = TypeVar("T", bound="GetWarehouseDeliveryOptionsResponseDataDeliveryOption")



@_attrs_define
class GetWarehouseDeliveryOptionsResponseDataDeliveryOption:
    """ 
        Attributes:
            id (str | Unset): Delivery option ID.
            name (str | Unset): Delivery option name.
            type_ (str | Unset): Delivery option type.
                Possible values:
                - STANDARD
                - EXPRESS
                - ECONOMY
                - SEND_BY_SELLER
                - INSTANT
                - SAMEDAY
                - NEXTDAY
                - CARGO
            description (str | Unset): Delivery option description.
            dimension_limit (GetWarehouseDeliveryOptionsResponseDataDeliveryOptionDimensionLimit | Unset):
            weight_limit (GetWarehouseDeliveryOptionsResponseDataDeliveryOptionWeightLimit | Unset):
            platform (list[str] | Unset): The platform on which the delivery option is available
                Possible values:
                - TIKTOK_SHOP
                - TOKOPEDIA
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    description: str | Unset = UNSET
    dimension_limit: GetWarehouseDeliveryOptionsResponseDataDeliveryOptionDimensionLimit | Unset = UNSET
    weight_limit: GetWarehouseDeliveryOptionsResponseDataDeliveryOptionWeightLimit | Unset = UNSET
    platform: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_warehouse_delivery_options_response_data_delivery_option_dimension_limit import GetWarehouseDeliveryOptionsResponseDataDeliveryOptionDimensionLimit # noqa: PLC0415
        from ..models.get_warehouse_delivery_options_response_data_delivery_option_weight_limit import GetWarehouseDeliveryOptionsResponseDataDeliveryOptionWeightLimit # noqa: PLC0415
        id = self.id

        name = self.name

        type_ = self.type_

        description = self.description

        dimension_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dimension_limit, Unset):
            dimension_limit = self.dimension_limit.to_dict()

        weight_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weight_limit, Unset):
            weight_limit = self.weight_limit.to_dict()

        platform: list[str] | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if description is not UNSET:
            field_dict["description"] = description
        if dimension_limit is not UNSET:
            field_dict["dimension_limit"] = dimension_limit
        if weight_limit is not UNSET:
            field_dict["weight_limit"] = weight_limit
        if platform is not UNSET:
            field_dict["platform"] = platform

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_warehouse_delivery_options_response_data_delivery_option_dimension_limit import GetWarehouseDeliveryOptionsResponseDataDeliveryOptionDimensionLimit # noqa: PLC0415
        from ..models.get_warehouse_delivery_options_response_data_delivery_option_weight_limit import GetWarehouseDeliveryOptionsResponseDataDeliveryOptionWeightLimit # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        description = d.pop("description", UNSET)

        _dimension_limit = d.pop("dimension_limit", UNSET)
        dimension_limit: GetWarehouseDeliveryOptionsResponseDataDeliveryOptionDimensionLimit | Unset
        if isinstance(_dimension_limit,  Unset):
            dimension_limit = UNSET
        else:
            dimension_limit = GetWarehouseDeliveryOptionsResponseDataDeliveryOptionDimensionLimit.from_dict(_dimension_limit)




        _weight_limit = d.pop("weight_limit", UNSET)
        weight_limit: GetWarehouseDeliveryOptionsResponseDataDeliveryOptionWeightLimit | Unset
        if isinstance(_weight_limit,  Unset):
            weight_limit = UNSET
        else:
            weight_limit = GetWarehouseDeliveryOptionsResponseDataDeliveryOptionWeightLimit.from_dict(_weight_limit)




        platform = cast(list[str], d.pop("platform", UNSET))


        get_warehouse_delivery_options_response_data_delivery_option = cls(
            id=id,
            name=name,
            type_=type_,
            description=description,
            dimension_limit=dimension_limit,
            weight_limit=weight_limit,
            platform=platform,
        )


        get_warehouse_delivery_options_response_data_delivery_option.additional_properties = d
        return get_warehouse_delivery_options_response_data_delivery_option

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
