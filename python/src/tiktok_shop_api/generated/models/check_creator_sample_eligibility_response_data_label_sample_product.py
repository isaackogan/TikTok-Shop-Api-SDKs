from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_creator_sample_eligibility_response_data_label_sample_product_sample_sku_list import (
        CheckCreatorSampleEligibilityResponseDataLabelSampleProductSampleSkuList,
    )


T = TypeVar("T", bound="CheckCreatorSampleEligibilityResponseDataLabelSampleProduct")


@_attrs_define
class CheckCreatorSampleEligibilityResponseDataLabelSampleProduct:
    """
    Attributes:
        sample_sku_list (list[CheckCreatorSampleEligibilityResponseDataLabelSampleProductSampleSkuList] | Unset): The
            sample product SKU information.
    """

    sample_sku_list: list[CheckCreatorSampleEligibilityResponseDataLabelSampleProductSampleSkuList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sample_sku_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sample_sku_list, Unset):
            sample_sku_list = []
            for sample_sku_list_item_data in self.sample_sku_list:
                sample_sku_list_item = sample_sku_list_item_data.to_dict()
                sample_sku_list.append(sample_sku_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sample_sku_list is not UNSET:
            field_dict["sample_sku_list"] = sample_sku_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_creator_sample_eligibility_response_data_label_sample_product_sample_sku_list import (
            CheckCreatorSampleEligibilityResponseDataLabelSampleProductSampleSkuList,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _sample_sku_list = d.pop("sample_sku_list", UNSET)
        sample_sku_list: list[CheckCreatorSampleEligibilityResponseDataLabelSampleProductSampleSkuList] | Unset = UNSET
        if _sample_sku_list is not UNSET:
            sample_sku_list = []
            for sample_sku_list_item_data in _sample_sku_list:
                sample_sku_list_item = (
                    CheckCreatorSampleEligibilityResponseDataLabelSampleProductSampleSkuList.from_dict(
                        sample_sku_list_item_data
                    )
                )

                sample_sku_list.append(sample_sku_list_item)

        check_creator_sample_eligibility_response_data_label_sample_product = cls(
            sample_sku_list=sample_sku_list,
        )

        check_creator_sample_eligibility_response_data_label_sample_product.additional_properties = d
        return check_creator_sample_eligibility_response_data_label_sample_product

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
