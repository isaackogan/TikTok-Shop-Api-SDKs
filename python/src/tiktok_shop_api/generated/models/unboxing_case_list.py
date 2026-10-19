from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.unboxing_case_list_unbox_sku_type import UnboxingCaseListUnboxSkuType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UnboxingCaseList")


@_attrs_define
class UnboxingCaseList:
    """
    Attributes:
        unbox_sku (str | Unset): Unboxed sku code associated with the actual unboxed item.
        unbox_sku_type (UnboxingCaseListUnboxSkuType | Unset): Indicates if the unboxed sku is a gift item
            Enumerations: NORMAL or GIFT
    """

    unbox_sku: str | Unset = UNSET
    unbox_sku_type: UnboxingCaseListUnboxSkuType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unbox_sku = self.unbox_sku

        unbox_sku_type: str | Unset = UNSET
        if not isinstance(self.unbox_sku_type, Unset):
            unbox_sku_type = self.unbox_sku_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unbox_sku is not UNSET:
            field_dict["unbox_sku"] = unbox_sku
        if unbox_sku_type is not UNSET:
            field_dict["unbox_sku_type"] = unbox_sku_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unbox_sku = d.pop("unbox_sku", UNSET)

        _unbox_sku_type = d.pop("unbox_sku_type", UNSET)
        unbox_sku_type: UnboxingCaseListUnboxSkuType | Unset
        if isinstance(_unbox_sku_type, Unset):
            unbox_sku_type = UNSET
        else:
            unbox_sku_type = UnboxingCaseListUnboxSkuType(_unbox_sku_type)

        unboxing_case_list = cls(
            unbox_sku=unbox_sku,
            unbox_sku_type=unbox_sku_type,
        )

        unboxing_case_list.additional_properties = d
        return unboxing_case_list

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
