from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_performance_response_data_performance_interval_breakdown_shop_tab_and_search_other import (
        GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearchOther,
    )
    from ..models.get_shop_performance_response_data_performance_interval_breakdown_shop_tab_and_search_search_attributed import (
        GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearchSearchAttributed,
    )
    from ..models.get_shop_performance_response_data_performance_interval_breakdown_shop_tab_and_search_shop_tab_attributed import (
        GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearchShopTabAttributed,
    )


T = TypeVar("T", bound="GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearch")


@_attrs_define
class GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearch:
    """
    Attributes:
        others (GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearchOther | Unset):
        search_attributed (GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearchSearchAttributed |
            Unset):
        shop_tab_attributed (GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearchShopTabAttributed
            | Unset):
    """

    others: GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearchOther | Unset = UNSET
    search_attributed: (
        GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearchSearchAttributed | Unset
    ) = UNSET
    shop_tab_attributed: (
        GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearchShopTabAttributed | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        others: dict[str, Any] | Unset = UNSET
        if not isinstance(self.others, Unset):
            others = self.others.to_dict()

        search_attributed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search_attributed, Unset):
            search_attributed = self.search_attributed.to_dict()

        shop_tab_attributed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shop_tab_attributed, Unset):
            shop_tab_attributed = self.shop_tab_attributed.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if others is not UNSET:
            field_dict["others"] = others
        if search_attributed is not UNSET:
            field_dict["search_attributed"] = search_attributed
        if shop_tab_attributed is not UNSET:
            field_dict["shop_tab_attributed"] = shop_tab_attributed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_performance_response_data_performance_interval_breakdown_shop_tab_and_search_other import (
            GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearchOther,  # noqa: PLC0415
        )
        from ..models.get_shop_performance_response_data_performance_interval_breakdown_shop_tab_and_search_search_attributed import (
            GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearchSearchAttributed,  # noqa: PLC0415
        )
        from ..models.get_shop_performance_response_data_performance_interval_breakdown_shop_tab_and_search_shop_tab_attributed import (
            GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearchShopTabAttributed,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _others = d.pop("others", UNSET)
        others: GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearchOther | Unset
        if isinstance(_others, Unset):
            others = UNSET
        else:
            others = GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearchOther.from_dict(_others)

        _search_attributed = d.pop("search_attributed", UNSET)
        search_attributed: (
            GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearchSearchAttributed | Unset
        )
        if isinstance(_search_attributed, Unset):
            search_attributed = UNSET
        else:
            search_attributed = (
                GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearchSearchAttributed.from_dict(
                    _search_attributed
                )
            )

        _shop_tab_attributed = d.pop("shop_tab_attributed", UNSET)
        shop_tab_attributed: (
            GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearchShopTabAttributed | Unset
        )
        if isinstance(_shop_tab_attributed, Unset):
            shop_tab_attributed = UNSET
        else:
            shop_tab_attributed = (
                GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearchShopTabAttributed.from_dict(
                    _shop_tab_attributed
                )
            )

        get_shop_performance_response_data_performance_interval_breakdown_shop_tab_and_search = cls(
            others=others,
            search_attributed=search_attributed,
            shop_tab_attributed=shop_tab_attributed,
        )

        get_shop_performance_response_data_performance_interval_breakdown_shop_tab_and_search.additional_properties = d
        return get_shop_performance_response_data_performance_interval_breakdown_shop_tab_and_search

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
