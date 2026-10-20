from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_sps_metric_top_items_response_data_aht_aftersales_type_item import GetSPSMetricTopItemsResponseDataAhtAftersalesTypeItem
  from ..models.get_sps_metric_top_items_response_data_nbfr_top_product_item import GetSPSMetricTopItemsResponseDataNbfrTopProductItem
  from ..models.get_sps_metric_top_items_response_data_nrr_top_product_item import GetSPSMetricTopItemsResponseDataNrrTopProductItem
  from ..models.get_sps_metric_top_items_response_data_otdr_logistics_item import GetSPSMetricTopItemsResponseDataOtdrLogisticsItem





T = TypeVar("T", bound="GetSPSMetricTopItemsResponseData")



@_attrs_define
class GetSPSMetricTopItemsResponseData:
    """ 
        Attributes:
            aht_aftersales_type_items (list[GetSPSMetricTopItemsResponseDataAhtAftersalesTypeItem] | Unset): Top product
                items for AHT, with fields for average handle duration and the top aftersales type.
            metric_code (str | Unset): Stable metric code selected in the request. One of: NRR, NBFR, OTDR, or AHT.
            nbfr_top_product_items (list[GetSPSMetricTopItemsResponseDataNbfrTopProductItem] | Unset): NBFR top product
                items.
            nrr_top_product_items (list[GetSPSMetricTopItemsResponseDataNrrTopProductItem] | Unset): NRR top product items.
            otdr_logistics_items (list[GetSPSMetricTopItemsResponseDataOtdrLogisticsItem] | Unset): OTDR logistics provider
                items.
            total_count (int | Unset): Number of items in the metric-specific list returned by this response.
     """

    aht_aftersales_type_items: list[GetSPSMetricTopItemsResponseDataAhtAftersalesTypeItem] | Unset = UNSET
    metric_code: str | Unset = UNSET
    nbfr_top_product_items: list[GetSPSMetricTopItemsResponseDataNbfrTopProductItem] | Unset = UNSET
    nrr_top_product_items: list[GetSPSMetricTopItemsResponseDataNrrTopProductItem] | Unset = UNSET
    otdr_logistics_items: list[GetSPSMetricTopItemsResponseDataOtdrLogisticsItem] | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_sps_metric_top_items_response_data_aht_aftersales_type_item import GetSPSMetricTopItemsResponseDataAhtAftersalesTypeItem # noqa: PLC0415
        from ..models.get_sps_metric_top_items_response_data_nbfr_top_product_item import GetSPSMetricTopItemsResponseDataNbfrTopProductItem # noqa: PLC0415
        from ..models.get_sps_metric_top_items_response_data_nrr_top_product_item import GetSPSMetricTopItemsResponseDataNrrTopProductItem # noqa: PLC0415
        from ..models.get_sps_metric_top_items_response_data_otdr_logistics_item import GetSPSMetricTopItemsResponseDataOtdrLogisticsItem # noqa: PLC0415
        aht_aftersales_type_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.aht_aftersales_type_items, Unset):
            aht_aftersales_type_items = []
            for aht_aftersales_type_items_item_data in self.aht_aftersales_type_items:
                aht_aftersales_type_items_item = aht_aftersales_type_items_item_data.to_dict()
                aht_aftersales_type_items.append(aht_aftersales_type_items_item)



        metric_code = self.metric_code

        nbfr_top_product_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nbfr_top_product_items, Unset):
            nbfr_top_product_items = []
            for nbfr_top_product_items_item_data in self.nbfr_top_product_items:
                nbfr_top_product_items_item = nbfr_top_product_items_item_data.to_dict()
                nbfr_top_product_items.append(nbfr_top_product_items_item)



        nrr_top_product_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nrr_top_product_items, Unset):
            nrr_top_product_items = []
            for nrr_top_product_items_item_data in self.nrr_top_product_items:
                nrr_top_product_items_item = nrr_top_product_items_item_data.to_dict()
                nrr_top_product_items.append(nrr_top_product_items_item)



        otdr_logistics_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.otdr_logistics_items, Unset):
            otdr_logistics_items = []
            for otdr_logistics_items_item_data in self.otdr_logistics_items:
                otdr_logistics_items_item = otdr_logistics_items_item_data.to_dict()
                otdr_logistics_items.append(otdr_logistics_items_item)



        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if aht_aftersales_type_items is not UNSET:
            field_dict["aht_aftersales_type_items"] = aht_aftersales_type_items
        if metric_code is not UNSET:
            field_dict["metric_code"] = metric_code
        if nbfr_top_product_items is not UNSET:
            field_dict["nbfr_top_product_items"] = nbfr_top_product_items
        if nrr_top_product_items is not UNSET:
            field_dict["nrr_top_product_items"] = nrr_top_product_items
        if otdr_logistics_items is not UNSET:
            field_dict["otdr_logistics_items"] = otdr_logistics_items
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_sps_metric_top_items_response_data_aht_aftersales_type_item import GetSPSMetricTopItemsResponseDataAhtAftersalesTypeItem # noqa: PLC0415
        from ..models.get_sps_metric_top_items_response_data_nbfr_top_product_item import GetSPSMetricTopItemsResponseDataNbfrTopProductItem # noqa: PLC0415
        from ..models.get_sps_metric_top_items_response_data_nrr_top_product_item import GetSPSMetricTopItemsResponseDataNrrTopProductItem # noqa: PLC0415
        from ..models.get_sps_metric_top_items_response_data_otdr_logistics_item import GetSPSMetricTopItemsResponseDataOtdrLogisticsItem # noqa: PLC0415
        d = dict(src_dict)
        _aht_aftersales_type_items = d.pop("aht_aftersales_type_items", UNSET)
        aht_aftersales_type_items: list[GetSPSMetricTopItemsResponseDataAhtAftersalesTypeItem] | Unset = UNSET
        if _aht_aftersales_type_items is not UNSET:
            aht_aftersales_type_items = []
            for aht_aftersales_type_items_item_data in _aht_aftersales_type_items:
                aht_aftersales_type_items_item = GetSPSMetricTopItemsResponseDataAhtAftersalesTypeItem.from_dict(aht_aftersales_type_items_item_data)



                aht_aftersales_type_items.append(aht_aftersales_type_items_item)


        metric_code = d.pop("metric_code", UNSET)

        _nbfr_top_product_items = d.pop("nbfr_top_product_items", UNSET)
        nbfr_top_product_items: list[GetSPSMetricTopItemsResponseDataNbfrTopProductItem] | Unset = UNSET
        if _nbfr_top_product_items is not UNSET:
            nbfr_top_product_items = []
            for nbfr_top_product_items_item_data in _nbfr_top_product_items:
                nbfr_top_product_items_item = GetSPSMetricTopItemsResponseDataNbfrTopProductItem.from_dict(nbfr_top_product_items_item_data)



                nbfr_top_product_items.append(nbfr_top_product_items_item)


        _nrr_top_product_items = d.pop("nrr_top_product_items", UNSET)
        nrr_top_product_items: list[GetSPSMetricTopItemsResponseDataNrrTopProductItem] | Unset = UNSET
        if _nrr_top_product_items is not UNSET:
            nrr_top_product_items = []
            for nrr_top_product_items_item_data in _nrr_top_product_items:
                nrr_top_product_items_item = GetSPSMetricTopItemsResponseDataNrrTopProductItem.from_dict(nrr_top_product_items_item_data)



                nrr_top_product_items.append(nrr_top_product_items_item)


        _otdr_logistics_items = d.pop("otdr_logistics_items", UNSET)
        otdr_logistics_items: list[GetSPSMetricTopItemsResponseDataOtdrLogisticsItem] | Unset = UNSET
        if _otdr_logistics_items is not UNSET:
            otdr_logistics_items = []
            for otdr_logistics_items_item_data in _otdr_logistics_items:
                otdr_logistics_items_item = GetSPSMetricTopItemsResponseDataOtdrLogisticsItem.from_dict(otdr_logistics_items_item_data)



                otdr_logistics_items.append(otdr_logistics_items_item)


        total_count = d.pop("total_count", UNSET)

        get_sps_metric_top_items_response_data = cls(
            aht_aftersales_type_items=aht_aftersales_type_items,
            metric_code=metric_code,
            nbfr_top_product_items=nbfr_top_product_items,
            nrr_top_product_items=nrr_top_product_items,
            otdr_logistics_items=otdr_logistics_items,
            total_count=total_count,
        )


        get_sps_metric_top_items_response_data.additional_properties = d
        return get_sps_metric_top_items_response_data

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
