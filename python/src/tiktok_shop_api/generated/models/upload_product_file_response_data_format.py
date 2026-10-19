from enum import StrEnum


class UploadProductFileResponseDataFormat(StrEnum):
    AVI = "AVI"
    FLV = "FLV"
    MKV = "MKV"
    MOV = "MOV"
    MP4 = "MP4"
    MPEG = "MPEG"
    PDF = "PDF"
    VALUE_7 = "3GP"
    WEBM = "WEBM"
    WMV = "WMV"

    def __str__(self) -> str:
        return str(self.value)
