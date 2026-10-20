from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.publish_global_product_response_data_product_sku import PublishGlobalProductResponseDataProductSku





T = TypeVar("T", bound="PublishGlobalProductResponseDataProduct")



@_attrs_define
class PublishGlobalProductResponseDataProduct:
    """ 
        Attributes:
            region (str | Unset): The market of this local product.
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
            shop_id (str | Unset): The ID of the local shop in the specified market. One market can only have one local
                shop.
            skus (list[PublishGlobalProductResponseDataProductSku] | Unset): The newly created local SKUs in the specified
                market.
            id (str | Unset): The newly generated local product ID.
     """

    region: str | Unset = UNSET
    shop_id: str | Unset = UNSET
    skus: list[PublishGlobalProductResponseDataProductSku] | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.publish_global_product_response_data_product_sku import PublishGlobalProductResponseDataProductSku # noqa: PLC0415
        region = self.region

        shop_id = self.shop_id

        skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skus, Unset):
            skus = []
            for skus_item_data in self.skus:
                skus_item = skus_item_data.to_dict()
                skus.append(skus_item)



        id = self.id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if region is not UNSET:
            field_dict["region"] = region
        if shop_id is not UNSET:
            field_dict["shop_id"] = shop_id
        if skus is not UNSET:
            field_dict["skus"] = skus
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.publish_global_product_response_data_product_sku import PublishGlobalProductResponseDataProductSku # noqa: PLC0415
        d = dict(src_dict)
        region = d.pop("region", UNSET)

        shop_id = d.pop("shop_id", UNSET)

        _skus = d.pop("skus", UNSET)
        skus: list[PublishGlobalProductResponseDataProductSku] | Unset = UNSET
        if _skus is not UNSET:
            skus = []
            for skus_item_data in _skus:
                skus_item = PublishGlobalProductResponseDataProductSku.from_dict(skus_item_data)



                skus.append(skus_item)


        id = d.pop("id", UNSET)

        publish_global_product_response_data_product = cls(
            region=region,
            shop_id=shop_id,
            skus=skus,
            id=id,
        )


        publish_global_product_response_data_product.additional_properties = d
        return publish_global_product_response_data_product

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
