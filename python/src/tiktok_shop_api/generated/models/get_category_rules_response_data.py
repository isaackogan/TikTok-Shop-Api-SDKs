from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_category_rules_response_data_cod import GetCategoryRulesResponseDataCod
    from ..models.get_category_rules_response_data_epr import GetCategoryRulesResponseDataEpr
    from ..models.get_category_rules_response_data_fee import GetCategoryRulesResponseDataFee
    from ..models.get_category_rules_response_data_manufacturer import GetCategoryRulesResponseDataManufacturer
    from ..models.get_category_rules_response_data_package_dimension import GetCategoryRulesResponseDataPackageDimension
    from ..models.get_category_rules_response_data_product_certification import (
        GetCategoryRulesResponseDataProductCertification,
    )
    from ..models.get_category_rules_response_data_responsible_person import (
        GetCategoryRulesResponseDataResponsiblePerson,
    )
    from ..models.get_category_rules_response_data_seller_sku import GetCategoryRulesResponseDataSellerSku
    from ..models.get_category_rules_response_data_size_chart import GetCategoryRulesResponseDataSizeChart


T = TypeVar("T", bound="GetCategoryRulesResponseData")


@_attrs_define
class GetCategoryRulesResponseData:
    """
    Attributes:
        product_certifications (list[GetCategoryRulesResponseDataProductCertification] | Unset): Certification related
            rules.
            As per TikTok Shop guidelines, certifications are required for certain restricted product categories. Refer to
            [TikTok Shop Restricted Products Policy](https://seller-
            us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=3238037484275457&from=policy) for information on
            product category restrictions.

            If this is empty, it means certifications are not required for this category.
        size_chart (GetCategoryRulesResponseDataSizeChart | Unset):
        cod (GetCategoryRulesResponseDataCod | Unset):
        package_dimension (GetCategoryRulesResponseDataPackageDimension | Unset):
        epr (GetCategoryRulesResponseDataEpr | Unset):
        responsible_person (GetCategoryRulesResponseDataResponsiblePerson | Unset):
        manufacturer (GetCategoryRulesResponseDataManufacturer | Unset):
        allowed_special_product_types (list[str] | Unset): The list of special product types, excluding regular
            products, that your shop is allowed to list in this category.

            Possible values based on the region:
            **US**
            - `PRE_ORDER`: The product is not yet available or released. Fulfillment can be extended by specifying a release
            date.
            - `MADE_TO_ORDER`: The product is produced only after the order is received. Fulfillment can be extended by
            specifying a duration.
            - `CUSTOM`: The product requires a fulfillment timeline that exceeds the standard due to other factors.
            Fulfillment can be extended by specifying a duration.

            **UK and SEA**
            - `PRE_ORDER`: The product is not yet available or released. Fulfillment can be extended by specifying a
            duration.

            **Note**: This field is omitted if you lack the permission to list special product types. Contact your account
            manager for assistance if you wish to list such products.
        fees (list[GetCategoryRulesResponseDataFee] | Unset): Product fees related rules.
        seller_sku (GetCategoryRulesResponseDataSellerSku | Unset):
    """

    product_certifications: list[GetCategoryRulesResponseDataProductCertification] | Unset = UNSET
    size_chart: GetCategoryRulesResponseDataSizeChart | Unset = UNSET
    cod: GetCategoryRulesResponseDataCod | Unset = UNSET
    package_dimension: GetCategoryRulesResponseDataPackageDimension | Unset = UNSET
    epr: GetCategoryRulesResponseDataEpr | Unset = UNSET
    responsible_person: GetCategoryRulesResponseDataResponsiblePerson | Unset = UNSET
    manufacturer: GetCategoryRulesResponseDataManufacturer | Unset = UNSET
    allowed_special_product_types: list[str] | Unset = UNSET
    fees: list[GetCategoryRulesResponseDataFee] | Unset = UNSET
    seller_sku: GetCategoryRulesResponseDataSellerSku | Unset = UNSET
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

        cod: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cod, Unset):
            cod = self.cod.to_dict()

        package_dimension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_dimension, Unset):
            package_dimension = self.package_dimension.to_dict()

        epr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.epr, Unset):
            epr = self.epr.to_dict()

        responsible_person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.responsible_person, Unset):
            responsible_person = self.responsible_person.to_dict()

        manufacturer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.manufacturer, Unset):
            manufacturer = self.manufacturer.to_dict()

        allowed_special_product_types: list[str] | Unset = UNSET
        if not isinstance(self.allowed_special_product_types, Unset):
            allowed_special_product_types = self.allowed_special_product_types

        fees: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fees, Unset):
            fees = []
            for fees_item_data in self.fees:
                fees_item = fees_item_data.to_dict()
                fees.append(fees_item)

        seller_sku: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seller_sku, Unset):
            seller_sku = self.seller_sku.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_certifications is not UNSET:
            field_dict["product_certifications"] = product_certifications
        if size_chart is not UNSET:
            field_dict["size_chart"] = size_chart
        if cod is not UNSET:
            field_dict["cod"] = cod
        if package_dimension is not UNSET:
            field_dict["package_dimension"] = package_dimension
        if epr is not UNSET:
            field_dict["epr"] = epr
        if responsible_person is not UNSET:
            field_dict["responsible_person"] = responsible_person
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if allowed_special_product_types is not UNSET:
            field_dict["allowed_special_product_types"] = allowed_special_product_types
        if fees is not UNSET:
            field_dict["fees"] = fees
        if seller_sku is not UNSET:
            field_dict["seller_sku"] = seller_sku

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_category_rules_response_data_cod import GetCategoryRulesResponseDataCod  # noqa: PLC0415
        from ..models.get_category_rules_response_data_epr import GetCategoryRulesResponseDataEpr  # noqa: PLC0415
        from ..models.get_category_rules_response_data_fee import GetCategoryRulesResponseDataFee  # noqa: PLC0415
        from ..models.get_category_rules_response_data_manufacturer import (
            GetCategoryRulesResponseDataManufacturer,  # noqa: PLC0415
        )
        from ..models.get_category_rules_response_data_package_dimension import (
            GetCategoryRulesResponseDataPackageDimension,  # noqa: PLC0415
        )
        from ..models.get_category_rules_response_data_product_certification import (
            GetCategoryRulesResponseDataProductCertification,  # noqa: PLC0415
        )
        from ..models.get_category_rules_response_data_responsible_person import (
            GetCategoryRulesResponseDataResponsiblePerson,  # noqa: PLC0415
        )
        from ..models.get_category_rules_response_data_seller_sku import (
            GetCategoryRulesResponseDataSellerSku,  # noqa: PLC0415
        )
        from ..models.get_category_rules_response_data_size_chart import (
            GetCategoryRulesResponseDataSizeChart,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _product_certifications = d.pop("product_certifications", UNSET)
        product_certifications: list[GetCategoryRulesResponseDataProductCertification] | Unset = UNSET
        if _product_certifications is not UNSET:
            product_certifications = []
            for product_certifications_item_data in _product_certifications:
                product_certifications_item = GetCategoryRulesResponseDataProductCertification.from_dict(
                    product_certifications_item_data
                )

                product_certifications.append(product_certifications_item)

        _size_chart = d.pop("size_chart", UNSET)
        size_chart: GetCategoryRulesResponseDataSizeChart | Unset
        if isinstance(_size_chart, Unset):
            size_chart = UNSET
        else:
            size_chart = GetCategoryRulesResponseDataSizeChart.from_dict(_size_chart)

        _cod = d.pop("cod", UNSET)
        cod: GetCategoryRulesResponseDataCod | Unset
        if isinstance(_cod, Unset):
            cod = UNSET
        else:
            cod = GetCategoryRulesResponseDataCod.from_dict(_cod)

        _package_dimension = d.pop("package_dimension", UNSET)
        package_dimension: GetCategoryRulesResponseDataPackageDimension | Unset
        if isinstance(_package_dimension, Unset):
            package_dimension = UNSET
        else:
            package_dimension = GetCategoryRulesResponseDataPackageDimension.from_dict(_package_dimension)

        _epr = d.pop("epr", UNSET)
        epr: GetCategoryRulesResponseDataEpr | Unset
        if isinstance(_epr, Unset):
            epr = UNSET
        else:
            epr = GetCategoryRulesResponseDataEpr.from_dict(_epr)

        _responsible_person = d.pop("responsible_person", UNSET)
        responsible_person: GetCategoryRulesResponseDataResponsiblePerson | Unset
        if isinstance(_responsible_person, Unset):
            responsible_person = UNSET
        else:
            responsible_person = GetCategoryRulesResponseDataResponsiblePerson.from_dict(_responsible_person)

        _manufacturer = d.pop("manufacturer", UNSET)
        manufacturer: GetCategoryRulesResponseDataManufacturer | Unset
        if isinstance(_manufacturer, Unset):
            manufacturer = UNSET
        else:
            manufacturer = GetCategoryRulesResponseDataManufacturer.from_dict(_manufacturer)

        allowed_special_product_types = cast(list[str], d.pop("allowed_special_product_types", UNSET))

        _fees = d.pop("fees", UNSET)
        fees: list[GetCategoryRulesResponseDataFee] | Unset = UNSET
        if _fees is not UNSET:
            fees = []
            for fees_item_data in _fees:
                fees_item = GetCategoryRulesResponseDataFee.from_dict(fees_item_data)

                fees.append(fees_item)

        _seller_sku = d.pop("seller_sku", UNSET)
        seller_sku: GetCategoryRulesResponseDataSellerSku | Unset
        if isinstance(_seller_sku, Unset):
            seller_sku = UNSET
        else:
            seller_sku = GetCategoryRulesResponseDataSellerSku.from_dict(_seller_sku)

        get_category_rules_response_data = cls(
            product_certifications=product_certifications,
            size_chart=size_chart,
            cod=cod,
            package_dimension=package_dimension,
            epr=epr,
            responsible_person=responsible_person,
            manufacturer=manufacturer,
            allowed_special_product_types=allowed_special_product_types,
            fees=fees,
            seller_sku=seller_sku,
        )

        get_category_rules_response_data.additional_properties = d
        return get_category_rules_response_data

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
