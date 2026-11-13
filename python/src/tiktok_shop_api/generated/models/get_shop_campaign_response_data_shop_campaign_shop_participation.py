from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_shop_campaign_response_data_shop_campaign_shop_participation_registration_statistic import GetShopCampaignResponseDataShopCampaignShopParticipationRegistrationStatistic
  from ..models.relation import Relation





T = TypeVar("T", bound="GetShopCampaignResponseDataShopCampaignShopParticipation")



@_attrs_define
class GetShopCampaignResponseDataShopCampaignShopParticipation:
    """ 
        Attributes:
            has_joined (bool | Unset): Whether a participation record exists. Omission means unknown. A record does not
                establish current approval or effective benefits.
            is_participating (bool | Unset): Whether the shop is currently participating. true when there is a registration
                pending review, approved, paused, or pending withdrawal review, or a valid submission. Omission means unknown.
            registration_statistics (GetShopCampaignResponseDataShopCampaignShopParticipationRegistrationStatistic | Unset):
            relation (Relation | Unset):
     """

    has_joined: bool | Unset = UNSET
    is_participating: bool | Unset = UNSET
    registration_statistics: GetShopCampaignResponseDataShopCampaignShopParticipationRegistrationStatistic | Unset = UNSET
    relation: Relation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shop_campaign_response_data_shop_campaign_shop_participation_registration_statistic import GetShopCampaignResponseDataShopCampaignShopParticipationRegistrationStatistic # noqa: PLC0415
        from ..models.relation import Relation # noqa: PLC0415
        has_joined = self.has_joined

        is_participating = self.is_participating

        registration_statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registration_statistics, Unset):
            registration_statistics = self.registration_statistics.to_dict()

        relation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relation, Unset):
            relation = self.relation.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if has_joined is not UNSET:
            field_dict["has_joined"] = has_joined
        if is_participating is not UNSET:
            field_dict["is_participating"] = is_participating
        if registration_statistics is not UNSET:
            field_dict["registration_statistics"] = registration_statistics
        if relation is not UNSET:
            field_dict["relation"] = relation

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_campaign_response_data_shop_campaign_shop_participation_registration_statistic import GetShopCampaignResponseDataShopCampaignShopParticipationRegistrationStatistic # noqa: PLC0415
        from ..models.relation import Relation # noqa: PLC0415
        d = dict(src_dict)
        has_joined = d.pop("has_joined", UNSET)

        is_participating = d.pop("is_participating", UNSET)

        _registration_statistics = d.pop("registration_statistics", UNSET)
        registration_statistics: GetShopCampaignResponseDataShopCampaignShopParticipationRegistrationStatistic | Unset
        if isinstance(_registration_statistics,  Unset):
            registration_statistics = UNSET
        else:
            registration_statistics = GetShopCampaignResponseDataShopCampaignShopParticipationRegistrationStatistic.from_dict(_registration_statistics)




        _relation = d.pop("relation", UNSET)
        relation: Relation | Unset
        if isinstance(_relation,  Unset):
            relation = UNSET
        else:
            relation = Relation.from_dict(_relation)




        get_shop_campaign_response_data_shop_campaign_shop_participation = cls(
            has_joined=has_joined,
            is_participating=is_participating,
            registration_statistics=registration_statistics,
            relation=relation,
        )


        get_shop_campaign_response_data_shop_campaign_shop_participation.additional_properties = d
        return get_shop_campaign_response_data_shop_campaign_shop_participation

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
