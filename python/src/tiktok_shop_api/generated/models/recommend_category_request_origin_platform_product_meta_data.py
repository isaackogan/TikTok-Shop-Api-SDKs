from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.recommend_category_request_origin_platform_product_meta_data_attribute_value_list import RecommendCategoryRequestOriginPlatformProductMetaDataAttributeValueList





T = TypeVar("T", bound="RecommendCategoryRequestOriginPlatformProductMetaData")



@_attrs_define
class RecommendCategoryRequestOriginPlatformProductMetaData:
    """ 
        Attributes:
            attribute_value_list (list[RecommendCategoryRequestOriginPlatformProductMetaDataAttributeValueList] | Unset): A
                list of product metadata attributes and their values.
     """

    attribute_value_list: list[RecommendCategoryRequestOriginPlatformProductMetaDataAttributeValueList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.recommend_category_request_origin_platform_product_meta_data_attribute_value_list import RecommendCategoryRequestOriginPlatformProductMetaDataAttributeValueList # noqa: PLC0415
        attribute_value_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attribute_value_list, Unset):
            attribute_value_list = []
            for attribute_value_list_item_data in self.attribute_value_list:
                attribute_value_list_item = attribute_value_list_item_data.to_dict()
                attribute_value_list.append(attribute_value_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if attribute_value_list is not UNSET:
            field_dict["attribute_value_list"] = attribute_value_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recommend_category_request_origin_platform_product_meta_data_attribute_value_list import RecommendCategoryRequestOriginPlatformProductMetaDataAttributeValueList # noqa: PLC0415
        d = dict(src_dict)
        _attribute_value_list = d.pop("attribute_value_list", UNSET)
        attribute_value_list: list[RecommendCategoryRequestOriginPlatformProductMetaDataAttributeValueList] | Unset = UNSET
        if _attribute_value_list is not UNSET:
            attribute_value_list = []
            for attribute_value_list_item_data in _attribute_value_list:
                attribute_value_list_item = RecommendCategoryRequestOriginPlatformProductMetaDataAttributeValueList.from_dict(attribute_value_list_item_data)



                attribute_value_list.append(attribute_value_list_item)


        recommend_category_request_origin_platform_product_meta_data = cls(
            attribute_value_list=attribute_value_list,
        )


        recommend_category_request_origin_platform_product_meta_data.additional_properties = d
        return recommend_category_request_origin_platform_product_meta_data

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
