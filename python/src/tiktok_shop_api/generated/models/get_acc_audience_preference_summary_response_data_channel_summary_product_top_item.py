from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.stat import Stat





T = TypeVar("T", bound="GetACCAudiencePreferenceSummaryResponseDataChannelSummaryProductTopItem")



@_attrs_define
class GetACCAudiencePreferenceSummaryResponseDataChannelSummaryProductTopItem:
    """ 
        Attributes:
            l2_category_id (str | Unset): ID of the product's level-2 category.
            l2_category_name (str | Unset): Name of the product's level-2 category.
            l3_category_id (str | Unset): ID of the product's level-3 category.
            l3_category_name (str | Unset): Name of the product's level-3 category.
            product_id (str | Unset): ID of the product.
            product_image_url (str | Unset): URL of the product image.
            product_name (str | Unset): Name of the product.
            product_scan_url (str | Unset): Share link for the product.
            stats (Stat | Unset):
     """

    l2_category_id: str | Unset = UNSET
    l2_category_name: str | Unset = UNSET
    l3_category_id: str | Unset = UNSET
    l3_category_name: str | Unset = UNSET
    product_id: str | Unset = UNSET
    product_image_url: str | Unset = UNSET
    product_name: str | Unset = UNSET
    product_scan_url: str | Unset = UNSET
    stats: Stat | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.stat import Stat # noqa: PLC0415
        l2_category_id = self.l2_category_id

        l2_category_name = self.l2_category_name

        l3_category_id = self.l3_category_id

        l3_category_name = self.l3_category_name

        product_id = self.product_id

        product_image_url = self.product_image_url

        product_name = self.product_name

        product_scan_url = self.product_scan_url

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if l2_category_id is not UNSET:
            field_dict["l2_category_id"] = l2_category_id
        if l2_category_name is not UNSET:
            field_dict["l2_category_name"] = l2_category_name
        if l3_category_id is not UNSET:
            field_dict["l3_category_id"] = l3_category_id
        if l3_category_name is not UNSET:
            field_dict["l3_category_name"] = l3_category_name
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_image_url is not UNSET:
            field_dict["product_image_url"] = product_image_url
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if product_scan_url is not UNSET:
            field_dict["product_scan_url"] = product_scan_url
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stat import Stat # noqa: PLC0415
        d = dict(src_dict)
        l2_category_id = d.pop("l2_category_id", UNSET)

        l2_category_name = d.pop("l2_category_name", UNSET)

        l3_category_id = d.pop("l3_category_id", UNSET)

        l3_category_name = d.pop("l3_category_name", UNSET)

        product_id = d.pop("product_id", UNSET)

        product_image_url = d.pop("product_image_url", UNSET)

        product_name = d.pop("product_name", UNSET)

        product_scan_url = d.pop("product_scan_url", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: Stat | Unset
        if isinstance(_stats,  Unset):
            stats = UNSET
        else:
            stats = Stat.from_dict(_stats)




        get_acc_audience_preference_summary_response_data_channel_summary_product_top_item = cls(
            l2_category_id=l2_category_id,
            l2_category_name=l2_category_name,
            l3_category_id=l3_category_id,
            l3_category_name=l3_category_name,
            product_id=product_id,
            product_image_url=product_image_url,
            product_name=product_name,
            product_scan_url=product_scan_url,
            stats=stats,
        )


        get_acc_audience_preference_summary_response_data_channel_summary_product_top_item.additional_properties = d
        return get_acc_audience_preference_summary_response_data_channel_summary_product_top_item

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
