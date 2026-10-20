from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.seo_word import SeoWord


T = TypeVar("T", bound="GetProductsSEOWordsResponseDataProduct")


@_attrs_define
class GetProductsSEOWordsResponseDataProduct:
    """
    Attributes:
        id (str | Unset): The product ID.
        seo_words (list[SeoWord] | Unset): The list of SEO keyword suggestions for the product title.
    """

    id: str | Unset = UNSET
    seo_words: list[SeoWord] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        seo_words: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.seo_words, Unset):
            seo_words = []
            for seo_words_item_data in self.seo_words:
                seo_words_item = seo_words_item_data.to_dict()
                seo_words.append(seo_words_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if seo_words is not UNSET:
            field_dict["seo_words"] = seo_words

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.seo_word import SeoWord  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _seo_words = d.pop("seo_words", UNSET)
        seo_words: list[SeoWord] | Unset = UNSET
        if _seo_words is not UNSET:
            seo_words = []
            for seo_words_item_data in _seo_words:
                seo_words_item = SeoWord.from_dict(seo_words_item_data)

                seo_words.append(seo_words_item)

        get_products_seo_words_response_data_product = cls(
            id=id,
            seo_words=seo_words,
        )

        get_products_seo_words_response_data_product.additional_properties = d
        return get_products_seo_words_response_data_product

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
