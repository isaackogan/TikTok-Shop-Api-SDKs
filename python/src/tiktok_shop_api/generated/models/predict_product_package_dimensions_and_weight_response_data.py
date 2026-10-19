from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.predict_product_package_dimensions_and_weight_response_data_package_dimension import (
        PredictProductPackageDimensionsAndWeightResponseDataPackageDimension,
    )
    from ..models.predict_product_package_dimensions_and_weight_response_data_package_weight import (
        PredictProductPackageDimensionsAndWeightResponseDataPackageWeight,
    )


T = TypeVar("T", bound="PredictProductPackageDimensionsAndWeightResponseData")


@_attrs_define
class PredictProductPackageDimensionsAndWeightResponseData:
    """
    Attributes:
        package_dimensions (PredictProductPackageDimensionsAndWeightResponseDataPackageDimension | Unset):
        package_weight (PredictProductPackageDimensionsAndWeightResponseDataPackageWeight | Unset):
    """

    package_dimensions: PredictProductPackageDimensionsAndWeightResponseDataPackageDimension | Unset = UNSET
    package_weight: PredictProductPackageDimensionsAndWeightResponseDataPackageWeight | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_dimensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_dimensions, Unset):
            package_dimensions = self.package_dimensions.to_dict()

        package_weight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_weight, Unset):
            package_weight = self.package_weight.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_dimensions is not UNSET:
            field_dict["package_dimensions"] = package_dimensions
        if package_weight is not UNSET:
            field_dict["package_weight"] = package_weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.predict_product_package_dimensions_and_weight_response_data_package_dimension import (
            PredictProductPackageDimensionsAndWeightResponseDataPackageDimension,  # noqa: PLC0415
        )
        from ..models.predict_product_package_dimensions_and_weight_response_data_package_weight import (
            PredictProductPackageDimensionsAndWeightResponseDataPackageWeight,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _package_dimensions = d.pop("package_dimensions", UNSET)
        package_dimensions: PredictProductPackageDimensionsAndWeightResponseDataPackageDimension | Unset
        if isinstance(_package_dimensions, Unset):
            package_dimensions = UNSET
        else:
            package_dimensions = PredictProductPackageDimensionsAndWeightResponseDataPackageDimension.from_dict(
                _package_dimensions
            )

        _package_weight = d.pop("package_weight", UNSET)
        package_weight: PredictProductPackageDimensionsAndWeightResponseDataPackageWeight | Unset
        if isinstance(_package_weight, Unset):
            package_weight = UNSET
        else:
            package_weight = PredictProductPackageDimensionsAndWeightResponseDataPackageWeight.from_dict(
                _package_weight
            )

        predict_product_package_dimensions_and_weight_response_data = cls(
            package_dimensions=package_dimensions,
            package_weight=package_weight,
        )

        predict_product_package_dimensions_and_weight_response_data.additional_properties = d
        return predict_product_package_dimensions_and_weight_response_data

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
