from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_inventory_request_sku import UpdateInventoryRequestSku





T = TypeVar("T", bound="UpdateInventoryRequest")



@_attrs_define
class UpdateInventoryRequest:
    """ 
        Attributes:
            skus (list[UpdateInventoryRequestSku]): A list of Stock Keeping Units (SKUs) used to identify distinct variants
                of the product.
            sku_warehouse_stock_update_mode (str | Unset): The mode used to update warehouse inventory for a SKU. This
                parameter was introduced in October 2026.

                Note:

                - If omitted, DEFAULT mode applies. This follows the behavior used before October 2026: the submitted warehouse
                list must include at least one warehouse already associated with the SKU. For example, if a SKU is associated
                with warehouses A and B, a request specifying only warehouse C does not meet this requirement. The list must
                also include A or B.
                - INCREMENTAL (1): Updates only the specified warehouses. You can specify warehouses regardless of whether they
                are already associated with the SKU. If an association does not exist, it is created and the inventory is set;
                otherwise, the inventory is updated. You can also use delete_warehouse_ids to specify warehouses to unlink from
                the SKU.
                - FULL (2): Updates inventory and uses the submitted SKU–warehouse list as the complete set of warehouse
                associations to retain. Any existing warehouse associations omitted from the list are removed. Providing
                delete_warehouse_ids in this mode returns an error.

                Important:

                - Unlinking a warehouse is subject to multiple restrictions. For example, the warehouse must have no unfulfilled
                orders, and the inventory remaining after unlinking must be sufficient to cover quantities locked for campaigns.
                - Avoid making inventory synchronization depend on successful warehouse unlinking. For this reason, FULL mode is
                not recommended for inventory synchronization.
                - Use INCREMENTAL mode to add warehouse associations or update inventory. To unlink warehouses, send separate
                requests using INCREMENTAL mode with delete_warehouse_ids.
     """

    skus: list[UpdateInventoryRequestSku]
    sku_warehouse_stock_update_mode: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_inventory_request_sku import UpdateInventoryRequestSku # noqa: PLC0415
        skus = []
        for skus_item_data in self.skus:
            skus_item = skus_item_data.to_dict()
            skus.append(skus_item)



        sku_warehouse_stock_update_mode = self.sku_warehouse_stock_update_mode


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "skus": skus,
        })
        if sku_warehouse_stock_update_mode is not UNSET:
            field_dict["sku_warehouse_stock_update_mode"] = sku_warehouse_stock_update_mode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_inventory_request_sku import UpdateInventoryRequestSku # noqa: PLC0415
        d = dict(src_dict)
        skus = []
        _skus = d.pop("skus")
        for skus_item_data in (_skus):
            skus_item = UpdateInventoryRequestSku.from_dict(skus_item_data)



            skus.append(skus_item)


        sku_warehouse_stock_update_mode = d.pop("sku_warehouse_stock_update_mode", UNSET)

        update_inventory_request = cls(
            skus=skus,
            sku_warehouse_stock_update_mode=sku_warehouse_stock_update_mode,
        )


        update_inventory_request.additional_properties = d
        return update_inventory_request

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
