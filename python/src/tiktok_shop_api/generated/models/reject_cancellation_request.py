from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reject_cancellation_request_image import RejectCancellationRequestImage


T = TypeVar("T", bound="RejectCancellationRequest")


@_attrs_define
class RejectCancellationRequest:
    """
    Attributes:
        reject_reason (str): Seller's reason for rejecting the buyer's order cancellation request. Use the [Get Decision
            Eligibility](https://partner.tiktokshop.com/docv2/page/69844a11eeba77049695c7f6) endpoint to retrieve the
            currently available rejection reasons for the same cancellation request, and submit the returned rejection
            reason name in this field.
        comment (str | Unset): Seller's comment on rejection decision. This is where a seller will provide more
            information about rejecting the request.
        images (list[RejectCancellationRequestImage] | Unset): List of images provided by the seller to support seller's
            decision to reject the order cancellation request.
    """

    reject_reason: str
    comment: str | Unset = UNSET
    images: list[RejectCancellationRequestImage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reject_reason = self.reject_reason

        comment = self.comment

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reject_reason": reject_reason,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reject_cancellation_request_image import RejectCancellationRequestImage  # noqa: PLC0415

        d = dict(src_dict)
        reject_reason = d.pop("reject_reason")

        comment = d.pop("comment", UNSET)

        _images = d.pop("images", UNSET)
        images: list[RejectCancellationRequestImage] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = RejectCancellationRequestImage.from_dict(images_item_data)

                images.append(images_item)

        reject_cancellation_request = cls(
            reject_reason=reject_reason,
            comment=comment,
            images=images,
        )

        reject_cancellation_request.additional_properties = d
        return reject_cancellation_request

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
