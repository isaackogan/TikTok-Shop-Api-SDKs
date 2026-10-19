from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_packages_response_data_shipping_service_info import (
        CreatePackagesResponseDataShippingServiceInfo,
    )
    from ..models.dimension import Dimension
    from ..models.weight import Weight


T = TypeVar("T", bound="CreatePackagesResponseData")


@_attrs_define
class CreatePackagesResponseData:
    """
    Attributes:
        dimension (Dimension | Unset):
        shipping_service_info (CreatePackagesResponseDataShippingServiceInfo | Unset):
        package_id (str | Unset): Package ID.
        weight (Weight | Unset):
        create_time (int | Unset): The time when the product was created.
            Unix timestamp.
    """

    dimension: Dimension | Unset = UNSET
    shipping_service_info: CreatePackagesResponseDataShippingServiceInfo | Unset = UNSET
    package_id: str | Unset = UNSET
    weight: Weight | Unset = UNSET
    create_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dimension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dimension, Unset):
            dimension = self.dimension.to_dict()

        shipping_service_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shipping_service_info, Unset):
            shipping_service_info = self.shipping_service_info.to_dict()

        package_id = self.package_id

        weight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()

        create_time = self.create_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if shipping_service_info is not UNSET:
            field_dict["shipping_service_info"] = shipping_service_info
        if package_id is not UNSET:
            field_dict["package_id"] = package_id
        if weight is not UNSET:
            field_dict["weight"] = weight
        if create_time is not UNSET:
            field_dict["create_time"] = create_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_packages_response_data_shipping_service_info import (
            CreatePackagesResponseDataShippingServiceInfo,  # noqa: PLC0415
        )
        from ..models.dimension import Dimension  # noqa: PLC0415
        from ..models.weight import Weight  # noqa: PLC0415

        d = dict(src_dict)
        _dimension = d.pop("dimension", UNSET)
        dimension: Dimension | Unset
        if isinstance(_dimension, Unset):
            dimension = UNSET
        else:
            dimension = Dimension.from_dict(_dimension)

        _shipping_service_info = d.pop("shipping_service_info", UNSET)
        shipping_service_info: CreatePackagesResponseDataShippingServiceInfo | Unset
        if isinstance(_shipping_service_info, Unset):
            shipping_service_info = UNSET
        else:
            shipping_service_info = CreatePackagesResponseDataShippingServiceInfo.from_dict(_shipping_service_info)

        package_id = d.pop("package_id", UNSET)

        _weight = d.pop("weight", UNSET)
        weight: Weight | Unset
        if isinstance(_weight, Unset):
            weight = UNSET
        else:
            weight = Weight.from_dict(_weight)

        create_time = d.pop("create_time", UNSET)

        create_packages_response_data = cls(
            dimension=dimension,
            shipping_service_info=shipping_service_info,
            package_id=package_id,
            weight=weight,
            create_time=create_time,
        )

        create_packages_response_data.additional_properties = d
        return create_packages_response_data

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
