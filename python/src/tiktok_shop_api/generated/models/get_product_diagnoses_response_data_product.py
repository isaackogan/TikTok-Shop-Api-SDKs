from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diagnosis import Diagnosis
    from ..models.listing_quality import ListingQuality


T = TypeVar("T", bound="GetProductDiagnosesResponseDataProduct")


@_attrs_define
class GetProductDiagnosesResponseDataProduct:
    """
    Attributes:
        id (str | Unset): The product ID.
        listing_quality (ListingQuality | Unset):
        diagnoses (list[Diagnosis] | Unset): Product diagnosis and optimization information.
    """

    id: str | Unset = UNSET
    listing_quality: ListingQuality | Unset = UNSET
    diagnoses: list[Diagnosis] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        listing_quality: dict[str, Any] | Unset = UNSET
        if not isinstance(self.listing_quality, Unset):
            listing_quality = self.listing_quality.to_dict()

        diagnoses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.diagnoses, Unset):
            diagnoses = []
            for diagnoses_item_data in self.diagnoses:
                diagnoses_item = diagnoses_item_data.to_dict()
                diagnoses.append(diagnoses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if listing_quality is not UNSET:
            field_dict["listing_quality"] = listing_quality
        if diagnoses is not UNSET:
            field_dict["diagnoses"] = diagnoses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diagnosis import Diagnosis  # noqa: PLC0415
        from ..models.listing_quality import ListingQuality  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _listing_quality = d.pop("listing_quality", UNSET)
        listing_quality: ListingQuality | Unset
        if isinstance(_listing_quality, Unset):
            listing_quality = UNSET
        else:
            listing_quality = ListingQuality.from_dict(_listing_quality)

        _diagnoses = d.pop("diagnoses", UNSET)
        diagnoses: list[Diagnosis] | Unset = UNSET
        if _diagnoses is not UNSET:
            diagnoses = []
            for diagnoses_item_data in _diagnoses:
                diagnoses_item = Diagnosis.from_dict(diagnoses_item_data)

                diagnoses.append(diagnoses_item)

        get_product_diagnoses_response_data_product = cls(
            id=id,
            listing_quality=listing_quality,
            diagnoses=diagnoses,
        )

        get_product_diagnoses_response_data_product.additional_properties = d
        return get_product_diagnoses_response_data_product

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
