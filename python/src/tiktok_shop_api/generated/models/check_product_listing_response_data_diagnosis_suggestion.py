from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_product_listing_response_data_diagnosis_suggestion_image import (
        CheckProductListingResponseDataDiagnosisSuggestionImage,
    )
    from ..models.seo_word import SeoWord
    from ..models.smart_text import SmartText


T = TypeVar("T", bound="CheckProductListingResponseDataDiagnosisSuggestion")


@_attrs_define
class CheckProductListingResponseDataDiagnosisSuggestion:
    """
    Attributes:
        seo_words (list[SeoWord] | Unset): The SEO keyword suggestions if `diagnoses.field` is "TITLE".
        smart_texts (list[SmartText] | Unset): The intelligent text suggestions for titles and descriptions.
        images (list[CheckProductListingResponseDataDiagnosisSuggestionImage] | Unset): The optimized main image. Only
            the first image in the main image set will be optimized.
    """

    seo_words: list[SeoWord] | Unset = UNSET
    smart_texts: list[SmartText] | Unset = UNSET
    images: list[CheckProductListingResponseDataDiagnosisSuggestionImage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        seo_words: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.seo_words, Unset):
            seo_words = []
            for seo_words_item_data in self.seo_words:
                seo_words_item = seo_words_item_data.to_dict()
                seo_words.append(seo_words_item)

        smart_texts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.smart_texts, Unset):
            smart_texts = []
            for smart_texts_item_data in self.smart_texts:
                smart_texts_item = smart_texts_item_data.to_dict()
                smart_texts.append(smart_texts_item)

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if seo_words is not UNSET:
            field_dict["seo_words"] = seo_words
        if smart_texts is not UNSET:
            field_dict["smart_texts"] = smart_texts
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_product_listing_response_data_diagnosis_suggestion_image import (
            CheckProductListingResponseDataDiagnosisSuggestionImage,  # noqa: PLC0415
        )
        from ..models.seo_word import SeoWord  # noqa: PLC0415
        from ..models.smart_text import SmartText  # noqa: PLC0415

        d = dict(src_dict)
        _seo_words = d.pop("seo_words", UNSET)
        seo_words: list[SeoWord] | Unset = UNSET
        if _seo_words is not UNSET:
            seo_words = []
            for seo_words_item_data in _seo_words:
                seo_words_item = SeoWord.from_dict(seo_words_item_data)

                seo_words.append(seo_words_item)

        _smart_texts = d.pop("smart_texts", UNSET)
        smart_texts: list[SmartText] | Unset = UNSET
        if _smart_texts is not UNSET:
            smart_texts = []
            for smart_texts_item_data in _smart_texts:
                smart_texts_item = SmartText.from_dict(smart_texts_item_data)

                smart_texts.append(smart_texts_item)

        _images = d.pop("images", UNSET)
        images: list[CheckProductListingResponseDataDiagnosisSuggestionImage] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = CheckProductListingResponseDataDiagnosisSuggestionImage.from_dict(images_item_data)

                images.append(images_item)

        check_product_listing_response_data_diagnosis_suggestion = cls(
            seo_words=seo_words,
            smart_texts=smart_texts,
            images=images,
        )

        check_product_listing_response_data_diagnosis_suggestion.additional_properties = d
        return check_product_listing_response_data_diagnosis_suggestion

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
