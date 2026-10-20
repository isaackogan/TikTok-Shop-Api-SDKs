from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_return_records_response_data_record_image import GetReturnRecordsResponseDataRecordImage
  from ..models.get_return_records_response_data_record_video import GetReturnRecordsResponseDataRecordVideo





T = TypeVar("T", bound="GetReturnRecordsResponseDataRecord")



@_attrs_define
class GetReturnRecordsResponseDataRecord:
    """ 
        Attributes:
            event (str | Unset): The event type that represents which lifecycle event this record describes. It can vary
                depending on the current status and the return flow of the request, including the initial request, seller
                actions, shipment events, and timeout or system events.
            role (str | Unset): The actor that initiated this lifecycle event. Possible values:
                - `BUYER`
                - `SELLER`
                - `OPERATOR`: The action was triggered manually by a customer service agent.
                - `SYSTEM`: The action was triggered automatically due to a policy reason.
            description (str | Unset): A human-readable description of this lifecycle event.
            reason_text (str | Unset): The corresponding text for a return reason, localized based on the locale input
                parameter.
            note (str | Unset): A note associated with the return record. Use role to identify the actor for the event.
            images (list[GetReturnRecordsResponseDataRecordImage] | Unset): Images provided by the seller or buyer. You can
                use the role field to differentiate whether the images are from the seller or buyer.
            videos (list[GetReturnRecordsResponseDataRecordVideo] | Unset): Videos uploaded by the buyer. Only buyers are
                allowed to upload videos.
            create_time (int | Unset): The Unix timestamp, in seconds, when this record entry was created.
     """

    event: str | Unset = UNSET
    role: str | Unset = UNSET
    description: str | Unset = UNSET
    reason_text: str | Unset = UNSET
    note: str | Unset = UNSET
    images: list[GetReturnRecordsResponseDataRecordImage] | Unset = UNSET
    videos: list[GetReturnRecordsResponseDataRecordVideo] | Unset = UNSET
    create_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_return_records_response_data_record_image import GetReturnRecordsResponseDataRecordImage # noqa: PLC0415
        from ..models.get_return_records_response_data_record_video import GetReturnRecordsResponseDataRecordVideo # noqa: PLC0415
        event = self.event

        role = self.role

        description = self.description

        reason_text = self.reason_text

        note = self.note

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)



        videos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.videos, Unset):
            videos = []
            for videos_item_data in self.videos:
                videos_item = videos_item_data.to_dict()
                videos.append(videos_item)



        create_time = self.create_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if event is not UNSET:
            field_dict["event"] = event
        if role is not UNSET:
            field_dict["role"] = role
        if description is not UNSET:
            field_dict["description"] = description
        if reason_text is not UNSET:
            field_dict["reason_text"] = reason_text
        if note is not UNSET:
            field_dict["note"] = note
        if images is not UNSET:
            field_dict["images"] = images
        if videos is not UNSET:
            field_dict["videos"] = videos
        if create_time is not UNSET:
            field_dict["create_time"] = create_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_return_records_response_data_record_image import GetReturnRecordsResponseDataRecordImage # noqa: PLC0415
        from ..models.get_return_records_response_data_record_video import GetReturnRecordsResponseDataRecordVideo # noqa: PLC0415
        d = dict(src_dict)
        event = d.pop("event", UNSET)

        role = d.pop("role", UNSET)

        description = d.pop("description", UNSET)

        reason_text = d.pop("reason_text", UNSET)

        note = d.pop("note", UNSET)

        _images = d.pop("images", UNSET)
        images: list[GetReturnRecordsResponseDataRecordImage] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = GetReturnRecordsResponseDataRecordImage.from_dict(images_item_data)



                images.append(images_item)


        _videos = d.pop("videos", UNSET)
        videos: list[GetReturnRecordsResponseDataRecordVideo] | Unset = UNSET
        if _videos is not UNSET:
            videos = []
            for videos_item_data in _videos:
                videos_item = GetReturnRecordsResponseDataRecordVideo.from_dict(videos_item_data)



                videos.append(videos_item)


        create_time = d.pop("create_time", UNSET)

        get_return_records_response_data_record = cls(
            event=event,
            role=role,
            description=description,
            reason_text=reason_text,
            note=note,
            images=images,
            videos=videos,
            create_time=create_time,
        )


        get_return_records_response_data_record.additional_properties = d
        return get_return_records_response_data_record

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
