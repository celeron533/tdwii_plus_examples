from typing import Any, List, Optional  # noqa

import pydicom


class ReferencedRTPrescriptionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedRTPrescriptionIndex(self) -> Optional[int]:
        if "ReferencedRTPrescriptionIndex" in self._dataset:
            return self._dataset.ReferencedRTPrescriptionIndex
        return None

    @ReferencedRTPrescriptionIndex.setter
    def ReferencedRTPrescriptionIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedRTPrescriptionIndex" in self._dataset:
                del self._dataset.ReferencedRTPrescriptionIndex
        else:
            self._dataset.ReferencedRTPrescriptionIndex = value