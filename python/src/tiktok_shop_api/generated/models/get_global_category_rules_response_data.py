from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_global_category_rules_response_data_manufacturer import (
        GetGlobalCategoryRulesResponseDataManufacturer,
    )
    from ..models.get_global_category_rules_response_data_product_certification import (
        GetGlobalCategoryRulesResponseDataProductCertification,
    )
    from ..models.get_global_category_rules_response_data_responsible_person import (
        GetGlobalCategoryRulesResponseDataResponsiblePerson,
    )
    from ..models.get_global_category_rules_response_data_size_chart import GetGlobalCategoryRulesResponseDataSizeChart


T = TypeVar("T", bound="GetGlobalCategoryRulesResponseData")


@_attrs_define
class GetGlobalCategoryRulesResponseData:
    """
    Attributes:
        product_certifications (list[GetGlobalCategoryRulesResponseDataProductCertification] | Unset): Certification
            related rules.
            As per TikTok Shop guidelines, certifications are required for certain restricted product categories. Refer to
            [TikTok Shop Restricted Products Policy](https://seller-
            us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=3238037484275457&from=policy) for information on
            product category restrictions.

            If this is empty, it means certifications are not required for this category.
        size_chart (GetGlobalCategoryRulesResponseDataSizeChart | Unset):
        responsible_person (GetGlobalCategoryRulesResponseDataResponsiblePerson | Unset):
        manufacturer (GetGlobalCategoryRulesResponseDataManufacturer | Unset):
    """

    product_certifications: list[GetGlobalCategoryRulesResponseDataProductCertification] | Unset = UNSET
    size_chart: GetGlobalCategoryRulesResponseDataSizeChart | Unset = UNSET
    responsible_person: GetGlobalCategoryRulesResponseDataResponsiblePerson | Unset = UNSET
    manufacturer: GetGlobalCategoryRulesResponseDataManufacturer | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_certifications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_certifications, Unset):
            product_certifications = []
            for product_certifications_item_data in self.product_certifications:
                product_certifications_item = product_certifications_item_data.to_dict()
                product_certifications.append(product_certifications_item)

        size_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.size_chart, Unset):
            size_chart = self.size_chart.to_dict()

        responsible_person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.responsible_person, Unset):
            responsible_person = self.responsible_person.to_dict()

        manufacturer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.manufacturer, Unset):
            manufacturer = self.manufacturer.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_certifications is not UNSET:
            field_dict["product_certifications"] = product_certifications
        if size_chart is not UNSET:
            field_dict["size_chart"] = size_chart
        if responsible_person is not UNSET:
            field_dict["responsible_person"] = responsible_person
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_global_category_rules_response_data_manufacturer import (
            GetGlobalCategoryRulesResponseDataManufacturer,  # noqa: PLC0415
        )
        from ..models.get_global_category_rules_response_data_product_certification import (
            GetGlobalCategoryRulesResponseDataProductCertification,  # noqa: PLC0415
        )
        from ..models.get_global_category_rules_response_data_responsible_person import (
            GetGlobalCategoryRulesResponseDataResponsiblePerson,  # noqa: PLC0415
        )
        from ..models.get_global_category_rules_response_data_size_chart import (
            GetGlobalCategoryRulesResponseDataSizeChart,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _product_certifications = d.pop("product_certifications", UNSET)
        product_certifications: list[GetGlobalCategoryRulesResponseDataProductCertification] | Unset = UNSET
        if _product_certifications is not UNSET:
            product_certifications = []
            for product_certifications_item_data in _product_certifications:
                product_certifications_item = GetGlobalCategoryRulesResponseDataProductCertification.from_dict(
                    product_certifications_item_data
                )

                product_certifications.append(product_certifications_item)

        _size_chart = d.pop("size_chart", UNSET)
        size_chart: GetGlobalCategoryRulesResponseDataSizeChart | Unset
        if isinstance(_size_chart, Unset):
            size_chart = UNSET
        else:
            size_chart = GetGlobalCategoryRulesResponseDataSizeChart.from_dict(_size_chart)

        _responsible_person = d.pop("responsible_person", UNSET)
        responsible_person: GetGlobalCategoryRulesResponseDataResponsiblePerson | Unset
        if isinstance(_responsible_person, Unset):
            responsible_person = UNSET
        else:
            responsible_person = GetGlobalCategoryRulesResponseDataResponsiblePerson.from_dict(_responsible_person)

        _manufacturer = d.pop("manufacturer", UNSET)
        manufacturer: GetGlobalCategoryRulesResponseDataManufacturer | Unset
        if isinstance(_manufacturer, Unset):
            manufacturer = UNSET
        else:
            manufacturer = GetGlobalCategoryRulesResponseDataManufacturer.from_dict(_manufacturer)

        get_global_category_rules_response_data = cls(
            product_certifications=product_certifications,
            size_chart=size_chart,
            responsible_person=responsible_person,
            manufacturer=manufacturer,
        )

        get_global_category_rules_response_data.additional_properties = d
        return get_global_category_rules_response_data

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
