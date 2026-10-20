from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_image_translation_tasks_response_data_translation_task import CreateImageTranslationTasksResponseDataTranslationTask





T = TypeVar("T", bound="CreateImageTranslationTasksResponseData")



@_attrs_define
class CreateImageTranslationTasksResponseData:
    """ 
        Attributes:
            translation_tasks (list[CreateImageTranslationTasksResponseDataTranslationTask] | Unset): The list of
                translation tasks created for the requested images.

                Each task corresponds to the translation of 1 image into 1 target language. So if you specified 2 target
                languages for an image, 2 tasks will be created.
     """

    translation_tasks: list[CreateImageTranslationTasksResponseDataTranslationTask] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_image_translation_tasks_response_data_translation_task import CreateImageTranslationTasksResponseDataTranslationTask # noqa: PLC0415
        translation_tasks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.translation_tasks, Unset):
            translation_tasks = []
            for translation_tasks_item_data in self.translation_tasks:
                translation_tasks_item = translation_tasks_item_data.to_dict()
                translation_tasks.append(translation_tasks_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if translation_tasks is not UNSET:
            field_dict["translation_tasks"] = translation_tasks

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_image_translation_tasks_response_data_translation_task import CreateImageTranslationTasksResponseDataTranslationTask # noqa: PLC0415
        d = dict(src_dict)
        _translation_tasks = d.pop("translation_tasks", UNSET)
        translation_tasks: list[CreateImageTranslationTasksResponseDataTranslationTask] | Unset = UNSET
        if _translation_tasks is not UNSET:
            translation_tasks = []
            for translation_tasks_item_data in _translation_tasks:
                translation_tasks_item = CreateImageTranslationTasksResponseDataTranslationTask.from_dict(translation_tasks_item_data)



                translation_tasks.append(translation_tasks_item)


        create_image_translation_tasks_response_data = cls(
            translation_tasks=translation_tasks,
        )


        create_image_translation_tasks_response_data.additional_properties = d
        return create_image_translation_tasks_response_data

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
