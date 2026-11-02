from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.metric import Metric





T = TypeVar("T", bound="GetACCLIVESalesFactorsResponseDataFactor")



@_attrs_define
class GetACCLIVESalesFactorsResponseDataFactor:
    """ 
        Attributes:
            factor_id (str | Unset): Stable LIVE factor identifier, such as label1. Pass this value unchanged as factor_id
                when filtering LIVE in Get ACC Audience Preference List; do not pass factor_name.
            factor_name (str | Unset): Localized display name of the LIVE factor, when available. Use factor_id, rather than
                this display name, when filtering LIVE preferences.
            metrics (Metric | Unset):
     """

    factor_id: str | Unset = UNSET
    factor_name: str | Unset = UNSET
    metrics: Metric | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.metric import Metric # noqa: PLC0415
        factor_id = self.factor_id

        factor_name = self.factor_name

        metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if factor_id is not UNSET:
            field_dict["factor_id"] = factor_id
        if factor_name is not UNSET:
            field_dict["factor_name"] = factor_name
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metric import Metric # noqa: PLC0415
        d = dict(src_dict)
        factor_id = d.pop("factor_id", UNSET)

        factor_name = d.pop("factor_name", UNSET)

        _metrics = d.pop("metrics", UNSET)
        metrics: Metric | Unset
        if isinstance(_metrics,  Unset):
            metrics = UNSET
        else:
            metrics = Metric.from_dict(_metrics)




        get_acclive_sales_factors_response_data_factor = cls(
            factor_id=factor_id,
            factor_name=factor_name,
            metrics=metrics,
        )


        get_acclive_sales_factors_response_data_factor.additional_properties = d
        return get_acclive_sales_factors_response_data_factor

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
