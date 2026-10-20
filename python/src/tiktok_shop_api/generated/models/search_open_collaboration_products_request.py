from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.category import Category
  from ..models.sales_price_range import SalesPriceRange
  from ..models.search_open_collaboration_products_request_commission_rate_range import SearchOpenCollaborationProductsRequestCommissionRateRange





T = TypeVar("T", bound="SearchOpenCollaborationProductsRequest")



@_attrs_define
class SearchOpenCollaborationProductsRequest:
    """ 
        Attributes:
            title_keywords (list[str] | Unset): A list of product keywords for searching. Product titles, or names, are
                loosely matched. Keywords in the list form a query and the resulting set of matching product names is based on
                the conjunctive operator `AND` between each keyword. For example, the keyword list `["Men", "Fashion"]` creates
                a query `"Men" AND "Fashion"` and the resulting set of matching product names contains the loosely matched
                conjuction of "Men" and "Fashion" such as "Male Fashionable". Maximum length of the list is 20 keywords. Maximum
                keyword string length is 255 characters.
            sales_price_range (SalesPriceRange | Unset):
            category (Category | Unset):
            commission_rate_range (SearchOpenCollaborationProductsRequestCommissionRateRange | Unset):
     """

    title_keywords: list[str] | Unset = UNSET
    sales_price_range: SalesPriceRange | Unset = UNSET
    category: Category | Unset = UNSET
    commission_rate_range: SearchOpenCollaborationProductsRequestCommissionRateRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.category import Category # noqa: PLC0415
        from ..models.sales_price_range import SalesPriceRange # noqa: PLC0415
        from ..models.search_open_collaboration_products_request_commission_rate_range import SearchOpenCollaborationProductsRequestCommissionRateRange # noqa: PLC0415
        title_keywords: list[str] | Unset = UNSET
        if not isinstance(self.title_keywords, Unset):
            title_keywords = self.title_keywords



        sales_price_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sales_price_range, Unset):
            sales_price_range = self.sales_price_range.to_dict()

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        commission_rate_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commission_rate_range, Unset):
            commission_rate_range = self.commission_rate_range.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if title_keywords is not UNSET:
            field_dict["title_keywords"] = title_keywords
        if sales_price_range is not UNSET:
            field_dict["sales_price_range"] = sales_price_range
        if category is not UNSET:
            field_dict["category"] = category
        if commission_rate_range is not UNSET:
            field_dict["commission_rate_range"] = commission_rate_range

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category import Category # noqa: PLC0415
        from ..models.sales_price_range import SalesPriceRange # noqa: PLC0415
        from ..models.search_open_collaboration_products_request_commission_rate_range import SearchOpenCollaborationProductsRequestCommissionRateRange # noqa: PLC0415
        d = dict(src_dict)
        title_keywords = cast(list[str], d.pop("title_keywords", UNSET))


        _sales_price_range = d.pop("sales_price_range", UNSET)
        sales_price_range: SalesPriceRange | Unset
        if isinstance(_sales_price_range,  Unset):
            sales_price_range = UNSET
        else:
            sales_price_range = SalesPriceRange.from_dict(_sales_price_range)




        _category = d.pop("category", UNSET)
        category: Category | Unset
        if isinstance(_category,  Unset):
            category = UNSET
        else:
            category = Category.from_dict(_category)




        _commission_rate_range = d.pop("commission_rate_range", UNSET)
        commission_rate_range: SearchOpenCollaborationProductsRequestCommissionRateRange | Unset
        if isinstance(_commission_rate_range,  Unset):
            commission_rate_range = UNSET
        else:
            commission_rate_range = SearchOpenCollaborationProductsRequestCommissionRateRange.from_dict(_commission_rate_range)




        search_open_collaboration_products_request = cls(
            title_keywords=title_keywords,
            sales_price_range=sales_price_range,
            category=category,
            commission_rate_range=commission_rate_range,
        )


        search_open_collaboration_products_request.additional_properties = d
        return search_open_collaboration_products_request

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
