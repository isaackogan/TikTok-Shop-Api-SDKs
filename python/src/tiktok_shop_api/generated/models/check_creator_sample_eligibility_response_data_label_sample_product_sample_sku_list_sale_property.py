from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CheckCreatorSampleEligibilityResponseDataLabelSampleProductSampleSkuListSaleProperty")



@_attrs_define
class CheckCreatorSampleEligibilityResponseDataLabelSampleProductSampleSkuListSaleProperty:
    """ 
        Attributes:
            id (str | Unset): A SKU property identifier, short for "Stock Keeping Unit Property ID", is a specific
                identification code assigned to a particular property or characteristic of a SKU.(i.e: "100000" means "color")
            name (str | Unset): The SKU property name.
            value_id (str | Unset): The SKU property value identifier is an identification code related to the specific
                values of the properties of a Stock Keeping Unit (SKU).
                When a SKU has certain properties like color, size, etc., each possible value for those properties has its own
                unique SKU property value identifier. For instance, if the property is "color" and the possible values are
                "red", "blue", "green", then "red" would have its own SKU property vvalue identifier, "blue" would have another
                one, and so on.
            value_name (str | Unset): The SKU property value name.
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    value_id: str | Unset = UNSET
    value_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        value_id = self.value_id

        value_name = self.value_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if value_id is not UNSET:
            field_dict["value_id"] = value_id
        if value_name is not UNSET:
            field_dict["value_name"] = value_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        value_id = d.pop("value_id", UNSET)

        value_name = d.pop("value_name", UNSET)

        check_creator_sample_eligibility_response_data_label_sample_product_sample_sku_list_sale_property = cls(
            id=id,
            name=name,
            value_id=value_id,
            value_name=value_name,
        )


        check_creator_sample_eligibility_response_data_label_sample_product_sample_sku_list_sale_property.additional_properties = d
        return check_creator_sample_eligibility_response_data_label_sample_product_sample_sku_list_sale_property

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
