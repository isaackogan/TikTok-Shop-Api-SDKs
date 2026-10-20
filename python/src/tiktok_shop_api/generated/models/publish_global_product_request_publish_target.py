from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.publish_global_product_request_publish_target_region import PublishGlobalProductRequestPublishTargetRegion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.publish_global_product_request_publish_target_sku import PublishGlobalProductRequestPublishTargetSku


T = TypeVar("T", bound="PublishGlobalProductRequestPublishTarget")


@_attrs_define
class PublishGlobalProductRequestPublishTarget:
    """
    Attributes:
        region (PublishGlobalProductRequestPublishTargetRegion): The new market where you want to publish the global
            product.
            Possible values:
            - AT: Austria
            - BE:Belgium
            - CZ:Czech Republic
            - DE: Germany
            - ES: Spain
            - FR: France
            - GB: United Kingdom
            - GR: Greece
            - HU:Hungary
            - ID: Indonesia
            - IE: Ireland
            - IT: Italy
            - JP: Japan
            - MY: Malaysia
            - NL: Netherlands(NL)
            - PH: Philippines
            - PO: Poland
            - PT:Portugal
            - SG: Singapore
            - TH: Thailand
            - US: United States
            - VN: Vietnam
            - MX: Mexico
        skus (list[PublishGlobalProductRequestPublishTargetSku]): The SKUs to be published in the specified market.
            - Max SKUs for EU, JP, UK, US: 300
            - Max SKUs for other regions: 100
        responsible_person_ids (list[str] | Unset): A list of responsible person IDs. Retrieve the IDs from the [Search
            Responsible Persons API](67066a55f17b7d02f95d2fb1).
            Default: The IDs provided when the global product was created.
            **Note**: Applicable only for the EU market in certain categories. Use the [Get Global Category Rules
            API](650a056df1fd3102b91b5b8e) to check the requirements.
        manufacturer_ids (list[str] | Unset): A list of manufacturer IDs. Retrieve the IDs from the [Search
            Manufacturers API](67066a580dcee902fa03ccf9).
            Default: The IDs provided when the global product was created.
            **Note**: Applicable only for the EU market in certain categories. Use the [Get Global Category Rules
            API](650a056df1fd3102b91b5b8e) to check the requirements.
    """

    region: PublishGlobalProductRequestPublishTargetRegion
    skus: list[PublishGlobalProductRequestPublishTargetSku]
    responsible_person_ids: list[str] | Unset = UNSET
    manufacturer_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region = self.region.value

        skus = []
        for skus_item_data in self.skus:
            skus_item = skus_item_data.to_dict()
            skus.append(skus_item)

        responsible_person_ids: list[str] | Unset = UNSET
        if not isinstance(self.responsible_person_ids, Unset):
            responsible_person_ids = self.responsible_person_ids

        manufacturer_ids: list[str] | Unset = UNSET
        if not isinstance(self.manufacturer_ids, Unset):
            manufacturer_ids = self.manufacturer_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "region": region,
                "skus": skus,
            }
        )
        if responsible_person_ids is not UNSET:
            field_dict["responsible_person_ids"] = responsible_person_ids
        if manufacturer_ids is not UNSET:
            field_dict["manufacturer_ids"] = manufacturer_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.publish_global_product_request_publish_target_sku import (
            PublishGlobalProductRequestPublishTargetSku,  # noqa: PLC0415
        )

        d = dict(src_dict)
        region = PublishGlobalProductRequestPublishTargetRegion(d.pop("region"))

        skus = []
        _skus = d.pop("skus")
        for skus_item_data in _skus:
            skus_item = PublishGlobalProductRequestPublishTargetSku.from_dict(skus_item_data)

            skus.append(skus_item)

        responsible_person_ids = cast(list[str], d.pop("responsible_person_ids", UNSET))

        manufacturer_ids = cast(list[str], d.pop("manufacturer_ids", UNSET))

        publish_global_product_request_publish_target = cls(
            region=region,
            skus=skus,
            responsible_person_ids=responsible_person_ids,
            manufacturer_ids=manufacturer_ids,
        )

        publish_global_product_request_publish_target.additional_properties = d
        return publish_global_product_request_publish_target

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
