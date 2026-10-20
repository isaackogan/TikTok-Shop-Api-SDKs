from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.check_listing_prerequisites_response_data_check_result import CheckListingPrerequisitesResponseDataCheckResult





T = TypeVar("T", bound="CheckListingPrerequisitesResponseData")



@_attrs_define
class CheckListingPrerequisitesResponseData:
    """ 
        Attributes:
            check_results (list[CheckListingPrerequisitesResponseDataCheckResult] | Unset): A list of results from checking
                whether a shop satisfies TikTok Shop requirements.
     """

    check_results: list[CheckListingPrerequisitesResponseDataCheckResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.check_listing_prerequisites_response_data_check_result import CheckListingPrerequisitesResponseDataCheckResult # noqa: PLC0415
        check_results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.check_results, Unset):
            check_results = []
            for check_results_item_data in self.check_results:
                check_results_item = check_results_item_data.to_dict()
                check_results.append(check_results_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if check_results is not UNSET:
            field_dict["check_results"] = check_results

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_listing_prerequisites_response_data_check_result import CheckListingPrerequisitesResponseDataCheckResult # noqa: PLC0415
        d = dict(src_dict)
        _check_results = d.pop("check_results", UNSET)
        check_results: list[CheckListingPrerequisitesResponseDataCheckResult] | Unset = UNSET
        if _check_results is not UNSET:
            check_results = []
            for check_results_item_data in _check_results:
                check_results_item = CheckListingPrerequisitesResponseDataCheckResult.from_dict(check_results_item_data)



                check_results.append(check_results_item)


        check_listing_prerequisites_response_data = cls(
            check_results=check_results,
        )


        check_listing_prerequisites_response_data.additional_properties = d
        return check_listing_prerequisites_response_data

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
