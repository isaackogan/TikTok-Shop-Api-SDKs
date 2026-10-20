from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.generate_publisher_sharing_links_in_batch_request_material_type import (
    GeneratePublisherSharingLinksInBatchRequestMaterialType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GeneratePublisherSharingLinksInBatchRequestMaterial")


@_attrs_define
class GeneratePublisherSharingLinksInBatchRequestMaterial:
    """
    Attributes:
        ids (list[str]): The list of material IDs. The maximum length is 50. When `type` is `PRODUCT`, provide 1 to 50
            product IDs.
        type_ (GeneratePublisherSharingLinksInBatchRequestMaterialType): The material type. Possible values:
            - `PRODUCT`: Provide product IDs in `ids`.
            - `CAMPAIGN`: Provide `promotion_campaign_schema`.
        promotion_campaign_schema (str | Unset): When `type` is set to `CAMPAIGN`, this field is required. This schema
            is associated with the Campaign page.
    """

    ids: list[str]
    type_: GeneratePublisherSharingLinksInBatchRequestMaterialType
    promotion_campaign_schema: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        type_ = self.type_.value

        promotion_campaign_schema = self.promotion_campaign_schema

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
                "type": type_,
            }
        )
        if promotion_campaign_schema is not UNSET:
            field_dict["promotion_campaign_schema"] = promotion_campaign_schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids"))

        type_ = GeneratePublisherSharingLinksInBatchRequestMaterialType(d.pop("type"))

        promotion_campaign_schema = d.pop("promotion_campaign_schema", UNSET)

        generate_publisher_sharing_links_in_batch_request_material = cls(
            ids=ids,
            type_=type_,
            promotion_campaign_schema=promotion_campaign_schema,
        )

        generate_publisher_sharing_links_in_batch_request_material.additional_properties = d
        return generate_publisher_sharing_links_in_batch_request_material

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
