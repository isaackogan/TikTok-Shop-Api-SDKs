from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail_indicator_data import (
        GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailIndicatorData,
    )
    from ..models.get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail_product_price import (
        GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailProductPrice,
    )
    from ..models.get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail_product_thumbnail import (
        GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailProductThumbnail,
    )


T = TypeVar("T", bound="GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetail")


@_attrs_define
class GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetail:
    """
    Attributes:
        product_id (str | Unset): The product identifier.
        product_status (str | Unset): The product status. This is an enumerated type with values:
            -  PRODUCT_UNSPECIFIED
            -  PRODUCT_PENDING
            -  PRODUCT_APPROVED
            -  PRODUCT_REJECTED
            -  PRODUCT_PENDING_CLOSED
            -  PRODUCT_CLOSED
        product_name (str | Unset): The product name.
        product_stock_count (str | Unset): The product's total available stock quantity across all SKUs.
        total_commission_percent (str | Unset): The total commission rate for the partner plan. It is the sum of
            `creator_commission_percent` and `partner_commission_percent`. The value is in hundredths of a percent. For
            example, a value of 1000 means 10.00%.
        creator_commission_percent (str | Unset): The commission rate for the creator in the partner plan. The value is
            in hundredths of a percent. For example, a value of 1000 means 10.00%.
        partner_commission_percent (str | Unset): The commission rate for the partner in the partner plan. The value is
            in hundredths of a percent. For example, a value of 1000 means 10.00%.
        plan_commission_percent (str | Unset): The commission rate for open collaboration. The value is in hundredths of
            a percent. For example, a value of 1000 means 10.00%.
        product_price
            (GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailProductPrice |
            Unset):
        product_thumbnail
            (GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailProductThumbnail |
            Unset):
        indicator_data
            (GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailIndicatorData |
            Unset):
    """

    product_id: str | Unset = UNSET
    product_status: str | Unset = UNSET
    product_name: str | Unset = UNSET
    product_stock_count: str | Unset = UNSET
    total_commission_percent: str | Unset = UNSET
    creator_commission_percent: str | Unset = UNSET
    partner_commission_percent: str | Unset = UNSET
    plan_commission_percent: str | Unset = UNSET
    product_price: (
        GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailProductPrice | Unset
    ) = UNSET
    product_thumbnail: (
        GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailProductThumbnail
        | Unset
    ) = UNSET
    indicator_data: (
        GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailIndicatorData | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        product_status = self.product_status

        product_name = self.product_name

        product_stock_count = self.product_stock_count

        total_commission_percent = self.total_commission_percent

        creator_commission_percent = self.creator_commission_percent

        partner_commission_percent = self.partner_commission_percent

        plan_commission_percent = self.plan_commission_percent

        product_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_price, Unset):
            product_price = self.product_price.to_dict()

        product_thumbnail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_thumbnail, Unset):
            product_thumbnail = self.product_thumbnail.to_dict()

        indicator_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.indicator_data, Unset):
            indicator_data = self.indicator_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_status is not UNSET:
            field_dict["product_status"] = product_status
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if product_stock_count is not UNSET:
            field_dict["product_stock_count"] = product_stock_count
        if total_commission_percent is not UNSET:
            field_dict["total_commission_percent"] = total_commission_percent
        if creator_commission_percent is not UNSET:
            field_dict["creator_commission_percent"] = creator_commission_percent
        if partner_commission_percent is not UNSET:
            field_dict["partner_commission_percent"] = partner_commission_percent
        if plan_commission_percent is not UNSET:
            field_dict["plan_commission_percent"] = plan_commission_percent
        if product_price is not UNSET:
            field_dict["product_price"] = product_price
        if product_thumbnail is not UNSET:
            field_dict["product_thumbnail"] = product_thumbnail
        if indicator_data is not UNSET:
            field_dict["indicator_data"] = indicator_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail_indicator_data import (
            GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailIndicatorData,  # noqa: PLC0415
        )
        from ..models.get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail_product_price import (
            GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailProductPrice,  # noqa: PLC0415
        )
        from ..models.get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail_product_thumbnail import (
            GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailProductThumbnail,  # noqa: PLC0415
        )

        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        product_status = d.pop("product_status", UNSET)

        product_name = d.pop("product_name", UNSET)

        product_stock_count = d.pop("product_stock_count", UNSET)

        total_commission_percent = d.pop("total_commission_percent", UNSET)

        creator_commission_percent = d.pop("creator_commission_percent", UNSET)

        partner_commission_percent = d.pop("partner_commission_percent", UNSET)

        plan_commission_percent = d.pop("plan_commission_percent", UNSET)

        _product_price = d.pop("product_price", UNSET)
        product_price: (
            GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailProductPrice
            | Unset
        )
        if isinstance(_product_price, Unset):
            product_price = UNSET
        else:
            product_price = GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailProductPrice.from_dict(
                _product_price
            )

        _product_thumbnail = d.pop("product_thumbnail", UNSET)
        product_thumbnail: (
            GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailProductThumbnail
            | Unset
        )
        if isinstance(_product_thumbnail, Unset):
            product_thumbnail = UNSET
        else:
            product_thumbnail = GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailProductThumbnail.from_dict(
                _product_thumbnail
            )

        _indicator_data = d.pop("indicator_data", UNSET)
        indicator_data: (
            GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailIndicatorData
            | Unset
        )
        if isinstance(_indicator_data, Unset):
            indicator_data = UNSET
        else:
            indicator_data = GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailIndicatorData.from_dict(
                _indicator_data
            )

        get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail = cls(
            product_id=product_id,
            product_status=product_status,
            product_name=product_name,
            product_stock_count=product_stock_count,
            total_commission_percent=total_commission_percent,
            creator_commission_percent=creator_commission_percent,
            partner_commission_percent=partner_commission_percent,
            plan_commission_percent=plan_commission_percent,
            product_price=product_price,
            product_thumbnail=product_thumbnail,
            indicator_data=indicator_data,
        )

        get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail.additional_properties = d
        return get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail

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
