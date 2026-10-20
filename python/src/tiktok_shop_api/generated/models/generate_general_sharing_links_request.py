from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generate_general_sharing_links_request_material import GenerateGeneralSharingLinksRequestMaterial


T = TypeVar("T", bound="GenerateGeneralSharingLinksRequest")


@_attrs_define
class GenerateGeneralSharingLinksRequest:
    """
    Attributes:
        material (GenerateGeneralSharingLinksRequestMaterial):
        campaign_id (str | Unset): If a creator adds products from a campaign, please include the campaign ID. The
            campaign ID can be found in the Affiliate Center or retrieved using the Get Affiliate Partner Campaign List API.
        link_type (str | Unset): Optional. For Tokopedia agencies, set this field to `TOKO`. The response returns the
            Tokopedia product URL in `sharing_link` and omits `deep_link` and `one_link`.
            If this field is omitted or set to another value, the response returns the TikTok Shop product URL in
            `sharing_link`. For `PRODUCT` requests, `deep_link` and `one_link` are also returned.
    """

    material: GenerateGeneralSharingLinksRequestMaterial
    campaign_id: str | Unset = UNSET
    link_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        material = self.material.to_dict()

        campaign_id = self.campaign_id

        link_type = self.link_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "material": material,
            }
        )
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if link_type is not UNSET:
            field_dict["link_type"] = link_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generate_general_sharing_links_request_material import (
            GenerateGeneralSharingLinksRequestMaterial,  # noqa: PLC0415
        )

        d = dict(src_dict)
        material = GenerateGeneralSharingLinksRequestMaterial.from_dict(d.pop("material"))

        campaign_id = d.pop("campaign_id", UNSET)

        link_type = d.pop("link_type", UNSET)

        generate_general_sharing_links_request = cls(
            material=material,
            campaign_id=campaign_id,
            link_type=link_type,
        )

        generate_general_sharing_links_request.additional_properties = d
        return generate_general_sharing_links_request

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
