from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_category_rules_response_data_product_certification_expiration_date import (
        GetCategoryRulesResponseDataProductCertificationExpirationDate,
    )
    from ..models.requirement_condition import RequirementCondition


T = TypeVar("T", bound="GetCategoryRulesResponseDataProductCertification")


@_attrs_define
class GetCategoryRulesResponseDataProductCertification:
    """
    Attributes:
        id (str | Unset): The ID to identify the type of certification required.
        name (str | Unset): The name of the certification type.
        is_required (bool | Unset): A flag to indicate if the certification is always required when creating or editing
            a product.
            - true: The certification is always required.
            - false: The certification is not required, or required only if certain conditions are met. Refer to
            `requirement_conditions` for the specific requirements.
        document_details (str | Unset): Details about the certification documents that you must submit, including the
            content, format, and any other guidelines.
        sample_image_url (str | Unset): The URL to view an image of the sample certification document.
        requirement_conditions (list[RequirementCondition] | Unset): A list of conditions that determine if the
            certification is required based on the seller's inputs for a product attribute. If any of the conditions is met,
            the certification is required; otherwise, it is optional.

            For example, there's a condition that states that the "Safety Data Sheet (SDS) for flammable materials"
            certification is required if the seller selects the value "Yes" for the attribute "Flammable Liquid?". For more
            scenario-based guidance on using this parameter, refer to the [Solution Guide - CAT-PRE-
            HAZMAT](https://partner.tiktokshop.com/openlearn/guide/usecase?parent_id=7256668359046153985).

            Applicable only if `is_required=false`.
        expiration_date (GetCategoryRulesResponseDataProductCertificationExpirationDate | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    is_required: bool | Unset = UNSET
    document_details: str | Unset = UNSET
    sample_image_url: str | Unset = UNSET
    requirement_conditions: list[RequirementCondition] | Unset = UNSET
    expiration_date: GetCategoryRulesResponseDataProductCertificationExpirationDate | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        is_required = self.is_required

        document_details = self.document_details

        sample_image_url = self.sample_image_url

        requirement_conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.requirement_conditions, Unset):
            requirement_conditions = []
            for requirement_conditions_item_data in self.requirement_conditions:
                requirement_conditions_item = requirement_conditions_item_data.to_dict()
                requirement_conditions.append(requirement_conditions_item)

        expiration_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if is_required is not UNSET:
            field_dict["is_required"] = is_required
        if document_details is not UNSET:
            field_dict["document_details"] = document_details
        if sample_image_url is not UNSET:
            field_dict["sample_image_url"] = sample_image_url
        if requirement_conditions is not UNSET:
            field_dict["requirement_conditions"] = requirement_conditions
        if expiration_date is not UNSET:
            field_dict["expiration_date"] = expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_category_rules_response_data_product_certification_expiration_date import (
            GetCategoryRulesResponseDataProductCertificationExpirationDate,  # noqa: PLC0415
        )
        from ..models.requirement_condition import RequirementCondition  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        is_required = d.pop("is_required", UNSET)

        document_details = d.pop("document_details", UNSET)

        sample_image_url = d.pop("sample_image_url", UNSET)

        _requirement_conditions = d.pop("requirement_conditions", UNSET)
        requirement_conditions: list[RequirementCondition] | Unset = UNSET
        if _requirement_conditions is not UNSET:
            requirement_conditions = []
            for requirement_conditions_item_data in _requirement_conditions:
                requirement_conditions_item = RequirementCondition.from_dict(requirement_conditions_item_data)

                requirement_conditions.append(requirement_conditions_item)

        _expiration_date = d.pop("expiration_date", UNSET)
        expiration_date: GetCategoryRulesResponseDataProductCertificationExpirationDate | Unset
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = GetCategoryRulesResponseDataProductCertificationExpirationDate.from_dict(_expiration_date)

        get_category_rules_response_data_product_certification = cls(
            id=id,
            name=name,
            is_required=is_required,
            document_details=document_details,
            sample_image_url=sample_image_url,
            requirement_conditions=requirement_conditions,
            expiration_date=expiration_date,
        )

        get_category_rules_response_data_product_certification.additional_properties = d
        return get_category_rules_response_data_product_certification

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
