from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.account_requirement import AccountRequirement
  from ..models.shop_requirement import ShopRequirement





T = TypeVar("T", bound="GetShortVideoCampaignResponseDataShortVideoCampaignParticipationRequirement")



@_attrs_define
class GetShortVideoCampaignResponseDataShortVideoCampaignParticipationRequirement:
    """ 
        Attributes:
            account_requirements (list[AccountRequirement] | Unset): Applicable requirements for linked accounts, account
                performance, and e-commerce permissions. Does not establish that any specific account has passed eligibility
                checks.
            max_account_registration_count (int | Unset): Maximum registration records each account may submit, as a
                positive integer. Omitted if unknown or inapplicable; omission does not mean unlimited. Not a video count limit
                or remaining registration quota.
            shop_requirements (list[ShopRequirement] | Unset): Applicable shop status, targeting, and other requirements,
                without targeting lists. Does not establish that the shop has passed eligibility checks.
     """

    account_requirements: list[AccountRequirement] | Unset = UNSET
    max_account_registration_count: int | Unset = UNSET
    shop_requirements: list[ShopRequirement] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.account_requirement import AccountRequirement # noqa: PLC0415
        from ..models.shop_requirement import ShopRequirement # noqa: PLC0415
        account_requirements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.account_requirements, Unset):
            account_requirements = []
            for account_requirements_item_data in self.account_requirements:
                account_requirements_item = account_requirements_item_data.to_dict()
                account_requirements.append(account_requirements_item)



        max_account_registration_count = self.max_account_registration_count

        shop_requirements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shop_requirements, Unset):
            shop_requirements = []
            for shop_requirements_item_data in self.shop_requirements:
                shop_requirements_item = shop_requirements_item_data.to_dict()
                shop_requirements.append(shop_requirements_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_requirements is not UNSET:
            field_dict["account_requirements"] = account_requirements
        if max_account_registration_count is not UNSET:
            field_dict["max_account_registration_count"] = max_account_registration_count
        if shop_requirements is not UNSET:
            field_dict["shop_requirements"] = shop_requirements

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_requirement import AccountRequirement # noqa: PLC0415
        from ..models.shop_requirement import ShopRequirement # noqa: PLC0415
        d = dict(src_dict)
        _account_requirements = d.pop("account_requirements", UNSET)
        account_requirements: list[AccountRequirement] | Unset = UNSET
        if _account_requirements is not UNSET:
            account_requirements = []
            for account_requirements_item_data in _account_requirements:
                account_requirements_item = AccountRequirement.from_dict(account_requirements_item_data)



                account_requirements.append(account_requirements_item)


        max_account_registration_count = d.pop("max_account_registration_count", UNSET)

        _shop_requirements = d.pop("shop_requirements", UNSET)
        shop_requirements: list[ShopRequirement] | Unset = UNSET
        if _shop_requirements is not UNSET:
            shop_requirements = []
            for shop_requirements_item_data in _shop_requirements:
                shop_requirements_item = ShopRequirement.from_dict(shop_requirements_item_data)



                shop_requirements.append(shop_requirements_item)


        get_short_video_campaign_response_data_short_video_campaign_participation_requirement = cls(
            account_requirements=account_requirements,
            max_account_registration_count=max_account_registration_count,
            shop_requirements=shop_requirements,
        )


        get_short_video_campaign_response_data_short_video_campaign_participation_requirement.additional_properties = d
        return get_short_video_campaign_response_data_short_video_campaign_participation_requirement

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
