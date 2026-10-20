from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.replicate_product_request_replicate_target_inventory_mode import ReplicateProductRequestReplicateTargetInventoryMode
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.product_attribute import ProductAttribute
  from ..models.replicate_product_request_replicate_target_certification import ReplicateProductRequestReplicateTargetCertification
  from ..models.replicate_product_request_replicate_target_sku import ReplicateProductRequestReplicateTargetSku





T = TypeVar("T", bound="ReplicateProductRequestReplicateTarget")



@_attrs_define
class ReplicateProductRequestReplicateTarget:
    """ 
        Attributes:
            certifications (list[ReplicateProductRequestReplicateTargetCertification] | Unset): The list of certifications
                for your product.
                Max count: 10

                As per TikTok Shop guidelines, certifications are required for certain restricted product categories. Retrieve
                the certification requirements for your product from the [Get Category Rules
                API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9). Refer to [TikTok Shop Restricted
                Products Policy](https://seller-
                us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=3238037484275457&from=policy) for information on
                product category restrictions.
            inventory_mode (ReplicateProductRequestReplicateTargetInventoryMode | Unset): The inventory mode for the
                replicated product in this target market. This field is applicable only to EU markets. Possible values:
                - SHARED: Inventory for interconnected products must remain consistent; otherwise, an error is returned.
                - EXCLUSIVE: Inventory for each product can be set independently without affecting the others.

                If omitted, the inventory mode defaults to EXCLUSIVE.
            manufacturer_ids (list[str] | Unset): A comma-delimited list of manufacturer IDs. Retrieve the IDs from the
                [Search Manufacturers API](67066a580dcee902fa03ccf9).

                **Note**: Applicable only for the EU market in certain categories. Use the [Get Category Rules
                API](6509c0febace3e02b74594a9) to check the requirements.
            product_attributes (list[ProductAttribute] | Unset): A list of general attributes (e.g. manufacturer, country of
                origin, materials used) that describe the product as a whole, regardless of variant.

                **Important**: The attributes available for use are determined by the system based on the product's assigned
                category, with some being mandatory. You must provide the product attributes marked as `is_required` in the
                response of the [Get Attributes API](6509c5784a0bb702c0561cc8) to avoid listing failure.
            region (str | Unset): The new market where you want to replicate the product.
            responsible_person_ids (list[str] | Unset): A comma-delimited list of responsible person IDs. Retrieve the IDs
                from the [Search Responsible Persons API](67066a55f17b7d02f95d2fb1).

                **Note**: Applicable only for the EU market in certain categories. Use the [Get Category Rules
                API](6509c0febace3e02b74594a9) to check the requirements.
            skus (list[ReplicateProductRequestReplicateTargetSku] | Unset): The SKUs to be published in the specified
                market.
                - Max SKUs for EU, JP, UK, US: 300
                - Max SKUs for other regions: 100
                Note: SKUs of all source country must be included.
     """

    certifications: list[ReplicateProductRequestReplicateTargetCertification] | Unset = UNSET
    inventory_mode: ReplicateProductRequestReplicateTargetInventoryMode | Unset = UNSET
    manufacturer_ids: list[str] | Unset = UNSET
    product_attributes: list[ProductAttribute] | Unset = UNSET
    region: str | Unset = UNSET
    responsible_person_ids: list[str] | Unset = UNSET
    skus: list[ReplicateProductRequestReplicateTargetSku] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.product_attribute import ProductAttribute # noqa: PLC0415
        from ..models.replicate_product_request_replicate_target_certification import ReplicateProductRequestReplicateTargetCertification # noqa: PLC0415
        from ..models.replicate_product_request_replicate_target_sku import ReplicateProductRequestReplicateTargetSku # noqa: PLC0415
        certifications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.certifications, Unset):
            certifications = []
            for certifications_item_data in self.certifications:
                certifications_item = certifications_item_data.to_dict()
                certifications.append(certifications_item)



        inventory_mode: str | Unset = UNSET
        if not isinstance(self.inventory_mode, Unset):
            inventory_mode = self.inventory_mode.value


        manufacturer_ids: list[str] | Unset = UNSET
        if not isinstance(self.manufacturer_ids, Unset):
            manufacturer_ids = self.manufacturer_ids



        product_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_attributes, Unset):
            product_attributes = []
            for product_attributes_item_data in self.product_attributes:
                product_attributes_item = product_attributes_item_data.to_dict()
                product_attributes.append(product_attributes_item)



        region = self.region

        responsible_person_ids: list[str] | Unset = UNSET
        if not isinstance(self.responsible_person_ids, Unset):
            responsible_person_ids = self.responsible_person_ids



        skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skus, Unset):
            skus = []
            for skus_item_data in self.skus:
                skus_item = skus_item_data.to_dict()
                skus.append(skus_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if certifications is not UNSET:
            field_dict["certifications"] = certifications
        if inventory_mode is not UNSET:
            field_dict["inventory_mode"] = inventory_mode
        if manufacturer_ids is not UNSET:
            field_dict["manufacturer_ids"] = manufacturer_ids
        if product_attributes is not UNSET:
            field_dict["product_attributes"] = product_attributes
        if region is not UNSET:
            field_dict["region"] = region
        if responsible_person_ids is not UNSET:
            field_dict["responsible_person_ids"] = responsible_person_ids
        if skus is not UNSET:
            field_dict["skus"] = skus

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_attribute import ProductAttribute # noqa: PLC0415
        from ..models.replicate_product_request_replicate_target_certification import ReplicateProductRequestReplicateTargetCertification # noqa: PLC0415
        from ..models.replicate_product_request_replicate_target_sku import ReplicateProductRequestReplicateTargetSku # noqa: PLC0415
        d = dict(src_dict)
        _certifications = d.pop("certifications", UNSET)
        certifications: list[ReplicateProductRequestReplicateTargetCertification] | Unset = UNSET
        if _certifications is not UNSET:
            certifications = []
            for certifications_item_data in _certifications:
                certifications_item = ReplicateProductRequestReplicateTargetCertification.from_dict(certifications_item_data)



                certifications.append(certifications_item)


        _inventory_mode = d.pop("inventory_mode", UNSET)
        inventory_mode: ReplicateProductRequestReplicateTargetInventoryMode | Unset
        if isinstance(_inventory_mode,  Unset):
            inventory_mode = UNSET
        else:
            inventory_mode = ReplicateProductRequestReplicateTargetInventoryMode(_inventory_mode)




        manufacturer_ids = cast(list[str], d.pop("manufacturer_ids", UNSET))


        _product_attributes = d.pop("product_attributes", UNSET)
        product_attributes: list[ProductAttribute] | Unset = UNSET
        if _product_attributes is not UNSET:
            product_attributes = []
            for product_attributes_item_data in _product_attributes:
                product_attributes_item = ProductAttribute.from_dict(product_attributes_item_data)



                product_attributes.append(product_attributes_item)


        region = d.pop("region", UNSET)

        responsible_person_ids = cast(list[str], d.pop("responsible_person_ids", UNSET))


        _skus = d.pop("skus", UNSET)
        skus: list[ReplicateProductRequestReplicateTargetSku] | Unset = UNSET
        if _skus is not UNSET:
            skus = []
            for skus_item_data in _skus:
                skus_item = ReplicateProductRequestReplicateTargetSku.from_dict(skus_item_data)



                skus.append(skus_item)


        replicate_product_request_replicate_target = cls(
            certifications=certifications,
            inventory_mode=inventory_mode,
            manufacturer_ids=manufacturer_ids,
            product_attributes=product_attributes,
            region=region,
            responsible_person_ids=responsible_person_ids,
            skus=skus,
        )


        replicate_product_request_replicate_target.additional_properties = d
        return replicate_product_request_replicate_target

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
