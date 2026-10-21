from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_size_charts_response_data_size_chart_image import SearchSizeChartsResponseDataSizeChartImage
  from ..models.search_size_charts_response_data_size_chart_size_chart_data import SearchSizeChartsResponseDataSizeChartSizeChartData





T = TypeVar("T", bound="SearchSizeChartsResponseDataSizeChart")



@_attrs_define
class SearchSizeChartsResponseDataSizeChart:
    """ 
        Attributes:
            template_id (str | Unset): The size chart template ID.
            template_name (str | Unset): The size chart template name.
            images (list[SearchSizeChartsResponseDataSizeChartImage] | Unset): The list of images included in a size chart.
            related_category_ids (list[str] | Unset): Leaf category IDs applicable to this size chart.
            size_chart_datas (list[SearchSizeChartsResponseDataSizeChartSizeChartData] | Unset): Localized structured size
                chart data. Each item contains a locale and the structured data for that locale.
            size_chart_mode (str | Unset): Filter size charts by usage mode. Possible values: REUSABLE_TEMPLATE: A size
                chart template that can be reused across multiple products. PRODUCT_SCOPED: A size chart created for and used by
                a single product. If omitted, the existing search behavior is preserved.
            target_regions (list[str] | Unset): Target country or market codes recorded for this size chart, used for
                localized content and images. The list may include historical targets. Omitted when no target regions are
                recorded; omission does not mean worldwide support. This field does not determine product publishing
                eligibility.
     """

    template_id: str | Unset = UNSET
    template_name: str | Unset = UNSET
    images: list[SearchSizeChartsResponseDataSizeChartImage] | Unset = UNSET
    related_category_ids: list[str] | Unset = UNSET
    size_chart_datas: list[SearchSizeChartsResponseDataSizeChartSizeChartData] | Unset = UNSET
    size_chart_mode: str | Unset = UNSET
    target_regions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_size_charts_response_data_size_chart_image import SearchSizeChartsResponseDataSizeChartImage # noqa: PLC0415
        from ..models.search_size_charts_response_data_size_chart_size_chart_data import SearchSizeChartsResponseDataSizeChartSizeChartData # noqa: PLC0415
        template_id = self.template_id

        template_name = self.template_name

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)



        related_category_ids: list[str] | Unset = UNSET
        if not isinstance(self.related_category_ids, Unset):
            related_category_ids = self.related_category_ids



        size_chart_datas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.size_chart_datas, Unset):
            size_chart_datas = []
            for size_chart_datas_item_data in self.size_chart_datas:
                size_chart_datas_item = size_chart_datas_item_data.to_dict()
                size_chart_datas.append(size_chart_datas_item)



        size_chart_mode = self.size_chart_mode

        target_regions: list[str] | Unset = UNSET
        if not isinstance(self.target_regions, Unset):
            target_regions = self.target_regions




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if template_id is not UNSET:
            field_dict["template_id"] = template_id
        if template_name is not UNSET:
            field_dict["template_name"] = template_name
        if images is not UNSET:
            field_dict["images"] = images
        if related_category_ids is not UNSET:
            field_dict["related_category_ids"] = related_category_ids
        if size_chart_datas is not UNSET:
            field_dict["size_chart_datas"] = size_chart_datas
        if size_chart_mode is not UNSET:
            field_dict["size_chart_mode"] = size_chart_mode
        if target_regions is not UNSET:
            field_dict["target_regions"] = target_regions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_size_charts_response_data_size_chart_image import SearchSizeChartsResponseDataSizeChartImage # noqa: PLC0415
        from ..models.search_size_charts_response_data_size_chart_size_chart_data import SearchSizeChartsResponseDataSizeChartSizeChartData # noqa: PLC0415
        d = dict(src_dict)
        template_id = d.pop("template_id", UNSET)

        template_name = d.pop("template_name", UNSET)

        _images = d.pop("images", UNSET)
        images: list[SearchSizeChartsResponseDataSizeChartImage] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = SearchSizeChartsResponseDataSizeChartImage.from_dict(images_item_data)



                images.append(images_item)


        related_category_ids = cast(list[str], d.pop("related_category_ids", UNSET))


        _size_chart_datas = d.pop("size_chart_datas", UNSET)
        size_chart_datas: list[SearchSizeChartsResponseDataSizeChartSizeChartData] | Unset = UNSET
        if _size_chart_datas is not UNSET:
            size_chart_datas = []
            for size_chart_datas_item_data in _size_chart_datas:
                size_chart_datas_item = SearchSizeChartsResponseDataSizeChartSizeChartData.from_dict(size_chart_datas_item_data)



                size_chart_datas.append(size_chart_datas_item)


        size_chart_mode = d.pop("size_chart_mode", UNSET)

        target_regions = cast(list[str], d.pop("target_regions", UNSET))


        search_size_charts_response_data_size_chart = cls(
            template_id=template_id,
            template_name=template_name,
            images=images,
            related_category_ids=related_category_ids,
            size_chart_datas=size_chart_datas,
            size_chart_mode=size_chart_mode,
            target_regions=target_regions,
        )


        search_size_charts_response_data_size_chart.additional_properties = d
        return search_size_charts_response_data_size_chart

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
