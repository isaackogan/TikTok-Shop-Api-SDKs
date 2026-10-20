from enum import StrEnum


class PrintInboundOrderLabelsRequestPrintItemsItem(StrEnum):
    CARTON_PALLET_LABEL = "CARTON_PALLET_LABEL"
    FBT_BARCODE = "FBT_BARCODE"
    PACKING_PICKING_LIST = "PACKING_PICKING_LIST"

    def __str__(self) -> str:
        return str(self.value)
