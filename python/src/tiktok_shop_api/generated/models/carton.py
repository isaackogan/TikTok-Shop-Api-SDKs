from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.carton_carton_type import CartonCartonType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.box_measurement import BoxMeasurement
  from ..models.item import Item





T = TypeVar("T", bound="Carton")



@_attrs_define
class Carton:
    """ 
        Attributes:
            carton_type (CartonCartonType): Indicates whether the carton is configured as single-SKU or multi-SKU.

                **Possible values:**
                * `SINGLE_SKU`: `items` must contain exactly one item.
                * `MULTI_SKU`: `items` must contain two or more items.
            items (list[Item]): Goods item list of a carton.
            quantity (int): Number of cartons that use this carton configuration.
            box_measurements (BoxMeasurement):
            carton_nums (list[str] | Unset): Identifiers assigned to the cartons represented by this configuration. Either
                every carton configuration in the request must provide a non-empty `carton_nums` array, or no configuration may
                provide any carton identifiers. When provided, the number of identifiers must equal this configuration's
                `quantity`; each identifier must use the format `C` followed by four digits and must be unique across the
                request. If none are provided, carton identifiers are generated automatically.
     """

    carton_type: CartonCartonType
    items: list[Item]
    quantity: int
    box_measurements: BoxMeasurement
    carton_nums: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.box_measurement import BoxMeasurement # noqa: PLC0415
        from ..models.item import Item # noqa: PLC0415
        carton_type = self.carton_type.value

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)



        quantity = self.quantity

        box_measurements = self.box_measurements.to_dict()

        carton_nums: list[str] | Unset = UNSET
        if not isinstance(self.carton_nums, Unset):
            carton_nums = self.carton_nums




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "carton_type": carton_type,
            "items": items,
            "quantity": quantity,
            "box_measurements": box_measurements,
        })
        if carton_nums is not UNSET:
            field_dict["carton_nums"] = carton_nums

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.box_measurement import BoxMeasurement # noqa: PLC0415
        from ..models.item import Item # noqa: PLC0415
        d = dict(src_dict)
        carton_type = CartonCartonType(d.pop("carton_type"))




        items = []
        _items = d.pop("items")
        for items_item_data in (_items):
            items_item = Item.from_dict(items_item_data)



            items.append(items_item)


        quantity = d.pop("quantity")

        box_measurements = BoxMeasurement.from_dict(d.pop("box_measurements"))




        carton_nums = cast(list[str], d.pop("carton_nums", UNSET))


        carton = cls(
            carton_type=carton_type,
            items=items,
            quantity=quantity,
            box_measurements=box_measurements,
            carton_nums=carton_nums,
        )


        carton.additional_properties = d
        return carton

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
