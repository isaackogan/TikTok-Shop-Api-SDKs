from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.carton import Carton
    from ..models.create_or_update_inbound_plan_request_goods_item import CreateOrUpdateInboundPlanRequestGoodsItem


T = TypeVar("T", bound="CreateOrUpdateInboundPlanRequest")


@_attrs_define
class CreateOrUpdateInboundPlanRequest:
    """
    Attributes:
        plan_id (str | Unset): Without plan id it is creating, with plan id it is updating.
        idempotent_key (str | Unset): Idempotency key for creating an inbound plan. Required when `plan_id` is not
            provided.
        goods_items (list[CreateOrUpdateInboundPlanRequestGoodsItem] | Unset): Goods item list.
        cartons (list[Carton] | Unset): Carton List.
    """

    plan_id: str | Unset = UNSET
    idempotent_key: str | Unset = UNSET
    goods_items: list[CreateOrUpdateInboundPlanRequestGoodsItem] | Unset = UNSET
    cartons: list[Carton] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan_id = self.plan_id

        idempotent_key = self.idempotent_key

        goods_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.goods_items, Unset):
            goods_items = []
            for goods_items_item_data in self.goods_items:
                goods_items_item = goods_items_item_data.to_dict()
                goods_items.append(goods_items_item)

        cartons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cartons, Unset):
            cartons = []
            for cartons_item_data in self.cartons:
                cartons_item = cartons_item_data.to_dict()
                cartons.append(cartons_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plan_id is not UNSET:
            field_dict["plan_id"] = plan_id
        if idempotent_key is not UNSET:
            field_dict["idempotent_key"] = idempotent_key
        if goods_items is not UNSET:
            field_dict["goods_items"] = goods_items
        if cartons is not UNSET:
            field_dict["cartons"] = cartons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.carton import Carton  # noqa: PLC0415
        from ..models.create_or_update_inbound_plan_request_goods_item import (
            CreateOrUpdateInboundPlanRequestGoodsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        plan_id = d.pop("plan_id", UNSET)

        idempotent_key = d.pop("idempotent_key", UNSET)

        _goods_items = d.pop("goods_items", UNSET)
        goods_items: list[CreateOrUpdateInboundPlanRequestGoodsItem] | Unset = UNSET
        if _goods_items is not UNSET:
            goods_items = []
            for goods_items_item_data in _goods_items:
                goods_items_item = CreateOrUpdateInboundPlanRequestGoodsItem.from_dict(goods_items_item_data)

                goods_items.append(goods_items_item)

        _cartons = d.pop("cartons", UNSET)
        cartons: list[Carton] | Unset = UNSET
        if _cartons is not UNSET:
            cartons = []
            for cartons_item_data in _cartons:
                cartons_item = Carton.from_dict(cartons_item_data)

                cartons.append(cartons_item)

        create_or_update_inbound_plan_request = cls(
            plan_id=plan_id,
            idempotent_key=idempotent_key,
            goods_items=goods_items,
            cartons=cartons,
        )

        create_or_update_inbound_plan_request.additional_properties = d
        return create_or_update_inbound_plan_request

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
