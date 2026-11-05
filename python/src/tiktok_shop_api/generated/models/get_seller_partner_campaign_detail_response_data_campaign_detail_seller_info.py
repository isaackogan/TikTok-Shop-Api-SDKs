from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_seller_partner_campaign_detail_response_data_campaign_detail_seller_info_image import GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerInfoImage





T = TypeVar("T", bound="GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerInfo")



@_attrs_define
class GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerInfo:
    """ 
        Attributes:
            image (GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerInfoImage | Unset):
            seller_id (str | Unset): ID of the seller associated with the campaign, encoded as a decimal string.
            shop_code (str | Unset): Business code identifying the shop. This is distinct from seller_id.
            shop_name (str | Unset): Display name of the shop.
     """

    image: GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerInfoImage | Unset = UNSET
    seller_id: str | Unset = UNSET
    shop_code: str | Unset = UNSET
    shop_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_seller_partner_campaign_detail_response_data_campaign_detail_seller_info_image import GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerInfoImage # noqa: PLC0415
        image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        seller_id = self.seller_id

        shop_code = self.shop_code

        shop_name = self.shop_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if image is not UNSET:
            field_dict["image"] = image
        if seller_id is not UNSET:
            field_dict["seller_id"] = seller_id
        if shop_code is not UNSET:
            field_dict["shop_code"] = shop_code
        if shop_name is not UNSET:
            field_dict["shop_name"] = shop_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_seller_partner_campaign_detail_response_data_campaign_detail_seller_info_image import GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerInfoImage # noqa: PLC0415
        d = dict(src_dict)
        _image = d.pop("image", UNSET)
        image: GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerInfoImage | Unset
        if isinstance(_image,  Unset):
            image = UNSET
        else:
            image = GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerInfoImage.from_dict(_image)




        seller_id = d.pop("seller_id", UNSET)

        shop_code = d.pop("shop_code", UNSET)

        shop_name = d.pop("shop_name", UNSET)

        get_seller_partner_campaign_detail_response_data_campaign_detail_seller_info = cls(
            image=image,
            seller_id=seller_id,
            shop_code=shop_code,
            shop_name=shop_name,
        )


        get_seller_partner_campaign_detail_response_data_campaign_detail_seller_info.additional_properties = d
        return get_seller_partner_campaign_detail_response_data_campaign_detail_seller_info

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
