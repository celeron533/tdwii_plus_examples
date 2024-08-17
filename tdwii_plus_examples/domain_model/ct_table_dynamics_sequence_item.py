from typing import Any, List, Optional  # noqa

import pydicom


class CTTableDynamicsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def TableSpeed(self) -> Optional[float]:
        if "TableSpeed" in self._dataset:
            return self._dataset.TableSpeed
        return None

    @TableSpeed.setter
    def TableSpeed(self, value: Optional[float]):
        if value is None:
            if "TableSpeed" in self._dataset:
                del self._dataset.TableSpeed
        else:
            self._dataset.TableSpeed = value

    @property
    def TableFeedPerRotation(self) -> Optional[float]:
        if "TableFeedPerRotation" in self._dataset:
            return self._dataset.TableFeedPerRotation
        return None

    @TableFeedPerRotation.setter
    def TableFeedPerRotation(self, value: Optional[float]):
        if value is None:
            if "TableFeedPerRotation" in self._dataset:
                del self._dataset.TableFeedPerRotation
        else:
            self._dataset.TableFeedPerRotation = value

    @property
    def SpiralPitchFactor(self) -> Optional[float]:
        if "SpiralPitchFactor" in self._dataset:
            return self._dataset.SpiralPitchFactor
        return None

    @SpiralPitchFactor.setter
    def SpiralPitchFactor(self, value: Optional[float]):
        if value is None:
            if "SpiralPitchFactor" in self._dataset:
                del self._dataset.SpiralPitchFactor
        else:
            self._dataset.SpiralPitchFactor = value
