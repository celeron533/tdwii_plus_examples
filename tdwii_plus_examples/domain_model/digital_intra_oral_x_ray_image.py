from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .acquisition_context_sequence_item import AcquisitionContextSequenceItem
from .alternate_container_identifier_sequence_item import (
    AlternateContainerIdentifierSequenceItem,
)
from .anatomic_region_sequence_item import AnatomicRegionSequenceItem
from .breed_registration_sequence_item import BreedRegistrationSequenceItem
from .code_sequence_item import CodeSequenceItem
from .coding_scheme_identification_sequence_item import (
    CodingSchemeIdentificationSequenceItem,
)
from .consent_for_clinical_trial_use_sequence_item import (
    ConsentForClinicalTrialUseSequenceItem,
)
from .consulting_physician_identification_sequence_item import (
    ConsultingPhysicianIdentificationSequenceItem,
)
from .container_component_sequence_item import ContainerComponentSequenceItem
from .context_group_identification_sequence_item import (
    ContextGroupIdentificationSequenceItem,
)
from .contrast_bolus_administration_route_sequence_item import (
    ContrastBolusAdministrationRouteSequenceItem,
)
from .contrast_bolus_agent_sequence_item import ContrastBolusAgentSequenceItem
from .contributing_equipment_sequence_item import ContributingEquipmentSequenceItem
from .conversion_source_attributes_sequence_item import (
    ConversionSourceAttributesSequenceItem,
)
from .device_sequence_item import DeviceSequenceItem
from .digital_signatures_sequence_item import DigitalSignaturesSequenceItem
from .encrypted_attributes_sequence_item import EncryptedAttributesSequenceItem
from .genetic_modifications_sequence_item import GeneticModificationsSequenceItem
from .group_of_patients_identification_sequence_item import (
    GroupOfPatientsIdentificationSequenceItem,
)
from .histogram_sequence_item import HistogramSequenceItem
from .hl7_structured_document_reference_sequence_item import (
    HL7StructuredDocumentReferenceSequenceItem,
)
from .icon_image_sequence_item import IconImageSequenceItem
from .intervention_sequence_item import InterventionSequenceItem
from .issuer_of_accession_number_sequence_item import (
    IssuerOfAccessionNumberSequenceItem,
)
from .issuer_of_admission_id_sequence_item import IssuerOfAdmissionIDSequenceItem
from .issuer_of_patient_id_qualifiers_sequence_item import (
    IssuerOfPatientIDQualifiersSequenceItem,
)
from .issuer_of_service_episode_id_sequence_item import (
    IssuerOfServiceEpisodeIDSequenceItem,
)
from .issuer_of_the_container_identifier_sequence_item import (
    IssuerOfTheContainerIdentifierSequenceItem,
)
from .mac_parameters_sequence_item import MACParametersSequenceItem
from .mapping_resource_identification_sequence_item import (
    MappingResourceIdentificationSequenceItem,
)
from .operator_identification_sequence_item import OperatorIdentificationSequenceItem
from .original_attributes_sequence_item import OriginalAttributesSequenceItem
from .other_clinical_trial_protocol_i_ds_sequence_item import (
    OtherClinicalTrialProtocolIDsSequenceItem,
)
from .other_patient_i_ds_sequence_item import OtherPatientIDsSequenceItem
from .performing_physician_identification_sequence_item import (
    PerformingPhysicianIdentificationSequenceItem,
)
from .physicians_of_record_identification_sequence_item import (
    PhysiciansOfRecordIdentificationSequenceItem,
)
from .physicians_reading_study_identification_sequence_item import (
    PhysiciansReadingStudyIdentificationSequenceItem,
)
from .primary_anatomic_structure_sequence_item import (
    PrimaryAnatomicStructureSequenceItem,
)
from .private_data_element_characteristics_sequence_item import (
    PrivateDataElementCharacteristicsSequenceItem,
)
from .real_world_value_mapping_sequence_item import RealWorldValueMappingSequenceItem
from .referenced_defined_protocol_sequence_item import (
    ReferencedDefinedProtocolSequenceItem,
)
from .referenced_image_sequence_item import ReferencedImageSequenceItem
from .referenced_instance_sequence_item import ReferencedInstanceSequenceItem
from .referenced_patient_photo_sequence_item import ReferencedPatientPhotoSequenceItem
from .referenced_patient_sequence_item import ReferencedPatientSequenceItem
from .referenced_performed_procedure_step_sequence_item import (
    ReferencedPerformedProcedureStepSequenceItem,
)
from .referenced_performed_protocol_sequence_item import (
    ReferencedPerformedProtocolSequenceItem,
)
from .referenced_series_sequence_item import ReferencedSeriesSequenceItem
from .referenced_study_sequence_item import ReferencedStudySequenceItem
from .referring_physician_identification_sequence_item import (
    ReferringPhysicianIdentificationSequenceItem,
)
from .related_series_sequence_item import RelatedSeriesSequenceItem
from .request_attributes_sequence_item import RequestAttributesSequenceItem
from .source_image_sequence_item import SourceImageSequenceItem
from .source_instance_sequence_item import SourceInstanceSequenceItem
from .source_patient_group_identification_sequence_item import (
    SourcePatientGroupIdentificationSequenceItem,
)
from .specimen_description_sequence_item import SpecimenDescriptionSequenceItem
from .strain_stock_sequence_item import StrainStockSequenceItem
from .studies_containing_other_referenced_instances_sequence_item import (
    StudiesContainingOtherReferencedInstancesSequenceItem,
)
from .udi_sequence_item import UDISequenceItem
from .voilut_sequence_item import VOILUTSequenceItem


class DigitalIntraOralXRayImage:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._IssuerOfTheContainerIdentifierSequence: List[IssuerOfTheContainerIdentifierSequenceItem] = []
        self._AlternateContainerIdentifierSequence: List[AlternateContainerIdentifierSequenceItem] = []
        self._ContainerTypeCodeSequence: List[CodeSequenceItem] = []
        self._ContainerComponentSequence: List[ContainerComponentSequenceItem] = []
        self._SpecimenDescriptionSequence: List[SpecimenDescriptionSequenceItem] = []
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._ReferencedInstanceSequence: List[ReferencedInstanceSequenceItem] = []
        self._SourceImageSequence: List[SourceImageSequenceItem] = []
        self._DerivationCodeSequence: List[CodeSequenceItem] = []
        self._SourceInstanceSequence: List[SourceInstanceSequenceItem] = []
        self._ReferencedPerformedProcedureStepSequence: List[ReferencedPerformedProcedureStepSequenceItem] = []
        self._ContrastBolusAgentSequence: List[ContrastBolusAgentSequenceItem] = []
        self._ContrastBolusAdministrationRouteSequence: List[ContrastBolusAdministrationRouteSequenceItem] = []
        self._ReferencedSeriesSequence: List[ReferencedSeriesSequenceItem] = []
        self._StudiesContainingOtherReferencedInstancesSequence: List[
            StudiesContainingOtherReferencedInstancesSequenceItem
        ] = []
        self._InstitutionalDepartmentTypeCodeSequence: List[CodeSequenceItem] = []
        self._UDISequence: List[UDISequenceItem] = []
        self._IssuerOfAccessionNumberSequence: List[IssuerOfAccessionNumberSequenceItem] = []
        self._ReferringPhysicianIdentificationSequence: List[ReferringPhysicianIdentificationSequenceItem] = []
        self._ConsultingPhysicianIdentificationSequence: List[ConsultingPhysicianIdentificationSequenceItem] = []
        self._ProcedureCodeSequence: List[CodeSequenceItem] = []
        self._PhysiciansOfRecordIdentificationSequence: List[PhysiciansOfRecordIdentificationSequenceItem] = []
        self._PhysiciansReadingStudyIdentificationSequence: List[PhysiciansReadingStudyIdentificationSequenceItem] = []
        self._ReferencedStudySequence: List[ReferencedStudySequenceItem] = []
        self._RequestingServiceCodeSequence: List[CodeSequenceItem] = []
        self._ReasonForPerformedProcedureCodeSequence: List[CodeSequenceItem] = []
        self._AnatomicRegionSequence: List[AnatomicRegionSequenceItem] = []
        self._PrimaryAnatomicStructureSequence: List[PrimaryAnatomicStructureSequenceItem] = []
        self._HistogramSequence: List[HistogramSequenceItem] = []
        self._AcquisitionContextSequence: List[AcquisitionContextSequenceItem] = []
        self._AnatomicRegionSequence: List[AnatomicRegionSequenceItem] = []
        self._PrimaryAnatomicStructureSequence: List[PrimaryAnatomicStructureSequenceItem] = []
        self._RealWorldValueMappingSequence: List[RealWorldValueMappingSequenceItem] = []
        self._IconImageSequence: List[IconImageSequenceItem] = []
        self._AnatomicRegionSequence: List[AnatomicRegionSequenceItem] = []
        self._PrimaryAnatomicStructureSequence: List[PrimaryAnatomicStructureSequenceItem] = []
        self._AdmittingDiagnosesCodeSequence: List[CodeSequenceItem] = []
        self._PatientSizeCodeSequence: List[CodeSequenceItem] = []
        self._ReasonForVisitCodeSequence: List[CodeSequenceItem] = []
        self._IssuerOfAdmissionIDSequence: List[IssuerOfAdmissionIDSequenceItem] = []
        self._IssuerOfServiceEpisodeIDSequence: List[IssuerOfServiceEpisodeIDSequenceItem] = []
        self._InterventionSequence: List[InterventionSequenceItem] = []
        self._VOILUTSequence: List[VOILUTSequenceItem] = []
        self._ReferencedPatientSequence: List[ReferencedPatientSequenceItem] = []
        self._IssuerOfPatientIDQualifiersSequence: List[IssuerOfPatientIDQualifiersSequenceItem] = []
        self._SourcePatientGroupIdentificationSequence: List[SourcePatientGroupIdentificationSequenceItem] = []
        self._GroupOfPatientsIdentificationSequence: List[GroupOfPatientsIdentificationSequenceItem] = []
        self._StrainStockSequence: List[StrainStockSequenceItem] = []
        self._StrainCodeSequence: List[CodeSequenceItem] = []
        self._GeneticModificationsSequence: List[GeneticModificationsSequenceItem] = []
        self._OtherPatientIDsSequence: List[OtherPatientIDsSequenceItem] = []
        self._ReferencedPatientPhotoSequence: List[ReferencedPatientPhotoSequenceItem] = []
        self._PatientSpeciesCodeSequence: List[CodeSequenceItem] = []
        self._PatientBreedCodeSequence: List[CodeSequenceItem] = []
        self._BreedRegistrationSequence: List[BreedRegistrationSequenceItem] = []
        self._DeidentificationMethodCodeSequence: List[CodeSequenceItem] = []
        self._ProjectionEponymousNameCodeSequence: List[CodeSequenceItem] = []
        self._ViewCodeSequence: List[CodeSequenceItem] = []
        self._PatientOrientationCodeSequence: List[CodeSequenceItem] = []
        self._PatientGantryRelationshipCodeSequence: List[CodeSequenceItem] = []
        self._OtherClinicalTrialProtocolIDsSequence: List[OtherClinicalTrialProtocolIDsSequenceItem] = []
        self._CodingSchemeIdentificationSequence: List[CodingSchemeIdentificationSequenceItem] = []
        self._ContextGroupIdentificationSequence: List[ContextGroupIdentificationSequenceItem] = []
        self._MappingResourceIdentificationSequence: List[MappingResourceIdentificationSequenceItem] = []
        self._PrivateDataElementCharacteristicsSequence: List[PrivateDataElementCharacteristicsSequenceItem] = []
        self._ReferencedDefinedProtocolSequence: List[ReferencedDefinedProtocolSequenceItem] = []
        self._ReferencedPerformedProtocolSequence: List[ReferencedPerformedProtocolSequenceItem] = []
        self._ContributingEquipmentSequence: List[ContributingEquipmentSequenceItem] = []
        self._ConversionSourceAttributesSequence: List[ConversionSourceAttributesSequenceItem] = []
        self._HL7StructuredDocumentReferenceSequence: List[HL7StructuredDocumentReferenceSequenceItem] = []
        self._EncryptedAttributesSequence: List[EncryptedAttributesSequenceItem] = []
        self._OriginalAttributesSequence: List[OriginalAttributesSequenceItem] = []
        self._MACParametersSequence: List[MACParametersSequenceItem] = []
        self._DigitalSignaturesSequence: List[DigitalSignaturesSequenceItem] = []
        self._DeviceSequence: List[DeviceSequenceItem] = []
        self._SeriesDescriptionCodeSequence: List[CodeSequenceItem] = []
        self._PerformingPhysicianIdentificationSequence: List[PerformingPhysicianIdentificationSequenceItem] = []
        self._OperatorIdentificationSequence: List[OperatorIdentificationSequenceItem] = []
        self._ReferencedPerformedProcedureStepSequence: List[ReferencedPerformedProcedureStepSequenceItem] = []
        self._RelatedSeriesSequence: List[RelatedSeriesSequenceItem] = []
        self._PerformedProtocolCodeSequence: List[CodeSequenceItem] = []
        self._RequestAttributesSequence: List[RequestAttributesSequenceItem] = []
        self._VOILUTSequence: List[VOILUTSequenceItem] = []
        self._ClinicalTrialTimePointTypeCodeSequence: List[CodeSequenceItem] = []
        self._ConsentForClinicalTrialUseSequence: List[ConsentForClinicalTrialUseSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def PlateID(self) -> Optional[str]:
        if "PlateID" in self._dataset:
            return self._dataset.PlateID
        return None

    @PlateID.setter
    def PlateID(self, value: Optional[str]):
        if value is None:
            if "PlateID" in self._dataset:
                del self._dataset.PlateID
        else:
            self._dataset.PlateID = value

    @property
    def CassetteID(self) -> Optional[str]:
        if "CassetteID" in self._dataset:
            return self._dataset.CassetteID
        return None

    @CassetteID.setter
    def CassetteID(self, value: Optional[str]):
        if value is None:
            if "CassetteID" in self._dataset:
                del self._dataset.CassetteID
        else:
            self._dataset.CassetteID = value

    @property
    def FieldOfViewShape(self) -> Optional[str]:
        if "FieldOfViewShape" in self._dataset:
            return self._dataset.FieldOfViewShape
        return None

    @FieldOfViewShape.setter
    def FieldOfViewShape(self, value: Optional[str]):
        if value is None:
            if "FieldOfViewShape" in self._dataset:
                del self._dataset.FieldOfViewShape
        else:
            self._dataset.FieldOfViewShape = value

    @property
    def FieldOfViewDimensions(self) -> Optional[List[int]]:
        if "FieldOfViewDimensions" in self._dataset:
            return self._dataset.FieldOfViewDimensions
        return None

    @FieldOfViewDimensions.setter
    def FieldOfViewDimensions(self, value: Optional[List[int]]):
        if value is None:
            if "FieldOfViewDimensions" in self._dataset:
                del self._dataset.FieldOfViewDimensions
        else:
            self._dataset.FieldOfViewDimensions = value

    @property
    def ImagerPixelSpacing(self) -> Optional[List[Decimal]]:
        if "ImagerPixelSpacing" in self._dataset:
            return self._dataset.ImagerPixelSpacing
        return None

    @ImagerPixelSpacing.setter
    def ImagerPixelSpacing(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ImagerPixelSpacing" in self._dataset:
                del self._dataset.ImagerPixelSpacing
        else:
            self._dataset.ImagerPixelSpacing = value

    @property
    def ExposureIndex(self) -> Optional[Decimal]:
        if "ExposureIndex" in self._dataset:
            return self._dataset.ExposureIndex
        return None

    @ExposureIndex.setter
    def ExposureIndex(self, value: Optional[Decimal]):
        if value is None:
            if "ExposureIndex" in self._dataset:
                del self._dataset.ExposureIndex
        else:
            self._dataset.ExposureIndex = value

    @property
    def TargetExposureIndex(self) -> Optional[Decimal]:
        if "TargetExposureIndex" in self._dataset:
            return self._dataset.TargetExposureIndex
        return None

    @TargetExposureIndex.setter
    def TargetExposureIndex(self, value: Optional[Decimal]):
        if value is None:
            if "TargetExposureIndex" in self._dataset:
                del self._dataset.TargetExposureIndex
        else:
            self._dataset.TargetExposureIndex = value

    @property
    def DeviationIndex(self) -> Optional[Decimal]:
        if "DeviationIndex" in self._dataset:
            return self._dataset.DeviationIndex
        return None

    @DeviationIndex.setter
    def DeviationIndex(self, value: Optional[Decimal]):
        if value is None:
            if "DeviationIndex" in self._dataset:
                del self._dataset.DeviationIndex
        else:
            self._dataset.DeviationIndex = value

    @property
    def Sensitivity(self) -> Optional[Decimal]:
        if "Sensitivity" in self._dataset:
            return self._dataset.Sensitivity
        return None

    @Sensitivity.setter
    def Sensitivity(self, value: Optional[Decimal]):
        if value is None:
            if "Sensitivity" in self._dataset:
                del self._dataset.Sensitivity
        else:
            self._dataset.Sensitivity = value

    @property
    def DetectorConditionsNominalFlag(self) -> Optional[str]:
        if "DetectorConditionsNominalFlag" in self._dataset:
            return self._dataset.DetectorConditionsNominalFlag
        return None

    @DetectorConditionsNominalFlag.setter
    def DetectorConditionsNominalFlag(self, value: Optional[str]):
        if value is None:
            if "DetectorConditionsNominalFlag" in self._dataset:
                del self._dataset.DetectorConditionsNominalFlag
        else:
            self._dataset.DetectorConditionsNominalFlag = value

    @property
    def DetectorTemperature(self) -> Optional[Decimal]:
        if "DetectorTemperature" in self._dataset:
            return self._dataset.DetectorTemperature
        return None

    @DetectorTemperature.setter
    def DetectorTemperature(self, value: Optional[Decimal]):
        if value is None:
            if "DetectorTemperature" in self._dataset:
                del self._dataset.DetectorTemperature
        else:
            self._dataset.DetectorTemperature = value

    @property
    def DetectorType(self) -> Optional[str]:
        if "DetectorType" in self._dataset:
            return self._dataset.DetectorType
        return None

    @DetectorType.setter
    def DetectorType(self, value: Optional[str]):
        if value is None:
            if "DetectorType" in self._dataset:
                del self._dataset.DetectorType
        else:
            self._dataset.DetectorType = value

    @property
    def DetectorConfiguration(self) -> Optional[str]:
        if "DetectorConfiguration" in self._dataset:
            return self._dataset.DetectorConfiguration
        return None

    @DetectorConfiguration.setter
    def DetectorConfiguration(self, value: Optional[str]):
        if value is None:
            if "DetectorConfiguration" in self._dataset:
                del self._dataset.DetectorConfiguration
        else:
            self._dataset.DetectorConfiguration = value

    @property
    def DetectorDescription(self) -> Optional[str]:
        if "DetectorDescription" in self._dataset:
            return self._dataset.DetectorDescription
        return None

    @DetectorDescription.setter
    def DetectorDescription(self, value: Optional[str]):
        if value is None:
            if "DetectorDescription" in self._dataset:
                del self._dataset.DetectorDescription
        else:
            self._dataset.DetectorDescription = value

    @property
    def DetectorMode(self) -> Optional[str]:
        if "DetectorMode" in self._dataset:
            return self._dataset.DetectorMode
        return None

    @DetectorMode.setter
    def DetectorMode(self, value: Optional[str]):
        if value is None:
            if "DetectorMode" in self._dataset:
                del self._dataset.DetectorMode
        else:
            self._dataset.DetectorMode = value

    @property
    def DetectorID(self) -> Optional[str]:
        if "DetectorID" in self._dataset:
            return self._dataset.DetectorID
        return None

    @DetectorID.setter
    def DetectorID(self, value: Optional[str]):
        if value is None:
            if "DetectorID" in self._dataset:
                del self._dataset.DetectorID
        else:
            self._dataset.DetectorID = value

    @property
    def DateOfLastDetectorCalibration(self) -> Optional[str]:
        if "DateOfLastDetectorCalibration" in self._dataset:
            return self._dataset.DateOfLastDetectorCalibration
        return None

    @DateOfLastDetectorCalibration.setter
    def DateOfLastDetectorCalibration(self, value: Optional[str]):
        if value is None:
            if "DateOfLastDetectorCalibration" in self._dataset:
                del self._dataset.DateOfLastDetectorCalibration
        else:
            self._dataset.DateOfLastDetectorCalibration = value

    @property
    def TimeOfLastDetectorCalibration(self) -> Optional[str]:
        if "TimeOfLastDetectorCalibration" in self._dataset:
            return self._dataset.TimeOfLastDetectorCalibration
        return None

    @TimeOfLastDetectorCalibration.setter
    def TimeOfLastDetectorCalibration(self, value: Optional[str]):
        if value is None:
            if "TimeOfLastDetectorCalibration" in self._dataset:
                del self._dataset.TimeOfLastDetectorCalibration
        else:
            self._dataset.TimeOfLastDetectorCalibration = value

    @property
    def ExposuresOnDetectorSinceLastCalibration(self) -> Optional[int]:
        if "ExposuresOnDetectorSinceLastCalibration" in self._dataset:
            return self._dataset.ExposuresOnDetectorSinceLastCalibration
        return None

    @ExposuresOnDetectorSinceLastCalibration.setter
    def ExposuresOnDetectorSinceLastCalibration(self, value: Optional[int]):
        if value is None:
            if "ExposuresOnDetectorSinceLastCalibration" in self._dataset:
                del self._dataset.ExposuresOnDetectorSinceLastCalibration
        else:
            self._dataset.ExposuresOnDetectorSinceLastCalibration = value

    @property
    def ExposuresOnDetectorSinceManufactured(self) -> Optional[int]:
        if "ExposuresOnDetectorSinceManufactured" in self._dataset:
            return self._dataset.ExposuresOnDetectorSinceManufactured
        return None

    @ExposuresOnDetectorSinceManufactured.setter
    def ExposuresOnDetectorSinceManufactured(self, value: Optional[int]):
        if value is None:
            if "ExposuresOnDetectorSinceManufactured" in self._dataset:
                del self._dataset.ExposuresOnDetectorSinceManufactured
        else:
            self._dataset.ExposuresOnDetectorSinceManufactured = value

    @property
    def DetectorTimeSinceLastExposure(self) -> Optional[Decimal]:
        if "DetectorTimeSinceLastExposure" in self._dataset:
            return self._dataset.DetectorTimeSinceLastExposure
        return None

    @DetectorTimeSinceLastExposure.setter
    def DetectorTimeSinceLastExposure(self, value: Optional[Decimal]):
        if value is None:
            if "DetectorTimeSinceLastExposure" in self._dataset:
                del self._dataset.DetectorTimeSinceLastExposure
        else:
            self._dataset.DetectorTimeSinceLastExposure = value

    @property
    def DetectorActiveTime(self) -> Optional[Decimal]:
        if "DetectorActiveTime" in self._dataset:
            return self._dataset.DetectorActiveTime
        return None

    @DetectorActiveTime.setter
    def DetectorActiveTime(self, value: Optional[Decimal]):
        if value is None:
            if "DetectorActiveTime" in self._dataset:
                del self._dataset.DetectorActiveTime
        else:
            self._dataset.DetectorActiveTime = value

    @property
    def DetectorActivationOffsetFromExposure(self) -> Optional[Decimal]:
        if "DetectorActivationOffsetFromExposure" in self._dataset:
            return self._dataset.DetectorActivationOffsetFromExposure
        return None

    @DetectorActivationOffsetFromExposure.setter
    def DetectorActivationOffsetFromExposure(self, value: Optional[Decimal]):
        if value is None:
            if "DetectorActivationOffsetFromExposure" in self._dataset:
                del self._dataset.DetectorActivationOffsetFromExposure
        else:
            self._dataset.DetectorActivationOffsetFromExposure = value

    @property
    def DetectorBinning(self) -> Optional[List[Decimal]]:
        if "DetectorBinning" in self._dataset:
            return self._dataset.DetectorBinning
        return None

    @DetectorBinning.setter
    def DetectorBinning(self, value: Optional[List[Decimal]]):
        if value is None:
            if "DetectorBinning" in self._dataset:
                del self._dataset.DetectorBinning
        else:
            self._dataset.DetectorBinning = value

    @property
    def DetectorElementPhysicalSize(self) -> Optional[List[Decimal]]:
        if "DetectorElementPhysicalSize" in self._dataset:
            return self._dataset.DetectorElementPhysicalSize
        return None

    @DetectorElementPhysicalSize.setter
    def DetectorElementPhysicalSize(self, value: Optional[List[Decimal]]):
        if value is None:
            if "DetectorElementPhysicalSize" in self._dataset:
                del self._dataset.DetectorElementPhysicalSize
        else:
            self._dataset.DetectorElementPhysicalSize = value

    @property
    def DetectorElementSpacing(self) -> Optional[List[Decimal]]:
        if "DetectorElementSpacing" in self._dataset:
            return self._dataset.DetectorElementSpacing
        return None

    @DetectorElementSpacing.setter
    def DetectorElementSpacing(self, value: Optional[List[Decimal]]):
        if value is None:
            if "DetectorElementSpacing" in self._dataset:
                del self._dataset.DetectorElementSpacing
        else:
            self._dataset.DetectorElementSpacing = value

    @property
    def DetectorActiveShape(self) -> Optional[str]:
        if "DetectorActiveShape" in self._dataset:
            return self._dataset.DetectorActiveShape
        return None

    @DetectorActiveShape.setter
    def DetectorActiveShape(self, value: Optional[str]):
        if value is None:
            if "DetectorActiveShape" in self._dataset:
                del self._dataset.DetectorActiveShape
        else:
            self._dataset.DetectorActiveShape = value

    @property
    def DetectorActiveDimensions(self) -> Optional[List[Decimal]]:
        if "DetectorActiveDimensions" in self._dataset:
            return self._dataset.DetectorActiveDimensions
        return None

    @DetectorActiveDimensions.setter
    def DetectorActiveDimensions(self, value: Optional[List[Decimal]]):
        if value is None:
            if "DetectorActiveDimensions" in self._dataset:
                del self._dataset.DetectorActiveDimensions
        else:
            self._dataset.DetectorActiveDimensions = value

    @property
    def DetectorActiveOrigin(self) -> Optional[List[Decimal]]:
        if "DetectorActiveOrigin" in self._dataset:
            return self._dataset.DetectorActiveOrigin
        return None

    @DetectorActiveOrigin.setter
    def DetectorActiveOrigin(self, value: Optional[List[Decimal]]):
        if value is None:
            if "DetectorActiveOrigin" in self._dataset:
                del self._dataset.DetectorActiveOrigin
        else:
            self._dataset.DetectorActiveOrigin = value

    @property
    def DetectorManufacturerName(self) -> Optional[str]:
        if "DetectorManufacturerName" in self._dataset:
            return self._dataset.DetectorManufacturerName
        return None

    @DetectorManufacturerName.setter
    def DetectorManufacturerName(self, value: Optional[str]):
        if value is None:
            if "DetectorManufacturerName" in self._dataset:
                del self._dataset.DetectorManufacturerName
        else:
            self._dataset.DetectorManufacturerName = value

    @property
    def DetectorManufacturerModelName(self) -> Optional[str]:
        if "DetectorManufacturerModelName" in self._dataset:
            return self._dataset.DetectorManufacturerModelName
        return None

    @DetectorManufacturerModelName.setter
    def DetectorManufacturerModelName(self, value: Optional[str]):
        if value is None:
            if "DetectorManufacturerModelName" in self._dataset:
                del self._dataset.DetectorManufacturerModelName
        else:
            self._dataset.DetectorManufacturerModelName = value

    @property
    def FieldOfViewOrigin(self) -> Optional[List[Decimal]]:
        if "FieldOfViewOrigin" in self._dataset:
            return self._dataset.FieldOfViewOrigin
        return None

    @FieldOfViewOrigin.setter
    def FieldOfViewOrigin(self, value: Optional[List[Decimal]]):
        if value is None:
            if "FieldOfViewOrigin" in self._dataset:
                del self._dataset.FieldOfViewOrigin
        else:
            self._dataset.FieldOfViewOrigin = value

    @property
    def FieldOfViewRotation(self) -> Optional[Decimal]:
        if "FieldOfViewRotation" in self._dataset:
            return self._dataset.FieldOfViewRotation
        return None

    @FieldOfViewRotation.setter
    def FieldOfViewRotation(self, value: Optional[Decimal]):
        if value is None:
            if "FieldOfViewRotation" in self._dataset:
                del self._dataset.FieldOfViewRotation
        else:
            self._dataset.FieldOfViewRotation = value

    @property
    def FieldOfViewHorizontalFlip(self) -> Optional[str]:
        if "FieldOfViewHorizontalFlip" in self._dataset:
            return self._dataset.FieldOfViewHorizontalFlip
        return None

    @FieldOfViewHorizontalFlip.setter
    def FieldOfViewHorizontalFlip(self, value: Optional[str]):
        if value is None:
            if "FieldOfViewHorizontalFlip" in self._dataset:
                del self._dataset.FieldOfViewHorizontalFlip
        else:
            self._dataset.FieldOfViewHorizontalFlip = value

    @property
    def PixelSpacing(self) -> Optional[List[Decimal]]:
        if "PixelSpacing" in self._dataset:
            return self._dataset.PixelSpacing
        return None

    @PixelSpacing.setter
    def PixelSpacing(self, value: Optional[List[Decimal]]):
        if value is None:
            if "PixelSpacing" in self._dataset:
                del self._dataset.PixelSpacing
        else:
            self._dataset.PixelSpacing = value

    @property
    def PixelSpacingCalibrationType(self) -> Optional[str]:
        if "PixelSpacingCalibrationType" in self._dataset:
            return self._dataset.PixelSpacingCalibrationType
        return None

    @PixelSpacingCalibrationType.setter
    def PixelSpacingCalibrationType(self, value: Optional[str]):
        if value is None:
            if "PixelSpacingCalibrationType" in self._dataset:
                del self._dataset.PixelSpacingCalibrationType
        else:
            self._dataset.PixelSpacingCalibrationType = value

    @property
    def PixelSpacingCalibrationDescription(self) -> Optional[str]:
        if "PixelSpacingCalibrationDescription" in self._dataset:
            return self._dataset.PixelSpacingCalibrationDescription
        return None

    @PixelSpacingCalibrationDescription.setter
    def PixelSpacingCalibrationDescription(self, value: Optional[str]):
        if value is None:
            if "PixelSpacingCalibrationDescription" in self._dataset:
                del self._dataset.PixelSpacingCalibrationDescription
        else:
            self._dataset.PixelSpacingCalibrationDescription = value

    @property
    def ContainerIdentifier(self) -> Optional[str]:
        if "ContainerIdentifier" in self._dataset:
            return self._dataset.ContainerIdentifier
        return None

    @ContainerIdentifier.setter
    def ContainerIdentifier(self, value: Optional[str]):
        if value is None:
            if "ContainerIdentifier" in self._dataset:
                del self._dataset.ContainerIdentifier
        else:
            self._dataset.ContainerIdentifier = value

    @property
    def IssuerOfTheContainerIdentifierSequence(self) -> Optional[List[IssuerOfTheContainerIdentifierSequenceItem]]:
        if "IssuerOfTheContainerIdentifierSequence" in self._dataset:
            if len(self._IssuerOfTheContainerIdentifierSequence) == len(self._dataset.IssuerOfTheContainerIdentifierSequence):
                return self._IssuerOfTheContainerIdentifierSequence
            else:
                return [
                    IssuerOfTheContainerIdentifierSequenceItem(x) for x in self._dataset.IssuerOfTheContainerIdentifierSequence
                ]
        return None

    @IssuerOfTheContainerIdentifierSequence.setter
    def IssuerOfTheContainerIdentifierSequence(self, value: Optional[List[IssuerOfTheContainerIdentifierSequenceItem]]):
        if value is None:
            self._IssuerOfTheContainerIdentifierSequence = []
            if "IssuerOfTheContainerIdentifierSequence" in self._dataset:
                del self._dataset.IssuerOfTheContainerIdentifierSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, IssuerOfTheContainerIdentifierSequenceItem) for item in value
        ):
            raise ValueError(
                "IssuerOfTheContainerIdentifierSequence must be a list of IssuerOfTheContainerIdentifierSequenceItem objects"
            )
        else:
            self._IssuerOfTheContainerIdentifierSequence = value
            if "IssuerOfTheContainerIdentifierSequence" not in self._dataset:
                self._dataset.IssuerOfTheContainerIdentifierSequence = pydicom.Sequence()
            self._dataset.IssuerOfTheContainerIdentifierSequence.clear()
            self._dataset.IssuerOfTheContainerIdentifierSequence.extend([item.to_dataset() for item in value])

    def add_IssuerOfTheContainerIdentifier(self, item: IssuerOfTheContainerIdentifierSequenceItem):
        if not isinstance(item, IssuerOfTheContainerIdentifierSequenceItem):
            raise ValueError("Item must be an instance of IssuerOfTheContainerIdentifierSequenceItem")
        self._IssuerOfTheContainerIdentifierSequence.append(item)
        if "IssuerOfTheContainerIdentifierSequence" not in self._dataset:
            self._dataset.IssuerOfTheContainerIdentifierSequence = pydicom.Sequence()
        self._dataset.IssuerOfTheContainerIdentifierSequence.append(item.to_dataset())

    @property
    def AlternateContainerIdentifierSequence(self) -> Optional[List[AlternateContainerIdentifierSequenceItem]]:
        if "AlternateContainerIdentifierSequence" in self._dataset:
            if len(self._AlternateContainerIdentifierSequence) == len(self._dataset.AlternateContainerIdentifierSequence):
                return self._AlternateContainerIdentifierSequence
            else:
                return [
                    AlternateContainerIdentifierSequenceItem(x) for x in self._dataset.AlternateContainerIdentifierSequence
                ]
        return None

    @AlternateContainerIdentifierSequence.setter
    def AlternateContainerIdentifierSequence(self, value: Optional[List[AlternateContainerIdentifierSequenceItem]]):
        if value is None:
            self._AlternateContainerIdentifierSequence = []
            if "AlternateContainerIdentifierSequence" in self._dataset:
                del self._dataset.AlternateContainerIdentifierSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, AlternateContainerIdentifierSequenceItem) for item in value
        ):
            raise ValueError(
                "AlternateContainerIdentifierSequence must be a list of AlternateContainerIdentifierSequenceItem objects"
            )
        else:
            self._AlternateContainerIdentifierSequence = value
            if "AlternateContainerIdentifierSequence" not in self._dataset:
                self._dataset.AlternateContainerIdentifierSequence = pydicom.Sequence()
            self._dataset.AlternateContainerIdentifierSequence.clear()
            self._dataset.AlternateContainerIdentifierSequence.extend([item.to_dataset() for item in value])

    def add_AlternateContainerIdentifier(self, item: AlternateContainerIdentifierSequenceItem):
        if not isinstance(item, AlternateContainerIdentifierSequenceItem):
            raise ValueError("Item must be an instance of AlternateContainerIdentifierSequenceItem")
        self._AlternateContainerIdentifierSequence.append(item)
        if "AlternateContainerIdentifierSequence" not in self._dataset:
            self._dataset.AlternateContainerIdentifierSequence = pydicom.Sequence()
        self._dataset.AlternateContainerIdentifierSequence.append(item.to_dataset())

    @property
    def ContainerTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ContainerTypeCodeSequence" in self._dataset:
            if len(self._ContainerTypeCodeSequence) == len(self._dataset.ContainerTypeCodeSequence):
                return self._ContainerTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ContainerTypeCodeSequence]
        return None

    @ContainerTypeCodeSequence.setter
    def ContainerTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ContainerTypeCodeSequence = []
            if "ContainerTypeCodeSequence" in self._dataset:
                del self._dataset.ContainerTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("ContainerTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ContainerTypeCodeSequence = value
            if "ContainerTypeCodeSequence" not in self._dataset:
                self._dataset.ContainerTypeCodeSequence = pydicom.Sequence()
            self._dataset.ContainerTypeCodeSequence.clear()
            self._dataset.ContainerTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_ContainerTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ContainerTypeCodeSequence.append(item)
        if "ContainerTypeCodeSequence" not in self._dataset:
            self._dataset.ContainerTypeCodeSequence = pydicom.Sequence()
        self._dataset.ContainerTypeCodeSequence.append(item.to_dataset())

    @property
    def ContainerDescription(self) -> Optional[str]:
        if "ContainerDescription" in self._dataset:
            return self._dataset.ContainerDescription
        return None

    @ContainerDescription.setter
    def ContainerDescription(self, value: Optional[str]):
        if value is None:
            if "ContainerDescription" in self._dataset:
                del self._dataset.ContainerDescription
        else:
            self._dataset.ContainerDescription = value

    @property
    def ContainerComponentSequence(self) -> Optional[List[ContainerComponentSequenceItem]]:
        if "ContainerComponentSequence" in self._dataset:
            if len(self._ContainerComponentSequence) == len(self._dataset.ContainerComponentSequence):
                return self._ContainerComponentSequence
            else:
                return [ContainerComponentSequenceItem(x) for x in self._dataset.ContainerComponentSequence]
        return None

    @ContainerComponentSequence.setter
    def ContainerComponentSequence(self, value: Optional[List[ContainerComponentSequenceItem]]):
        if value is None:
            self._ContainerComponentSequence = []
            if "ContainerComponentSequence" in self._dataset:
                del self._dataset.ContainerComponentSequence
        elif not isinstance(value, list) or not all(isinstance(item, ContainerComponentSequenceItem) for item in value):
            raise ValueError("ContainerComponentSequence must be a list of ContainerComponentSequenceItem objects")
        else:
            self._ContainerComponentSequence = value
            if "ContainerComponentSequence" not in self._dataset:
                self._dataset.ContainerComponentSequence = pydicom.Sequence()
            self._dataset.ContainerComponentSequence.clear()
            self._dataset.ContainerComponentSequence.extend([item.to_dataset() for item in value])

    def add_ContainerComponent(self, item: ContainerComponentSequenceItem):
        if not isinstance(item, ContainerComponentSequenceItem):
            raise ValueError("Item must be an instance of ContainerComponentSequenceItem")
        self._ContainerComponentSequence.append(item)
        if "ContainerComponentSequence" not in self._dataset:
            self._dataset.ContainerComponentSequence = pydicom.Sequence()
        self._dataset.ContainerComponentSequence.append(item.to_dataset())

    @property
    def SpecimenDescriptionSequence(self) -> Optional[List[SpecimenDescriptionSequenceItem]]:
        if "SpecimenDescriptionSequence" in self._dataset:
            if len(self._SpecimenDescriptionSequence) == len(self._dataset.SpecimenDescriptionSequence):
                return self._SpecimenDescriptionSequence
            else:
                return [SpecimenDescriptionSequenceItem(x) for x in self._dataset.SpecimenDescriptionSequence]
        return None

    @SpecimenDescriptionSequence.setter
    def SpecimenDescriptionSequence(self, value: Optional[List[SpecimenDescriptionSequenceItem]]):
        if value is None:
            self._SpecimenDescriptionSequence = []
            if "SpecimenDescriptionSequence" in self._dataset:
                del self._dataset.SpecimenDescriptionSequence
        elif not isinstance(value, list) or not all(isinstance(item, SpecimenDescriptionSequenceItem) for item in value):
            raise ValueError("SpecimenDescriptionSequence must be a list of SpecimenDescriptionSequenceItem objects")
        else:
            self._SpecimenDescriptionSequence = value
            if "SpecimenDescriptionSequence" not in self._dataset:
                self._dataset.SpecimenDescriptionSequence = pydicom.Sequence()
            self._dataset.SpecimenDescriptionSequence.clear()
            self._dataset.SpecimenDescriptionSequence.extend([item.to_dataset() for item in value])

    def add_SpecimenDescription(self, item: SpecimenDescriptionSequenceItem):
        if not isinstance(item, SpecimenDescriptionSequenceItem):
            raise ValueError("Item must be an instance of SpecimenDescriptionSequenceItem")
        self._SpecimenDescriptionSequence.append(item)
        if "SpecimenDescriptionSequence" not in self._dataset:
            self._dataset.SpecimenDescriptionSequence = pydicom.Sequence()
        self._dataset.SpecimenDescriptionSequence.append(item.to_dataset())

    @property
    def ClinicalTrialCoordinatingCenterName(self) -> Optional[str]:
        if "ClinicalTrialCoordinatingCenterName" in self._dataset:
            return self._dataset.ClinicalTrialCoordinatingCenterName
        return None

    @ClinicalTrialCoordinatingCenterName.setter
    def ClinicalTrialCoordinatingCenterName(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialCoordinatingCenterName" in self._dataset:
                del self._dataset.ClinicalTrialCoordinatingCenterName
        else:
            self._dataset.ClinicalTrialCoordinatingCenterName = value

    @property
    def ClinicalTrialSeriesID(self) -> Optional[str]:
        if "ClinicalTrialSeriesID" in self._dataset:
            return self._dataset.ClinicalTrialSeriesID
        return None

    @ClinicalTrialSeriesID.setter
    def ClinicalTrialSeriesID(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialSeriesID" in self._dataset:
                del self._dataset.ClinicalTrialSeriesID
        else:
            self._dataset.ClinicalTrialSeriesID = value

    @property
    def ClinicalTrialSeriesDescription(self) -> Optional[str]:
        if "ClinicalTrialSeriesDescription" in self._dataset:
            return self._dataset.ClinicalTrialSeriesDescription
        return None

    @ClinicalTrialSeriesDescription.setter
    def ClinicalTrialSeriesDescription(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialSeriesDescription" in self._dataset:
                del self._dataset.ClinicalTrialSeriesDescription
        else:
            self._dataset.ClinicalTrialSeriesDescription = value

    @property
    def IssuerOfClinicalTrialSeriesID(self) -> Optional[str]:
        if "IssuerOfClinicalTrialSeriesID" in self._dataset:
            return self._dataset.IssuerOfClinicalTrialSeriesID
        return None

    @IssuerOfClinicalTrialSeriesID.setter
    def IssuerOfClinicalTrialSeriesID(self, value: Optional[str]):
        if value is None:
            if "IssuerOfClinicalTrialSeriesID" in self._dataset:
                del self._dataset.IssuerOfClinicalTrialSeriesID
        else:
            self._dataset.IssuerOfClinicalTrialSeriesID = value

    @property
    def ReferencedImageSequence(self) -> Optional[List[ReferencedImageSequenceItem]]:
        if "ReferencedImageSequence" in self._dataset:
            if len(self._ReferencedImageSequence) == len(self._dataset.ReferencedImageSequence):
                return self._ReferencedImageSequence
            else:
                return [ReferencedImageSequenceItem(x) for x in self._dataset.ReferencedImageSequence]
        return None

    @ReferencedImageSequence.setter
    def ReferencedImageSequence(self, value: Optional[List[ReferencedImageSequenceItem]]):
        if value is None:
            self._ReferencedImageSequence = []
            if "ReferencedImageSequence" in self._dataset:
                del self._dataset.ReferencedImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedImageSequenceItem) for item in value):
            raise ValueError("ReferencedImageSequence must be a list of ReferencedImageSequenceItem objects")
        else:
            self._ReferencedImageSequence = value
            if "ReferencedImageSequence" not in self._dataset:
                self._dataset.ReferencedImageSequence = pydicom.Sequence()
            self._dataset.ReferencedImageSequence.clear()
            self._dataset.ReferencedImageSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedImage(self, item: ReferencedImageSequenceItem):
        if not isinstance(item, ReferencedImageSequenceItem):
            raise ValueError("Item must be an instance of ReferencedImageSequenceItem")
        self._ReferencedImageSequence.append(item)
        if "ReferencedImageSequence" not in self._dataset:
            self._dataset.ReferencedImageSequence = pydicom.Sequence()
        self._dataset.ReferencedImageSequence.append(item.to_dataset())

    @property
    def ReferencedInstanceSequence(self) -> Optional[List[ReferencedInstanceSequenceItem]]:
        if "ReferencedInstanceSequence" in self._dataset:
            if len(self._ReferencedInstanceSequence) == len(self._dataset.ReferencedInstanceSequence):
                return self._ReferencedInstanceSequence
            else:
                return [ReferencedInstanceSequenceItem(x) for x in self._dataset.ReferencedInstanceSequence]
        return None

    @ReferencedInstanceSequence.setter
    def ReferencedInstanceSequence(self, value: Optional[List[ReferencedInstanceSequenceItem]]):
        if value is None:
            self._ReferencedInstanceSequence = []
            if "ReferencedInstanceSequence" in self._dataset:
                del self._dataset.ReferencedInstanceSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedInstanceSequenceItem) for item in value):
            raise ValueError("ReferencedInstanceSequence must be a list of ReferencedInstanceSequenceItem objects")
        else:
            self._ReferencedInstanceSequence = value
            if "ReferencedInstanceSequence" not in self._dataset:
                self._dataset.ReferencedInstanceSequence = pydicom.Sequence()
            self._dataset.ReferencedInstanceSequence.clear()
            self._dataset.ReferencedInstanceSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedInstance(self, item: ReferencedInstanceSequenceItem):
        if not isinstance(item, ReferencedInstanceSequenceItem):
            raise ValueError("Item must be an instance of ReferencedInstanceSequenceItem")
        self._ReferencedInstanceSequence.append(item)
        if "ReferencedInstanceSequence" not in self._dataset:
            self._dataset.ReferencedInstanceSequence = pydicom.Sequence()
        self._dataset.ReferencedInstanceSequence.append(item.to_dataset())

    @property
    def DerivationDescription(self) -> Optional[str]:
        if "DerivationDescription" in self._dataset:
            return self._dataset.DerivationDescription
        return None

    @DerivationDescription.setter
    def DerivationDescription(self, value: Optional[str]):
        if value is None:
            if "DerivationDescription" in self._dataset:
                del self._dataset.DerivationDescription
        else:
            self._dataset.DerivationDescription = value

    @property
    def SourceImageSequence(self) -> Optional[List[SourceImageSequenceItem]]:
        if "SourceImageSequence" in self._dataset:
            if len(self._SourceImageSequence) == len(self._dataset.SourceImageSequence):
                return self._SourceImageSequence
            else:
                return [SourceImageSequenceItem(x) for x in self._dataset.SourceImageSequence]
        return None

    @SourceImageSequence.setter
    def SourceImageSequence(self, value: Optional[List[SourceImageSequenceItem]]):
        if value is None:
            self._SourceImageSequence = []
            if "SourceImageSequence" in self._dataset:
                del self._dataset.SourceImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, SourceImageSequenceItem) for item in value):
            raise ValueError("SourceImageSequence must be a list of SourceImageSequenceItem objects")
        else:
            self._SourceImageSequence = value
            if "SourceImageSequence" not in self._dataset:
                self._dataset.SourceImageSequence = pydicom.Sequence()
            self._dataset.SourceImageSequence.clear()
            self._dataset.SourceImageSequence.extend([item.to_dataset() for item in value])

    def add_SourceImage(self, item: SourceImageSequenceItem):
        if not isinstance(item, SourceImageSequenceItem):
            raise ValueError("Item must be an instance of SourceImageSequenceItem")
        self._SourceImageSequence.append(item)
        if "SourceImageSequence" not in self._dataset:
            self._dataset.SourceImageSequence = pydicom.Sequence()
        self._dataset.SourceImageSequence.append(item.to_dataset())

    @property
    def DerivationCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "DerivationCodeSequence" in self._dataset:
            if len(self._DerivationCodeSequence) == len(self._dataset.DerivationCodeSequence):
                return self._DerivationCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.DerivationCodeSequence]
        return None

    @DerivationCodeSequence.setter
    def DerivationCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._DerivationCodeSequence = []
            if "DerivationCodeSequence" in self._dataset:
                del self._dataset.DerivationCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("DerivationCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._DerivationCodeSequence = value
            if "DerivationCodeSequence" not in self._dataset:
                self._dataset.DerivationCodeSequence = pydicom.Sequence()
            self._dataset.DerivationCodeSequence.clear()
            self._dataset.DerivationCodeSequence.extend([item.to_dataset() for item in value])

    def add_DerivationCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._DerivationCodeSequence.append(item)
        if "DerivationCodeSequence" not in self._dataset:
            self._dataset.DerivationCodeSequence = pydicom.Sequence()
        self._dataset.DerivationCodeSequence.append(item.to_dataset())

    @property
    def SourceInstanceSequence(self) -> Optional[List[SourceInstanceSequenceItem]]:
        if "SourceInstanceSequence" in self._dataset:
            if len(self._SourceInstanceSequence) == len(self._dataset.SourceInstanceSequence):
                return self._SourceInstanceSequence
            else:
                return [SourceInstanceSequenceItem(x) for x in self._dataset.SourceInstanceSequence]
        return None

    @SourceInstanceSequence.setter
    def SourceInstanceSequence(self, value: Optional[List[SourceInstanceSequenceItem]]):
        if value is None:
            self._SourceInstanceSequence = []
            if "SourceInstanceSequence" in self._dataset:
                del self._dataset.SourceInstanceSequence
        elif not isinstance(value, list) or not all(isinstance(item, SourceInstanceSequenceItem) for item in value):
            raise ValueError("SourceInstanceSequence must be a list of SourceInstanceSequenceItem objects")
        else:
            self._SourceInstanceSequence = value
            if "SourceInstanceSequence" not in self._dataset:
                self._dataset.SourceInstanceSequence = pydicom.Sequence()
            self._dataset.SourceInstanceSequence.clear()
            self._dataset.SourceInstanceSequence.extend([item.to_dataset() for item in value])

    def add_SourceInstance(self, item: SourceInstanceSequenceItem):
        if not isinstance(item, SourceInstanceSequenceItem):
            raise ValueError("Item must be an instance of SourceInstanceSequenceItem")
        self._SourceInstanceSequence.append(item)
        if "SourceInstanceSequence" not in self._dataset:
            self._dataset.SourceInstanceSequence = pydicom.Sequence()
        self._dataset.SourceInstanceSequence.append(item.to_dataset())

    @property
    def Modality(self) -> Optional[str]:
        if "Modality" in self._dataset:
            return self._dataset.Modality
        return None

    @Modality.setter
    def Modality(self, value: Optional[str]):
        if value is None:
            if "Modality" in self._dataset:
                del self._dataset.Modality
        else:
            self._dataset.Modality = value

    @property
    def PresentationIntentType(self) -> Optional[str]:
        if "PresentationIntentType" in self._dataset:
            return self._dataset.PresentationIntentType
        return None

    @PresentationIntentType.setter
    def PresentationIntentType(self, value: Optional[str]):
        if value is None:
            if "PresentationIntentType" in self._dataset:
                del self._dataset.PresentationIntentType
        else:
            self._dataset.PresentationIntentType = value

    @property
    def ReferencedPerformedProcedureStepSequence(self) -> Optional[List[ReferencedPerformedProcedureStepSequenceItem]]:
        if "ReferencedPerformedProcedureStepSequence" in self._dataset:
            if len(self._ReferencedPerformedProcedureStepSequence) == len(
                self._dataset.ReferencedPerformedProcedureStepSequence
            ):
                return self._ReferencedPerformedProcedureStepSequence
            else:
                return [
                    ReferencedPerformedProcedureStepSequenceItem(x)
                    for x in self._dataset.ReferencedPerformedProcedureStepSequence
                ]
        return None

    @ReferencedPerformedProcedureStepSequence.setter
    def ReferencedPerformedProcedureStepSequence(self, value: Optional[List[ReferencedPerformedProcedureStepSequenceItem]]):
        if value is None:
            self._ReferencedPerformedProcedureStepSequence = []
            if "ReferencedPerformedProcedureStepSequence" in self._dataset:
                del self._dataset.ReferencedPerformedProcedureStepSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedPerformedProcedureStepSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferencedPerformedProcedureStepSequence must be a list of ReferencedPerformedProcedureStepSequenceItem"
                " objects"
            )
        else:
            self._ReferencedPerformedProcedureStepSequence = value
            if "ReferencedPerformedProcedureStepSequence" not in self._dataset:
                self._dataset.ReferencedPerformedProcedureStepSequence = pydicom.Sequence()
            self._dataset.ReferencedPerformedProcedureStepSequence.clear()
            self._dataset.ReferencedPerformedProcedureStepSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedPerformedProcedureStep(self, item: ReferencedPerformedProcedureStepSequenceItem):
        if not isinstance(item, ReferencedPerformedProcedureStepSequenceItem):
            raise ValueError("Item must be an instance of ReferencedPerformedProcedureStepSequenceItem")
        self._ReferencedPerformedProcedureStepSequence.append(item)
        if "ReferencedPerformedProcedureStepSequence" not in self._dataset:
            self._dataset.ReferencedPerformedProcedureStepSequence = pydicom.Sequence()
        self._dataset.ReferencedPerformedProcedureStepSequence.append(item.to_dataset())

    @property
    def KVP(self) -> Optional[Decimal]:
        if "KVP" in self._dataset:
            return self._dataset.KVP
        return None

    @KVP.setter
    def KVP(self, value: Optional[Decimal]):
        if value is None:
            if "KVP" in self._dataset:
                del self._dataset.KVP
        else:
            self._dataset.KVP = value

    @property
    def DistanceSourceToDetector(self) -> Optional[Decimal]:
        if "DistanceSourceToDetector" in self._dataset:
            return self._dataset.DistanceSourceToDetector
        return None

    @DistanceSourceToDetector.setter
    def DistanceSourceToDetector(self, value: Optional[Decimal]):
        if value is None:
            if "DistanceSourceToDetector" in self._dataset:
                del self._dataset.DistanceSourceToDetector
        else:
            self._dataset.DistanceSourceToDetector = value

    @property
    def DistanceSourceToPatient(self) -> Optional[Decimal]:
        if "DistanceSourceToPatient" in self._dataset:
            return self._dataset.DistanceSourceToPatient
        return None

    @DistanceSourceToPatient.setter
    def DistanceSourceToPatient(self, value: Optional[Decimal]):
        if value is None:
            if "DistanceSourceToPatient" in self._dataset:
                del self._dataset.DistanceSourceToPatient
        else:
            self._dataset.DistanceSourceToPatient = value

    @property
    def ExposureTime(self) -> Optional[int]:
        if "ExposureTime" in self._dataset:
            return self._dataset.ExposureTime
        return None

    @ExposureTime.setter
    def ExposureTime(self, value: Optional[int]):
        if value is None:
            if "ExposureTime" in self._dataset:
                del self._dataset.ExposureTime
        else:
            self._dataset.ExposureTime = value

    @property
    def XRayTubeCurrent(self) -> Optional[int]:
        if "XRayTubeCurrent" in self._dataset:
            return self._dataset.XRayTubeCurrent
        return None

    @XRayTubeCurrent.setter
    def XRayTubeCurrent(self, value: Optional[int]):
        if value is None:
            if "XRayTubeCurrent" in self._dataset:
                del self._dataset.XRayTubeCurrent
        else:
            self._dataset.XRayTubeCurrent = value

    @property
    def Exposure(self) -> Optional[int]:
        if "Exposure" in self._dataset:
            return self._dataset.Exposure
        return None

    @Exposure.setter
    def Exposure(self, value: Optional[int]):
        if value is None:
            if "Exposure" in self._dataset:
                del self._dataset.Exposure
        else:
            self._dataset.Exposure = value

    @property
    def ExposureInuAs(self) -> Optional[int]:
        if "ExposureInuAs" in self._dataset:
            return self._dataset.ExposureInuAs
        return None

    @ExposureInuAs.setter
    def ExposureInuAs(self, value: Optional[int]):
        if value is None:
            if "ExposureInuAs" in self._dataset:
                del self._dataset.ExposureInuAs
        else:
            self._dataset.ExposureInuAs = value

    @property
    def RectificationType(self) -> Optional[str]:
        if "RectificationType" in self._dataset:
            return self._dataset.RectificationType
        return None

    @RectificationType.setter
    def RectificationType(self, value: Optional[str]):
        if value is None:
            if "RectificationType" in self._dataset:
                del self._dataset.RectificationType
        else:
            self._dataset.RectificationType = value

    @property
    def ImageAndFluoroscopyAreaDoseProduct(self) -> Optional[Decimal]:
        if "ImageAndFluoroscopyAreaDoseProduct" in self._dataset:
            return self._dataset.ImageAndFluoroscopyAreaDoseProduct
        return None

    @ImageAndFluoroscopyAreaDoseProduct.setter
    def ImageAndFluoroscopyAreaDoseProduct(self, value: Optional[Decimal]):
        if value is None:
            if "ImageAndFluoroscopyAreaDoseProduct" in self._dataset:
                del self._dataset.ImageAndFluoroscopyAreaDoseProduct
        else:
            self._dataset.ImageAndFluoroscopyAreaDoseProduct = value

    @property
    def FilterType(self) -> Optional[str]:
        if "FilterType" in self._dataset:
            return self._dataset.FilterType
        return None

    @FilterType.setter
    def FilterType(self, value: Optional[str]):
        if value is None:
            if "FilterType" in self._dataset:
                del self._dataset.FilterType
        else:
            self._dataset.FilterType = value

    @property
    def AnodeTargetMaterial(self) -> Optional[str]:
        if "AnodeTargetMaterial" in self._dataset:
            return self._dataset.AnodeTargetMaterial
        return None

    @AnodeTargetMaterial.setter
    def AnodeTargetMaterial(self, value: Optional[str]):
        if value is None:
            if "AnodeTargetMaterial" in self._dataset:
                del self._dataset.AnodeTargetMaterial
        else:
            self._dataset.AnodeTargetMaterial = value

    @property
    def BodyPartThickness(self) -> Optional[Decimal]:
        if "BodyPartThickness" in self._dataset:
            return self._dataset.BodyPartThickness
        return None

    @BodyPartThickness.setter
    def BodyPartThickness(self, value: Optional[Decimal]):
        if value is None:
            if "BodyPartThickness" in self._dataset:
                del self._dataset.BodyPartThickness
        else:
            self._dataset.BodyPartThickness = value

    @property
    def RelativeXRayExposure(self) -> Optional[int]:
        if "RelativeXRayExposure" in self._dataset:
            return self._dataset.RelativeXRayExposure
        return None

    @RelativeXRayExposure.setter
    def RelativeXRayExposure(self, value: Optional[int]):
        if value is None:
            if "RelativeXRayExposure" in self._dataset:
                del self._dataset.RelativeXRayExposure
        else:
            self._dataset.RelativeXRayExposure = value

    @property
    def ExposureIndex(self) -> Optional[Decimal]:
        if "ExposureIndex" in self._dataset:
            return self._dataset.ExposureIndex
        return None

    @ExposureIndex.setter
    def ExposureIndex(self, value: Optional[Decimal]):
        if value is None:
            if "ExposureIndex" in self._dataset:
                del self._dataset.ExposureIndex
        else:
            self._dataset.ExposureIndex = value

    @property
    def TargetExposureIndex(self) -> Optional[Decimal]:
        if "TargetExposureIndex" in self._dataset:
            return self._dataset.TargetExposureIndex
        return None

    @TargetExposureIndex.setter
    def TargetExposureIndex(self, value: Optional[Decimal]):
        if value is None:
            if "TargetExposureIndex" in self._dataset:
                del self._dataset.TargetExposureIndex
        else:
            self._dataset.TargetExposureIndex = value

    @property
    def DeviationIndex(self) -> Optional[Decimal]:
        if "DeviationIndex" in self._dataset:
            return self._dataset.DeviationIndex
        return None

    @DeviationIndex.setter
    def DeviationIndex(self, value: Optional[Decimal]):
        if value is None:
            if "DeviationIndex" in self._dataset:
                del self._dataset.DeviationIndex
        else:
            self._dataset.DeviationIndex = value

    @property
    def FilterMaterial(self) -> Optional[List[str]]:
        if "FilterMaterial" in self._dataset:
            return self._dataset.FilterMaterial
        return None

    @FilterMaterial.setter
    def FilterMaterial(self, value: Optional[List[str]]):
        if value is None:
            if "FilterMaterial" in self._dataset:
                del self._dataset.FilterMaterial
        else:
            self._dataset.FilterMaterial = value

    @property
    def FilterThicknessMinimum(self) -> Optional[List[Decimal]]:
        if "FilterThicknessMinimum" in self._dataset:
            return self._dataset.FilterThicknessMinimum
        return None

    @FilterThicknessMinimum.setter
    def FilterThicknessMinimum(self, value: Optional[List[Decimal]]):
        if value is None:
            if "FilterThicknessMinimum" in self._dataset:
                del self._dataset.FilterThicknessMinimum
        else:
            self._dataset.FilterThicknessMinimum = value

    @property
    def FilterThicknessMaximum(self) -> Optional[List[Decimal]]:
        if "FilterThicknessMaximum" in self._dataset:
            return self._dataset.FilterThicknessMaximum
        return None

    @FilterThicknessMaximum.setter
    def FilterThicknessMaximum(self, value: Optional[List[Decimal]]):
        if value is None:
            if "FilterThicknessMaximum" in self._dataset:
                del self._dataset.FilterThicknessMaximum
        else:
            self._dataset.FilterThicknessMaximum = value

    @property
    def FilterBeamPathLengthMinimum(self) -> Optional[List[float]]:
        if "FilterBeamPathLengthMinimum" in self._dataset:
            return self._dataset.FilterBeamPathLengthMinimum
        return None

    @FilterBeamPathLengthMinimum.setter
    def FilterBeamPathLengthMinimum(self, value: Optional[List[float]]):
        if value is None:
            if "FilterBeamPathLengthMinimum" in self._dataset:
                del self._dataset.FilterBeamPathLengthMinimum
        else:
            self._dataset.FilterBeamPathLengthMinimum = value

    @property
    def FilterBeamPathLengthMaximum(self) -> Optional[List[float]]:
        if "FilterBeamPathLengthMaximum" in self._dataset:
            return self._dataset.FilterBeamPathLengthMaximum
        return None

    @FilterBeamPathLengthMaximum.setter
    def FilterBeamPathLengthMaximum(self, value: Optional[List[float]]):
        if value is None:
            if "FilterBeamPathLengthMaximum" in self._dataset:
                del self._dataset.FilterBeamPathLengthMaximum
        else:
            self._dataset.FilterBeamPathLengthMaximum = value

    @property
    def ExposureTimeInuS(self) -> Optional[Decimal]:
        if "ExposureTimeInuS" in self._dataset:
            return self._dataset.ExposureTimeInuS
        return None

    @ExposureTimeInuS.setter
    def ExposureTimeInuS(self, value: Optional[Decimal]):
        if value is None:
            if "ExposureTimeInuS" in self._dataset:
                del self._dataset.ExposureTimeInuS
        else:
            self._dataset.ExposureTimeInuS = value

    @property
    def XRayTubeCurrentInuA(self) -> Optional[Decimal]:
        if "XRayTubeCurrentInuA" in self._dataset:
            return self._dataset.XRayTubeCurrentInuA
        return None

    @XRayTubeCurrentInuA.setter
    def XRayTubeCurrentInuA(self, value: Optional[Decimal]):
        if value is None:
            if "XRayTubeCurrentInuA" in self._dataset:
                del self._dataset.XRayTubeCurrentInuA
        else:
            self._dataset.XRayTubeCurrentInuA = value

    @property
    def EntranceDose(self) -> Optional[int]:
        if "EntranceDose" in self._dataset:
            return self._dataset.EntranceDose
        return None

    @EntranceDose.setter
    def EntranceDose(self, value: Optional[int]):
        if value is None:
            if "EntranceDose" in self._dataset:
                del self._dataset.EntranceDose
        else:
            self._dataset.EntranceDose = value

    @property
    def ExposedArea(self) -> Optional[List[int]]:
        if "ExposedArea" in self._dataset:
            return self._dataset.ExposedArea
        return None

    @ExposedArea.setter
    def ExposedArea(self, value: Optional[List[int]]):
        if value is None:
            if "ExposedArea" in self._dataset:
                del self._dataset.ExposedArea
        else:
            self._dataset.ExposedArea = value

    @property
    def DistanceSourceToEntrance(self) -> Optional[Decimal]:
        if "DistanceSourceToEntrance" in self._dataset:
            return self._dataset.DistanceSourceToEntrance
        return None

    @DistanceSourceToEntrance.setter
    def DistanceSourceToEntrance(self, value: Optional[Decimal]):
        if value is None:
            if "DistanceSourceToEntrance" in self._dataset:
                del self._dataset.DistanceSourceToEntrance
        else:
            self._dataset.DistanceSourceToEntrance = value

    @property
    def CommentsOnRadiationDose(self) -> Optional[str]:
        if "CommentsOnRadiationDose" in self._dataset:
            return self._dataset.CommentsOnRadiationDose
        return None

    @CommentsOnRadiationDose.setter
    def CommentsOnRadiationDose(self, value: Optional[str]):
        if value is None:
            if "CommentsOnRadiationDose" in self._dataset:
                del self._dataset.CommentsOnRadiationDose
        else:
            self._dataset.CommentsOnRadiationDose = value

    @property
    def XRayOutput(self) -> Optional[Decimal]:
        if "XRayOutput" in self._dataset:
            return self._dataset.XRayOutput
        return None

    @XRayOutput.setter
    def XRayOutput(self, value: Optional[Decimal]):
        if value is None:
            if "XRayOutput" in self._dataset:
                del self._dataset.XRayOutput
        else:
            self._dataset.XRayOutput = value

    @property
    def HalfValueLayer(self) -> Optional[Decimal]:
        if "HalfValueLayer" in self._dataset:
            return self._dataset.HalfValueLayer
        return None

    @HalfValueLayer.setter
    def HalfValueLayer(self, value: Optional[Decimal]):
        if value is None:
            if "HalfValueLayer" in self._dataset:
                del self._dataset.HalfValueLayer
        else:
            self._dataset.HalfValueLayer = value

    @property
    def OrganDose(self) -> Optional[Decimal]:
        if "OrganDose" in self._dataset:
            return self._dataset.OrganDose
        return None

    @OrganDose.setter
    def OrganDose(self, value: Optional[Decimal]):
        if value is None:
            if "OrganDose" in self._dataset:
                del self._dataset.OrganDose
        else:
            self._dataset.OrganDose = value

    @property
    def OrganExposed(self) -> Optional[str]:
        if "OrganExposed" in self._dataset:
            return self._dataset.OrganExposed
        return None

    @OrganExposed.setter
    def OrganExposed(self, value: Optional[str]):
        if value is None:
            if "OrganExposed" in self._dataset:
                del self._dataset.OrganExposed
        else:
            self._dataset.OrganExposed = value

    @property
    def EntranceDoseInmGy(self) -> Optional[Decimal]:
        if "EntranceDoseInmGy" in self._dataset:
            return self._dataset.EntranceDoseInmGy
        return None

    @EntranceDoseInmGy.setter
    def EntranceDoseInmGy(self, value: Optional[Decimal]):
        if value is None:
            if "EntranceDoseInmGy" in self._dataset:
                del self._dataset.EntranceDoseInmGy
        else:
            self._dataset.EntranceDoseInmGy = value

    @property
    def EntranceDoseDerivation(self) -> Optional[str]:
        if "EntranceDoseDerivation" in self._dataset:
            return self._dataset.EntranceDoseDerivation
        return None

    @EntranceDoseDerivation.setter
    def EntranceDoseDerivation(self, value: Optional[str]):
        if value is None:
            if "EntranceDoseDerivation" in self._dataset:
                del self._dataset.EntranceDoseDerivation
        else:
            self._dataset.EntranceDoseDerivation = value

    @property
    def ContrastBolusAgent(self) -> Optional[str]:
        if "ContrastBolusAgent" in self._dataset:
            return self._dataset.ContrastBolusAgent
        return None

    @ContrastBolusAgent.setter
    def ContrastBolusAgent(self, value: Optional[str]):
        if value is None:
            if "ContrastBolusAgent" in self._dataset:
                del self._dataset.ContrastBolusAgent
        else:
            self._dataset.ContrastBolusAgent = value

    @property
    def ContrastBolusAgentSequence(self) -> Optional[List[ContrastBolusAgentSequenceItem]]:
        if "ContrastBolusAgentSequence" in self._dataset:
            if len(self._ContrastBolusAgentSequence) == len(self._dataset.ContrastBolusAgentSequence):
                return self._ContrastBolusAgentSequence
            else:
                return [ContrastBolusAgentSequenceItem(x) for x in self._dataset.ContrastBolusAgentSequence]
        return None

    @ContrastBolusAgentSequence.setter
    def ContrastBolusAgentSequence(self, value: Optional[List[ContrastBolusAgentSequenceItem]]):
        if value is None:
            self._ContrastBolusAgentSequence = []
            if "ContrastBolusAgentSequence" in self._dataset:
                del self._dataset.ContrastBolusAgentSequence
        elif not isinstance(value, list) or not all(isinstance(item, ContrastBolusAgentSequenceItem) for item in value):
            raise ValueError("ContrastBolusAgentSequence must be a list of ContrastBolusAgentSequenceItem objects")
        else:
            self._ContrastBolusAgentSequence = value
            if "ContrastBolusAgentSequence" not in self._dataset:
                self._dataset.ContrastBolusAgentSequence = pydicom.Sequence()
            self._dataset.ContrastBolusAgentSequence.clear()
            self._dataset.ContrastBolusAgentSequence.extend([item.to_dataset() for item in value])

    def add_ContrastBolusAgent(self, item: ContrastBolusAgentSequenceItem):
        if not isinstance(item, ContrastBolusAgentSequenceItem):
            raise ValueError("Item must be an instance of ContrastBolusAgentSequenceItem")
        self._ContrastBolusAgentSequence.append(item)
        if "ContrastBolusAgentSequence" not in self._dataset:
            self._dataset.ContrastBolusAgentSequence = pydicom.Sequence()
        self._dataset.ContrastBolusAgentSequence.append(item.to_dataset())

    @property
    def ContrastBolusAdministrationRouteSequence(self) -> Optional[List[ContrastBolusAdministrationRouteSequenceItem]]:
        if "ContrastBolusAdministrationRouteSequence" in self._dataset:
            if len(self._ContrastBolusAdministrationRouteSequence) == len(
                self._dataset.ContrastBolusAdministrationRouteSequence
            ):
                return self._ContrastBolusAdministrationRouteSequence
            else:
                return [
                    ContrastBolusAdministrationRouteSequenceItem(x)
                    for x in self._dataset.ContrastBolusAdministrationRouteSequence
                ]
        return None

    @ContrastBolusAdministrationRouteSequence.setter
    def ContrastBolusAdministrationRouteSequence(self, value: Optional[List[ContrastBolusAdministrationRouteSequenceItem]]):
        if value is None:
            self._ContrastBolusAdministrationRouteSequence = []
            if "ContrastBolusAdministrationRouteSequence" in self._dataset:
                del self._dataset.ContrastBolusAdministrationRouteSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ContrastBolusAdministrationRouteSequenceItem) for item in value
        ):
            raise ValueError(
                "ContrastBolusAdministrationRouteSequence must be a list of ContrastBolusAdministrationRouteSequenceItem"
                " objects"
            )
        else:
            self._ContrastBolusAdministrationRouteSequence = value
            if "ContrastBolusAdministrationRouteSequence" not in self._dataset:
                self._dataset.ContrastBolusAdministrationRouteSequence = pydicom.Sequence()
            self._dataset.ContrastBolusAdministrationRouteSequence.clear()
            self._dataset.ContrastBolusAdministrationRouteSequence.extend([item.to_dataset() for item in value])

    def add_ContrastBolusAdministrationRoute(self, item: ContrastBolusAdministrationRouteSequenceItem):
        if not isinstance(item, ContrastBolusAdministrationRouteSequenceItem):
            raise ValueError("Item must be an instance of ContrastBolusAdministrationRouteSequenceItem")
        self._ContrastBolusAdministrationRouteSequence.append(item)
        if "ContrastBolusAdministrationRouteSequence" not in self._dataset:
            self._dataset.ContrastBolusAdministrationRouteSequence = pydicom.Sequence()
        self._dataset.ContrastBolusAdministrationRouteSequence.append(item.to_dataset())

    @property
    def ContrastBolusRoute(self) -> Optional[str]:
        if "ContrastBolusRoute" in self._dataset:
            return self._dataset.ContrastBolusRoute
        return None

    @ContrastBolusRoute.setter
    def ContrastBolusRoute(self, value: Optional[str]):
        if value is None:
            if "ContrastBolusRoute" in self._dataset:
                del self._dataset.ContrastBolusRoute
        else:
            self._dataset.ContrastBolusRoute = value

    @property
    def ContrastBolusVolume(self) -> Optional[Decimal]:
        if "ContrastBolusVolume" in self._dataset:
            return self._dataset.ContrastBolusVolume
        return None

    @ContrastBolusVolume.setter
    def ContrastBolusVolume(self, value: Optional[Decimal]):
        if value is None:
            if "ContrastBolusVolume" in self._dataset:
                del self._dataset.ContrastBolusVolume
        else:
            self._dataset.ContrastBolusVolume = value

    @property
    def ContrastBolusStartTime(self) -> Optional[str]:
        if "ContrastBolusStartTime" in self._dataset:
            return self._dataset.ContrastBolusStartTime
        return None

    @ContrastBolusStartTime.setter
    def ContrastBolusStartTime(self, value: Optional[str]):
        if value is None:
            if "ContrastBolusStartTime" in self._dataset:
                del self._dataset.ContrastBolusStartTime
        else:
            self._dataset.ContrastBolusStartTime = value

    @property
    def ContrastBolusStopTime(self) -> Optional[str]:
        if "ContrastBolusStopTime" in self._dataset:
            return self._dataset.ContrastBolusStopTime
        return None

    @ContrastBolusStopTime.setter
    def ContrastBolusStopTime(self, value: Optional[str]):
        if value is None:
            if "ContrastBolusStopTime" in self._dataset:
                del self._dataset.ContrastBolusStopTime
        else:
            self._dataset.ContrastBolusStopTime = value

    @property
    def ContrastBolusTotalDose(self) -> Optional[Decimal]:
        if "ContrastBolusTotalDose" in self._dataset:
            return self._dataset.ContrastBolusTotalDose
        return None

    @ContrastBolusTotalDose.setter
    def ContrastBolusTotalDose(self, value: Optional[Decimal]):
        if value is None:
            if "ContrastBolusTotalDose" in self._dataset:
                del self._dataset.ContrastBolusTotalDose
        else:
            self._dataset.ContrastBolusTotalDose = value

    @property
    def ContrastFlowRate(self) -> Optional[List[Decimal]]:
        if "ContrastFlowRate" in self._dataset:
            return self._dataset.ContrastFlowRate
        return None

    @ContrastFlowRate.setter
    def ContrastFlowRate(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ContrastFlowRate" in self._dataset:
                del self._dataset.ContrastFlowRate
        else:
            self._dataset.ContrastFlowRate = value

    @property
    def ContrastFlowDuration(self) -> Optional[List[Decimal]]:
        if "ContrastFlowDuration" in self._dataset:
            return self._dataset.ContrastFlowDuration
        return None

    @ContrastFlowDuration.setter
    def ContrastFlowDuration(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ContrastFlowDuration" in self._dataset:
                del self._dataset.ContrastFlowDuration
        else:
            self._dataset.ContrastFlowDuration = value

    @property
    def ContrastBolusIngredient(self) -> Optional[str]:
        if "ContrastBolusIngredient" in self._dataset:
            return self._dataset.ContrastBolusIngredient
        return None

    @ContrastBolusIngredient.setter
    def ContrastBolusIngredient(self, value: Optional[str]):
        if value is None:
            if "ContrastBolusIngredient" in self._dataset:
                del self._dataset.ContrastBolusIngredient
        else:
            self._dataset.ContrastBolusIngredient = value

    @property
    def ContrastBolusIngredientConcentration(self) -> Optional[Decimal]:
        if "ContrastBolusIngredientConcentration" in self._dataset:
            return self._dataset.ContrastBolusIngredientConcentration
        return None

    @ContrastBolusIngredientConcentration.setter
    def ContrastBolusIngredientConcentration(self, value: Optional[Decimal]):
        if value is None:
            if "ContrastBolusIngredientConcentration" in self._dataset:
                del self._dataset.ContrastBolusIngredientConcentration
        else:
            self._dataset.ContrastBolusIngredientConcentration = value

    @property
    def Modality(self) -> Optional[str]:
        if "Modality" in self._dataset:
            return self._dataset.Modality
        return None

    @Modality.setter
    def Modality(self, value: Optional[str]):
        if value is None:
            if "Modality" in self._dataset:
                del self._dataset.Modality
        else:
            self._dataset.Modality = value

    @property
    def TomoLayerHeight(self) -> Optional[Decimal]:
        if "TomoLayerHeight" in self._dataset:
            return self._dataset.TomoLayerHeight
        return None

    @TomoLayerHeight.setter
    def TomoLayerHeight(self, value: Optional[Decimal]):
        if value is None:
            if "TomoLayerHeight" in self._dataset:
                del self._dataset.TomoLayerHeight
        else:
            self._dataset.TomoLayerHeight = value

    @property
    def TomoAngle(self) -> Optional[Decimal]:
        if "TomoAngle" in self._dataset:
            return self._dataset.TomoAngle
        return None

    @TomoAngle.setter
    def TomoAngle(self, value: Optional[Decimal]):
        if value is None:
            if "TomoAngle" in self._dataset:
                del self._dataset.TomoAngle
        else:
            self._dataset.TomoAngle = value

    @property
    def TomoTime(self) -> Optional[Decimal]:
        if "TomoTime" in self._dataset:
            return self._dataset.TomoTime
        return None

    @TomoTime.setter
    def TomoTime(self, value: Optional[Decimal]):
        if value is None:
            if "TomoTime" in self._dataset:
                del self._dataset.TomoTime
        else:
            self._dataset.TomoTime = value

    @property
    def TomoType(self) -> Optional[str]:
        if "TomoType" in self._dataset:
            return self._dataset.TomoType
        return None

    @TomoType.setter
    def TomoType(self, value: Optional[str]):
        if value is None:
            if "TomoType" in self._dataset:
                del self._dataset.TomoType
        else:
            self._dataset.TomoType = value

    @property
    def TomoClass(self) -> Optional[str]:
        if "TomoClass" in self._dataset:
            return self._dataset.TomoClass
        return None

    @TomoClass.setter
    def TomoClass(self, value: Optional[str]):
        if value is None:
            if "TomoClass" in self._dataset:
                del self._dataset.TomoClass
        else:
            self._dataset.TomoClass = value

    @property
    def NumberOfTomosynthesisSourceImages(self) -> Optional[int]:
        if "NumberOfTomosynthesisSourceImages" in self._dataset:
            return self._dataset.NumberOfTomosynthesisSourceImages
        return None

    @NumberOfTomosynthesisSourceImages.setter
    def NumberOfTomosynthesisSourceImages(self, value: Optional[int]):
        if value is None:
            if "NumberOfTomosynthesisSourceImages" in self._dataset:
                del self._dataset.NumberOfTomosynthesisSourceImages
        else:
            self._dataset.NumberOfTomosynthesisSourceImages = value

    @property
    def OverlayRows(self) -> Optional[int]:
        if "OverlayRows" in self._dataset:
            return self._dataset.OverlayRows
        return None

    @OverlayRows.setter
    def OverlayRows(self, value: Optional[int]):
        if value is None:
            if "OverlayRows" in self._dataset:
                del self._dataset.OverlayRows
        else:
            self._dataset.OverlayRows = value

    @property
    def OverlayColumns(self) -> Optional[int]:
        if "OverlayColumns" in self._dataset:
            return self._dataset.OverlayColumns
        return None

    @OverlayColumns.setter
    def OverlayColumns(self, value: Optional[int]):
        if value is None:
            if "OverlayColumns" in self._dataset:
                del self._dataset.OverlayColumns
        else:
            self._dataset.OverlayColumns = value

    @property
    def OverlayDescription(self) -> Optional[str]:
        if "OverlayDescription" in self._dataset:
            return self._dataset.OverlayDescription
        return None

    @OverlayDescription.setter
    def OverlayDescription(self, value: Optional[str]):
        if value is None:
            if "OverlayDescription" in self._dataset:
                del self._dataset.OverlayDescription
        else:
            self._dataset.OverlayDescription = value

    @property
    def OverlayType(self) -> Optional[str]:
        if "OverlayType" in self._dataset:
            return self._dataset.OverlayType
        return None

    @OverlayType.setter
    def OverlayType(self, value: Optional[str]):
        if value is None:
            if "OverlayType" in self._dataset:
                del self._dataset.OverlayType
        else:
            self._dataset.OverlayType = value

    @property
    def OverlaySubtype(self) -> Optional[str]:
        if "OverlaySubtype" in self._dataset:
            return self._dataset.OverlaySubtype
        return None

    @OverlaySubtype.setter
    def OverlaySubtype(self, value: Optional[str]):
        if value is None:
            if "OverlaySubtype" in self._dataset:
                del self._dataset.OverlaySubtype
        else:
            self._dataset.OverlaySubtype = value

    @property
    def OverlayOrigin(self) -> Optional[List[int]]:
        if "OverlayOrigin" in self._dataset:
            return self._dataset.OverlayOrigin
        return None

    @OverlayOrigin.setter
    def OverlayOrigin(self, value: Optional[List[int]]):
        if value is None:
            if "OverlayOrigin" in self._dataset:
                del self._dataset.OverlayOrigin
        else:
            self._dataset.OverlayOrigin = value

    @property
    def OverlayBitsAllocated(self) -> Optional[int]:
        if "OverlayBitsAllocated" in self._dataset:
            return self._dataset.OverlayBitsAllocated
        return None

    @OverlayBitsAllocated.setter
    def OverlayBitsAllocated(self, value: Optional[int]):
        if value is None:
            if "OverlayBitsAllocated" in self._dataset:
                del self._dataset.OverlayBitsAllocated
        else:
            self._dataset.OverlayBitsAllocated = value

    @property
    def OverlayBitPosition(self) -> Optional[int]:
        if "OverlayBitPosition" in self._dataset:
            return self._dataset.OverlayBitPosition
        return None

    @OverlayBitPosition.setter
    def OverlayBitPosition(self, value: Optional[int]):
        if value is None:
            if "OverlayBitPosition" in self._dataset:
                del self._dataset.OverlayBitPosition
        else:
            self._dataset.OverlayBitPosition = value

    @property
    def ROIArea(self) -> Optional[int]:
        if "ROIArea" in self._dataset:
            return self._dataset.ROIArea
        return None

    @ROIArea.setter
    def ROIArea(self, value: Optional[int]):
        if value is None:
            if "ROIArea" in self._dataset:
                del self._dataset.ROIArea
        else:
            self._dataset.ROIArea = value

    @property
    def ROIMean(self) -> Optional[Decimal]:
        if "ROIMean" in self._dataset:
            return self._dataset.ROIMean
        return None

    @ROIMean.setter
    def ROIMean(self, value: Optional[Decimal]):
        if value is None:
            if "ROIMean" in self._dataset:
                del self._dataset.ROIMean
        else:
            self._dataset.ROIMean = value

    @property
    def ROIStandardDeviation(self) -> Optional[Decimal]:
        if "ROIStandardDeviation" in self._dataset:
            return self._dataset.ROIStandardDeviation
        return None

    @ROIStandardDeviation.setter
    def ROIStandardDeviation(self, value: Optional[Decimal]):
        if value is None:
            if "ROIStandardDeviation" in self._dataset:
                del self._dataset.ROIStandardDeviation
        else:
            self._dataset.ROIStandardDeviation = value

    @property
    def OverlayLabel(self) -> Optional[str]:
        if "OverlayLabel" in self._dataset:
            return self._dataset.OverlayLabel
        return None

    @OverlayLabel.setter
    def OverlayLabel(self, value: Optional[str]):
        if value is None:
            if "OverlayLabel" in self._dataset:
                del self._dataset.OverlayLabel
        else:
            self._dataset.OverlayLabel = value

    @property
    def OverlayData(self) -> Optional[bytes]:
        if "OverlayData" in self._dataset:
            return self._dataset.OverlayData
        return None

    @OverlayData.setter
    def OverlayData(self, value: Optional[bytes]):
        if value is None:
            if "OverlayData" in self._dataset:
                del self._dataset.OverlayData
        else:
            self._dataset.OverlayData = value

    @property
    def ReferencedSeriesSequence(self) -> Optional[List[ReferencedSeriesSequenceItem]]:
        if "ReferencedSeriesSequence" in self._dataset:
            if len(self._ReferencedSeriesSequence) == len(self._dataset.ReferencedSeriesSequence):
                return self._ReferencedSeriesSequence
            else:
                return [ReferencedSeriesSequenceItem(x) for x in self._dataset.ReferencedSeriesSequence]
        return None

    @ReferencedSeriesSequence.setter
    def ReferencedSeriesSequence(self, value: Optional[List[ReferencedSeriesSequenceItem]]):
        if value is None:
            self._ReferencedSeriesSequence = []
            if "ReferencedSeriesSequence" in self._dataset:
                del self._dataset.ReferencedSeriesSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedSeriesSequenceItem) for item in value):
            raise ValueError("ReferencedSeriesSequence must be a list of ReferencedSeriesSequenceItem objects")
        else:
            self._ReferencedSeriesSequence = value
            if "ReferencedSeriesSequence" not in self._dataset:
                self._dataset.ReferencedSeriesSequence = pydicom.Sequence()
            self._dataset.ReferencedSeriesSequence.clear()
            self._dataset.ReferencedSeriesSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedSeries(self, item: ReferencedSeriesSequenceItem):
        if not isinstance(item, ReferencedSeriesSequenceItem):
            raise ValueError("Item must be an instance of ReferencedSeriesSequenceItem")
        self._ReferencedSeriesSequence.append(item)
        if "ReferencedSeriesSequence" not in self._dataset:
            self._dataset.ReferencedSeriesSequence = pydicom.Sequence()
        self._dataset.ReferencedSeriesSequence.append(item.to_dataset())

    @property
    def StudiesContainingOtherReferencedInstancesSequence(
        self,
    ) -> Optional[List[StudiesContainingOtherReferencedInstancesSequenceItem]]:
        if "StudiesContainingOtherReferencedInstancesSequence" in self._dataset:
            if len(self._StudiesContainingOtherReferencedInstancesSequence) == len(
                self._dataset.StudiesContainingOtherReferencedInstancesSequence
            ):
                return self._StudiesContainingOtherReferencedInstancesSequence
            else:
                return [
                    StudiesContainingOtherReferencedInstancesSequenceItem(x)
                    for x in self._dataset.StudiesContainingOtherReferencedInstancesSequence
                ]
        return None

    @StudiesContainingOtherReferencedInstancesSequence.setter
    def StudiesContainingOtherReferencedInstancesSequence(
        self, value: Optional[List[StudiesContainingOtherReferencedInstancesSequenceItem]]
    ):
        if value is None:
            self._StudiesContainingOtherReferencedInstancesSequence = []
            if "StudiesContainingOtherReferencedInstancesSequence" in self._dataset:
                del self._dataset.StudiesContainingOtherReferencedInstancesSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, StudiesContainingOtherReferencedInstancesSequenceItem) for item in value
        ):
            raise ValueError(
                "StudiesContainingOtherReferencedInstancesSequence must be a list of"
                " StudiesContainingOtherReferencedInstancesSequenceItem objects"
            )
        else:
            self._StudiesContainingOtherReferencedInstancesSequence = value
            if "StudiesContainingOtherReferencedInstancesSequence" not in self._dataset:
                self._dataset.StudiesContainingOtherReferencedInstancesSequence = pydicom.Sequence()
            self._dataset.StudiesContainingOtherReferencedInstancesSequence.clear()
            self._dataset.StudiesContainingOtherReferencedInstancesSequence.extend([item.to_dataset() for item in value])

    def add_StudiesContainingOtherReferencedInstances(self, item: StudiesContainingOtherReferencedInstancesSequenceItem):
        if not isinstance(item, StudiesContainingOtherReferencedInstancesSequenceItem):
            raise ValueError("Item must be an instance of StudiesContainingOtherReferencedInstancesSequenceItem")
        self._StudiesContainingOtherReferencedInstancesSequence.append(item)
        if "StudiesContainingOtherReferencedInstancesSequence" not in self._dataset:
            self._dataset.StudiesContainingOtherReferencedInstancesSequence = pydicom.Sequence()
        self._dataset.StudiesContainingOtherReferencedInstancesSequence.append(item.to_dataset())

    @property
    def Manufacturer(self) -> Optional[str]:
        if "Manufacturer" in self._dataset:
            return self._dataset.Manufacturer
        return None

    @Manufacturer.setter
    def Manufacturer(self, value: Optional[str]):
        if value is None:
            if "Manufacturer" in self._dataset:
                del self._dataset.Manufacturer
        else:
            self._dataset.Manufacturer = value

    @property
    def InstitutionName(self) -> Optional[str]:
        if "InstitutionName" in self._dataset:
            return self._dataset.InstitutionName
        return None

    @InstitutionName.setter
    def InstitutionName(self, value: Optional[str]):
        if value is None:
            if "InstitutionName" in self._dataset:
                del self._dataset.InstitutionName
        else:
            self._dataset.InstitutionName = value

    @property
    def InstitutionAddress(self) -> Optional[str]:
        if "InstitutionAddress" in self._dataset:
            return self._dataset.InstitutionAddress
        return None

    @InstitutionAddress.setter
    def InstitutionAddress(self, value: Optional[str]):
        if value is None:
            if "InstitutionAddress" in self._dataset:
                del self._dataset.InstitutionAddress
        else:
            self._dataset.InstitutionAddress = value

    @property
    def StationName(self) -> Optional[str]:
        if "StationName" in self._dataset:
            return self._dataset.StationName
        return None

    @StationName.setter
    def StationName(self, value: Optional[str]):
        if value is None:
            if "StationName" in self._dataset:
                del self._dataset.StationName
        else:
            self._dataset.StationName = value

    @property
    def InstitutionalDepartmentName(self) -> Optional[str]:
        if "InstitutionalDepartmentName" in self._dataset:
            return self._dataset.InstitutionalDepartmentName
        return None

    @InstitutionalDepartmentName.setter
    def InstitutionalDepartmentName(self, value: Optional[str]):
        if value is None:
            if "InstitutionalDepartmentName" in self._dataset:
                del self._dataset.InstitutionalDepartmentName
        else:
            self._dataset.InstitutionalDepartmentName = value

    @property
    def InstitutionalDepartmentTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "InstitutionalDepartmentTypeCodeSequence" in self._dataset:
            if len(self._InstitutionalDepartmentTypeCodeSequence) == len(
                self._dataset.InstitutionalDepartmentTypeCodeSequence
            ):
                return self._InstitutionalDepartmentTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.InstitutionalDepartmentTypeCodeSequence]
        return None

    @InstitutionalDepartmentTypeCodeSequence.setter
    def InstitutionalDepartmentTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._InstitutionalDepartmentTypeCodeSequence = []
            if "InstitutionalDepartmentTypeCodeSequence" in self._dataset:
                del self._dataset.InstitutionalDepartmentTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("InstitutionalDepartmentTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._InstitutionalDepartmentTypeCodeSequence = value
            if "InstitutionalDepartmentTypeCodeSequence" not in self._dataset:
                self._dataset.InstitutionalDepartmentTypeCodeSequence = pydicom.Sequence()
            self._dataset.InstitutionalDepartmentTypeCodeSequence.clear()
            self._dataset.InstitutionalDepartmentTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_InstitutionalDepartmentTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._InstitutionalDepartmentTypeCodeSequence.append(item)
        if "InstitutionalDepartmentTypeCodeSequence" not in self._dataset:
            self._dataset.InstitutionalDepartmentTypeCodeSequence = pydicom.Sequence()
        self._dataset.InstitutionalDepartmentTypeCodeSequence.append(item.to_dataset())

    @property
    def ManufacturerModelName(self) -> Optional[str]:
        if "ManufacturerModelName" in self._dataset:
            return self._dataset.ManufacturerModelName
        return None

    @ManufacturerModelName.setter
    def ManufacturerModelName(self, value: Optional[str]):
        if value is None:
            if "ManufacturerModelName" in self._dataset:
                del self._dataset.ManufacturerModelName
        else:
            self._dataset.ManufacturerModelName = value

    @property
    def DeviceSerialNumber(self) -> Optional[str]:
        if "DeviceSerialNumber" in self._dataset:
            return self._dataset.DeviceSerialNumber
        return None

    @DeviceSerialNumber.setter
    def DeviceSerialNumber(self, value: Optional[str]):
        if value is None:
            if "DeviceSerialNumber" in self._dataset:
                del self._dataset.DeviceSerialNumber
        else:
            self._dataset.DeviceSerialNumber = value

    @property
    def DeviceUID(self) -> Optional[str]:
        if "DeviceUID" in self._dataset:
            return self._dataset.DeviceUID
        return None

    @DeviceUID.setter
    def DeviceUID(self, value: Optional[str]):
        if value is None:
            if "DeviceUID" in self._dataset:
                del self._dataset.DeviceUID
        else:
            self._dataset.DeviceUID = value

    @property
    def GantryID(self) -> Optional[str]:
        if "GantryID" in self._dataset:
            return self._dataset.GantryID
        return None

    @GantryID.setter
    def GantryID(self, value: Optional[str]):
        if value is None:
            if "GantryID" in self._dataset:
                del self._dataset.GantryID
        else:
            self._dataset.GantryID = value

    @property
    def UDISequence(self) -> Optional[List[UDISequenceItem]]:
        if "UDISequence" in self._dataset:
            if len(self._UDISequence) == len(self._dataset.UDISequence):
                return self._UDISequence
            else:
                return [UDISequenceItem(x) for x in self._dataset.UDISequence]
        return None

    @UDISequence.setter
    def UDISequence(self, value: Optional[List[UDISequenceItem]]):
        if value is None:
            self._UDISequence = []
            if "UDISequence" in self._dataset:
                del self._dataset.UDISequence
        elif not isinstance(value, list) or not all(isinstance(item, UDISequenceItem) for item in value):
            raise ValueError("UDISequence must be a list of UDISequenceItem objects")
        else:
            self._UDISequence = value
            if "UDISequence" not in self._dataset:
                self._dataset.UDISequence = pydicom.Sequence()
            self._dataset.UDISequence.clear()
            self._dataset.UDISequence.extend([item.to_dataset() for item in value])

    def add_UDI(self, item: UDISequenceItem):
        if not isinstance(item, UDISequenceItem):
            raise ValueError("Item must be an instance of UDISequenceItem")
        self._UDISequence.append(item)
        if "UDISequence" not in self._dataset:
            self._dataset.UDISequence = pydicom.Sequence()
        self._dataset.UDISequence.append(item.to_dataset())

    @property
    def ManufacturerDeviceClassUID(self) -> Optional[List[str]]:
        if "ManufacturerDeviceClassUID" in self._dataset:
            return self._dataset.ManufacturerDeviceClassUID
        return None

    @ManufacturerDeviceClassUID.setter
    def ManufacturerDeviceClassUID(self, value: Optional[List[str]]):
        if value is None:
            if "ManufacturerDeviceClassUID" in self._dataset:
                del self._dataset.ManufacturerDeviceClassUID
        else:
            self._dataset.ManufacturerDeviceClassUID = value

    @property
    def SoftwareVersions(self) -> Optional[List[str]]:
        if "SoftwareVersions" in self._dataset:
            return self._dataset.SoftwareVersions
        return None

    @SoftwareVersions.setter
    def SoftwareVersions(self, value: Optional[List[str]]):
        if value is None:
            if "SoftwareVersions" in self._dataset:
                del self._dataset.SoftwareVersions
        else:
            self._dataset.SoftwareVersions = value

    @property
    def SpatialResolution(self) -> Optional[Decimal]:
        if "SpatialResolution" in self._dataset:
            return self._dataset.SpatialResolution
        return None

    @SpatialResolution.setter
    def SpatialResolution(self, value: Optional[Decimal]):
        if value is None:
            if "SpatialResolution" in self._dataset:
                del self._dataset.SpatialResolution
        else:
            self._dataset.SpatialResolution = value

    @property
    def DateOfLastCalibration(self) -> Optional[List[str]]:
        if "DateOfLastCalibration" in self._dataset:
            return self._dataset.DateOfLastCalibration
        return None

    @DateOfLastCalibration.setter
    def DateOfLastCalibration(self, value: Optional[List[str]]):
        if value is None:
            if "DateOfLastCalibration" in self._dataset:
                del self._dataset.DateOfLastCalibration
        else:
            self._dataset.DateOfLastCalibration = value

    @property
    def TimeOfLastCalibration(self) -> Optional[List[str]]:
        if "TimeOfLastCalibration" in self._dataset:
            return self._dataset.TimeOfLastCalibration
        return None

    @TimeOfLastCalibration.setter
    def TimeOfLastCalibration(self, value: Optional[List[str]]):
        if value is None:
            if "TimeOfLastCalibration" in self._dataset:
                del self._dataset.TimeOfLastCalibration
        else:
            self._dataset.TimeOfLastCalibration = value

    @property
    def DateOfManufacture(self) -> Optional[str]:
        if "DateOfManufacture" in self._dataset:
            return self._dataset.DateOfManufacture
        return None

    @DateOfManufacture.setter
    def DateOfManufacture(self, value: Optional[str]):
        if value is None:
            if "DateOfManufacture" in self._dataset:
                del self._dataset.DateOfManufacture
        else:
            self._dataset.DateOfManufacture = value

    @property
    def DateOfInstallation(self) -> Optional[str]:
        if "DateOfInstallation" in self._dataset:
            return self._dataset.DateOfInstallation
        return None

    @DateOfInstallation.setter
    def DateOfInstallation(self, value: Optional[str]):
        if value is None:
            if "DateOfInstallation" in self._dataset:
                del self._dataset.DateOfInstallation
        else:
            self._dataset.DateOfInstallation = value

    @property
    def PixelPaddingValue(self) -> Optional[int]:
        if "PixelPaddingValue" in self._dataset:
            return self._dataset.PixelPaddingValue
        return None

    @PixelPaddingValue.setter
    def PixelPaddingValue(self, value: Optional[int]):
        if value is None:
            if "PixelPaddingValue" in self._dataset:
                del self._dataset.PixelPaddingValue
        else:
            self._dataset.PixelPaddingValue = value

    @property
    def GridID(self) -> Optional[str]:
        if "GridID" in self._dataset:
            return self._dataset.GridID
        return None

    @GridID.setter
    def GridID(self, value: Optional[str]):
        if value is None:
            if "GridID" in self._dataset:
                del self._dataset.GridID
        else:
            self._dataset.GridID = value

    @property
    def Grid(self) -> Optional[List[str]]:
        if "Grid" in self._dataset:
            return self._dataset.Grid
        return None

    @Grid.setter
    def Grid(self, value: Optional[List[str]]):
        if value is None:
            if "Grid" in self._dataset:
                del self._dataset.Grid
        else:
            self._dataset.Grid = value

    @property
    def GridAbsorbingMaterial(self) -> Optional[str]:
        if "GridAbsorbingMaterial" in self._dataset:
            return self._dataset.GridAbsorbingMaterial
        return None

    @GridAbsorbingMaterial.setter
    def GridAbsorbingMaterial(self, value: Optional[str]):
        if value is None:
            if "GridAbsorbingMaterial" in self._dataset:
                del self._dataset.GridAbsorbingMaterial
        else:
            self._dataset.GridAbsorbingMaterial = value

    @property
    def GridSpacingMaterial(self) -> Optional[str]:
        if "GridSpacingMaterial" in self._dataset:
            return self._dataset.GridSpacingMaterial
        return None

    @GridSpacingMaterial.setter
    def GridSpacingMaterial(self, value: Optional[str]):
        if value is None:
            if "GridSpacingMaterial" in self._dataset:
                del self._dataset.GridSpacingMaterial
        else:
            self._dataset.GridSpacingMaterial = value

    @property
    def GridThickness(self) -> Optional[Decimal]:
        if "GridThickness" in self._dataset:
            return self._dataset.GridThickness
        return None

    @GridThickness.setter
    def GridThickness(self, value: Optional[Decimal]):
        if value is None:
            if "GridThickness" in self._dataset:
                del self._dataset.GridThickness
        else:
            self._dataset.GridThickness = value

    @property
    def GridPitch(self) -> Optional[Decimal]:
        if "GridPitch" in self._dataset:
            return self._dataset.GridPitch
        return None

    @GridPitch.setter
    def GridPitch(self, value: Optional[Decimal]):
        if value is None:
            if "GridPitch" in self._dataset:
                del self._dataset.GridPitch
        else:
            self._dataset.GridPitch = value

    @property
    def GridAspectRatio(self) -> Optional[List[int]]:
        if "GridAspectRatio" in self._dataset:
            return self._dataset.GridAspectRatio
        return None

    @GridAspectRatio.setter
    def GridAspectRatio(self, value: Optional[List[int]]):
        if value is None:
            if "GridAspectRatio" in self._dataset:
                del self._dataset.GridAspectRatio
        else:
            self._dataset.GridAspectRatio = value

    @property
    def GridPeriod(self) -> Optional[Decimal]:
        if "GridPeriod" in self._dataset:
            return self._dataset.GridPeriod
        return None

    @GridPeriod.setter
    def GridPeriod(self, value: Optional[Decimal]):
        if value is None:
            if "GridPeriod" in self._dataset:
                del self._dataset.GridPeriod
        else:
            self._dataset.GridPeriod = value

    @property
    def GridFocalDistance(self) -> Optional[Decimal]:
        if "GridFocalDistance" in self._dataset:
            return self._dataset.GridFocalDistance
        return None

    @GridFocalDistance.setter
    def GridFocalDistance(self, value: Optional[Decimal]):
        if value is None:
            if "GridFocalDistance" in self._dataset:
                del self._dataset.GridFocalDistance
        else:
            self._dataset.GridFocalDistance = value

    @property
    def StudyDate(self) -> Optional[str]:
        if "StudyDate" in self._dataset:
            return self._dataset.StudyDate
        return None

    @StudyDate.setter
    def StudyDate(self, value: Optional[str]):
        if value is None:
            if "StudyDate" in self._dataset:
                del self._dataset.StudyDate
        else:
            self._dataset.StudyDate = value

    @property
    def StudyTime(self) -> Optional[str]:
        if "StudyTime" in self._dataset:
            return self._dataset.StudyTime
        return None

    @StudyTime.setter
    def StudyTime(self, value: Optional[str]):
        if value is None:
            if "StudyTime" in self._dataset:
                del self._dataset.StudyTime
        else:
            self._dataset.StudyTime = value

    @property
    def AccessionNumber(self) -> Optional[str]:
        if "AccessionNumber" in self._dataset:
            return self._dataset.AccessionNumber
        return None

    @AccessionNumber.setter
    def AccessionNumber(self, value: Optional[str]):
        if value is None:
            if "AccessionNumber" in self._dataset:
                del self._dataset.AccessionNumber
        else:
            self._dataset.AccessionNumber = value

    @property
    def IssuerOfAccessionNumberSequence(self) -> Optional[List[IssuerOfAccessionNumberSequenceItem]]:
        if "IssuerOfAccessionNumberSequence" in self._dataset:
            if len(self._IssuerOfAccessionNumberSequence) == len(self._dataset.IssuerOfAccessionNumberSequence):
                return self._IssuerOfAccessionNumberSequence
            else:
                return [IssuerOfAccessionNumberSequenceItem(x) for x in self._dataset.IssuerOfAccessionNumberSequence]
        return None

    @IssuerOfAccessionNumberSequence.setter
    def IssuerOfAccessionNumberSequence(self, value: Optional[List[IssuerOfAccessionNumberSequenceItem]]):
        if value is None:
            self._IssuerOfAccessionNumberSequence = []
            if "IssuerOfAccessionNumberSequence" in self._dataset:
                del self._dataset.IssuerOfAccessionNumberSequence
        elif not isinstance(value, list) or not all(isinstance(item, IssuerOfAccessionNumberSequenceItem) for item in value):
            raise ValueError("IssuerOfAccessionNumberSequence must be a list of IssuerOfAccessionNumberSequenceItem objects")
        else:
            self._IssuerOfAccessionNumberSequence = value
            if "IssuerOfAccessionNumberSequence" not in self._dataset:
                self._dataset.IssuerOfAccessionNumberSequence = pydicom.Sequence()
            self._dataset.IssuerOfAccessionNumberSequence.clear()
            self._dataset.IssuerOfAccessionNumberSequence.extend([item.to_dataset() for item in value])

    def add_IssuerOfAccessionNumber(self, item: IssuerOfAccessionNumberSequenceItem):
        if not isinstance(item, IssuerOfAccessionNumberSequenceItem):
            raise ValueError("Item must be an instance of IssuerOfAccessionNumberSequenceItem")
        self._IssuerOfAccessionNumberSequence.append(item)
        if "IssuerOfAccessionNumberSequence" not in self._dataset:
            self._dataset.IssuerOfAccessionNumberSequence = pydicom.Sequence()
        self._dataset.IssuerOfAccessionNumberSequence.append(item.to_dataset())

    @property
    def ReferringPhysicianName(self) -> Optional[str]:
        if "ReferringPhysicianName" in self._dataset:
            return self._dataset.ReferringPhysicianName
        return None

    @ReferringPhysicianName.setter
    def ReferringPhysicianName(self, value: Optional[str]):
        if value is None:
            if "ReferringPhysicianName" in self._dataset:
                del self._dataset.ReferringPhysicianName
        else:
            self._dataset.ReferringPhysicianName = value

    @property
    def ReferringPhysicianIdentificationSequence(self) -> Optional[List[ReferringPhysicianIdentificationSequenceItem]]:
        if "ReferringPhysicianIdentificationSequence" in self._dataset:
            if len(self._ReferringPhysicianIdentificationSequence) == len(
                self._dataset.ReferringPhysicianIdentificationSequence
            ):
                return self._ReferringPhysicianIdentificationSequence
            else:
                return [
                    ReferringPhysicianIdentificationSequenceItem(x)
                    for x in self._dataset.ReferringPhysicianIdentificationSequence
                ]
        return None

    @ReferringPhysicianIdentificationSequence.setter
    def ReferringPhysicianIdentificationSequence(self, value: Optional[List[ReferringPhysicianIdentificationSequenceItem]]):
        if value is None:
            self._ReferringPhysicianIdentificationSequence = []
            if "ReferringPhysicianIdentificationSequence" in self._dataset:
                del self._dataset.ReferringPhysicianIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferringPhysicianIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferringPhysicianIdentificationSequence must be a list of ReferringPhysicianIdentificationSequenceItem"
                " objects"
            )
        else:
            self._ReferringPhysicianIdentificationSequence = value
            if "ReferringPhysicianIdentificationSequence" not in self._dataset:
                self._dataset.ReferringPhysicianIdentificationSequence = pydicom.Sequence()
            self._dataset.ReferringPhysicianIdentificationSequence.clear()
            self._dataset.ReferringPhysicianIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_ReferringPhysicianIdentification(self, item: ReferringPhysicianIdentificationSequenceItem):
        if not isinstance(item, ReferringPhysicianIdentificationSequenceItem):
            raise ValueError("Item must be an instance of ReferringPhysicianIdentificationSequenceItem")
        self._ReferringPhysicianIdentificationSequence.append(item)
        if "ReferringPhysicianIdentificationSequence" not in self._dataset:
            self._dataset.ReferringPhysicianIdentificationSequence = pydicom.Sequence()
        self._dataset.ReferringPhysicianIdentificationSequence.append(item.to_dataset())

    @property
    def ConsultingPhysicianName(self) -> Optional[List[str]]:
        if "ConsultingPhysicianName" in self._dataset:
            return self._dataset.ConsultingPhysicianName
        return None

    @ConsultingPhysicianName.setter
    def ConsultingPhysicianName(self, value: Optional[List[str]]):
        if value is None:
            if "ConsultingPhysicianName" in self._dataset:
                del self._dataset.ConsultingPhysicianName
        else:
            self._dataset.ConsultingPhysicianName = value

    @property
    def ConsultingPhysicianIdentificationSequence(self) -> Optional[List[ConsultingPhysicianIdentificationSequenceItem]]:
        if "ConsultingPhysicianIdentificationSequence" in self._dataset:
            if len(self._ConsultingPhysicianIdentificationSequence) == len(
                self._dataset.ConsultingPhysicianIdentificationSequence
            ):
                return self._ConsultingPhysicianIdentificationSequence
            else:
                return [
                    ConsultingPhysicianIdentificationSequenceItem(x)
                    for x in self._dataset.ConsultingPhysicianIdentificationSequence
                ]
        return None

    @ConsultingPhysicianIdentificationSequence.setter
    def ConsultingPhysicianIdentificationSequence(self, value: Optional[List[ConsultingPhysicianIdentificationSequenceItem]]):
        if value is None:
            self._ConsultingPhysicianIdentificationSequence = []
            if "ConsultingPhysicianIdentificationSequence" in self._dataset:
                del self._dataset.ConsultingPhysicianIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ConsultingPhysicianIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                "ConsultingPhysicianIdentificationSequence must be a list of ConsultingPhysicianIdentificationSequenceItem"
                " objects"
            )
        else:
            self._ConsultingPhysicianIdentificationSequence = value
            if "ConsultingPhysicianIdentificationSequence" not in self._dataset:
                self._dataset.ConsultingPhysicianIdentificationSequence = pydicom.Sequence()
            self._dataset.ConsultingPhysicianIdentificationSequence.clear()
            self._dataset.ConsultingPhysicianIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_ConsultingPhysicianIdentification(self, item: ConsultingPhysicianIdentificationSequenceItem):
        if not isinstance(item, ConsultingPhysicianIdentificationSequenceItem):
            raise ValueError("Item must be an instance of ConsultingPhysicianIdentificationSequenceItem")
        self._ConsultingPhysicianIdentificationSequence.append(item)
        if "ConsultingPhysicianIdentificationSequence" not in self._dataset:
            self._dataset.ConsultingPhysicianIdentificationSequence = pydicom.Sequence()
        self._dataset.ConsultingPhysicianIdentificationSequence.append(item.to_dataset())

    @property
    def StudyDescription(self) -> Optional[str]:
        if "StudyDescription" in self._dataset:
            return self._dataset.StudyDescription
        return None

    @StudyDescription.setter
    def StudyDescription(self, value: Optional[str]):
        if value is None:
            if "StudyDescription" in self._dataset:
                del self._dataset.StudyDescription
        else:
            self._dataset.StudyDescription = value

    @property
    def ProcedureCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ProcedureCodeSequence" in self._dataset:
            if len(self._ProcedureCodeSequence) == len(self._dataset.ProcedureCodeSequence):
                return self._ProcedureCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ProcedureCodeSequence]
        return None

    @ProcedureCodeSequence.setter
    def ProcedureCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ProcedureCodeSequence = []
            if "ProcedureCodeSequence" in self._dataset:
                del self._dataset.ProcedureCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("ProcedureCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ProcedureCodeSequence = value
            if "ProcedureCodeSequence" not in self._dataset:
                self._dataset.ProcedureCodeSequence = pydicom.Sequence()
            self._dataset.ProcedureCodeSequence.clear()
            self._dataset.ProcedureCodeSequence.extend([item.to_dataset() for item in value])

    def add_ProcedureCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ProcedureCodeSequence.append(item)
        if "ProcedureCodeSequence" not in self._dataset:
            self._dataset.ProcedureCodeSequence = pydicom.Sequence()
        self._dataset.ProcedureCodeSequence.append(item.to_dataset())

    @property
    def PhysiciansOfRecord(self) -> Optional[List[str]]:
        if "PhysiciansOfRecord" in self._dataset:
            return self._dataset.PhysiciansOfRecord
        return None

    @PhysiciansOfRecord.setter
    def PhysiciansOfRecord(self, value: Optional[List[str]]):
        if value is None:
            if "PhysiciansOfRecord" in self._dataset:
                del self._dataset.PhysiciansOfRecord
        else:
            self._dataset.PhysiciansOfRecord = value

    @property
    def PhysiciansOfRecordIdentificationSequence(self) -> Optional[List[PhysiciansOfRecordIdentificationSequenceItem]]:
        if "PhysiciansOfRecordIdentificationSequence" in self._dataset:
            if len(self._PhysiciansOfRecordIdentificationSequence) == len(
                self._dataset.PhysiciansOfRecordIdentificationSequence
            ):
                return self._PhysiciansOfRecordIdentificationSequence
            else:
                return [
                    PhysiciansOfRecordIdentificationSequenceItem(x)
                    for x in self._dataset.PhysiciansOfRecordIdentificationSequence
                ]
        return None

    @PhysiciansOfRecordIdentificationSequence.setter
    def PhysiciansOfRecordIdentificationSequence(self, value: Optional[List[PhysiciansOfRecordIdentificationSequenceItem]]):
        if value is None:
            self._PhysiciansOfRecordIdentificationSequence = []
            if "PhysiciansOfRecordIdentificationSequence" in self._dataset:
                del self._dataset.PhysiciansOfRecordIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PhysiciansOfRecordIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                "PhysiciansOfRecordIdentificationSequence must be a list of PhysiciansOfRecordIdentificationSequenceItem"
                " objects"
            )
        else:
            self._PhysiciansOfRecordIdentificationSequence = value
            if "PhysiciansOfRecordIdentificationSequence" not in self._dataset:
                self._dataset.PhysiciansOfRecordIdentificationSequence = pydicom.Sequence()
            self._dataset.PhysiciansOfRecordIdentificationSequence.clear()
            self._dataset.PhysiciansOfRecordIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_PhysiciansOfRecordIdentification(self, item: PhysiciansOfRecordIdentificationSequenceItem):
        if not isinstance(item, PhysiciansOfRecordIdentificationSequenceItem):
            raise ValueError("Item must be an instance of PhysiciansOfRecordIdentificationSequenceItem")
        self._PhysiciansOfRecordIdentificationSequence.append(item)
        if "PhysiciansOfRecordIdentificationSequence" not in self._dataset:
            self._dataset.PhysiciansOfRecordIdentificationSequence = pydicom.Sequence()
        self._dataset.PhysiciansOfRecordIdentificationSequence.append(item.to_dataset())

    @property
    def NameOfPhysiciansReadingStudy(self) -> Optional[List[str]]:
        if "NameOfPhysiciansReadingStudy" in self._dataset:
            return self._dataset.NameOfPhysiciansReadingStudy
        return None

    @NameOfPhysiciansReadingStudy.setter
    def NameOfPhysiciansReadingStudy(self, value: Optional[List[str]]):
        if value is None:
            if "NameOfPhysiciansReadingStudy" in self._dataset:
                del self._dataset.NameOfPhysiciansReadingStudy
        else:
            self._dataset.NameOfPhysiciansReadingStudy = value

    @property
    def PhysiciansReadingStudyIdentificationSequence(self) -> Optional[List[PhysiciansReadingStudyIdentificationSequenceItem]]:
        if "PhysiciansReadingStudyIdentificationSequence" in self._dataset:
            if len(self._PhysiciansReadingStudyIdentificationSequence) == len(
                self._dataset.PhysiciansReadingStudyIdentificationSequence
            ):
                return self._PhysiciansReadingStudyIdentificationSequence
            else:
                return [
                    PhysiciansReadingStudyIdentificationSequenceItem(x)
                    for x in self._dataset.PhysiciansReadingStudyIdentificationSequence
                ]
        return None

    @PhysiciansReadingStudyIdentificationSequence.setter
    def PhysiciansReadingStudyIdentificationSequence(
        self, value: Optional[List[PhysiciansReadingStudyIdentificationSequenceItem]]
    ):
        if value is None:
            self._PhysiciansReadingStudyIdentificationSequence = []
            if "PhysiciansReadingStudyIdentificationSequence" in self._dataset:
                del self._dataset.PhysiciansReadingStudyIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PhysiciansReadingStudyIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                "PhysiciansReadingStudyIdentificationSequence must be a list of"
                " PhysiciansReadingStudyIdentificationSequenceItem objects"
            )
        else:
            self._PhysiciansReadingStudyIdentificationSequence = value
            if "PhysiciansReadingStudyIdentificationSequence" not in self._dataset:
                self._dataset.PhysiciansReadingStudyIdentificationSequence = pydicom.Sequence()
            self._dataset.PhysiciansReadingStudyIdentificationSequence.clear()
            self._dataset.PhysiciansReadingStudyIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_PhysiciansReadingStudyIdentification(self, item: PhysiciansReadingStudyIdentificationSequenceItem):
        if not isinstance(item, PhysiciansReadingStudyIdentificationSequenceItem):
            raise ValueError("Item must be an instance of PhysiciansReadingStudyIdentificationSequenceItem")
        self._PhysiciansReadingStudyIdentificationSequence.append(item)
        if "PhysiciansReadingStudyIdentificationSequence" not in self._dataset:
            self._dataset.PhysiciansReadingStudyIdentificationSequence = pydicom.Sequence()
        self._dataset.PhysiciansReadingStudyIdentificationSequence.append(item.to_dataset())

    @property
    def ReferencedStudySequence(self) -> Optional[List[ReferencedStudySequenceItem]]:
        if "ReferencedStudySequence" in self._dataset:
            if len(self._ReferencedStudySequence) == len(self._dataset.ReferencedStudySequence):
                return self._ReferencedStudySequence
            else:
                return [ReferencedStudySequenceItem(x) for x in self._dataset.ReferencedStudySequence]
        return None

    @ReferencedStudySequence.setter
    def ReferencedStudySequence(self, value: Optional[List[ReferencedStudySequenceItem]]):
        if value is None:
            self._ReferencedStudySequence = []
            if "ReferencedStudySequence" in self._dataset:
                del self._dataset.ReferencedStudySequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedStudySequenceItem) for item in value):
            raise ValueError("ReferencedStudySequence must be a list of ReferencedStudySequenceItem objects")
        else:
            self._ReferencedStudySequence = value
            if "ReferencedStudySequence" not in self._dataset:
                self._dataset.ReferencedStudySequence = pydicom.Sequence()
            self._dataset.ReferencedStudySequence.clear()
            self._dataset.ReferencedStudySequence.extend([item.to_dataset() for item in value])

    def add_ReferencedStudy(self, item: ReferencedStudySequenceItem):
        if not isinstance(item, ReferencedStudySequenceItem):
            raise ValueError("Item must be an instance of ReferencedStudySequenceItem")
        self._ReferencedStudySequence.append(item)
        if "ReferencedStudySequence" not in self._dataset:
            self._dataset.ReferencedStudySequence = pydicom.Sequence()
        self._dataset.ReferencedStudySequence.append(item.to_dataset())

    @property
    def StudyInstanceUID(self) -> Optional[str]:
        if "StudyInstanceUID" in self._dataset:
            return self._dataset.StudyInstanceUID
        return None

    @StudyInstanceUID.setter
    def StudyInstanceUID(self, value: Optional[str]):
        if value is None:
            if "StudyInstanceUID" in self._dataset:
                del self._dataset.StudyInstanceUID
        else:
            self._dataset.StudyInstanceUID = value

    @property
    def StudyID(self) -> Optional[str]:
        if "StudyID" in self._dataset:
            return self._dataset.StudyID
        return None

    @StudyID.setter
    def StudyID(self, value: Optional[str]):
        if value is None:
            if "StudyID" in self._dataset:
                del self._dataset.StudyID
        else:
            self._dataset.StudyID = value

    @property
    def RequestingService(self) -> Optional[str]:
        if "RequestingService" in self._dataset:
            return self._dataset.RequestingService
        return None

    @RequestingService.setter
    def RequestingService(self, value: Optional[str]):
        if value is None:
            if "RequestingService" in self._dataset:
                del self._dataset.RequestingService
        else:
            self._dataset.RequestingService = value

    @property
    def RequestingServiceCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RequestingServiceCodeSequence" in self._dataset:
            if len(self._RequestingServiceCodeSequence) == len(self._dataset.RequestingServiceCodeSequence):
                return self._RequestingServiceCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RequestingServiceCodeSequence]
        return None

    @RequestingServiceCodeSequence.setter
    def RequestingServiceCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RequestingServiceCodeSequence = []
            if "RequestingServiceCodeSequence" in self._dataset:
                del self._dataset.RequestingServiceCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("RequestingServiceCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RequestingServiceCodeSequence = value
            if "RequestingServiceCodeSequence" not in self._dataset:
                self._dataset.RequestingServiceCodeSequence = pydicom.Sequence()
            self._dataset.RequestingServiceCodeSequence.clear()
            self._dataset.RequestingServiceCodeSequence.extend([item.to_dataset() for item in value])

    def add_RequestingServiceCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._RequestingServiceCodeSequence.append(item)
        if "RequestingServiceCodeSequence" not in self._dataset:
            self._dataset.RequestingServiceCodeSequence = pydicom.Sequence()
        self._dataset.RequestingServiceCodeSequence.append(item.to_dataset())

    @property
    def ReasonForPerformedProcedureCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ReasonForPerformedProcedureCodeSequence" in self._dataset:
            if len(self._ReasonForPerformedProcedureCodeSequence) == len(
                self._dataset.ReasonForPerformedProcedureCodeSequence
            ):
                return self._ReasonForPerformedProcedureCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ReasonForPerformedProcedureCodeSequence]
        return None

    @ReasonForPerformedProcedureCodeSequence.setter
    def ReasonForPerformedProcedureCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ReasonForPerformedProcedureCodeSequence = []
            if "ReasonForPerformedProcedureCodeSequence" in self._dataset:
                del self._dataset.ReasonForPerformedProcedureCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("ReasonForPerformedProcedureCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ReasonForPerformedProcedureCodeSequence = value
            if "ReasonForPerformedProcedureCodeSequence" not in self._dataset:
                self._dataset.ReasonForPerformedProcedureCodeSequence = pydicom.Sequence()
            self._dataset.ReasonForPerformedProcedureCodeSequence.clear()
            self._dataset.ReasonForPerformedProcedureCodeSequence.extend([item.to_dataset() for item in value])

    def add_ReasonForPerformedProcedureCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ReasonForPerformedProcedureCodeSequence.append(item)
        if "ReasonForPerformedProcedureCodeSequence" not in self._dataset:
            self._dataset.ReasonForPerformedProcedureCodeSequence = pydicom.Sequence()
        self._dataset.ReasonForPerformedProcedureCodeSequence.append(item.to_dataset())

    @property
    def SamplesPerPixel(self) -> Optional[int]:
        if "SamplesPerPixel" in self._dataset:
            return self._dataset.SamplesPerPixel
        return None

    @SamplesPerPixel.setter
    def SamplesPerPixel(self, value: Optional[int]):
        if value is None:
            if "SamplesPerPixel" in self._dataset:
                del self._dataset.SamplesPerPixel
        else:
            self._dataset.SamplesPerPixel = value

    @property
    def PhotometricInterpretation(self) -> Optional[str]:
        if "PhotometricInterpretation" in self._dataset:
            return self._dataset.PhotometricInterpretation
        return None

    @PhotometricInterpretation.setter
    def PhotometricInterpretation(self, value: Optional[str]):
        if value is None:
            if "PhotometricInterpretation" in self._dataset:
                del self._dataset.PhotometricInterpretation
        else:
            self._dataset.PhotometricInterpretation = value

    @property
    def PlanarConfiguration(self) -> Optional[int]:
        if "PlanarConfiguration" in self._dataset:
            return self._dataset.PlanarConfiguration
        return None

    @PlanarConfiguration.setter
    def PlanarConfiguration(self, value: Optional[int]):
        if value is None:
            if "PlanarConfiguration" in self._dataset:
                del self._dataset.PlanarConfiguration
        else:
            self._dataset.PlanarConfiguration = value

    @property
    def Rows(self) -> Optional[int]:
        if "Rows" in self._dataset:
            return self._dataset.Rows
        return None

    @Rows.setter
    def Rows(self, value: Optional[int]):
        if value is None:
            if "Rows" in self._dataset:
                del self._dataset.Rows
        else:
            self._dataset.Rows = value

    @property
    def Columns(self) -> Optional[int]:
        if "Columns" in self._dataset:
            return self._dataset.Columns
        return None

    @Columns.setter
    def Columns(self, value: Optional[int]):
        if value is None:
            if "Columns" in self._dataset:
                del self._dataset.Columns
        else:
            self._dataset.Columns = value

    @property
    def PixelAspectRatio(self) -> Optional[List[int]]:
        if "PixelAspectRatio" in self._dataset:
            return self._dataset.PixelAspectRatio
        return None

    @PixelAspectRatio.setter
    def PixelAspectRatio(self, value: Optional[List[int]]):
        if value is None:
            if "PixelAspectRatio" in self._dataset:
                del self._dataset.PixelAspectRatio
        else:
            self._dataset.PixelAspectRatio = value

    @property
    def BitsAllocated(self) -> Optional[int]:
        if "BitsAllocated" in self._dataset:
            return self._dataset.BitsAllocated
        return None

    @BitsAllocated.setter
    def BitsAllocated(self, value: Optional[int]):
        if value is None:
            if "BitsAllocated" in self._dataset:
                del self._dataset.BitsAllocated
        else:
            self._dataset.BitsAllocated = value

    @property
    def BitsStored(self) -> Optional[int]:
        if "BitsStored" in self._dataset:
            return self._dataset.BitsStored
        return None

    @BitsStored.setter
    def BitsStored(self, value: Optional[int]):
        if value is None:
            if "BitsStored" in self._dataset:
                del self._dataset.BitsStored
        else:
            self._dataset.BitsStored = value

    @property
    def HighBit(self) -> Optional[int]:
        if "HighBit" in self._dataset:
            return self._dataset.HighBit
        return None

    @HighBit.setter
    def HighBit(self, value: Optional[int]):
        if value is None:
            if "HighBit" in self._dataset:
                del self._dataset.HighBit
        else:
            self._dataset.HighBit = value

    @property
    def PixelRepresentation(self) -> Optional[int]:
        if "PixelRepresentation" in self._dataset:
            return self._dataset.PixelRepresentation
        return None

    @PixelRepresentation.setter
    def PixelRepresentation(self, value: Optional[int]):
        if value is None:
            if "PixelRepresentation" in self._dataset:
                del self._dataset.PixelRepresentation
        else:
            self._dataset.PixelRepresentation = value

    @property
    def SmallestImagePixelValue(self) -> Optional[int]:
        if "SmallestImagePixelValue" in self._dataset:
            return self._dataset.SmallestImagePixelValue
        return None

    @SmallestImagePixelValue.setter
    def SmallestImagePixelValue(self, value: Optional[int]):
        if value is None:
            if "SmallestImagePixelValue" in self._dataset:
                del self._dataset.SmallestImagePixelValue
        else:
            self._dataset.SmallestImagePixelValue = value

    @property
    def LargestImagePixelValue(self) -> Optional[int]:
        if "LargestImagePixelValue" in self._dataset:
            return self._dataset.LargestImagePixelValue
        return None

    @LargestImagePixelValue.setter
    def LargestImagePixelValue(self, value: Optional[int]):
        if value is None:
            if "LargestImagePixelValue" in self._dataset:
                del self._dataset.LargestImagePixelValue
        else:
            self._dataset.LargestImagePixelValue = value

    @property
    def PixelPaddingRangeLimit(self) -> Optional[int]:
        if "PixelPaddingRangeLimit" in self._dataset:
            return self._dataset.PixelPaddingRangeLimit
        return None

    @PixelPaddingRangeLimit.setter
    def PixelPaddingRangeLimit(self, value: Optional[int]):
        if value is None:
            if "PixelPaddingRangeLimit" in self._dataset:
                del self._dataset.PixelPaddingRangeLimit
        else:
            self._dataset.PixelPaddingRangeLimit = value

    @property
    def RedPaletteColorLookupTableDescriptor(self) -> Optional[List[int]]:
        if "RedPaletteColorLookupTableDescriptor" in self._dataset:
            return self._dataset.RedPaletteColorLookupTableDescriptor
        return None

    @RedPaletteColorLookupTableDescriptor.setter
    def RedPaletteColorLookupTableDescriptor(self, value: Optional[List[int]]):
        if value is None:
            if "RedPaletteColorLookupTableDescriptor" in self._dataset:
                del self._dataset.RedPaletteColorLookupTableDescriptor
        else:
            self._dataset.RedPaletteColorLookupTableDescriptor = value

    @property
    def GreenPaletteColorLookupTableDescriptor(self) -> Optional[List[int]]:
        if "GreenPaletteColorLookupTableDescriptor" in self._dataset:
            return self._dataset.GreenPaletteColorLookupTableDescriptor
        return None

    @GreenPaletteColorLookupTableDescriptor.setter
    def GreenPaletteColorLookupTableDescriptor(self, value: Optional[List[int]]):
        if value is None:
            if "GreenPaletteColorLookupTableDescriptor" in self._dataset:
                del self._dataset.GreenPaletteColorLookupTableDescriptor
        else:
            self._dataset.GreenPaletteColorLookupTableDescriptor = value

    @property
    def BluePaletteColorLookupTableDescriptor(self) -> Optional[List[int]]:
        if "BluePaletteColorLookupTableDescriptor" in self._dataset:
            return self._dataset.BluePaletteColorLookupTableDescriptor
        return None

    @BluePaletteColorLookupTableDescriptor.setter
    def BluePaletteColorLookupTableDescriptor(self, value: Optional[List[int]]):
        if value is None:
            if "BluePaletteColorLookupTableDescriptor" in self._dataset:
                del self._dataset.BluePaletteColorLookupTableDescriptor
        else:
            self._dataset.BluePaletteColorLookupTableDescriptor = value

    @property
    def RedPaletteColorLookupTableData(self) -> Optional[bytes]:
        if "RedPaletteColorLookupTableData" in self._dataset:
            return self._dataset.RedPaletteColorLookupTableData
        return None

    @RedPaletteColorLookupTableData.setter
    def RedPaletteColorLookupTableData(self, value: Optional[bytes]):
        if value is None:
            if "RedPaletteColorLookupTableData" in self._dataset:
                del self._dataset.RedPaletteColorLookupTableData
        else:
            self._dataset.RedPaletteColorLookupTableData = value

    @property
    def GreenPaletteColorLookupTableData(self) -> Optional[bytes]:
        if "GreenPaletteColorLookupTableData" in self._dataset:
            return self._dataset.GreenPaletteColorLookupTableData
        return None

    @GreenPaletteColorLookupTableData.setter
    def GreenPaletteColorLookupTableData(self, value: Optional[bytes]):
        if value is None:
            if "GreenPaletteColorLookupTableData" in self._dataset:
                del self._dataset.GreenPaletteColorLookupTableData
        else:
            self._dataset.GreenPaletteColorLookupTableData = value

    @property
    def BluePaletteColorLookupTableData(self) -> Optional[bytes]:
        if "BluePaletteColorLookupTableData" in self._dataset:
            return self._dataset.BluePaletteColorLookupTableData
        return None

    @BluePaletteColorLookupTableData.setter
    def BluePaletteColorLookupTableData(self, value: Optional[bytes]):
        if value is None:
            if "BluePaletteColorLookupTableData" in self._dataset:
                del self._dataset.BluePaletteColorLookupTableData
        else:
            self._dataset.BluePaletteColorLookupTableData = value

    @property
    def ICCProfile(self) -> Optional[bytes]:
        if "ICCProfile" in self._dataset:
            return self._dataset.ICCProfile
        return None

    @ICCProfile.setter
    def ICCProfile(self, value: Optional[bytes]):
        if value is None:
            if "ICCProfile" in self._dataset:
                del self._dataset.ICCProfile
        else:
            self._dataset.ICCProfile = value

    @property
    def ColorSpace(self) -> Optional[str]:
        if "ColorSpace" in self._dataset:
            return self._dataset.ColorSpace
        return None

    @ColorSpace.setter
    def ColorSpace(self, value: Optional[str]):
        if value is None:
            if "ColorSpace" in self._dataset:
                del self._dataset.ColorSpace
        else:
            self._dataset.ColorSpace = value

    @property
    def PixelDataProviderURL(self) -> Optional[str]:
        if "PixelDataProviderURL" in self._dataset:
            return self._dataset.PixelDataProviderURL
        return None

    @PixelDataProviderURL.setter
    def PixelDataProviderURL(self, value: Optional[str]):
        if value is None:
            if "PixelDataProviderURL" in self._dataset:
                del self._dataset.PixelDataProviderURL
        else:
            self._dataset.PixelDataProviderURL = value

    @property
    def ExtendedOffsetTable(self) -> Optional[bytes]:
        if "ExtendedOffsetTable" in self._dataset:
            return self._dataset.ExtendedOffsetTable
        return None

    @ExtendedOffsetTable.setter
    def ExtendedOffsetTable(self, value: Optional[bytes]):
        if value is None:
            if "ExtendedOffsetTable" in self._dataset:
                del self._dataset.ExtendedOffsetTable
        else:
            self._dataset.ExtendedOffsetTable = value

    @property
    def ExtendedOffsetTableLengths(self) -> Optional[bytes]:
        if "ExtendedOffsetTableLengths" in self._dataset:
            return self._dataset.ExtendedOffsetTableLengths
        return None

    @ExtendedOffsetTableLengths.setter
    def ExtendedOffsetTableLengths(self, value: Optional[bytes]):
        if value is None:
            if "ExtendedOffsetTableLengths" in self._dataset:
                del self._dataset.ExtendedOffsetTableLengths
        else:
            self._dataset.ExtendedOffsetTableLengths = value

    @property
    def PixelData(self) -> Optional[bytes]:
        if "PixelData" in self._dataset:
            return self._dataset.PixelData
        return None

    @PixelData.setter
    def PixelData(self, value: Optional[bytes]):
        if value is None:
            if "PixelData" in self._dataset:
                del self._dataset.PixelData
        else:
            self._dataset.PixelData = value

    @property
    def AnatomicRegionSequence(self) -> Optional[List[AnatomicRegionSequenceItem]]:
        if "AnatomicRegionSequence" in self._dataset:
            if len(self._AnatomicRegionSequence) == len(self._dataset.AnatomicRegionSequence):
                return self._AnatomicRegionSequence
            else:
                return [AnatomicRegionSequenceItem(x) for x in self._dataset.AnatomicRegionSequence]
        return None

    @AnatomicRegionSequence.setter
    def AnatomicRegionSequence(self, value: Optional[List[AnatomicRegionSequenceItem]]):
        if value is None:
            self._AnatomicRegionSequence = []
            if "AnatomicRegionSequence" in self._dataset:
                del self._dataset.AnatomicRegionSequence
        elif not isinstance(value, list) or not all(isinstance(item, AnatomicRegionSequenceItem) for item in value):
            raise ValueError("AnatomicRegionSequence must be a list of AnatomicRegionSequenceItem objects")
        else:
            self._AnatomicRegionSequence = value
            if "AnatomicRegionSequence" not in self._dataset:
                self._dataset.AnatomicRegionSequence = pydicom.Sequence()
            self._dataset.AnatomicRegionSequence.clear()
            self._dataset.AnatomicRegionSequence.extend([item.to_dataset() for item in value])

    def add_AnatomicRegion(self, item: AnatomicRegionSequenceItem):
        if not isinstance(item, AnatomicRegionSequenceItem):
            raise ValueError("Item must be an instance of AnatomicRegionSequenceItem")
        self._AnatomicRegionSequence.append(item)
        if "AnatomicRegionSequence" not in self._dataset:
            self._dataset.AnatomicRegionSequence = pydicom.Sequence()
        self._dataset.AnatomicRegionSequence.append(item.to_dataset())

    @property
    def PrimaryAnatomicStructureSequence(self) -> Optional[List[PrimaryAnatomicStructureSequenceItem]]:
        if "PrimaryAnatomicStructureSequence" in self._dataset:
            if len(self._PrimaryAnatomicStructureSequence) == len(self._dataset.PrimaryAnatomicStructureSequence):
                return self._PrimaryAnatomicStructureSequence
            else:
                return [PrimaryAnatomicStructureSequenceItem(x) for x in self._dataset.PrimaryAnatomicStructureSequence]
        return None

    @PrimaryAnatomicStructureSequence.setter
    def PrimaryAnatomicStructureSequence(self, value: Optional[List[PrimaryAnatomicStructureSequenceItem]]):
        if value is None:
            self._PrimaryAnatomicStructureSequence = []
            if "PrimaryAnatomicStructureSequence" in self._dataset:
                del self._dataset.PrimaryAnatomicStructureSequence
        elif not isinstance(value, list) or not all(isinstance(item, PrimaryAnatomicStructureSequenceItem) for item in value):
            raise ValueError("PrimaryAnatomicStructureSequence must be a list of PrimaryAnatomicStructureSequenceItem objects")
        else:
            self._PrimaryAnatomicStructureSequence = value
            if "PrimaryAnatomicStructureSequence" not in self._dataset:
                self._dataset.PrimaryAnatomicStructureSequence = pydicom.Sequence()
            self._dataset.PrimaryAnatomicStructureSequence.clear()
            self._dataset.PrimaryAnatomicStructureSequence.extend([item.to_dataset() for item in value])

    def add_PrimaryAnatomicStructure(self, item: PrimaryAnatomicStructureSequenceItem):
        if not isinstance(item, PrimaryAnatomicStructureSequenceItem):
            raise ValueError("Item must be an instance of PrimaryAnatomicStructureSequenceItem")
        self._PrimaryAnatomicStructureSequence.append(item)
        if "PrimaryAnatomicStructureSequence" not in self._dataset:
            self._dataset.PrimaryAnatomicStructureSequence = pydicom.Sequence()
        self._dataset.PrimaryAnatomicStructureSequence.append(item.to_dataset())

    @property
    def ImageLaterality(self) -> Optional[str]:
        if "ImageLaterality" in self._dataset:
            return self._dataset.ImageLaterality
        return None

    @ImageLaterality.setter
    def ImageLaterality(self, value: Optional[str]):
        if value is None:
            if "ImageLaterality" in self._dataset:
                del self._dataset.ImageLaterality
        else:
            self._dataset.ImageLaterality = value

    @property
    def FrameOfReferenceUID(self) -> Optional[str]:
        if "FrameOfReferenceUID" in self._dataset:
            return self._dataset.FrameOfReferenceUID
        return None

    @FrameOfReferenceUID.setter
    def FrameOfReferenceUID(self, value: Optional[str]):
        if value is None:
            if "FrameOfReferenceUID" in self._dataset:
                del self._dataset.FrameOfReferenceUID
        else:
            self._dataset.FrameOfReferenceUID = value

    @property
    def PositionReferenceIndicator(self) -> Optional[str]:
        if "PositionReferenceIndicator" in self._dataset:
            return self._dataset.PositionReferenceIndicator
        return None

    @PositionReferenceIndicator.setter
    def PositionReferenceIndicator(self, value: Optional[str]):
        if value is None:
            if "PositionReferenceIndicator" in self._dataset:
                del self._dataset.PositionReferenceIndicator
        else:
            self._dataset.PositionReferenceIndicator = value

    @property
    def HistogramSequence(self) -> Optional[List[HistogramSequenceItem]]:
        if "HistogramSequence" in self._dataset:
            if len(self._HistogramSequence) == len(self._dataset.HistogramSequence):
                return self._HistogramSequence
            else:
                return [HistogramSequenceItem(x) for x in self._dataset.HistogramSequence]
        return None

    @HistogramSequence.setter
    def HistogramSequence(self, value: Optional[List[HistogramSequenceItem]]):
        if value is None:
            self._HistogramSequence = []
            if "HistogramSequence" in self._dataset:
                del self._dataset.HistogramSequence
        elif not isinstance(value, list) or not all(isinstance(item, HistogramSequenceItem) for item in value):
            raise ValueError("HistogramSequence must be a list of HistogramSequenceItem objects")
        else:
            self._HistogramSequence = value
            if "HistogramSequence" not in self._dataset:
                self._dataset.HistogramSequence = pydicom.Sequence()
            self._dataset.HistogramSequence.clear()
            self._dataset.HistogramSequence.extend([item.to_dataset() for item in value])

    def add_Histogram(self, item: HistogramSequenceItem):
        if not isinstance(item, HistogramSequenceItem):
            raise ValueError("Item must be an instance of HistogramSequenceItem")
        self._HistogramSequence.append(item)
        if "HistogramSequence" not in self._dataset:
            self._dataset.HistogramSequence = pydicom.Sequence()
        self._dataset.HistogramSequence.append(item.to_dataset())

    @property
    def AcquisitionContextSequence(self) -> Optional[List[AcquisitionContextSequenceItem]]:
        if "AcquisitionContextSequence" in self._dataset:
            if len(self._AcquisitionContextSequence) == len(self._dataset.AcquisitionContextSequence):
                return self._AcquisitionContextSequence
            else:
                return [AcquisitionContextSequenceItem(x) for x in self._dataset.AcquisitionContextSequence]
        return None

    @AcquisitionContextSequence.setter
    def AcquisitionContextSequence(self, value: Optional[List[AcquisitionContextSequenceItem]]):
        if value is None:
            self._AcquisitionContextSequence = []
            if "AcquisitionContextSequence" in self._dataset:
                del self._dataset.AcquisitionContextSequence
        elif not isinstance(value, list) or not all(isinstance(item, AcquisitionContextSequenceItem) for item in value):
            raise ValueError("AcquisitionContextSequence must be a list of AcquisitionContextSequenceItem objects")
        else:
            self._AcquisitionContextSequence = value
            if "AcquisitionContextSequence" not in self._dataset:
                self._dataset.AcquisitionContextSequence = pydicom.Sequence()
            self._dataset.AcquisitionContextSequence.clear()
            self._dataset.AcquisitionContextSequence.extend([item.to_dataset() for item in value])

    def add_AcquisitionContext(self, item: AcquisitionContextSequenceItem):
        if not isinstance(item, AcquisitionContextSequenceItem):
            raise ValueError("Item must be an instance of AcquisitionContextSequenceItem")
        self._AcquisitionContextSequence.append(item)
        if "AcquisitionContextSequence" not in self._dataset:
            self._dataset.AcquisitionContextSequence = pydicom.Sequence()
        self._dataset.AcquisitionContextSequence.append(item.to_dataset())

    @property
    def AcquisitionContextDescription(self) -> Optional[str]:
        if "AcquisitionContextDescription" in self._dataset:
            return self._dataset.AcquisitionContextDescription
        return None

    @AcquisitionContextDescription.setter
    def AcquisitionContextDescription(self, value: Optional[str]):
        if value is None:
            if "AcquisitionContextDescription" in self._dataset:
                del self._dataset.AcquisitionContextDescription
        else:
            self._dataset.AcquisitionContextDescription = value

    @property
    def ImageType(self) -> Optional[List[str]]:
        if "ImageType" in self._dataset:
            return self._dataset.ImageType
        return None

    @ImageType.setter
    def ImageType(self, value: Optional[List[str]]):
        if value is None:
            if "ImageType" in self._dataset:
                del self._dataset.ImageType
        else:
            self._dataset.ImageType = value

    @property
    def ContentDate(self) -> Optional[str]:
        if "ContentDate" in self._dataset:
            return self._dataset.ContentDate
        return None

    @ContentDate.setter
    def ContentDate(self, value: Optional[str]):
        if value is None:
            if "ContentDate" in self._dataset:
                del self._dataset.ContentDate
        else:
            self._dataset.ContentDate = value

    @property
    def ContentTime(self) -> Optional[str]:
        if "ContentTime" in self._dataset:
            return self._dataset.ContentTime
        return None

    @ContentTime.setter
    def ContentTime(self, value: Optional[str]):
        if value is None:
            if "ContentTime" in self._dataset:
                del self._dataset.ContentTime
        else:
            self._dataset.ContentTime = value

    @property
    def AnatomicRegionSequence(self) -> Optional[List[AnatomicRegionSequenceItem]]:
        if "AnatomicRegionSequence" in self._dataset:
            if len(self._AnatomicRegionSequence) == len(self._dataset.AnatomicRegionSequence):
                return self._AnatomicRegionSequence
            else:
                return [AnatomicRegionSequenceItem(x) for x in self._dataset.AnatomicRegionSequence]
        return None

    @AnatomicRegionSequence.setter
    def AnatomicRegionSequence(self, value: Optional[List[AnatomicRegionSequenceItem]]):
        if value is None:
            self._AnatomicRegionSequence = []
            if "AnatomicRegionSequence" in self._dataset:
                del self._dataset.AnatomicRegionSequence
        elif not isinstance(value, list) or not all(isinstance(item, AnatomicRegionSequenceItem) for item in value):
            raise ValueError("AnatomicRegionSequence must be a list of AnatomicRegionSequenceItem objects")
        else:
            self._AnatomicRegionSequence = value
            if "AnatomicRegionSequence" not in self._dataset:
                self._dataset.AnatomicRegionSequence = pydicom.Sequence()
            self._dataset.AnatomicRegionSequence.clear()
            self._dataset.AnatomicRegionSequence.extend([item.to_dataset() for item in value])

    def PrimaryAnatomicStructureSequence(self) -> Optional[List[PrimaryAnatomicStructureSequenceItem]]:
        if "PrimaryAnatomicStructureSequence" in self._dataset:
            if len(self._PrimaryAnatomicStructureSequence) == len(self._dataset.PrimaryAnatomicStructureSequence):
                return self._PrimaryAnatomicStructureSequence
            else:
                return [PrimaryAnatomicStructureSequenceItem(x) for x in self._dataset.PrimaryAnatomicStructureSequence]
        return None

    @PrimaryAnatomicStructureSequence.setter
    def PrimaryAnatomicStructureSequence(self, value: Optional[List[PrimaryAnatomicStructureSequenceItem]]):
        if value is None:
            self._PrimaryAnatomicStructureSequence = []
            if "PrimaryAnatomicStructureSequence" in self._dataset:
                del self._dataset.PrimaryAnatomicStructureSequence
        elif not isinstance(value, list) or not all(isinstance(item, PrimaryAnatomicStructureSequenceItem) for item in value):
            raise ValueError("PrimaryAnatomicStructureSequence must be a list of PrimaryAnatomicStructureSequenceItem objects")
        else:
            self._PrimaryAnatomicStructureSequence = value
            if "PrimaryAnatomicStructureSequence" not in self._dataset:
                self._dataset.PrimaryAnatomicStructureSequence = pydicom.Sequence()
            self._dataset.PrimaryAnatomicStructureSequence.clear()
            self._dataset.PrimaryAnatomicStructureSequence.extend([item.to_dataset() for item in value])

    def InstanceNumber(self) -> Optional[int]:
        if "InstanceNumber" in self._dataset:
            return self._dataset.InstanceNumber
        return None

    @InstanceNumber.setter
    def InstanceNumber(self, value: Optional[int]):
        if value is None:
            if "InstanceNumber" in self._dataset:
                del self._dataset.InstanceNumber
        else:
            self._dataset.InstanceNumber = value

    @property
    def PatientOrientation(self) -> Optional[List[str]]:
        if "PatientOrientation" in self._dataset:
            return self._dataset.PatientOrientation
        return None

    @PatientOrientation.setter
    def PatientOrientation(self, value: Optional[List[str]]):
        if value is None:
            if "PatientOrientation" in self._dataset:
                del self._dataset.PatientOrientation
        else:
            self._dataset.PatientOrientation = value

    @property
    def ImageLaterality(self) -> Optional[str]:
        if "ImageLaterality" in self._dataset:
            return self._dataset.ImageLaterality
        return None

    @ImageLaterality.setter
    def ImageLaterality(self, value: Optional[str]):
        if value is None:
            if "ImageLaterality" in self._dataset:
                del self._dataset.ImageLaterality
        else:
            self._dataset.ImageLaterality = value

    @property
    def ImageComments(self) -> Optional[str]:
        if "ImageComments" in self._dataset:
            return self._dataset.ImageComments
        return None

    @ImageComments.setter
    def ImageComments(self, value: Optional[str]):
        if value is None:
            if "ImageComments" in self._dataset:
                del self._dataset.ImageComments
        else:
            self._dataset.ImageComments = value

    @property
    def QualityControlImage(self) -> Optional[str]:
        if "QualityControlImage" in self._dataset:
            return self._dataset.QualityControlImage
        return None

    @QualityControlImage.setter
    def QualityControlImage(self, value: Optional[str]):
        if value is None:
            if "QualityControlImage" in self._dataset:
                del self._dataset.QualityControlImage
        else:
            self._dataset.QualityControlImage = value

    @property
    def BurnedInAnnotation(self) -> Optional[str]:
        if "BurnedInAnnotation" in self._dataset:
            return self._dataset.BurnedInAnnotation
        return None

    @BurnedInAnnotation.setter
    def BurnedInAnnotation(self, value: Optional[str]):
        if value is None:
            if "BurnedInAnnotation" in self._dataset:
                del self._dataset.BurnedInAnnotation
        else:
            self._dataset.BurnedInAnnotation = value

    @property
    def RecognizableVisualFeatures(self) -> Optional[str]:
        if "RecognizableVisualFeatures" in self._dataset:
            return self._dataset.RecognizableVisualFeatures
        return None

    @RecognizableVisualFeatures.setter
    def RecognizableVisualFeatures(self, value: Optional[str]):
        if value is None:
            if "RecognizableVisualFeatures" in self._dataset:
                del self._dataset.RecognizableVisualFeatures
        else:
            self._dataset.RecognizableVisualFeatures = value

    @property
    def LossyImageCompression(self) -> Optional[str]:
        if "LossyImageCompression" in self._dataset:
            return self._dataset.LossyImageCompression
        return None

    @LossyImageCompression.setter
    def LossyImageCompression(self, value: Optional[str]):
        if value is None:
            if "LossyImageCompression" in self._dataset:
                del self._dataset.LossyImageCompression
        else:
            self._dataset.LossyImageCompression = value

    @property
    def LossyImageCompressionRatio(self) -> Optional[List[Decimal]]:
        if "LossyImageCompressionRatio" in self._dataset:
            return self._dataset.LossyImageCompressionRatio
        return None

    @LossyImageCompressionRatio.setter
    def LossyImageCompressionRatio(self, value: Optional[List[Decimal]]):
        if value is None:
            if "LossyImageCompressionRatio" in self._dataset:
                del self._dataset.LossyImageCompressionRatio
        else:
            self._dataset.LossyImageCompressionRatio = value

    @property
    def LossyImageCompressionMethod(self) -> Optional[List[str]]:
        if "LossyImageCompressionMethod" in self._dataset:
            return self._dataset.LossyImageCompressionMethod
        return None

    @LossyImageCompressionMethod.setter
    def LossyImageCompressionMethod(self, value: Optional[List[str]]):
        if value is None:
            if "LossyImageCompressionMethod" in self._dataset:
                del self._dataset.LossyImageCompressionMethod
        else:
            self._dataset.LossyImageCompressionMethod = value

    @property
    def RealWorldValueMappingSequence(self) -> Optional[List[RealWorldValueMappingSequenceItem]]:
        if "RealWorldValueMappingSequence" in self._dataset:
            if len(self._RealWorldValueMappingSequence) == len(self._dataset.RealWorldValueMappingSequence):
                return self._RealWorldValueMappingSequence
            else:
                return [RealWorldValueMappingSequenceItem(x) for x in self._dataset.RealWorldValueMappingSequence]
        return None

    @RealWorldValueMappingSequence.setter
    def RealWorldValueMappingSequence(self, value: Optional[List[RealWorldValueMappingSequenceItem]]):
        if value is None:
            self._RealWorldValueMappingSequence = []
            if "RealWorldValueMappingSequence" in self._dataset:
                del self._dataset.RealWorldValueMappingSequence
        elif not isinstance(value, list) or not all(isinstance(item, RealWorldValueMappingSequenceItem) for item in value):
            raise ValueError("RealWorldValueMappingSequence must be a list of RealWorldValueMappingSequenceItem objects")
        else:
            self._RealWorldValueMappingSequence = value
            if "RealWorldValueMappingSequence" not in self._dataset:
                self._dataset.RealWorldValueMappingSequence = pydicom.Sequence()
            self._dataset.RealWorldValueMappingSequence.clear()
            self._dataset.RealWorldValueMappingSequence.extend([item.to_dataset() for item in value])

    def add_RealWorldValueMapping(self, item: RealWorldValueMappingSequenceItem):
        if not isinstance(item, RealWorldValueMappingSequenceItem):
            raise ValueError("Item must be an instance of RealWorldValueMappingSequenceItem")
        self._RealWorldValueMappingSequence.append(item)
        if "RealWorldValueMappingSequence" not in self._dataset:
            self._dataset.RealWorldValueMappingSequence = pydicom.Sequence()
        self._dataset.RealWorldValueMappingSequence.append(item.to_dataset())

    @property
    def IconImageSequence(self) -> Optional[List[IconImageSequenceItem]]:
        if "IconImageSequence" in self._dataset:
            if len(self._IconImageSequence) == len(self._dataset.IconImageSequence):
                return self._IconImageSequence
            else:
                return [IconImageSequenceItem(x) for x in self._dataset.IconImageSequence]
        return None

    @IconImageSequence.setter
    def IconImageSequence(self, value: Optional[List[IconImageSequenceItem]]):
        if value is None:
            self._IconImageSequence = []
            if "IconImageSequence" in self._dataset:
                del self._dataset.IconImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, IconImageSequenceItem) for item in value):
            raise ValueError("IconImageSequence must be a list of IconImageSequenceItem objects")
        else:
            self._IconImageSequence = value
            if "IconImageSequence" not in self._dataset:
                self._dataset.IconImageSequence = pydicom.Sequence()
            self._dataset.IconImageSequence.clear()
            self._dataset.IconImageSequence.extend([item.to_dataset() for item in value])

    def add_IconImage(self, item: IconImageSequenceItem):
        if not isinstance(item, IconImageSequenceItem):
            raise ValueError("Item must be an instance of IconImageSequenceItem")
        self._IconImageSequence.append(item)
        if "IconImageSequence" not in self._dataset:
            self._dataset.IconImageSequence = pydicom.Sequence()
        self._dataset.IconImageSequence.append(item.to_dataset())

    @property
    def PresentationLUTShape(self) -> Optional[str]:
        if "PresentationLUTShape" in self._dataset:
            return self._dataset.PresentationLUTShape
        return None

    @PresentationLUTShape.setter
    def PresentationLUTShape(self, value: Optional[str]):
        if value is None:
            if "PresentationLUTShape" in self._dataset:
                del self._dataset.PresentationLUTShape
        else:
            self._dataset.PresentationLUTShape = value

    @property
    def KVP(self) -> Optional[Decimal]:
        if "KVP" in self._dataset:
            return self._dataset.KVP
        return None

    @KVP.setter
    def KVP(self, value: Optional[Decimal]):
        if value is None:
            if "KVP" in self._dataset:
                del self._dataset.KVP
        else:
            self._dataset.KVP = value

    @property
    def GeneratorID(self) -> Optional[str]:
        if "GeneratorID" in self._dataset:
            return self._dataset.GeneratorID
        return None

    @GeneratorID.setter
    def GeneratorID(self, value: Optional[str]):
        if value is None:
            if "GeneratorID" in self._dataset:
                del self._dataset.GeneratorID
        else:
            self._dataset.GeneratorID = value

    @property
    def ExposureTime(self) -> Optional[int]:
        if "ExposureTime" in self._dataset:
            return self._dataset.ExposureTime
        return None

    @ExposureTime.setter
    def ExposureTime(self, value: Optional[int]):
        if value is None:
            if "ExposureTime" in self._dataset:
                del self._dataset.ExposureTime
        else:
            self._dataset.ExposureTime = value

    @property
    def XRayTubeCurrent(self) -> Optional[int]:
        if "XRayTubeCurrent" in self._dataset:
            return self._dataset.XRayTubeCurrent
        return None

    @XRayTubeCurrent.setter
    def XRayTubeCurrent(self, value: Optional[int]):
        if value is None:
            if "XRayTubeCurrent" in self._dataset:
                del self._dataset.XRayTubeCurrent
        else:
            self._dataset.XRayTubeCurrent = value

    @property
    def Exposure(self) -> Optional[int]:
        if "Exposure" in self._dataset:
            return self._dataset.Exposure
        return None

    @Exposure.setter
    def Exposure(self, value: Optional[int]):
        if value is None:
            if "Exposure" in self._dataset:
                del self._dataset.Exposure
        else:
            self._dataset.Exposure = value

    @property
    def ExposureInuAs(self) -> Optional[int]:
        if "ExposureInuAs" in self._dataset:
            return self._dataset.ExposureInuAs
        return None

    @ExposureInuAs.setter
    def ExposureInuAs(self, value: Optional[int]):
        if value is None:
            if "ExposureInuAs" in self._dataset:
                del self._dataset.ExposureInuAs
        else:
            self._dataset.ExposureInuAs = value

    @property
    def RectificationType(self) -> Optional[str]:
        if "RectificationType" in self._dataset:
            return self._dataset.RectificationType
        return None

    @RectificationType.setter
    def RectificationType(self, value: Optional[str]):
        if value is None:
            if "RectificationType" in self._dataset:
                del self._dataset.RectificationType
        else:
            self._dataset.RectificationType = value

    @property
    def FocalSpots(self) -> Optional[List[Decimal]]:
        if "FocalSpots" in self._dataset:
            return self._dataset.FocalSpots
        return None

    @FocalSpots.setter
    def FocalSpots(self, value: Optional[List[Decimal]]):
        if value is None:
            if "FocalSpots" in self._dataset:
                del self._dataset.FocalSpots
        else:
            self._dataset.FocalSpots = value

    @property
    def AnodeTargetMaterial(self) -> Optional[str]:
        if "AnodeTargetMaterial" in self._dataset:
            return self._dataset.AnodeTargetMaterial
        return None

    @AnodeTargetMaterial.setter
    def AnodeTargetMaterial(self, value: Optional[str]):
        if value is None:
            if "AnodeTargetMaterial" in self._dataset:
                del self._dataset.AnodeTargetMaterial
        else:
            self._dataset.AnodeTargetMaterial = value

    @property
    def ExposureControlMode(self) -> Optional[str]:
        if "ExposureControlMode" in self._dataset:
            return self._dataset.ExposureControlMode
        return None

    @ExposureControlMode.setter
    def ExposureControlMode(self, value: Optional[str]):
        if value is None:
            if "ExposureControlMode" in self._dataset:
                del self._dataset.ExposureControlMode
        else:
            self._dataset.ExposureControlMode = value

    @property
    def ExposureControlModeDescription(self) -> Optional[str]:
        if "ExposureControlModeDescription" in self._dataset:
            return self._dataset.ExposureControlModeDescription
        return None

    @ExposureControlModeDescription.setter
    def ExposureControlModeDescription(self, value: Optional[str]):
        if value is None:
            if "ExposureControlModeDescription" in self._dataset:
                del self._dataset.ExposureControlModeDescription
        else:
            self._dataset.ExposureControlModeDescription = value

    @property
    def ExposureStatus(self) -> Optional[str]:
        if "ExposureStatus" in self._dataset:
            return self._dataset.ExposureStatus
        return None

    @ExposureStatus.setter
    def ExposureStatus(self, value: Optional[str]):
        if value is None:
            if "ExposureStatus" in self._dataset:
                del self._dataset.ExposureStatus
        else:
            self._dataset.ExposureStatus = value

    @property
    def PhototimerSetting(self) -> Optional[Decimal]:
        if "PhototimerSetting" in self._dataset:
            return self._dataset.PhototimerSetting
        return None

    @PhototimerSetting.setter
    def PhototimerSetting(self, value: Optional[Decimal]):
        if value is None:
            if "PhototimerSetting" in self._dataset:
                del self._dataset.PhototimerSetting
        else:
            self._dataset.PhototimerSetting = value

    @property
    def ExposureTimeInuS(self) -> Optional[Decimal]:
        if "ExposureTimeInuS" in self._dataset:
            return self._dataset.ExposureTimeInuS
        return None

    @ExposureTimeInuS.setter
    def ExposureTimeInuS(self, value: Optional[Decimal]):
        if value is None:
            if "ExposureTimeInuS" in self._dataset:
                del self._dataset.ExposureTimeInuS
        else:
            self._dataset.ExposureTimeInuS = value

    @property
    def XRayTubeCurrentInuA(self) -> Optional[Decimal]:
        if "XRayTubeCurrentInuA" in self._dataset:
            return self._dataset.XRayTubeCurrentInuA
        return None

    @XRayTubeCurrentInuA.setter
    def XRayTubeCurrentInuA(self, value: Optional[Decimal]):
        if value is None:
            if "XRayTubeCurrentInuA" in self._dataset:
                del self._dataset.XRayTubeCurrentInuA
        else:
            self._dataset.XRayTubeCurrentInuA = value

    @property
    def FilterType(self) -> Optional[str]:
        if "FilterType" in self._dataset:
            return self._dataset.FilterType
        return None

    @FilterType.setter
    def FilterType(self, value: Optional[str]):
        if value is None:
            if "FilterType" in self._dataset:
                del self._dataset.FilterType
        else:
            self._dataset.FilterType = value

    @property
    def FilterMaterial(self) -> Optional[List[str]]:
        if "FilterMaterial" in self._dataset:
            return self._dataset.FilterMaterial
        return None

    @FilterMaterial.setter
    def FilterMaterial(self, value: Optional[List[str]]):
        if value is None:
            if "FilterMaterial" in self._dataset:
                del self._dataset.FilterMaterial
        else:
            self._dataset.FilterMaterial = value

    @property
    def FilterThicknessMinimum(self) -> Optional[List[Decimal]]:
        if "FilterThicknessMinimum" in self._dataset:
            return self._dataset.FilterThicknessMinimum
        return None

    @FilterThicknessMinimum.setter
    def FilterThicknessMinimum(self, value: Optional[List[Decimal]]):
        if value is None:
            if "FilterThicknessMinimum" in self._dataset:
                del self._dataset.FilterThicknessMinimum
        else:
            self._dataset.FilterThicknessMinimum = value

    @property
    def FilterThicknessMaximum(self) -> Optional[List[Decimal]]:
        if "FilterThicknessMaximum" in self._dataset:
            return self._dataset.FilterThicknessMaximum
        return None

    @FilterThicknessMaximum.setter
    def FilterThicknessMaximum(self, value: Optional[List[Decimal]]):
        if value is None:
            if "FilterThicknessMaximum" in self._dataset:
                del self._dataset.FilterThicknessMaximum
        else:
            self._dataset.FilterThicknessMaximum = value

    @property
    def FilterBeamPathLengthMinimum(self) -> Optional[List[float]]:
        if "FilterBeamPathLengthMinimum" in self._dataset:
            return self._dataset.FilterBeamPathLengthMinimum
        return None

    @FilterBeamPathLengthMinimum.setter
    def FilterBeamPathLengthMinimum(self, value: Optional[List[float]]):
        if value is None:
            if "FilterBeamPathLengthMinimum" in self._dataset:
                del self._dataset.FilterBeamPathLengthMinimum
        else:
            self._dataset.FilterBeamPathLengthMinimum = value

    @property
    def FilterBeamPathLengthMaximum(self) -> Optional[List[float]]:
        if "FilterBeamPathLengthMaximum" in self._dataset:
            return self._dataset.FilterBeamPathLengthMaximum
        return None

    @FilterBeamPathLengthMaximum.setter
    def FilterBeamPathLengthMaximum(self, value: Optional[List[float]]):
        if value is None:
            if "FilterBeamPathLengthMaximum" in self._dataset:
                del self._dataset.FilterBeamPathLengthMaximum
        else:
            self._dataset.FilterBeamPathLengthMaximum = value

    @property
    def AnatomicRegionSequence(self) -> Optional[List[AnatomicRegionSequenceItem]]:
        if "AnatomicRegionSequence" in self._dataset:
            if len(self._AnatomicRegionSequence) == len(self._dataset.AnatomicRegionSequence):
                return self._AnatomicRegionSequence
            else:
                return [AnatomicRegionSequenceItem(x) for x in self._dataset.AnatomicRegionSequence]
        return None

    @AnatomicRegionSequence.setter
    def AnatomicRegionSequence(self, value: Optional[List[AnatomicRegionSequenceItem]]):
        if value is None:
            self._AnatomicRegionSequence = []
            if "AnatomicRegionSequence" in self._dataset:
                del self._dataset.AnatomicRegionSequence
        elif not isinstance(value, list) or not all(isinstance(item, AnatomicRegionSequenceItem) for item in value):
            raise ValueError("AnatomicRegionSequence must be a list of AnatomicRegionSequenceItem objects")
        else:
            self._AnatomicRegionSequence = value
            if "AnatomicRegionSequence" not in self._dataset:
                self._dataset.AnatomicRegionSequence = pydicom.Sequence()
            self._dataset.AnatomicRegionSequence.clear()
            self._dataset.AnatomicRegionSequence.extend([item.to_dataset() for item in value])

    def PrimaryAnatomicStructureSequence(self) -> Optional[List[PrimaryAnatomicStructureSequenceItem]]:
        if "PrimaryAnatomicStructureSequence" in self._dataset:
            if len(self._PrimaryAnatomicStructureSequence) == len(self._dataset.PrimaryAnatomicStructureSequence):
                return self._PrimaryAnatomicStructureSequence
            else:
                return [PrimaryAnatomicStructureSequenceItem(x) for x in self._dataset.PrimaryAnatomicStructureSequence]
        return None

    @PrimaryAnatomicStructureSequence.setter
    def PrimaryAnatomicStructureSequence(self, value: Optional[List[PrimaryAnatomicStructureSequenceItem]]):
        if value is None:
            self._PrimaryAnatomicStructureSequence = []
            if "PrimaryAnatomicStructureSequence" in self._dataset:
                del self._dataset.PrimaryAnatomicStructureSequence
        elif not isinstance(value, list) or not all(isinstance(item, PrimaryAnatomicStructureSequenceItem) for item in value):
            raise ValueError("PrimaryAnatomicStructureSequence must be a list of PrimaryAnatomicStructureSequenceItem objects")
        else:
            self._PrimaryAnatomicStructureSequence = value
            if "PrimaryAnatomicStructureSequence" not in self._dataset:
                self._dataset.PrimaryAnatomicStructureSequence = pydicom.Sequence()
            self._dataset.PrimaryAnatomicStructureSequence.clear()
            self._dataset.PrimaryAnatomicStructureSequence.extend([item.to_dataset() for item in value])

    def PositionerType(self) -> Optional[str]:
        if "PositionerType" in self._dataset:
            return self._dataset.PositionerType
        return None

    @PositionerType.setter
    def PositionerType(self, value: Optional[str]):
        if value is None:
            if "PositionerType" in self._dataset:
                del self._dataset.PositionerType
        else:
            self._dataset.PositionerType = value

    @property
    def ImageLaterality(self) -> Optional[str]:
        if "ImageLaterality" in self._dataset:
            return self._dataset.ImageLaterality
        return None

    @ImageLaterality.setter
    def ImageLaterality(self, value: Optional[str]):
        if value is None:
            if "ImageLaterality" in self._dataset:
                del self._dataset.ImageLaterality
        else:
            self._dataset.ImageLaterality = value

    @property
    def AdmittingDiagnosesDescription(self) -> Optional[List[str]]:
        if "AdmittingDiagnosesDescription" in self._dataset:
            return self._dataset.AdmittingDiagnosesDescription
        return None

    @AdmittingDiagnosesDescription.setter
    def AdmittingDiagnosesDescription(self, value: Optional[List[str]]):
        if value is None:
            if "AdmittingDiagnosesDescription" in self._dataset:
                del self._dataset.AdmittingDiagnosesDescription
        else:
            self._dataset.AdmittingDiagnosesDescription = value

    @property
    def AdmittingDiagnosesCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "AdmittingDiagnosesCodeSequence" in self._dataset:
            if len(self._AdmittingDiagnosesCodeSequence) == len(self._dataset.AdmittingDiagnosesCodeSequence):
                return self._AdmittingDiagnosesCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.AdmittingDiagnosesCodeSequence]
        return None

    @AdmittingDiagnosesCodeSequence.setter
    def AdmittingDiagnosesCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._AdmittingDiagnosesCodeSequence = []
            if "AdmittingDiagnosesCodeSequence" in self._dataset:
                del self._dataset.AdmittingDiagnosesCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("AdmittingDiagnosesCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._AdmittingDiagnosesCodeSequence = value
            if "AdmittingDiagnosesCodeSequence" not in self._dataset:
                self._dataset.AdmittingDiagnosesCodeSequence = pydicom.Sequence()
            self._dataset.AdmittingDiagnosesCodeSequence.clear()
            self._dataset.AdmittingDiagnosesCodeSequence.extend([item.to_dataset() for item in value])

    def add_AdmittingDiagnosesCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._AdmittingDiagnosesCodeSequence.append(item)
        if "AdmittingDiagnosesCodeSequence" not in self._dataset:
            self._dataset.AdmittingDiagnosesCodeSequence = pydicom.Sequence()
        self._dataset.AdmittingDiagnosesCodeSequence.append(item.to_dataset())

    @property
    def PatientAge(self) -> Optional[str]:
        if "PatientAge" in self._dataset:
            return self._dataset.PatientAge
        return None

    @PatientAge.setter
    def PatientAge(self, value: Optional[str]):
        if value is None:
            if "PatientAge" in self._dataset:
                del self._dataset.PatientAge
        else:
            self._dataset.PatientAge = value

    @property
    def PatientSize(self) -> Optional[Decimal]:
        if "PatientSize" in self._dataset:
            return self._dataset.PatientSize
        return None

    @PatientSize.setter
    def PatientSize(self, value: Optional[Decimal]):
        if value is None:
            if "PatientSize" in self._dataset:
                del self._dataset.PatientSize
        else:
            self._dataset.PatientSize = value

    @property
    def PatientSizeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PatientSizeCodeSequence" in self._dataset:
            if len(self._PatientSizeCodeSequence) == len(self._dataset.PatientSizeCodeSequence):
                return self._PatientSizeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PatientSizeCodeSequence]
        return None

    @PatientSizeCodeSequence.setter
    def PatientSizeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PatientSizeCodeSequence = []
            if "PatientSizeCodeSequence" in self._dataset:
                del self._dataset.PatientSizeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("PatientSizeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PatientSizeCodeSequence = value
            if "PatientSizeCodeSequence" not in self._dataset:
                self._dataset.PatientSizeCodeSequence = pydicom.Sequence()
            self._dataset.PatientSizeCodeSequence.clear()
            self._dataset.PatientSizeCodeSequence.extend([item.to_dataset() for item in value])

    def add_PatientSizeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._PatientSizeCodeSequence.append(item)
        if "PatientSizeCodeSequence" not in self._dataset:
            self._dataset.PatientSizeCodeSequence = pydicom.Sequence()
        self._dataset.PatientSizeCodeSequence.append(item.to_dataset())

    @property
    def PatientBodyMassIndex(self) -> Optional[Decimal]:
        if "PatientBodyMassIndex" in self._dataset:
            return self._dataset.PatientBodyMassIndex
        return None

    @PatientBodyMassIndex.setter
    def PatientBodyMassIndex(self, value: Optional[Decimal]):
        if value is None:
            if "PatientBodyMassIndex" in self._dataset:
                del self._dataset.PatientBodyMassIndex
        else:
            self._dataset.PatientBodyMassIndex = value

    @property
    def MeasuredAPDimension(self) -> Optional[Decimal]:
        if "MeasuredAPDimension" in self._dataset:
            return self._dataset.MeasuredAPDimension
        return None

    @MeasuredAPDimension.setter
    def MeasuredAPDimension(self, value: Optional[Decimal]):
        if value is None:
            if "MeasuredAPDimension" in self._dataset:
                del self._dataset.MeasuredAPDimension
        else:
            self._dataset.MeasuredAPDimension = value

    @property
    def MeasuredLateralDimension(self) -> Optional[Decimal]:
        if "MeasuredLateralDimension" in self._dataset:
            return self._dataset.MeasuredLateralDimension
        return None

    @MeasuredLateralDimension.setter
    def MeasuredLateralDimension(self, value: Optional[Decimal]):
        if value is None:
            if "MeasuredLateralDimension" in self._dataset:
                del self._dataset.MeasuredLateralDimension
        else:
            self._dataset.MeasuredLateralDimension = value

    @property
    def PatientWeight(self) -> Optional[Decimal]:
        if "PatientWeight" in self._dataset:
            return self._dataset.PatientWeight
        return None

    @PatientWeight.setter
    def PatientWeight(self, value: Optional[Decimal]):
        if value is None:
            if "PatientWeight" in self._dataset:
                del self._dataset.PatientWeight
        else:
            self._dataset.PatientWeight = value

    @property
    def MedicalAlerts(self) -> Optional[List[str]]:
        if "MedicalAlerts" in self._dataset:
            return self._dataset.MedicalAlerts
        return None

    @MedicalAlerts.setter
    def MedicalAlerts(self, value: Optional[List[str]]):
        if value is None:
            if "MedicalAlerts" in self._dataset:
                del self._dataset.MedicalAlerts
        else:
            self._dataset.MedicalAlerts = value

    @property
    def Allergies(self) -> Optional[List[str]]:
        if "Allergies" in self._dataset:
            return self._dataset.Allergies
        return None

    @Allergies.setter
    def Allergies(self, value: Optional[List[str]]):
        if value is None:
            if "Allergies" in self._dataset:
                del self._dataset.Allergies
        else:
            self._dataset.Allergies = value

    @property
    def Occupation(self) -> Optional[str]:
        if "Occupation" in self._dataset:
            return self._dataset.Occupation
        return None

    @Occupation.setter
    def Occupation(self, value: Optional[str]):
        if value is None:
            if "Occupation" in self._dataset:
                del self._dataset.Occupation
        else:
            self._dataset.Occupation = value

    @property
    def SmokingStatus(self) -> Optional[str]:
        if "SmokingStatus" in self._dataset:
            return self._dataset.SmokingStatus
        return None

    @SmokingStatus.setter
    def SmokingStatus(self, value: Optional[str]):
        if value is None:
            if "SmokingStatus" in self._dataset:
                del self._dataset.SmokingStatus
        else:
            self._dataset.SmokingStatus = value

    @property
    def AdditionalPatientHistory(self) -> Optional[str]:
        if "AdditionalPatientHistory" in self._dataset:
            return self._dataset.AdditionalPatientHistory
        return None

    @AdditionalPatientHistory.setter
    def AdditionalPatientHistory(self, value: Optional[str]):
        if value is None:
            if "AdditionalPatientHistory" in self._dataset:
                del self._dataset.AdditionalPatientHistory
        else:
            self._dataset.AdditionalPatientHistory = value

    @property
    def PregnancyStatus(self) -> Optional[int]:
        if "PregnancyStatus" in self._dataset:
            return self._dataset.PregnancyStatus
        return None

    @PregnancyStatus.setter
    def PregnancyStatus(self, value: Optional[int]):
        if value is None:
            if "PregnancyStatus" in self._dataset:
                del self._dataset.PregnancyStatus
        else:
            self._dataset.PregnancyStatus = value

    @property
    def LastMenstrualDate(self) -> Optional[str]:
        if "LastMenstrualDate" in self._dataset:
            return self._dataset.LastMenstrualDate
        return None

    @LastMenstrualDate.setter
    def LastMenstrualDate(self, value: Optional[str]):
        if value is None:
            if "LastMenstrualDate" in self._dataset:
                del self._dataset.LastMenstrualDate
        else:
            self._dataset.LastMenstrualDate = value

    @property
    def PatientSexNeutered(self) -> Optional[str]:
        if "PatientSexNeutered" in self._dataset:
            return self._dataset.PatientSexNeutered
        return None

    @PatientSexNeutered.setter
    def PatientSexNeutered(self, value: Optional[str]):
        if value is None:
            if "PatientSexNeutered" in self._dataset:
                del self._dataset.PatientSexNeutered
        else:
            self._dataset.PatientSexNeutered = value

    @property
    def ReasonForVisit(self) -> Optional[str]:
        if "ReasonForVisit" in self._dataset:
            return self._dataset.ReasonForVisit
        return None

    @ReasonForVisit.setter
    def ReasonForVisit(self, value: Optional[str]):
        if value is None:
            if "ReasonForVisit" in self._dataset:
                del self._dataset.ReasonForVisit
        else:
            self._dataset.ReasonForVisit = value

    @property
    def ReasonForVisitCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ReasonForVisitCodeSequence" in self._dataset:
            if len(self._ReasonForVisitCodeSequence) == len(self._dataset.ReasonForVisitCodeSequence):
                return self._ReasonForVisitCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ReasonForVisitCodeSequence]
        return None

    @ReasonForVisitCodeSequence.setter
    def ReasonForVisitCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ReasonForVisitCodeSequence = []
            if "ReasonForVisitCodeSequence" in self._dataset:
                del self._dataset.ReasonForVisitCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("ReasonForVisitCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ReasonForVisitCodeSequence = value
            if "ReasonForVisitCodeSequence" not in self._dataset:
                self._dataset.ReasonForVisitCodeSequence = pydicom.Sequence()
            self._dataset.ReasonForVisitCodeSequence.clear()
            self._dataset.ReasonForVisitCodeSequence.extend([item.to_dataset() for item in value])

    def add_ReasonForVisitCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ReasonForVisitCodeSequence.append(item)
        if "ReasonForVisitCodeSequence" not in self._dataset:
            self._dataset.ReasonForVisitCodeSequence = pydicom.Sequence()
        self._dataset.ReasonForVisitCodeSequence.append(item.to_dataset())

    @property
    def AdmissionID(self) -> Optional[str]:
        if "AdmissionID" in self._dataset:
            return self._dataset.AdmissionID
        return None

    @AdmissionID.setter
    def AdmissionID(self, value: Optional[str]):
        if value is None:
            if "AdmissionID" in self._dataset:
                del self._dataset.AdmissionID
        else:
            self._dataset.AdmissionID = value

    @property
    def IssuerOfAdmissionIDSequence(self) -> Optional[List[IssuerOfAdmissionIDSequenceItem]]:
        if "IssuerOfAdmissionIDSequence" in self._dataset:
            if len(self._IssuerOfAdmissionIDSequence) == len(self._dataset.IssuerOfAdmissionIDSequence):
                return self._IssuerOfAdmissionIDSequence
            else:
                return [IssuerOfAdmissionIDSequenceItem(x) for x in self._dataset.IssuerOfAdmissionIDSequence]
        return None

    @IssuerOfAdmissionIDSequence.setter
    def IssuerOfAdmissionIDSequence(self, value: Optional[List[IssuerOfAdmissionIDSequenceItem]]):
        if value is None:
            self._IssuerOfAdmissionIDSequence = []
            if "IssuerOfAdmissionIDSequence" in self._dataset:
                del self._dataset.IssuerOfAdmissionIDSequence
        elif not isinstance(value, list) or not all(isinstance(item, IssuerOfAdmissionIDSequenceItem) for item in value):
            raise ValueError("IssuerOfAdmissionIDSequence must be a list of IssuerOfAdmissionIDSequenceItem objects")
        else:
            self._IssuerOfAdmissionIDSequence = value
            if "IssuerOfAdmissionIDSequence" not in self._dataset:
                self._dataset.IssuerOfAdmissionIDSequence = pydicom.Sequence()
            self._dataset.IssuerOfAdmissionIDSequence.clear()
            self._dataset.IssuerOfAdmissionIDSequence.extend([item.to_dataset() for item in value])

    def add_IssuerOfAdmissionID(self, item: IssuerOfAdmissionIDSequenceItem):
        if not isinstance(item, IssuerOfAdmissionIDSequenceItem):
            raise ValueError("Item must be an instance of IssuerOfAdmissionIDSequenceItem")
        self._IssuerOfAdmissionIDSequence.append(item)
        if "IssuerOfAdmissionIDSequence" not in self._dataset:
            self._dataset.IssuerOfAdmissionIDSequence = pydicom.Sequence()
        self._dataset.IssuerOfAdmissionIDSequence.append(item.to_dataset())

    @property
    def ServiceEpisodeID(self) -> Optional[str]:
        if "ServiceEpisodeID" in self._dataset:
            return self._dataset.ServiceEpisodeID
        return None

    @ServiceEpisodeID.setter
    def ServiceEpisodeID(self, value: Optional[str]):
        if value is None:
            if "ServiceEpisodeID" in self._dataset:
                del self._dataset.ServiceEpisodeID
        else:
            self._dataset.ServiceEpisodeID = value

    @property
    def ServiceEpisodeDescription(self) -> Optional[str]:
        if "ServiceEpisodeDescription" in self._dataset:
            return self._dataset.ServiceEpisodeDescription
        return None

    @ServiceEpisodeDescription.setter
    def ServiceEpisodeDescription(self, value: Optional[str]):
        if value is None:
            if "ServiceEpisodeDescription" in self._dataset:
                del self._dataset.ServiceEpisodeDescription
        else:
            self._dataset.ServiceEpisodeDescription = value

    @property
    def IssuerOfServiceEpisodeIDSequence(self) -> Optional[List[IssuerOfServiceEpisodeIDSequenceItem]]:
        if "IssuerOfServiceEpisodeIDSequence" in self._dataset:
            if len(self._IssuerOfServiceEpisodeIDSequence) == len(self._dataset.IssuerOfServiceEpisodeIDSequence):
                return self._IssuerOfServiceEpisodeIDSequence
            else:
                return [IssuerOfServiceEpisodeIDSequenceItem(x) for x in self._dataset.IssuerOfServiceEpisodeIDSequence]
        return None

    @IssuerOfServiceEpisodeIDSequence.setter
    def IssuerOfServiceEpisodeIDSequence(self, value: Optional[List[IssuerOfServiceEpisodeIDSequenceItem]]):
        if value is None:
            self._IssuerOfServiceEpisodeIDSequence = []
            if "IssuerOfServiceEpisodeIDSequence" in self._dataset:
                del self._dataset.IssuerOfServiceEpisodeIDSequence
        elif not isinstance(value, list) or not all(isinstance(item, IssuerOfServiceEpisodeIDSequenceItem) for item in value):
            raise ValueError("IssuerOfServiceEpisodeIDSequence must be a list of IssuerOfServiceEpisodeIDSequenceItem objects")
        else:
            self._IssuerOfServiceEpisodeIDSequence = value
            if "IssuerOfServiceEpisodeIDSequence" not in self._dataset:
                self._dataset.IssuerOfServiceEpisodeIDSequence = pydicom.Sequence()
            self._dataset.IssuerOfServiceEpisodeIDSequence.clear()
            self._dataset.IssuerOfServiceEpisodeIDSequence.extend([item.to_dataset() for item in value])

    def add_IssuerOfServiceEpisodeID(self, item: IssuerOfServiceEpisodeIDSequenceItem):
        if not isinstance(item, IssuerOfServiceEpisodeIDSequenceItem):
            raise ValueError("Item must be an instance of IssuerOfServiceEpisodeIDSequenceItem")
        self._IssuerOfServiceEpisodeIDSequence.append(item)
        if "IssuerOfServiceEpisodeIDSequence" not in self._dataset:
            self._dataset.IssuerOfServiceEpisodeIDSequence = pydicom.Sequence()
        self._dataset.IssuerOfServiceEpisodeIDSequence.append(item.to_dataset())

    @property
    def PatientState(self) -> Optional[str]:
        if "PatientState" in self._dataset:
            return self._dataset.PatientState
        return None

    @PatientState.setter
    def PatientState(self, value: Optional[str]):
        if value is None:
            if "PatientState" in self._dataset:
                del self._dataset.PatientState
        else:
            self._dataset.PatientState = value

    @property
    def InterventionSequence(self) -> Optional[List[InterventionSequenceItem]]:
        if "InterventionSequence" in self._dataset:
            if len(self._InterventionSequence) == len(self._dataset.InterventionSequence):
                return self._InterventionSequence
            else:
                return [InterventionSequenceItem(x) for x in self._dataset.InterventionSequence]
        return None

    @InterventionSequence.setter
    def InterventionSequence(self, value: Optional[List[InterventionSequenceItem]]):
        if value is None:
            self._InterventionSequence = []
            if "InterventionSequence" in self._dataset:
                del self._dataset.InterventionSequence
        elif not isinstance(value, list) or not all(isinstance(item, InterventionSequenceItem) for item in value):
            raise ValueError("InterventionSequence must be a list of InterventionSequenceItem objects")
        else:
            self._InterventionSequence = value
            if "InterventionSequence" not in self._dataset:
                self._dataset.InterventionSequence = pydicom.Sequence()
            self._dataset.InterventionSequence.clear()
            self._dataset.InterventionSequence.extend([item.to_dataset() for item in value])

    def add_Intervention(self, item: InterventionSequenceItem):
        if not isinstance(item, InterventionSequenceItem):
            raise ValueError("Item must be an instance of InterventionSequenceItem")
        self._InterventionSequence.append(item)
        if "InterventionSequence" not in self._dataset:
            self._dataset.InterventionSequence = pydicom.Sequence()
        self._dataset.InterventionSequence.append(item.to_dataset())

    @property
    def WindowCenter(self) -> Optional[List[Decimal]]:
        if "WindowCenter" in self._dataset:
            return self._dataset.WindowCenter
        return None

    @WindowCenter.setter
    def WindowCenter(self, value: Optional[List[Decimal]]):
        if value is None:
            if "WindowCenter" in self._dataset:
                del self._dataset.WindowCenter
        else:
            self._dataset.WindowCenter = value

    @property
    def WindowWidth(self) -> Optional[List[Decimal]]:
        if "WindowWidth" in self._dataset:
            return self._dataset.WindowWidth
        return None

    @WindowWidth.setter
    def WindowWidth(self, value: Optional[List[Decimal]]):
        if value is None:
            if "WindowWidth" in self._dataset:
                del self._dataset.WindowWidth
        else:
            self._dataset.WindowWidth = value

    @property
    def WindowCenterWidthExplanation(self) -> Optional[List[str]]:
        if "WindowCenterWidthExplanation" in self._dataset:
            return self._dataset.WindowCenterWidthExplanation
        return None

    @WindowCenterWidthExplanation.setter
    def WindowCenterWidthExplanation(self, value: Optional[List[str]]):
        if value is None:
            if "WindowCenterWidthExplanation" in self._dataset:
                del self._dataset.WindowCenterWidthExplanation
        else:
            self._dataset.WindowCenterWidthExplanation = value

    @property
    def VOILUTFunction(self) -> Optional[str]:
        if "VOILUTFunction" in self._dataset:
            return self._dataset.VOILUTFunction
        return None

    @VOILUTFunction.setter
    def VOILUTFunction(self, value: Optional[str]):
        if value is None:
            if "VOILUTFunction" in self._dataset:
                del self._dataset.VOILUTFunction
        else:
            self._dataset.VOILUTFunction = value

    @property
    def VOILUTSequence(self) -> Optional[List[VOILUTSequenceItem]]:
        if "VOILUTSequence" in self._dataset:
            if len(self._VOILUTSequence) == len(self._dataset.VOILUTSequence):
                return self._VOILUTSequence
            else:
                return [VOILUTSequenceItem(x) for x in self._dataset.VOILUTSequence]
        return None

    @VOILUTSequence.setter
    def VOILUTSequence(self, value: Optional[List[VOILUTSequenceItem]]):
        if value is None:
            self._VOILUTSequence = []
            if "VOILUTSequence" in self._dataset:
                del self._dataset.VOILUTSequence
        elif not isinstance(value, list) or not all(isinstance(item, VOILUTSequenceItem) for item in value):
            raise ValueError("VOILUTSequence must be a list of VOILUTSequenceItem objects")
        else:
            self._VOILUTSequence = value
            if "VOILUTSequence" not in self._dataset:
                self._dataset.VOILUTSequence = pydicom.Sequence()
            self._dataset.VOILUTSequence.clear()
            self._dataset.VOILUTSequence.extend([item.to_dataset() for item in value])

    def add_VOILUT(self, item: VOILUTSequenceItem):
        if not isinstance(item, VOILUTSequenceItem):
            raise ValueError("Item must be an instance of VOILUTSequenceItem")
        self._VOILUTSequence.append(item)
        if "VOILUTSequence" not in self._dataset:
            self._dataset.VOILUTSequence = pydicom.Sequence()
        self._dataset.VOILUTSequence.append(item.to_dataset())

    @property
    def ReferencedPatientSequence(self) -> Optional[List[ReferencedPatientSequenceItem]]:
        if "ReferencedPatientSequence" in self._dataset:
            if len(self._ReferencedPatientSequence) == len(self._dataset.ReferencedPatientSequence):
                return self._ReferencedPatientSequence
            else:
                return [ReferencedPatientSequenceItem(x) for x in self._dataset.ReferencedPatientSequence]
        return None

    @ReferencedPatientSequence.setter
    def ReferencedPatientSequence(self, value: Optional[List[ReferencedPatientSequenceItem]]):
        if value is None:
            self._ReferencedPatientSequence = []
            if "ReferencedPatientSequence" in self._dataset:
                del self._dataset.ReferencedPatientSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedPatientSequenceItem) for item in value):
            raise ValueError("ReferencedPatientSequence must be a list of ReferencedPatientSequenceItem objects")
        else:
            self._ReferencedPatientSequence = value
            if "ReferencedPatientSequence" not in self._dataset:
                self._dataset.ReferencedPatientSequence = pydicom.Sequence()
            self._dataset.ReferencedPatientSequence.clear()
            self._dataset.ReferencedPatientSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedPatient(self, item: ReferencedPatientSequenceItem):
        if not isinstance(item, ReferencedPatientSequenceItem):
            raise ValueError("Item must be an instance of ReferencedPatientSequenceItem")
        self._ReferencedPatientSequence.append(item)
        if "ReferencedPatientSequence" not in self._dataset:
            self._dataset.ReferencedPatientSequence = pydicom.Sequence()
        self._dataset.ReferencedPatientSequence.append(item.to_dataset())

    @property
    def PatientName(self) -> Optional[str]:
        if "PatientName" in self._dataset:
            return self._dataset.PatientName
        return None

    @PatientName.setter
    def PatientName(self, value: Optional[str]):
        if value is None:
            if "PatientName" in self._dataset:
                del self._dataset.PatientName
        else:
            self._dataset.PatientName = value

    @property
    def PatientID(self) -> Optional[str]:
        if "PatientID" in self._dataset:
            return self._dataset.PatientID
        return None

    @PatientID.setter
    def PatientID(self, value: Optional[str]):
        if value is None:
            if "PatientID" in self._dataset:
                del self._dataset.PatientID
        else:
            self._dataset.PatientID = value

    @property
    def IssuerOfPatientID(self) -> Optional[str]:
        if "IssuerOfPatientID" in self._dataset:
            return self._dataset.IssuerOfPatientID
        return None

    @IssuerOfPatientID.setter
    def IssuerOfPatientID(self, value: Optional[str]):
        if value is None:
            if "IssuerOfPatientID" in self._dataset:
                del self._dataset.IssuerOfPatientID
        else:
            self._dataset.IssuerOfPatientID = value

    @property
    def TypeOfPatientID(self) -> Optional[str]:
        if "TypeOfPatientID" in self._dataset:
            return self._dataset.TypeOfPatientID
        return None

    @TypeOfPatientID.setter
    def TypeOfPatientID(self, value: Optional[str]):
        if value is None:
            if "TypeOfPatientID" in self._dataset:
                del self._dataset.TypeOfPatientID
        else:
            self._dataset.TypeOfPatientID = value

    @property
    def IssuerOfPatientIDQualifiersSequence(self) -> Optional[List[IssuerOfPatientIDQualifiersSequenceItem]]:
        if "IssuerOfPatientIDQualifiersSequence" in self._dataset:
            if len(self._IssuerOfPatientIDQualifiersSequence) == len(self._dataset.IssuerOfPatientIDQualifiersSequence):
                return self._IssuerOfPatientIDQualifiersSequence
            else:
                return [IssuerOfPatientIDQualifiersSequenceItem(x) for x in self._dataset.IssuerOfPatientIDQualifiersSequence]
        return None

    @IssuerOfPatientIDQualifiersSequence.setter
    def IssuerOfPatientIDQualifiersSequence(self, value: Optional[List[IssuerOfPatientIDQualifiersSequenceItem]]):
        if value is None:
            self._IssuerOfPatientIDQualifiersSequence = []
            if "IssuerOfPatientIDQualifiersSequence" in self._dataset:
                del self._dataset.IssuerOfPatientIDQualifiersSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, IssuerOfPatientIDQualifiersSequenceItem) for item in value
        ):
            raise ValueError(
                "IssuerOfPatientIDQualifiersSequence must be a list of IssuerOfPatientIDQualifiersSequenceItem objects"
            )
        else:
            self._IssuerOfPatientIDQualifiersSequence = value
            if "IssuerOfPatientIDQualifiersSequence" not in self._dataset:
                self._dataset.IssuerOfPatientIDQualifiersSequence = pydicom.Sequence()
            self._dataset.IssuerOfPatientIDQualifiersSequence.clear()
            self._dataset.IssuerOfPatientIDQualifiersSequence.extend([item.to_dataset() for item in value])

    def add_IssuerOfPatientIDQualifiers(self, item: IssuerOfPatientIDQualifiersSequenceItem):
        if not isinstance(item, IssuerOfPatientIDQualifiersSequenceItem):
            raise ValueError("Item must be an instance of IssuerOfPatientIDQualifiersSequenceItem")
        self._IssuerOfPatientIDQualifiersSequence.append(item)
        if "IssuerOfPatientIDQualifiersSequence" not in self._dataset:
            self._dataset.IssuerOfPatientIDQualifiersSequence = pydicom.Sequence()
        self._dataset.IssuerOfPatientIDQualifiersSequence.append(item.to_dataset())

    @property
    def SourcePatientGroupIdentificationSequence(self) -> Optional[List[SourcePatientGroupIdentificationSequenceItem]]:
        if "SourcePatientGroupIdentificationSequence" in self._dataset:
            if len(self._SourcePatientGroupIdentificationSequence) == len(
                self._dataset.SourcePatientGroupIdentificationSequence
            ):
                return self._SourcePatientGroupIdentificationSequence
            else:
                return [
                    SourcePatientGroupIdentificationSequenceItem(x)
                    for x in self._dataset.SourcePatientGroupIdentificationSequence
                ]
        return None

    @SourcePatientGroupIdentificationSequence.setter
    def SourcePatientGroupIdentificationSequence(self, value: Optional[List[SourcePatientGroupIdentificationSequenceItem]]):
        if value is None:
            self._SourcePatientGroupIdentificationSequence = []
            if "SourcePatientGroupIdentificationSequence" in self._dataset:
                del self._dataset.SourcePatientGroupIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, SourcePatientGroupIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                "SourcePatientGroupIdentificationSequence must be a list of SourcePatientGroupIdentificationSequenceItem"
                " objects"
            )
        else:
            self._SourcePatientGroupIdentificationSequence = value
            if "SourcePatientGroupIdentificationSequence" not in self._dataset:
                self._dataset.SourcePatientGroupIdentificationSequence = pydicom.Sequence()
            self._dataset.SourcePatientGroupIdentificationSequence.clear()
            self._dataset.SourcePatientGroupIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_SourcePatientGroupIdentification(self, item: SourcePatientGroupIdentificationSequenceItem):
        if not isinstance(item, SourcePatientGroupIdentificationSequenceItem):
            raise ValueError("Item must be an instance of SourcePatientGroupIdentificationSequenceItem")
        self._SourcePatientGroupIdentificationSequence.append(item)
        if "SourcePatientGroupIdentificationSequence" not in self._dataset:
            self._dataset.SourcePatientGroupIdentificationSequence = pydicom.Sequence()
        self._dataset.SourcePatientGroupIdentificationSequence.append(item.to_dataset())

    @property
    def GroupOfPatientsIdentificationSequence(self) -> Optional[List[GroupOfPatientsIdentificationSequenceItem]]:
        if "GroupOfPatientsIdentificationSequence" in self._dataset:
            if len(self._GroupOfPatientsIdentificationSequence) == len(self._dataset.GroupOfPatientsIdentificationSequence):
                return self._GroupOfPatientsIdentificationSequence
            else:
                return [
                    GroupOfPatientsIdentificationSequenceItem(x) for x in self._dataset.GroupOfPatientsIdentificationSequence
                ]
        return None

    @GroupOfPatientsIdentificationSequence.setter
    def GroupOfPatientsIdentificationSequence(self, value: Optional[List[GroupOfPatientsIdentificationSequenceItem]]):
        if value is None:
            self._GroupOfPatientsIdentificationSequence = []
            if "GroupOfPatientsIdentificationSequence" in self._dataset:
                del self._dataset.GroupOfPatientsIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, GroupOfPatientsIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                "GroupOfPatientsIdentificationSequence must be a list of GroupOfPatientsIdentificationSequenceItem objects"
            )
        else:
            self._GroupOfPatientsIdentificationSequence = value
            if "GroupOfPatientsIdentificationSequence" not in self._dataset:
                self._dataset.GroupOfPatientsIdentificationSequence = pydicom.Sequence()
            self._dataset.GroupOfPatientsIdentificationSequence.clear()
            self._dataset.GroupOfPatientsIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_GroupOfPatientsIdentification(self, item: GroupOfPatientsIdentificationSequenceItem):
        if not isinstance(item, GroupOfPatientsIdentificationSequenceItem):
            raise ValueError("Item must be an instance of GroupOfPatientsIdentificationSequenceItem")
        self._GroupOfPatientsIdentificationSequence.append(item)
        if "GroupOfPatientsIdentificationSequence" not in self._dataset:
            self._dataset.GroupOfPatientsIdentificationSequence = pydicom.Sequence()
        self._dataset.GroupOfPatientsIdentificationSequence.append(item.to_dataset())

    @property
    def PatientBirthDate(self) -> Optional[str]:
        if "PatientBirthDate" in self._dataset:
            return self._dataset.PatientBirthDate
        return None

    @PatientBirthDate.setter
    def PatientBirthDate(self, value: Optional[str]):
        if value is None:
            if "PatientBirthDate" in self._dataset:
                del self._dataset.PatientBirthDate
        else:
            self._dataset.PatientBirthDate = value

    @property
    def PatientBirthTime(self) -> Optional[str]:
        if "PatientBirthTime" in self._dataset:
            return self._dataset.PatientBirthTime
        return None

    @PatientBirthTime.setter
    def PatientBirthTime(self, value: Optional[str]):
        if value is None:
            if "PatientBirthTime" in self._dataset:
                del self._dataset.PatientBirthTime
        else:
            self._dataset.PatientBirthTime = value

    @property
    def PatientBirthDateInAlternativeCalendar(self) -> Optional[str]:
        if "PatientBirthDateInAlternativeCalendar" in self._dataset:
            return self._dataset.PatientBirthDateInAlternativeCalendar
        return None

    @PatientBirthDateInAlternativeCalendar.setter
    def PatientBirthDateInAlternativeCalendar(self, value: Optional[str]):
        if value is None:
            if "PatientBirthDateInAlternativeCalendar" in self._dataset:
                del self._dataset.PatientBirthDateInAlternativeCalendar
        else:
            self._dataset.PatientBirthDateInAlternativeCalendar = value

    @property
    def PatientDeathDateInAlternativeCalendar(self) -> Optional[str]:
        if "PatientDeathDateInAlternativeCalendar" in self._dataset:
            return self._dataset.PatientDeathDateInAlternativeCalendar
        return None

    @PatientDeathDateInAlternativeCalendar.setter
    def PatientDeathDateInAlternativeCalendar(self, value: Optional[str]):
        if value is None:
            if "PatientDeathDateInAlternativeCalendar" in self._dataset:
                del self._dataset.PatientDeathDateInAlternativeCalendar
        else:
            self._dataset.PatientDeathDateInAlternativeCalendar = value

    @property
    def PatientAlternativeCalendar(self) -> Optional[str]:
        if "PatientAlternativeCalendar" in self._dataset:
            return self._dataset.PatientAlternativeCalendar
        return None

    @PatientAlternativeCalendar.setter
    def PatientAlternativeCalendar(self, value: Optional[str]):
        if value is None:
            if "PatientAlternativeCalendar" in self._dataset:
                del self._dataset.PatientAlternativeCalendar
        else:
            self._dataset.PatientAlternativeCalendar = value

    @property
    def PatientSex(self) -> Optional[str]:
        if "PatientSex" in self._dataset:
            return self._dataset.PatientSex
        return None

    @PatientSex.setter
    def PatientSex(self, value: Optional[str]):
        if value is None:
            if "PatientSex" in self._dataset:
                del self._dataset.PatientSex
        else:
            self._dataset.PatientSex = value

    @property
    def QualityControlSubject(self) -> Optional[str]:
        if "QualityControlSubject" in self._dataset:
            return self._dataset.QualityControlSubject
        return None

    @QualityControlSubject.setter
    def QualityControlSubject(self, value: Optional[str]):
        if value is None:
            if "QualityControlSubject" in self._dataset:
                del self._dataset.QualityControlSubject
        else:
            self._dataset.QualityControlSubject = value

    @property
    def StrainDescription(self) -> Optional[str]:
        if "StrainDescription" in self._dataset:
            return self._dataset.StrainDescription
        return None

    @StrainDescription.setter
    def StrainDescription(self, value: Optional[str]):
        if value is None:
            if "StrainDescription" in self._dataset:
                del self._dataset.StrainDescription
        else:
            self._dataset.StrainDescription = value

    @property
    def StrainNomenclature(self) -> Optional[str]:
        if "StrainNomenclature" in self._dataset:
            return self._dataset.StrainNomenclature
        return None

    @StrainNomenclature.setter
    def StrainNomenclature(self, value: Optional[str]):
        if value is None:
            if "StrainNomenclature" in self._dataset:
                del self._dataset.StrainNomenclature
        else:
            self._dataset.StrainNomenclature = value

    @property
    def StrainStockSequence(self) -> Optional[List[StrainStockSequenceItem]]:
        if "StrainStockSequence" in self._dataset:
            if len(self._StrainStockSequence) == len(self._dataset.StrainStockSequence):
                return self._StrainStockSequence
            else:
                return [StrainStockSequenceItem(x) for x in self._dataset.StrainStockSequence]
        return None

    @StrainStockSequence.setter
    def StrainStockSequence(self, value: Optional[List[StrainStockSequenceItem]]):
        if value is None:
            self._StrainStockSequence = []
            if "StrainStockSequence" in self._dataset:
                del self._dataset.StrainStockSequence
        elif not isinstance(value, list) or not all(isinstance(item, StrainStockSequenceItem) for item in value):
            raise ValueError("StrainStockSequence must be a list of StrainStockSequenceItem objects")
        else:
            self._StrainStockSequence = value
            if "StrainStockSequence" not in self._dataset:
                self._dataset.StrainStockSequence = pydicom.Sequence()
            self._dataset.StrainStockSequence.clear()
            self._dataset.StrainStockSequence.extend([item.to_dataset() for item in value])

    def add_StrainStock(self, item: StrainStockSequenceItem):
        if not isinstance(item, StrainStockSequenceItem):
            raise ValueError("Item must be an instance of StrainStockSequenceItem")
        self._StrainStockSequence.append(item)
        if "StrainStockSequence" not in self._dataset:
            self._dataset.StrainStockSequence = pydicom.Sequence()
        self._dataset.StrainStockSequence.append(item.to_dataset())

    @property
    def StrainAdditionalInformation(self) -> Optional[str]:
        if "StrainAdditionalInformation" in self._dataset:
            return self._dataset.StrainAdditionalInformation
        return None

    @StrainAdditionalInformation.setter
    def StrainAdditionalInformation(self, value: Optional[str]):
        if value is None:
            if "StrainAdditionalInformation" in self._dataset:
                del self._dataset.StrainAdditionalInformation
        else:
            self._dataset.StrainAdditionalInformation = value

    @property
    def StrainCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "StrainCodeSequence" in self._dataset:
            if len(self._StrainCodeSequence) == len(self._dataset.StrainCodeSequence):
                return self._StrainCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.StrainCodeSequence]
        return None

    @StrainCodeSequence.setter
    def StrainCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._StrainCodeSequence = []
            if "StrainCodeSequence" in self._dataset:
                del self._dataset.StrainCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("StrainCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._StrainCodeSequence = value
            if "StrainCodeSequence" not in self._dataset:
                self._dataset.StrainCodeSequence = pydicom.Sequence()
            self._dataset.StrainCodeSequence.clear()
            self._dataset.StrainCodeSequence.extend([item.to_dataset() for item in value])

    def add_StrainCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._StrainCodeSequence.append(item)
        if "StrainCodeSequence" not in self._dataset:
            self._dataset.StrainCodeSequence = pydicom.Sequence()
        self._dataset.StrainCodeSequence.append(item.to_dataset())

    @property
    def GeneticModificationsSequence(self) -> Optional[List[GeneticModificationsSequenceItem]]:
        if "GeneticModificationsSequence" in self._dataset:
            if len(self._GeneticModificationsSequence) == len(self._dataset.GeneticModificationsSequence):
                return self._GeneticModificationsSequence
            else:
                return [GeneticModificationsSequenceItem(x) for x in self._dataset.GeneticModificationsSequence]
        return None

    @GeneticModificationsSequence.setter
    def GeneticModificationsSequence(self, value: Optional[List[GeneticModificationsSequenceItem]]):
        if value is None:
            self._GeneticModificationsSequence = []
            if "GeneticModificationsSequence" in self._dataset:
                del self._dataset.GeneticModificationsSequence
        elif not isinstance(value, list) or not all(isinstance(item, GeneticModificationsSequenceItem) for item in value):
            raise ValueError("GeneticModificationsSequence must be a list of GeneticModificationsSequenceItem objects")
        else:
            self._GeneticModificationsSequence = value
            if "GeneticModificationsSequence" not in self._dataset:
                self._dataset.GeneticModificationsSequence = pydicom.Sequence()
            self._dataset.GeneticModificationsSequence.clear()
            self._dataset.GeneticModificationsSequence.extend([item.to_dataset() for item in value])

    def add_GeneticModifications(self, item: GeneticModificationsSequenceItem):
        if not isinstance(item, GeneticModificationsSequenceItem):
            raise ValueError("Item must be an instance of GeneticModificationsSequenceItem")
        self._GeneticModificationsSequence.append(item)
        if "GeneticModificationsSequence" not in self._dataset:
            self._dataset.GeneticModificationsSequence = pydicom.Sequence()
        self._dataset.GeneticModificationsSequence.append(item.to_dataset())

    @property
    def OtherPatientNames(self) -> Optional[List[str]]:
        if "OtherPatientNames" in self._dataset:
            return self._dataset.OtherPatientNames
        return None

    @OtherPatientNames.setter
    def OtherPatientNames(self, value: Optional[List[str]]):
        if value is None:
            if "OtherPatientNames" in self._dataset:
                del self._dataset.OtherPatientNames
        else:
            self._dataset.OtherPatientNames = value

    @property
    def OtherPatientIDsSequence(self) -> Optional[List[OtherPatientIDsSequenceItem]]:
        if "OtherPatientIDsSequence" in self._dataset:
            if len(self._OtherPatientIDsSequence) == len(self._dataset.OtherPatientIDsSequence):
                return self._OtherPatientIDsSequence
            else:
                return [OtherPatientIDsSequenceItem(x) for x in self._dataset.OtherPatientIDsSequence]
        return None

    @OtherPatientIDsSequence.setter
    def OtherPatientIDsSequence(self, value: Optional[List[OtherPatientIDsSequenceItem]]):
        if value is None:
            self._OtherPatientIDsSequence = []
            if "OtherPatientIDsSequence" in self._dataset:
                del self._dataset.OtherPatientIDsSequence
        elif not isinstance(value, list) or not all(isinstance(item, OtherPatientIDsSequenceItem) for item in value):
            raise ValueError("OtherPatientIDsSequence must be a list of OtherPatientIDsSequenceItem objects")
        else:
            self._OtherPatientIDsSequence = value
            if "OtherPatientIDsSequence" not in self._dataset:
                self._dataset.OtherPatientIDsSequence = pydicom.Sequence()
            self._dataset.OtherPatientIDsSequence.clear()
            self._dataset.OtherPatientIDsSequence.extend([item.to_dataset() for item in value])

    def add_OtherPatientIDs(self, item: OtherPatientIDsSequenceItem):
        if not isinstance(item, OtherPatientIDsSequenceItem):
            raise ValueError("Item must be an instance of OtherPatientIDsSequenceItem")
        self._OtherPatientIDsSequence.append(item)
        if "OtherPatientIDsSequence" not in self._dataset:
            self._dataset.OtherPatientIDsSequence = pydicom.Sequence()
        self._dataset.OtherPatientIDsSequence.append(item.to_dataset())

    @property
    def ReferencedPatientPhotoSequence(self) -> Optional[List[ReferencedPatientPhotoSequenceItem]]:
        if "ReferencedPatientPhotoSequence" in self._dataset:
            if len(self._ReferencedPatientPhotoSequence) == len(self._dataset.ReferencedPatientPhotoSequence):
                return self._ReferencedPatientPhotoSequence
            else:
                return [ReferencedPatientPhotoSequenceItem(x) for x in self._dataset.ReferencedPatientPhotoSequence]
        return None

    @ReferencedPatientPhotoSequence.setter
    def ReferencedPatientPhotoSequence(self, value: Optional[List[ReferencedPatientPhotoSequenceItem]]):
        if value is None:
            self._ReferencedPatientPhotoSequence = []
            if "ReferencedPatientPhotoSequence" in self._dataset:
                del self._dataset.ReferencedPatientPhotoSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedPatientPhotoSequenceItem) for item in value):
            raise ValueError("ReferencedPatientPhotoSequence must be a list of ReferencedPatientPhotoSequenceItem objects")
        else:
            self._ReferencedPatientPhotoSequence = value
            if "ReferencedPatientPhotoSequence" not in self._dataset:
                self._dataset.ReferencedPatientPhotoSequence = pydicom.Sequence()
            self._dataset.ReferencedPatientPhotoSequence.clear()
            self._dataset.ReferencedPatientPhotoSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedPatientPhoto(self, item: ReferencedPatientPhotoSequenceItem):
        if not isinstance(item, ReferencedPatientPhotoSequenceItem):
            raise ValueError("Item must be an instance of ReferencedPatientPhotoSequenceItem")
        self._ReferencedPatientPhotoSequence.append(item)
        if "ReferencedPatientPhotoSequence" not in self._dataset:
            self._dataset.ReferencedPatientPhotoSequence = pydicom.Sequence()
        self._dataset.ReferencedPatientPhotoSequence.append(item.to_dataset())

    @property
    def EthnicGroup(self) -> Optional[str]:
        if "EthnicGroup" in self._dataset:
            return self._dataset.EthnicGroup
        return None

    @EthnicGroup.setter
    def EthnicGroup(self, value: Optional[str]):
        if value is None:
            if "EthnicGroup" in self._dataset:
                del self._dataset.EthnicGroup
        else:
            self._dataset.EthnicGroup = value

    @property
    def PatientSpeciesDescription(self) -> Optional[str]:
        if "PatientSpeciesDescription" in self._dataset:
            return self._dataset.PatientSpeciesDescription
        return None

    @PatientSpeciesDescription.setter
    def PatientSpeciesDescription(self, value: Optional[str]):
        if value is None:
            if "PatientSpeciesDescription" in self._dataset:
                del self._dataset.PatientSpeciesDescription
        else:
            self._dataset.PatientSpeciesDescription = value

    @property
    def PatientSpeciesCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PatientSpeciesCodeSequence" in self._dataset:
            if len(self._PatientSpeciesCodeSequence) == len(self._dataset.PatientSpeciesCodeSequence):
                return self._PatientSpeciesCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PatientSpeciesCodeSequence]
        return None

    @PatientSpeciesCodeSequence.setter
    def PatientSpeciesCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PatientSpeciesCodeSequence = []
            if "PatientSpeciesCodeSequence" in self._dataset:
                del self._dataset.PatientSpeciesCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("PatientSpeciesCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PatientSpeciesCodeSequence = value
            if "PatientSpeciesCodeSequence" not in self._dataset:
                self._dataset.PatientSpeciesCodeSequence = pydicom.Sequence()
            self._dataset.PatientSpeciesCodeSequence.clear()
            self._dataset.PatientSpeciesCodeSequence.extend([item.to_dataset() for item in value])

    def add_PatientSpeciesCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._PatientSpeciesCodeSequence.append(item)
        if "PatientSpeciesCodeSequence" not in self._dataset:
            self._dataset.PatientSpeciesCodeSequence = pydicom.Sequence()
        self._dataset.PatientSpeciesCodeSequence.append(item.to_dataset())

    @property
    def PatientBreedDescription(self) -> Optional[str]:
        if "PatientBreedDescription" in self._dataset:
            return self._dataset.PatientBreedDescription
        return None

    @PatientBreedDescription.setter
    def PatientBreedDescription(self, value: Optional[str]):
        if value is None:
            if "PatientBreedDescription" in self._dataset:
                del self._dataset.PatientBreedDescription
        else:
            self._dataset.PatientBreedDescription = value

    @property
    def PatientBreedCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PatientBreedCodeSequence" in self._dataset:
            if len(self._PatientBreedCodeSequence) == len(self._dataset.PatientBreedCodeSequence):
                return self._PatientBreedCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PatientBreedCodeSequence]
        return None

    @PatientBreedCodeSequence.setter
    def PatientBreedCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PatientBreedCodeSequence = []
            if "PatientBreedCodeSequence" in self._dataset:
                del self._dataset.PatientBreedCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("PatientBreedCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PatientBreedCodeSequence = value
            if "PatientBreedCodeSequence" not in self._dataset:
                self._dataset.PatientBreedCodeSequence = pydicom.Sequence()
            self._dataset.PatientBreedCodeSequence.clear()
            self._dataset.PatientBreedCodeSequence.extend([item.to_dataset() for item in value])

    def add_PatientBreedCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._PatientBreedCodeSequence.append(item)
        if "PatientBreedCodeSequence" not in self._dataset:
            self._dataset.PatientBreedCodeSequence = pydicom.Sequence()
        self._dataset.PatientBreedCodeSequence.append(item.to_dataset())

    @property
    def BreedRegistrationSequence(self) -> Optional[List[BreedRegistrationSequenceItem]]:
        if "BreedRegistrationSequence" in self._dataset:
            if len(self._BreedRegistrationSequence) == len(self._dataset.BreedRegistrationSequence):
                return self._BreedRegistrationSequence
            else:
                return [BreedRegistrationSequenceItem(x) for x in self._dataset.BreedRegistrationSequence]
        return None

    @BreedRegistrationSequence.setter
    def BreedRegistrationSequence(self, value: Optional[List[BreedRegistrationSequenceItem]]):
        if value is None:
            self._BreedRegistrationSequence = []
            if "BreedRegistrationSequence" in self._dataset:
                del self._dataset.BreedRegistrationSequence
        elif not isinstance(value, list) or not all(isinstance(item, BreedRegistrationSequenceItem) for item in value):
            raise ValueError("BreedRegistrationSequence must be a list of BreedRegistrationSequenceItem objects")
        else:
            self._BreedRegistrationSequence = value
            if "BreedRegistrationSequence" not in self._dataset:
                self._dataset.BreedRegistrationSequence = pydicom.Sequence()
            self._dataset.BreedRegistrationSequence.clear()
            self._dataset.BreedRegistrationSequence.extend([item.to_dataset() for item in value])

    def add_BreedRegistration(self, item: BreedRegistrationSequenceItem):
        if not isinstance(item, BreedRegistrationSequenceItem):
            raise ValueError("Item must be an instance of BreedRegistrationSequenceItem")
        self._BreedRegistrationSequence.append(item)
        if "BreedRegistrationSequence" not in self._dataset:
            self._dataset.BreedRegistrationSequence = pydicom.Sequence()
        self._dataset.BreedRegistrationSequence.append(item.to_dataset())

    @property
    def ResponsiblePerson(self) -> Optional[str]:
        if "ResponsiblePerson" in self._dataset:
            return self._dataset.ResponsiblePerson
        return None

    @ResponsiblePerson.setter
    def ResponsiblePerson(self, value: Optional[str]):
        if value is None:
            if "ResponsiblePerson" in self._dataset:
                del self._dataset.ResponsiblePerson
        else:
            self._dataset.ResponsiblePerson = value

    @property
    def ResponsiblePersonRole(self) -> Optional[str]:
        if "ResponsiblePersonRole" in self._dataset:
            return self._dataset.ResponsiblePersonRole
        return None

    @ResponsiblePersonRole.setter
    def ResponsiblePersonRole(self, value: Optional[str]):
        if value is None:
            if "ResponsiblePersonRole" in self._dataset:
                del self._dataset.ResponsiblePersonRole
        else:
            self._dataset.ResponsiblePersonRole = value

    @property
    def ResponsibleOrganization(self) -> Optional[str]:
        if "ResponsibleOrganization" in self._dataset:
            return self._dataset.ResponsibleOrganization
        return None

    @ResponsibleOrganization.setter
    def ResponsibleOrganization(self, value: Optional[str]):
        if value is None:
            if "ResponsibleOrganization" in self._dataset:
                del self._dataset.ResponsibleOrganization
        else:
            self._dataset.ResponsibleOrganization = value

    @property
    def PatientComments(self) -> Optional[str]:
        if "PatientComments" in self._dataset:
            return self._dataset.PatientComments
        return None

    @PatientComments.setter
    def PatientComments(self, value: Optional[str]):
        if value is None:
            if "PatientComments" in self._dataset:
                del self._dataset.PatientComments
        else:
            self._dataset.PatientComments = value

    @property
    def PatientIdentityRemoved(self) -> Optional[str]:
        if "PatientIdentityRemoved" in self._dataset:
            return self._dataset.PatientIdentityRemoved
        return None

    @PatientIdentityRemoved.setter
    def PatientIdentityRemoved(self, value: Optional[str]):
        if value is None:
            if "PatientIdentityRemoved" in self._dataset:
                del self._dataset.PatientIdentityRemoved
        else:
            self._dataset.PatientIdentityRemoved = value

    @property
    def DeidentificationMethod(self) -> Optional[List[str]]:
        if "DeidentificationMethod" in self._dataset:
            return self._dataset.DeidentificationMethod
        return None

    @DeidentificationMethod.setter
    def DeidentificationMethod(self, value: Optional[List[str]]):
        if value is None:
            if "DeidentificationMethod" in self._dataset:
                del self._dataset.DeidentificationMethod
        else:
            self._dataset.DeidentificationMethod = value

    @property
    def DeidentificationMethodCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "DeidentificationMethodCodeSequence" in self._dataset:
            if len(self._DeidentificationMethodCodeSequence) == len(self._dataset.DeidentificationMethodCodeSequence):
                return self._DeidentificationMethodCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.DeidentificationMethodCodeSequence]
        return None

    @DeidentificationMethodCodeSequence.setter
    def DeidentificationMethodCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._DeidentificationMethodCodeSequence = []
            if "DeidentificationMethodCodeSequence" in self._dataset:
                del self._dataset.DeidentificationMethodCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("DeidentificationMethodCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._DeidentificationMethodCodeSequence = value
            if "DeidentificationMethodCodeSequence" not in self._dataset:
                self._dataset.DeidentificationMethodCodeSequence = pydicom.Sequence()
            self._dataset.DeidentificationMethodCodeSequence.clear()
            self._dataset.DeidentificationMethodCodeSequence.extend([item.to_dataset() for item in value])

    def add_DeidentificationMethodCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._DeidentificationMethodCodeSequence.append(item)
        if "DeidentificationMethodCodeSequence" not in self._dataset:
            self._dataset.DeidentificationMethodCodeSequence = pydicom.Sequence()
        self._dataset.DeidentificationMethodCodeSequence.append(item.to_dataset())

    @property
    def DistanceSourceToDetector(self) -> Optional[Decimal]:
        if "DistanceSourceToDetector" in self._dataset:
            return self._dataset.DistanceSourceToDetector
        return None

    @DistanceSourceToDetector.setter
    def DistanceSourceToDetector(self, value: Optional[Decimal]):
        if value is None:
            if "DistanceSourceToDetector" in self._dataset:
                del self._dataset.DistanceSourceToDetector
        else:
            self._dataset.DistanceSourceToDetector = value

    @property
    def DistanceSourceToPatient(self) -> Optional[Decimal]:
        if "DistanceSourceToPatient" in self._dataset:
            return self._dataset.DistanceSourceToPatient
        return None

    @DistanceSourceToPatient.setter
    def DistanceSourceToPatient(self, value: Optional[Decimal]):
        if value is None:
            if "DistanceSourceToPatient" in self._dataset:
                del self._dataset.DistanceSourceToPatient
        else:
            self._dataset.DistanceSourceToPatient = value

    @property
    def EstimatedRadiographicMagnificationFactor(self) -> Optional[Decimal]:
        if "EstimatedRadiographicMagnificationFactor" in self._dataset:
            return self._dataset.EstimatedRadiographicMagnificationFactor
        return None

    @EstimatedRadiographicMagnificationFactor.setter
    def EstimatedRadiographicMagnificationFactor(self, value: Optional[Decimal]):
        if value is None:
            if "EstimatedRadiographicMagnificationFactor" in self._dataset:
                del self._dataset.EstimatedRadiographicMagnificationFactor
        else:
            self._dataset.EstimatedRadiographicMagnificationFactor = value

    @property
    def TableAngle(self) -> Optional[Decimal]:
        if "TableAngle" in self._dataset:
            return self._dataset.TableAngle
        return None

    @TableAngle.setter
    def TableAngle(self, value: Optional[Decimal]):
        if value is None:
            if "TableAngle" in self._dataset:
                del self._dataset.TableAngle
        else:
            self._dataset.TableAngle = value

    @property
    def TableType(self) -> Optional[str]:
        if "TableType" in self._dataset:
            return self._dataset.TableType
        return None

    @TableType.setter
    def TableType(self, value: Optional[str]):
        if value is None:
            if "TableType" in self._dataset:
                del self._dataset.TableType
        else:
            self._dataset.TableType = value

    @property
    def BodyPartThickness(self) -> Optional[Decimal]:
        if "BodyPartThickness" in self._dataset:
            return self._dataset.BodyPartThickness
        return None

    @BodyPartThickness.setter
    def BodyPartThickness(self, value: Optional[Decimal]):
        if value is None:
            if "BodyPartThickness" in self._dataset:
                del self._dataset.BodyPartThickness
        else:
            self._dataset.BodyPartThickness = value

    @property
    def CompressionForce(self) -> Optional[Decimal]:
        if "CompressionForce" in self._dataset:
            return self._dataset.CompressionForce
        return None

    @CompressionForce.setter
    def CompressionForce(self, value: Optional[Decimal]):
        if value is None:
            if "CompressionForce" in self._dataset:
                del self._dataset.CompressionForce
        else:
            self._dataset.CompressionForce = value

    @property
    def CompressionPressure(self) -> Optional[Decimal]:
        if "CompressionPressure" in self._dataset:
            return self._dataset.CompressionPressure
        return None

    @CompressionPressure.setter
    def CompressionPressure(self, value: Optional[Decimal]):
        if value is None:
            if "CompressionPressure" in self._dataset:
                del self._dataset.CompressionPressure
        else:
            self._dataset.CompressionPressure = value

    @property
    def PaddleDescription(self) -> Optional[str]:
        if "PaddleDescription" in self._dataset:
            return self._dataset.PaddleDescription
        return None

    @PaddleDescription.setter
    def PaddleDescription(self, value: Optional[str]):
        if value is None:
            if "PaddleDescription" in self._dataset:
                del self._dataset.PaddleDescription
        else:
            self._dataset.PaddleDescription = value

    @property
    def CompressionContactArea(self) -> Optional[Decimal]:
        if "CompressionContactArea" in self._dataset:
            return self._dataset.CompressionContactArea
        return None

    @CompressionContactArea.setter
    def CompressionContactArea(self, value: Optional[Decimal]):
        if value is None:
            if "CompressionContactArea" in self._dataset:
                del self._dataset.CompressionContactArea
        else:
            self._dataset.CompressionContactArea = value

    @property
    def ColumnAngulation(self) -> Optional[Decimal]:
        if "ColumnAngulation" in self._dataset:
            return self._dataset.ColumnAngulation
        return None

    @ColumnAngulation.setter
    def ColumnAngulation(self, value: Optional[Decimal]):
        if value is None:
            if "ColumnAngulation" in self._dataset:
                del self._dataset.ColumnAngulation
        else:
            self._dataset.ColumnAngulation = value

    @property
    def PositionerType(self) -> Optional[str]:
        if "PositionerType" in self._dataset:
            return self._dataset.PositionerType
        return None

    @PositionerType.setter
    def PositionerType(self, value: Optional[str]):
        if value is None:
            if "PositionerType" in self._dataset:
                del self._dataset.PositionerType
        else:
            self._dataset.PositionerType = value

    @property
    def PositionerPrimaryAngle(self) -> Optional[Decimal]:
        if "PositionerPrimaryAngle" in self._dataset:
            return self._dataset.PositionerPrimaryAngle
        return None

    @PositionerPrimaryAngle.setter
    def PositionerPrimaryAngle(self, value: Optional[Decimal]):
        if value is None:
            if "PositionerPrimaryAngle" in self._dataset:
                del self._dataset.PositionerPrimaryAngle
        else:
            self._dataset.PositionerPrimaryAngle = value

    @property
    def PositionerSecondaryAngle(self) -> Optional[Decimal]:
        if "PositionerSecondaryAngle" in self._dataset:
            return self._dataset.PositionerSecondaryAngle
        return None

    @PositionerSecondaryAngle.setter
    def PositionerSecondaryAngle(self, value: Optional[Decimal]):
        if value is None:
            if "PositionerSecondaryAngle" in self._dataset:
                del self._dataset.PositionerSecondaryAngle
        else:
            self._dataset.PositionerSecondaryAngle = value

    @property
    def DetectorPrimaryAngle(self) -> Optional[Decimal]:
        if "DetectorPrimaryAngle" in self._dataset:
            return self._dataset.DetectorPrimaryAngle
        return None

    @DetectorPrimaryAngle.setter
    def DetectorPrimaryAngle(self, value: Optional[Decimal]):
        if value is None:
            if "DetectorPrimaryAngle" in self._dataset:
                del self._dataset.DetectorPrimaryAngle
        else:
            self._dataset.DetectorPrimaryAngle = value

    @property
    def DetectorSecondaryAngle(self) -> Optional[Decimal]:
        if "DetectorSecondaryAngle" in self._dataset:
            return self._dataset.DetectorSecondaryAngle
        return None

    @DetectorSecondaryAngle.setter
    def DetectorSecondaryAngle(self, value: Optional[Decimal]):
        if value is None:
            if "DetectorSecondaryAngle" in self._dataset:
                del self._dataset.DetectorSecondaryAngle
        else:
            self._dataset.DetectorSecondaryAngle = value

    @property
    def PatientPosition(self) -> Optional[str]:
        if "PatientPosition" in self._dataset:
            return self._dataset.PatientPosition
        return None

    @PatientPosition.setter
    def PatientPosition(self, value: Optional[str]):
        if value is None:
            if "PatientPosition" in self._dataset:
                del self._dataset.PatientPosition
        else:
            self._dataset.PatientPosition = value

    @property
    def ViewPosition(self) -> Optional[str]:
        if "ViewPosition" in self._dataset:
            return self._dataset.ViewPosition
        return None

    @ViewPosition.setter
    def ViewPosition(self, value: Optional[str]):
        if value is None:
            if "ViewPosition" in self._dataset:
                del self._dataset.ViewPosition
        else:
            self._dataset.ViewPosition = value

    @property
    def ProjectionEponymousNameCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ProjectionEponymousNameCodeSequence" in self._dataset:
            if len(self._ProjectionEponymousNameCodeSequence) == len(self._dataset.ProjectionEponymousNameCodeSequence):
                return self._ProjectionEponymousNameCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ProjectionEponymousNameCodeSequence]
        return None

    @ProjectionEponymousNameCodeSequence.setter
    def ProjectionEponymousNameCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ProjectionEponymousNameCodeSequence = []
            if "ProjectionEponymousNameCodeSequence" in self._dataset:
                del self._dataset.ProjectionEponymousNameCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("ProjectionEponymousNameCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ProjectionEponymousNameCodeSequence = value
            if "ProjectionEponymousNameCodeSequence" not in self._dataset:
                self._dataset.ProjectionEponymousNameCodeSequence = pydicom.Sequence()
            self._dataset.ProjectionEponymousNameCodeSequence.clear()
            self._dataset.ProjectionEponymousNameCodeSequence.extend([item.to_dataset() for item in value])

    def add_ProjectionEponymousNameCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ProjectionEponymousNameCodeSequence.append(item)
        if "ProjectionEponymousNameCodeSequence" not in self._dataset:
            self._dataset.ProjectionEponymousNameCodeSequence = pydicom.Sequence()
        self._dataset.ProjectionEponymousNameCodeSequence.append(item.to_dataset())

    @property
    def ViewCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ViewCodeSequence" in self._dataset:
            if len(self._ViewCodeSequence) == len(self._dataset.ViewCodeSequence):
                return self._ViewCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ViewCodeSequence]
        return None

    @ViewCodeSequence.setter
    def ViewCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ViewCodeSequence = []
            if "ViewCodeSequence" in self._dataset:
                del self._dataset.ViewCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("ViewCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ViewCodeSequence = value
            if "ViewCodeSequence" not in self._dataset:
                self._dataset.ViewCodeSequence = pydicom.Sequence()
            self._dataset.ViewCodeSequence.clear()
            self._dataset.ViewCodeSequence.extend([item.to_dataset() for item in value])

    def add_ViewCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ViewCodeSequence.append(item)
        if "ViewCodeSequence" not in self._dataset:
            self._dataset.ViewCodeSequence = pydicom.Sequence()
        self._dataset.ViewCodeSequence.append(item.to_dataset())

    @property
    def PatientOrientationCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PatientOrientationCodeSequence" in self._dataset:
            if len(self._PatientOrientationCodeSequence) == len(self._dataset.PatientOrientationCodeSequence):
                return self._PatientOrientationCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PatientOrientationCodeSequence]
        return None

    @PatientOrientationCodeSequence.setter
    def PatientOrientationCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PatientOrientationCodeSequence = []
            if "PatientOrientationCodeSequence" in self._dataset:
                del self._dataset.PatientOrientationCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("PatientOrientationCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PatientOrientationCodeSequence = value
            if "PatientOrientationCodeSequence" not in self._dataset:
                self._dataset.PatientOrientationCodeSequence = pydicom.Sequence()
            self._dataset.PatientOrientationCodeSequence.clear()
            self._dataset.PatientOrientationCodeSequence.extend([item.to_dataset() for item in value])

    def add_PatientOrientationCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._PatientOrientationCodeSequence.append(item)
        if "PatientOrientationCodeSequence" not in self._dataset:
            self._dataset.PatientOrientationCodeSequence = pydicom.Sequence()
        self._dataset.PatientOrientationCodeSequence.append(item.to_dataset())

    @property
    def PatientGantryRelationshipCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PatientGantryRelationshipCodeSequence" in self._dataset:
            if len(self._PatientGantryRelationshipCodeSequence) == len(self._dataset.PatientGantryRelationshipCodeSequence):
                return self._PatientGantryRelationshipCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PatientGantryRelationshipCodeSequence]
        return None

    @PatientGantryRelationshipCodeSequence.setter
    def PatientGantryRelationshipCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PatientGantryRelationshipCodeSequence = []
            if "PatientGantryRelationshipCodeSequence" in self._dataset:
                del self._dataset.PatientGantryRelationshipCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("PatientGantryRelationshipCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PatientGantryRelationshipCodeSequence = value
            if "PatientGantryRelationshipCodeSequence" not in self._dataset:
                self._dataset.PatientGantryRelationshipCodeSequence = pydicom.Sequence()
            self._dataset.PatientGantryRelationshipCodeSequence.clear()
            self._dataset.PatientGantryRelationshipCodeSequence.extend([item.to_dataset() for item in value])

    def add_PatientGantryRelationshipCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._PatientGantryRelationshipCodeSequence.append(item)
        if "PatientGantryRelationshipCodeSequence" not in self._dataset:
            self._dataset.PatientGantryRelationshipCodeSequence = pydicom.Sequence()
        self._dataset.PatientGantryRelationshipCodeSequence.append(item.to_dataset())

    @property
    def ClinicalTrialSponsorName(self) -> Optional[str]:
        if "ClinicalTrialSponsorName" in self._dataset:
            return self._dataset.ClinicalTrialSponsorName
        return None

    @ClinicalTrialSponsorName.setter
    def ClinicalTrialSponsorName(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialSponsorName" in self._dataset:
                del self._dataset.ClinicalTrialSponsorName
        else:
            self._dataset.ClinicalTrialSponsorName = value

    @property
    def ClinicalTrialProtocolID(self) -> Optional[str]:
        if "ClinicalTrialProtocolID" in self._dataset:
            return self._dataset.ClinicalTrialProtocolID
        return None

    @ClinicalTrialProtocolID.setter
    def ClinicalTrialProtocolID(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialProtocolID" in self._dataset:
                del self._dataset.ClinicalTrialProtocolID
        else:
            self._dataset.ClinicalTrialProtocolID = value

    @property
    def ClinicalTrialProtocolName(self) -> Optional[str]:
        if "ClinicalTrialProtocolName" in self._dataset:
            return self._dataset.ClinicalTrialProtocolName
        return None

    @ClinicalTrialProtocolName.setter
    def ClinicalTrialProtocolName(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialProtocolName" in self._dataset:
                del self._dataset.ClinicalTrialProtocolName
        else:
            self._dataset.ClinicalTrialProtocolName = value

    @property
    def IssuerOfClinicalTrialProtocolID(self) -> Optional[str]:
        if "IssuerOfClinicalTrialProtocolID" in self._dataset:
            return self._dataset.IssuerOfClinicalTrialProtocolID
        return None

    @IssuerOfClinicalTrialProtocolID.setter
    def IssuerOfClinicalTrialProtocolID(self, value: Optional[str]):
        if value is None:
            if "IssuerOfClinicalTrialProtocolID" in self._dataset:
                del self._dataset.IssuerOfClinicalTrialProtocolID
        else:
            self._dataset.IssuerOfClinicalTrialProtocolID = value

    @property
    def OtherClinicalTrialProtocolIDsSequence(self) -> Optional[List[OtherClinicalTrialProtocolIDsSequenceItem]]:
        if "OtherClinicalTrialProtocolIDsSequence" in self._dataset:
            if len(self._OtherClinicalTrialProtocolIDsSequence) == len(self._dataset.OtherClinicalTrialProtocolIDsSequence):
                return self._OtherClinicalTrialProtocolIDsSequence
            else:
                return [
                    OtherClinicalTrialProtocolIDsSequenceItem(x) for x in self._dataset.OtherClinicalTrialProtocolIDsSequence
                ]
        return None

    @OtherClinicalTrialProtocolIDsSequence.setter
    def OtherClinicalTrialProtocolIDsSequence(self, value: Optional[List[OtherClinicalTrialProtocolIDsSequenceItem]]):
        if value is None:
            self._OtherClinicalTrialProtocolIDsSequence = []
            if "OtherClinicalTrialProtocolIDsSequence" in self._dataset:
                del self._dataset.OtherClinicalTrialProtocolIDsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, OtherClinicalTrialProtocolIDsSequenceItem) for item in value
        ):
            raise ValueError(
                "OtherClinicalTrialProtocolIDsSequence must be a list of OtherClinicalTrialProtocolIDsSequenceItem objects"
            )
        else:
            self._OtherClinicalTrialProtocolIDsSequence = value
            if "OtherClinicalTrialProtocolIDsSequence" not in self._dataset:
                self._dataset.OtherClinicalTrialProtocolIDsSequence = pydicom.Sequence()
            self._dataset.OtherClinicalTrialProtocolIDsSequence.clear()
            self._dataset.OtherClinicalTrialProtocolIDsSequence.extend([item.to_dataset() for item in value])

    def add_OtherClinicalTrialProtocolIDs(self, item: OtherClinicalTrialProtocolIDsSequenceItem):
        if not isinstance(item, OtherClinicalTrialProtocolIDsSequenceItem):
            raise ValueError("Item must be an instance of OtherClinicalTrialProtocolIDsSequenceItem")
        self._OtherClinicalTrialProtocolIDsSequence.append(item)
        if "OtherClinicalTrialProtocolIDsSequence" not in self._dataset:
            self._dataset.OtherClinicalTrialProtocolIDsSequence = pydicom.Sequence()
        self._dataset.OtherClinicalTrialProtocolIDsSequence.append(item.to_dataset())

    @property
    def ClinicalTrialSiteID(self) -> Optional[str]:
        if "ClinicalTrialSiteID" in self._dataset:
            return self._dataset.ClinicalTrialSiteID
        return None

    @ClinicalTrialSiteID.setter
    def ClinicalTrialSiteID(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialSiteID" in self._dataset:
                del self._dataset.ClinicalTrialSiteID
        else:
            self._dataset.ClinicalTrialSiteID = value

    @property
    def ClinicalTrialSiteName(self) -> Optional[str]:
        if "ClinicalTrialSiteName" in self._dataset:
            return self._dataset.ClinicalTrialSiteName
        return None

    @ClinicalTrialSiteName.setter
    def ClinicalTrialSiteName(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialSiteName" in self._dataset:
                del self._dataset.ClinicalTrialSiteName
        else:
            self._dataset.ClinicalTrialSiteName = value

    @property
    def IssuerOfClinicalTrialSiteID(self) -> Optional[str]:
        if "IssuerOfClinicalTrialSiteID" in self._dataset:
            return self._dataset.IssuerOfClinicalTrialSiteID
        return None

    @IssuerOfClinicalTrialSiteID.setter
    def IssuerOfClinicalTrialSiteID(self, value: Optional[str]):
        if value is None:
            if "IssuerOfClinicalTrialSiteID" in self._dataset:
                del self._dataset.IssuerOfClinicalTrialSiteID
        else:
            self._dataset.IssuerOfClinicalTrialSiteID = value

    @property
    def ClinicalTrialSubjectID(self) -> Optional[str]:
        if "ClinicalTrialSubjectID" in self._dataset:
            return self._dataset.ClinicalTrialSubjectID
        return None

    @ClinicalTrialSubjectID.setter
    def ClinicalTrialSubjectID(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialSubjectID" in self._dataset:
                del self._dataset.ClinicalTrialSubjectID
        else:
            self._dataset.ClinicalTrialSubjectID = value

    @property
    def IssuerOfClinicalTrialSubjectID(self) -> Optional[str]:
        if "IssuerOfClinicalTrialSubjectID" in self._dataset:
            return self._dataset.IssuerOfClinicalTrialSubjectID
        return None

    @IssuerOfClinicalTrialSubjectID.setter
    def IssuerOfClinicalTrialSubjectID(self, value: Optional[str]):
        if value is None:
            if "IssuerOfClinicalTrialSubjectID" in self._dataset:
                del self._dataset.IssuerOfClinicalTrialSubjectID
        else:
            self._dataset.IssuerOfClinicalTrialSubjectID = value

    @property
    def ClinicalTrialSubjectReadingID(self) -> Optional[str]:
        if "ClinicalTrialSubjectReadingID" in self._dataset:
            return self._dataset.ClinicalTrialSubjectReadingID
        return None

    @ClinicalTrialSubjectReadingID.setter
    def ClinicalTrialSubjectReadingID(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialSubjectReadingID" in self._dataset:
                del self._dataset.ClinicalTrialSubjectReadingID
        else:
            self._dataset.ClinicalTrialSubjectReadingID = value

    @property
    def IssuerOfClinicalTrialSubjectReadingID(self) -> Optional[str]:
        if "IssuerOfClinicalTrialSubjectReadingID" in self._dataset:
            return self._dataset.IssuerOfClinicalTrialSubjectReadingID
        return None

    @IssuerOfClinicalTrialSubjectReadingID.setter
    def IssuerOfClinicalTrialSubjectReadingID(self, value: Optional[str]):
        if value is None:
            if "IssuerOfClinicalTrialSubjectReadingID" in self._dataset:
                del self._dataset.IssuerOfClinicalTrialSubjectReadingID
        else:
            self._dataset.IssuerOfClinicalTrialSubjectReadingID = value

    @property
    def ClinicalTrialProtocolEthicsCommitteeName(self) -> Optional[str]:
        if "ClinicalTrialProtocolEthicsCommitteeName" in self._dataset:
            return self._dataset.ClinicalTrialProtocolEthicsCommitteeName
        return None

    @ClinicalTrialProtocolEthicsCommitteeName.setter
    def ClinicalTrialProtocolEthicsCommitteeName(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialProtocolEthicsCommitteeName" in self._dataset:
                del self._dataset.ClinicalTrialProtocolEthicsCommitteeName
        else:
            self._dataset.ClinicalTrialProtocolEthicsCommitteeName = value

    @property
    def ClinicalTrialProtocolEthicsCommitteeApprovalNumber(self) -> Optional[str]:
        if "ClinicalTrialProtocolEthicsCommitteeApprovalNumber" in self._dataset:
            return self._dataset.ClinicalTrialProtocolEthicsCommitteeApprovalNumber
        return None

    @ClinicalTrialProtocolEthicsCommitteeApprovalNumber.setter
    def ClinicalTrialProtocolEthicsCommitteeApprovalNumber(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialProtocolEthicsCommitteeApprovalNumber" in self._dataset:
                del self._dataset.ClinicalTrialProtocolEthicsCommitteeApprovalNumber
        else:
            self._dataset.ClinicalTrialProtocolEthicsCommitteeApprovalNumber = value

    @property
    def SpecificCharacterSet(self) -> Optional[List[str]]:
        if "SpecificCharacterSet" in self._dataset:
            return self._dataset.SpecificCharacterSet
        return None

    @SpecificCharacterSet.setter
    def SpecificCharacterSet(self, value: Optional[List[str]]):
        if value is None:
            if "SpecificCharacterSet" in self._dataset:
                del self._dataset.SpecificCharacterSet
        else:
            self._dataset.SpecificCharacterSet = value

    @property
    def InstanceCreationDate(self) -> Optional[str]:
        if "InstanceCreationDate" in self._dataset:
            return self._dataset.InstanceCreationDate
        return None

    @InstanceCreationDate.setter
    def InstanceCreationDate(self, value: Optional[str]):
        if value is None:
            if "InstanceCreationDate" in self._dataset:
                del self._dataset.InstanceCreationDate
        else:
            self._dataset.InstanceCreationDate = value

    @property
    def InstanceCreationTime(self) -> Optional[str]:
        if "InstanceCreationTime" in self._dataset:
            return self._dataset.InstanceCreationTime
        return None

    @InstanceCreationTime.setter
    def InstanceCreationTime(self, value: Optional[str]):
        if value is None:
            if "InstanceCreationTime" in self._dataset:
                del self._dataset.InstanceCreationTime
        else:
            self._dataset.InstanceCreationTime = value

    @property
    def InstanceCreatorUID(self) -> Optional[str]:
        if "InstanceCreatorUID" in self._dataset:
            return self._dataset.InstanceCreatorUID
        return None

    @InstanceCreatorUID.setter
    def InstanceCreatorUID(self, value: Optional[str]):
        if value is None:
            if "InstanceCreatorUID" in self._dataset:
                del self._dataset.InstanceCreatorUID
        else:
            self._dataset.InstanceCreatorUID = value

    @property
    def InstanceCoercionDateTime(self) -> Optional[str]:
        if "InstanceCoercionDateTime" in self._dataset:
            return self._dataset.InstanceCoercionDateTime
        return None

    @InstanceCoercionDateTime.setter
    def InstanceCoercionDateTime(self, value: Optional[str]):
        if value is None:
            if "InstanceCoercionDateTime" in self._dataset:
                del self._dataset.InstanceCoercionDateTime
        else:
            self._dataset.InstanceCoercionDateTime = value

    @property
    def SOPClassUID(self) -> Optional[str]:
        if "SOPClassUID" in self._dataset:
            return self._dataset.SOPClassUID
        return None

    @SOPClassUID.setter
    def SOPClassUID(self, value: Optional[str]):
        if value is None:
            if "SOPClassUID" in self._dataset:
                del self._dataset.SOPClassUID
        else:
            self._dataset.SOPClassUID = value

    @property
    def SOPInstanceUID(self) -> Optional[str]:
        if "SOPInstanceUID" in self._dataset:
            return self._dataset.SOPInstanceUID
        return None

    @SOPInstanceUID.setter
    def SOPInstanceUID(self, value: Optional[str]):
        if value is None:
            if "SOPInstanceUID" in self._dataset:
                del self._dataset.SOPInstanceUID
        else:
            self._dataset.SOPInstanceUID = value

    @property
    def RelatedGeneralSOPClassUID(self) -> Optional[List[str]]:
        if "RelatedGeneralSOPClassUID" in self._dataset:
            return self._dataset.RelatedGeneralSOPClassUID
        return None

    @RelatedGeneralSOPClassUID.setter
    def RelatedGeneralSOPClassUID(self, value: Optional[List[str]]):
        if value is None:
            if "RelatedGeneralSOPClassUID" in self._dataset:
                del self._dataset.RelatedGeneralSOPClassUID
        else:
            self._dataset.RelatedGeneralSOPClassUID = value

    @property
    def OriginalSpecializedSOPClassUID(self) -> Optional[str]:
        if "OriginalSpecializedSOPClassUID" in self._dataset:
            return self._dataset.OriginalSpecializedSOPClassUID
        return None

    @OriginalSpecializedSOPClassUID.setter
    def OriginalSpecializedSOPClassUID(self, value: Optional[str]):
        if value is None:
            if "OriginalSpecializedSOPClassUID" in self._dataset:
                del self._dataset.OriginalSpecializedSOPClassUID
        else:
            self._dataset.OriginalSpecializedSOPClassUID = value

    @property
    def SyntheticData(self) -> Optional[str]:
        if "SyntheticData" in self._dataset:
            return self._dataset.SyntheticData
        return None

    @SyntheticData.setter
    def SyntheticData(self, value: Optional[str]):
        if value is None:
            if "SyntheticData" in self._dataset:
                del self._dataset.SyntheticData
        else:
            self._dataset.SyntheticData = value

    @property
    def QueryRetrieveView(self) -> Optional[str]:
        if "QueryRetrieveView" in self._dataset:
            return self._dataset.QueryRetrieveView
        return None

    @QueryRetrieveView.setter
    def QueryRetrieveView(self, value: Optional[str]):
        if value is None:
            if "QueryRetrieveView" in self._dataset:
                del self._dataset.QueryRetrieveView
        else:
            self._dataset.QueryRetrieveView = value

    @property
    def CodingSchemeIdentificationSequence(self) -> Optional[List[CodingSchemeIdentificationSequenceItem]]:
        if "CodingSchemeIdentificationSequence" in self._dataset:
            if len(self._CodingSchemeIdentificationSequence) == len(self._dataset.CodingSchemeIdentificationSequence):
                return self._CodingSchemeIdentificationSequence
            else:
                return [CodingSchemeIdentificationSequenceItem(x) for x in self._dataset.CodingSchemeIdentificationSequence]
        return None

    @CodingSchemeIdentificationSequence.setter
    def CodingSchemeIdentificationSequence(self, value: Optional[List[CodingSchemeIdentificationSequenceItem]]):
        if value is None:
            self._CodingSchemeIdentificationSequence = []
            if "CodingSchemeIdentificationSequence" in self._dataset:
                del self._dataset.CodingSchemeIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, CodingSchemeIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                "CodingSchemeIdentificationSequence must be a list of CodingSchemeIdentificationSequenceItem objects"
            )
        else:
            self._CodingSchemeIdentificationSequence = value
            if "CodingSchemeIdentificationSequence" not in self._dataset:
                self._dataset.CodingSchemeIdentificationSequence = pydicom.Sequence()
            self._dataset.CodingSchemeIdentificationSequence.clear()
            self._dataset.CodingSchemeIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_CodingSchemeIdentification(self, item: CodingSchemeIdentificationSequenceItem):
        if not isinstance(item, CodingSchemeIdentificationSequenceItem):
            raise ValueError("Item must be an instance of CodingSchemeIdentificationSequenceItem")
        self._CodingSchemeIdentificationSequence.append(item)
        if "CodingSchemeIdentificationSequence" not in self._dataset:
            self._dataset.CodingSchemeIdentificationSequence = pydicom.Sequence()
        self._dataset.CodingSchemeIdentificationSequence.append(item.to_dataset())

    @property
    def ContextGroupIdentificationSequence(self) -> Optional[List[ContextGroupIdentificationSequenceItem]]:
        if "ContextGroupIdentificationSequence" in self._dataset:
            if len(self._ContextGroupIdentificationSequence) == len(self._dataset.ContextGroupIdentificationSequence):
                return self._ContextGroupIdentificationSequence
            else:
                return [ContextGroupIdentificationSequenceItem(x) for x in self._dataset.ContextGroupIdentificationSequence]
        return None

    @ContextGroupIdentificationSequence.setter
    def ContextGroupIdentificationSequence(self, value: Optional[List[ContextGroupIdentificationSequenceItem]]):
        if value is None:
            self._ContextGroupIdentificationSequence = []
            if "ContextGroupIdentificationSequence" in self._dataset:
                del self._dataset.ContextGroupIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ContextGroupIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                "ContextGroupIdentificationSequence must be a list of ContextGroupIdentificationSequenceItem objects"
            )
        else:
            self._ContextGroupIdentificationSequence = value
            if "ContextGroupIdentificationSequence" not in self._dataset:
                self._dataset.ContextGroupIdentificationSequence = pydicom.Sequence()
            self._dataset.ContextGroupIdentificationSequence.clear()
            self._dataset.ContextGroupIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_ContextGroupIdentification(self, item: ContextGroupIdentificationSequenceItem):
        if not isinstance(item, ContextGroupIdentificationSequenceItem):
            raise ValueError("Item must be an instance of ContextGroupIdentificationSequenceItem")
        self._ContextGroupIdentificationSequence.append(item)
        if "ContextGroupIdentificationSequence" not in self._dataset:
            self._dataset.ContextGroupIdentificationSequence = pydicom.Sequence()
        self._dataset.ContextGroupIdentificationSequence.append(item.to_dataset())

    @property
    def MappingResourceIdentificationSequence(self) -> Optional[List[MappingResourceIdentificationSequenceItem]]:
        if "MappingResourceIdentificationSequence" in self._dataset:
            if len(self._MappingResourceIdentificationSequence) == len(self._dataset.MappingResourceIdentificationSequence):
                return self._MappingResourceIdentificationSequence
            else:
                return [
                    MappingResourceIdentificationSequenceItem(x) for x in self._dataset.MappingResourceIdentificationSequence
                ]
        return None

    @MappingResourceIdentificationSequence.setter
    def MappingResourceIdentificationSequence(self, value: Optional[List[MappingResourceIdentificationSequenceItem]]):
        if value is None:
            self._MappingResourceIdentificationSequence = []
            if "MappingResourceIdentificationSequence" in self._dataset:
                del self._dataset.MappingResourceIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, MappingResourceIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                "MappingResourceIdentificationSequence must be a list of MappingResourceIdentificationSequenceItem objects"
            )
        else:
            self._MappingResourceIdentificationSequence = value
            if "MappingResourceIdentificationSequence" not in self._dataset:
                self._dataset.MappingResourceIdentificationSequence = pydicom.Sequence()
            self._dataset.MappingResourceIdentificationSequence.clear()
            self._dataset.MappingResourceIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_MappingResourceIdentification(self, item: MappingResourceIdentificationSequenceItem):
        if not isinstance(item, MappingResourceIdentificationSequenceItem):
            raise ValueError("Item must be an instance of MappingResourceIdentificationSequenceItem")
        self._MappingResourceIdentificationSequence.append(item)
        if "MappingResourceIdentificationSequence" not in self._dataset:
            self._dataset.MappingResourceIdentificationSequence = pydicom.Sequence()
        self._dataset.MappingResourceIdentificationSequence.append(item.to_dataset())

    @property
    def TimezoneOffsetFromUTC(self) -> Optional[str]:
        if "TimezoneOffsetFromUTC" in self._dataset:
            return self._dataset.TimezoneOffsetFromUTC
        return None

    @TimezoneOffsetFromUTC.setter
    def TimezoneOffsetFromUTC(self, value: Optional[str]):
        if value is None:
            if "TimezoneOffsetFromUTC" in self._dataset:
                del self._dataset.TimezoneOffsetFromUTC
        else:
            self._dataset.TimezoneOffsetFromUTC = value

    @property
    def PrivateDataElementCharacteristicsSequence(self) -> Optional[List[PrivateDataElementCharacteristicsSequenceItem]]:
        if "PrivateDataElementCharacteristicsSequence" in self._dataset:
            if len(self._PrivateDataElementCharacteristicsSequence) == len(
                self._dataset.PrivateDataElementCharacteristicsSequence
            ):
                return self._PrivateDataElementCharacteristicsSequence
            else:
                return [
                    PrivateDataElementCharacteristicsSequenceItem(x)
                    for x in self._dataset.PrivateDataElementCharacteristicsSequence
                ]
        return None

    @PrivateDataElementCharacteristicsSequence.setter
    def PrivateDataElementCharacteristicsSequence(self, value: Optional[List[PrivateDataElementCharacteristicsSequenceItem]]):
        if value is None:
            self._PrivateDataElementCharacteristicsSequence = []
            if "PrivateDataElementCharacteristicsSequence" in self._dataset:
                del self._dataset.PrivateDataElementCharacteristicsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PrivateDataElementCharacteristicsSequenceItem) for item in value
        ):
            raise ValueError(
                "PrivateDataElementCharacteristicsSequence must be a list of PrivateDataElementCharacteristicsSequenceItem"
                " objects"
            )
        else:
            self._PrivateDataElementCharacteristicsSequence = value
            if "PrivateDataElementCharacteristicsSequence" not in self._dataset:
                self._dataset.PrivateDataElementCharacteristicsSequence = pydicom.Sequence()
            self._dataset.PrivateDataElementCharacteristicsSequence.clear()
            self._dataset.PrivateDataElementCharacteristicsSequence.extend([item.to_dataset() for item in value])

    def add_PrivateDataElementCharacteristics(self, item: PrivateDataElementCharacteristicsSequenceItem):
        if not isinstance(item, PrivateDataElementCharacteristicsSequenceItem):
            raise ValueError("Item must be an instance of PrivateDataElementCharacteristicsSequenceItem")
        self._PrivateDataElementCharacteristicsSequence.append(item)
        if "PrivateDataElementCharacteristicsSequence" not in self._dataset:
            self._dataset.PrivateDataElementCharacteristicsSequence = pydicom.Sequence()
        self._dataset.PrivateDataElementCharacteristicsSequence.append(item.to_dataset())

    @property
    def ContentQualification(self) -> Optional[str]:
        if "ContentQualification" in self._dataset:
            return self._dataset.ContentQualification
        return None

    @ContentQualification.setter
    def ContentQualification(self, value: Optional[str]):
        if value is None:
            if "ContentQualification" in self._dataset:
                del self._dataset.ContentQualification
        else:
            self._dataset.ContentQualification = value

    @property
    def ReferencedDefinedProtocolSequence(self) -> Optional[List[ReferencedDefinedProtocolSequenceItem]]:
        if "ReferencedDefinedProtocolSequence" in self._dataset:
            if len(self._ReferencedDefinedProtocolSequence) == len(self._dataset.ReferencedDefinedProtocolSequence):
                return self._ReferencedDefinedProtocolSequence
            else:
                return [ReferencedDefinedProtocolSequenceItem(x) for x in self._dataset.ReferencedDefinedProtocolSequence]
        return None

    @ReferencedDefinedProtocolSequence.setter
    def ReferencedDefinedProtocolSequence(self, value: Optional[List[ReferencedDefinedProtocolSequenceItem]]):
        if value is None:
            self._ReferencedDefinedProtocolSequence = []
            if "ReferencedDefinedProtocolSequence" in self._dataset:
                del self._dataset.ReferencedDefinedProtocolSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedDefinedProtocolSequenceItem) for item in value):
            raise ValueError(
                "ReferencedDefinedProtocolSequence must be a list of ReferencedDefinedProtocolSequenceItem objects"
            )
        else:
            self._ReferencedDefinedProtocolSequence = value
            if "ReferencedDefinedProtocolSequence" not in self._dataset:
                self._dataset.ReferencedDefinedProtocolSequence = pydicom.Sequence()
            self._dataset.ReferencedDefinedProtocolSequence.clear()
            self._dataset.ReferencedDefinedProtocolSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedDefinedProtocol(self, item: ReferencedDefinedProtocolSequenceItem):
        if not isinstance(item, ReferencedDefinedProtocolSequenceItem):
            raise ValueError("Item must be an instance of ReferencedDefinedProtocolSequenceItem")
        self._ReferencedDefinedProtocolSequence.append(item)
        if "ReferencedDefinedProtocolSequence" not in self._dataset:
            self._dataset.ReferencedDefinedProtocolSequence = pydicom.Sequence()
        self._dataset.ReferencedDefinedProtocolSequence.append(item.to_dataset())

    @property
    def ReferencedPerformedProtocolSequence(self) -> Optional[List[ReferencedPerformedProtocolSequenceItem]]:
        if "ReferencedPerformedProtocolSequence" in self._dataset:
            if len(self._ReferencedPerformedProtocolSequence) == len(self._dataset.ReferencedPerformedProtocolSequence):
                return self._ReferencedPerformedProtocolSequence
            else:
                return [ReferencedPerformedProtocolSequenceItem(x) for x in self._dataset.ReferencedPerformedProtocolSequence]
        return None

    @ReferencedPerformedProtocolSequence.setter
    def ReferencedPerformedProtocolSequence(self, value: Optional[List[ReferencedPerformedProtocolSequenceItem]]):
        if value is None:
            self._ReferencedPerformedProtocolSequence = []
            if "ReferencedPerformedProtocolSequence" in self._dataset:
                del self._dataset.ReferencedPerformedProtocolSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedPerformedProtocolSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferencedPerformedProtocolSequence must be a list of ReferencedPerformedProtocolSequenceItem objects"
            )
        else:
            self._ReferencedPerformedProtocolSequence = value
            if "ReferencedPerformedProtocolSequence" not in self._dataset:
                self._dataset.ReferencedPerformedProtocolSequence = pydicom.Sequence()
            self._dataset.ReferencedPerformedProtocolSequence.clear()
            self._dataset.ReferencedPerformedProtocolSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedPerformedProtocol(self, item: ReferencedPerformedProtocolSequenceItem):
        if not isinstance(item, ReferencedPerformedProtocolSequenceItem):
            raise ValueError("Item must be an instance of ReferencedPerformedProtocolSequenceItem")
        self._ReferencedPerformedProtocolSequence.append(item)
        if "ReferencedPerformedProtocolSequence" not in self._dataset:
            self._dataset.ReferencedPerformedProtocolSequence = pydicom.Sequence()
        self._dataset.ReferencedPerformedProtocolSequence.append(item.to_dataset())

    @property
    def ContributingEquipmentSequence(self) -> Optional[List[ContributingEquipmentSequenceItem]]:
        if "ContributingEquipmentSequence" in self._dataset:
            if len(self._ContributingEquipmentSequence) == len(self._dataset.ContributingEquipmentSequence):
                return self._ContributingEquipmentSequence
            else:
                return [ContributingEquipmentSequenceItem(x) for x in self._dataset.ContributingEquipmentSequence]
        return None

    @ContributingEquipmentSequence.setter
    def ContributingEquipmentSequence(self, value: Optional[List[ContributingEquipmentSequenceItem]]):
        if value is None:
            self._ContributingEquipmentSequence = []
            if "ContributingEquipmentSequence" in self._dataset:
                del self._dataset.ContributingEquipmentSequence
        elif not isinstance(value, list) or not all(isinstance(item, ContributingEquipmentSequenceItem) for item in value):
            raise ValueError("ContributingEquipmentSequence must be a list of ContributingEquipmentSequenceItem objects")
        else:
            self._ContributingEquipmentSequence = value
            if "ContributingEquipmentSequence" not in self._dataset:
                self._dataset.ContributingEquipmentSequence = pydicom.Sequence()
            self._dataset.ContributingEquipmentSequence.clear()
            self._dataset.ContributingEquipmentSequence.extend([item.to_dataset() for item in value])

    def add_ContributingEquipment(self, item: ContributingEquipmentSequenceItem):
        if not isinstance(item, ContributingEquipmentSequenceItem):
            raise ValueError("Item must be an instance of ContributingEquipmentSequenceItem")
        self._ContributingEquipmentSequence.append(item)
        if "ContributingEquipmentSequence" not in self._dataset:
            self._dataset.ContributingEquipmentSequence = pydicom.Sequence()
        self._dataset.ContributingEquipmentSequence.append(item.to_dataset())

    @property
    def InstanceNumber(self) -> Optional[int]:
        if "InstanceNumber" in self._dataset:
            return self._dataset.InstanceNumber
        return None

    @InstanceNumber.setter
    def InstanceNumber(self, value: Optional[int]):
        if value is None:
            if "InstanceNumber" in self._dataset:
                del self._dataset.InstanceNumber
        else:
            self._dataset.InstanceNumber = value

    @property
    def ConversionSourceAttributesSequence(self) -> Optional[List[ConversionSourceAttributesSequenceItem]]:
        if "ConversionSourceAttributesSequence" in self._dataset:
            if len(self._ConversionSourceAttributesSequence) == len(self._dataset.ConversionSourceAttributesSequence):
                return self._ConversionSourceAttributesSequence
            else:
                return [ConversionSourceAttributesSequenceItem(x) for x in self._dataset.ConversionSourceAttributesSequence]
        return None

    @ConversionSourceAttributesSequence.setter
    def ConversionSourceAttributesSequence(self, value: Optional[List[ConversionSourceAttributesSequenceItem]]):
        if value is None:
            self._ConversionSourceAttributesSequence = []
            if "ConversionSourceAttributesSequence" in self._dataset:
                del self._dataset.ConversionSourceAttributesSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ConversionSourceAttributesSequenceItem) for item in value
        ):
            raise ValueError(
                "ConversionSourceAttributesSequence must be a list of ConversionSourceAttributesSequenceItem objects"
            )
        else:
            self._ConversionSourceAttributesSequence = value
            if "ConversionSourceAttributesSequence" not in self._dataset:
                self._dataset.ConversionSourceAttributesSequence = pydicom.Sequence()
            self._dataset.ConversionSourceAttributesSequence.clear()
            self._dataset.ConversionSourceAttributesSequence.extend([item.to_dataset() for item in value])

    def add_ConversionSourceAttributes(self, item: ConversionSourceAttributesSequenceItem):
        if not isinstance(item, ConversionSourceAttributesSequenceItem):
            raise ValueError("Item must be an instance of ConversionSourceAttributesSequenceItem")
        self._ConversionSourceAttributesSequence.append(item)
        if "ConversionSourceAttributesSequence" not in self._dataset:
            self._dataset.ConversionSourceAttributesSequence = pydicom.Sequence()
        self._dataset.ConversionSourceAttributesSequence.append(item.to_dataset())

    @property
    def LongitudinalTemporalInformationModified(self) -> Optional[str]:
        if "LongitudinalTemporalInformationModified" in self._dataset:
            return self._dataset.LongitudinalTemporalInformationModified
        return None

    @LongitudinalTemporalInformationModified.setter
    def LongitudinalTemporalInformationModified(self, value: Optional[str]):
        if value is None:
            if "LongitudinalTemporalInformationModified" in self._dataset:
                del self._dataset.LongitudinalTemporalInformationModified
        else:
            self._dataset.LongitudinalTemporalInformationModified = value

    @property
    def HL7StructuredDocumentReferenceSequence(self) -> Optional[List[HL7StructuredDocumentReferenceSequenceItem]]:
        if "HL7StructuredDocumentReferenceSequence" in self._dataset:
            if len(self._HL7StructuredDocumentReferenceSequence) == len(self._dataset.HL7StructuredDocumentReferenceSequence):
                return self._HL7StructuredDocumentReferenceSequence
            else:
                return [
                    HL7StructuredDocumentReferenceSequenceItem(x) for x in self._dataset.HL7StructuredDocumentReferenceSequence
                ]
        return None

    @HL7StructuredDocumentReferenceSequence.setter
    def HL7StructuredDocumentReferenceSequence(self, value: Optional[List[HL7StructuredDocumentReferenceSequenceItem]]):
        if value is None:
            self._HL7StructuredDocumentReferenceSequence = []
            if "HL7StructuredDocumentReferenceSequence" in self._dataset:
                del self._dataset.HL7StructuredDocumentReferenceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, HL7StructuredDocumentReferenceSequenceItem) for item in value
        ):
            raise ValueError(
                "HL7StructuredDocumentReferenceSequence must be a list of HL7StructuredDocumentReferenceSequenceItem objects"
            )
        else:
            self._HL7StructuredDocumentReferenceSequence = value
            if "HL7StructuredDocumentReferenceSequence" not in self._dataset:
                self._dataset.HL7StructuredDocumentReferenceSequence = pydicom.Sequence()
            self._dataset.HL7StructuredDocumentReferenceSequence.clear()
            self._dataset.HL7StructuredDocumentReferenceSequence.extend([item.to_dataset() for item in value])

    def add_HL7StructuredDocumentReference(self, item: HL7StructuredDocumentReferenceSequenceItem):
        if not isinstance(item, HL7StructuredDocumentReferenceSequenceItem):
            raise ValueError("Item must be an instance of HL7StructuredDocumentReferenceSequenceItem")
        self._HL7StructuredDocumentReferenceSequence.append(item)
        if "HL7StructuredDocumentReferenceSequence" not in self._dataset:
            self._dataset.HL7StructuredDocumentReferenceSequence = pydicom.Sequence()
        self._dataset.HL7StructuredDocumentReferenceSequence.append(item.to_dataset())

    @property
    def SOPInstanceStatus(self) -> Optional[str]:
        if "SOPInstanceStatus" in self._dataset:
            return self._dataset.SOPInstanceStatus
        return None

    @SOPInstanceStatus.setter
    def SOPInstanceStatus(self, value: Optional[str]):
        if value is None:
            if "SOPInstanceStatus" in self._dataset:
                del self._dataset.SOPInstanceStatus
        else:
            self._dataset.SOPInstanceStatus = value

    @property
    def SOPAuthorizationDateTime(self) -> Optional[str]:
        if "SOPAuthorizationDateTime" in self._dataset:
            return self._dataset.SOPAuthorizationDateTime
        return None

    @SOPAuthorizationDateTime.setter
    def SOPAuthorizationDateTime(self, value: Optional[str]):
        if value is None:
            if "SOPAuthorizationDateTime" in self._dataset:
                del self._dataset.SOPAuthorizationDateTime
        else:
            self._dataset.SOPAuthorizationDateTime = value

    @property
    def SOPAuthorizationComment(self) -> Optional[str]:
        if "SOPAuthorizationComment" in self._dataset:
            return self._dataset.SOPAuthorizationComment
        return None

    @SOPAuthorizationComment.setter
    def SOPAuthorizationComment(self, value: Optional[str]):
        if value is None:
            if "SOPAuthorizationComment" in self._dataset:
                del self._dataset.SOPAuthorizationComment
        else:
            self._dataset.SOPAuthorizationComment = value

    @property
    def AuthorizationEquipmentCertificationNumber(self) -> Optional[str]:
        if "AuthorizationEquipmentCertificationNumber" in self._dataset:
            return self._dataset.AuthorizationEquipmentCertificationNumber
        return None

    @AuthorizationEquipmentCertificationNumber.setter
    def AuthorizationEquipmentCertificationNumber(self, value: Optional[str]):
        if value is None:
            if "AuthorizationEquipmentCertificationNumber" in self._dataset:
                del self._dataset.AuthorizationEquipmentCertificationNumber
        else:
            self._dataset.AuthorizationEquipmentCertificationNumber = value

    @property
    def EncryptedAttributesSequence(self) -> Optional[List[EncryptedAttributesSequenceItem]]:
        if "EncryptedAttributesSequence" in self._dataset:
            if len(self._EncryptedAttributesSequence) == len(self._dataset.EncryptedAttributesSequence):
                return self._EncryptedAttributesSequence
            else:
                return [EncryptedAttributesSequenceItem(x) for x in self._dataset.EncryptedAttributesSequence]
        return None

    @EncryptedAttributesSequence.setter
    def EncryptedAttributesSequence(self, value: Optional[List[EncryptedAttributesSequenceItem]]):
        if value is None:
            self._EncryptedAttributesSequence = []
            if "EncryptedAttributesSequence" in self._dataset:
                del self._dataset.EncryptedAttributesSequence
        elif not isinstance(value, list) or not all(isinstance(item, EncryptedAttributesSequenceItem) for item in value):
            raise ValueError("EncryptedAttributesSequence must be a list of EncryptedAttributesSequenceItem objects")
        else:
            self._EncryptedAttributesSequence = value
            if "EncryptedAttributesSequence" not in self._dataset:
                self._dataset.EncryptedAttributesSequence = pydicom.Sequence()
            self._dataset.EncryptedAttributesSequence.clear()
            self._dataset.EncryptedAttributesSequence.extend([item.to_dataset() for item in value])

    def add_EncryptedAttributes(self, item: EncryptedAttributesSequenceItem):
        if not isinstance(item, EncryptedAttributesSequenceItem):
            raise ValueError("Item must be an instance of EncryptedAttributesSequenceItem")
        self._EncryptedAttributesSequence.append(item)
        if "EncryptedAttributesSequence" not in self._dataset:
            self._dataset.EncryptedAttributesSequence = pydicom.Sequence()
        self._dataset.EncryptedAttributesSequence.append(item.to_dataset())

    @property
    def OriginalAttributesSequence(self) -> Optional[List[OriginalAttributesSequenceItem]]:
        if "OriginalAttributesSequence" in self._dataset:
            if len(self._OriginalAttributesSequence) == len(self._dataset.OriginalAttributesSequence):
                return self._OriginalAttributesSequence
            else:
                return [OriginalAttributesSequenceItem(x) for x in self._dataset.OriginalAttributesSequence]
        return None

    @OriginalAttributesSequence.setter
    def OriginalAttributesSequence(self, value: Optional[List[OriginalAttributesSequenceItem]]):
        if value is None:
            self._OriginalAttributesSequence = []
            if "OriginalAttributesSequence" in self._dataset:
                del self._dataset.OriginalAttributesSequence
        elif not isinstance(value, list) or not all(isinstance(item, OriginalAttributesSequenceItem) for item in value):
            raise ValueError("OriginalAttributesSequence must be a list of OriginalAttributesSequenceItem objects")
        else:
            self._OriginalAttributesSequence = value
            if "OriginalAttributesSequence" not in self._dataset:
                self._dataset.OriginalAttributesSequence = pydicom.Sequence()
            self._dataset.OriginalAttributesSequence.clear()
            self._dataset.OriginalAttributesSequence.extend([item.to_dataset() for item in value])

    def add_OriginalAttributes(self, item: OriginalAttributesSequenceItem):
        if not isinstance(item, OriginalAttributesSequenceItem):
            raise ValueError("Item must be an instance of OriginalAttributesSequenceItem")
        self._OriginalAttributesSequence.append(item)
        if "OriginalAttributesSequence" not in self._dataset:
            self._dataset.OriginalAttributesSequence = pydicom.Sequence()
        self._dataset.OriginalAttributesSequence.append(item.to_dataset())

    @property
    def InstanceOriginStatus(self) -> Optional[str]:
        if "InstanceOriginStatus" in self._dataset:
            return self._dataset.InstanceOriginStatus
        return None

    @InstanceOriginStatus.setter
    def InstanceOriginStatus(self, value: Optional[str]):
        if value is None:
            if "InstanceOriginStatus" in self._dataset:
                del self._dataset.InstanceOriginStatus
        else:
            self._dataset.InstanceOriginStatus = value

    @property
    def BarcodeValue(self) -> Optional[str]:
        if "BarcodeValue" in self._dataset:
            return self._dataset.BarcodeValue
        return None

    @BarcodeValue.setter
    def BarcodeValue(self, value: Optional[str]):
        if value is None:
            if "BarcodeValue" in self._dataset:
                del self._dataset.BarcodeValue
        else:
            self._dataset.BarcodeValue = value

    @property
    def MACParametersSequence(self) -> Optional[List[MACParametersSequenceItem]]:
        if "MACParametersSequence" in self._dataset:
            if len(self._MACParametersSequence) == len(self._dataset.MACParametersSequence):
                return self._MACParametersSequence
            else:
                return [MACParametersSequenceItem(x) for x in self._dataset.MACParametersSequence]
        return None

    @MACParametersSequence.setter
    def MACParametersSequence(self, value: Optional[List[MACParametersSequenceItem]]):
        if value is None:
            self._MACParametersSequence = []
            if "MACParametersSequence" in self._dataset:
                del self._dataset.MACParametersSequence
        elif not isinstance(value, list) or not all(isinstance(item, MACParametersSequenceItem) for item in value):
            raise ValueError("MACParametersSequence must be a list of MACParametersSequenceItem objects")
        else:
            self._MACParametersSequence = value
            if "MACParametersSequence" not in self._dataset:
                self._dataset.MACParametersSequence = pydicom.Sequence()
            self._dataset.MACParametersSequence.clear()
            self._dataset.MACParametersSequence.extend([item.to_dataset() for item in value])

    def add_MACParameters(self, item: MACParametersSequenceItem):
        if not isinstance(item, MACParametersSequenceItem):
            raise ValueError("Item must be an instance of MACParametersSequenceItem")
        self._MACParametersSequence.append(item)
        if "MACParametersSequence" not in self._dataset:
            self._dataset.MACParametersSequence = pydicom.Sequence()
        self._dataset.MACParametersSequence.append(item.to_dataset())

    @property
    def DigitalSignaturesSequence(self) -> Optional[List[DigitalSignaturesSequenceItem]]:
        if "DigitalSignaturesSequence" in self._dataset:
            if len(self._DigitalSignaturesSequence) == len(self._dataset.DigitalSignaturesSequence):
                return self._DigitalSignaturesSequence
            else:
                return [DigitalSignaturesSequenceItem(x) for x in self._dataset.DigitalSignaturesSequence]
        return None

    @DigitalSignaturesSequence.setter
    def DigitalSignaturesSequence(self, value: Optional[List[DigitalSignaturesSequenceItem]]):
        if value is None:
            self._DigitalSignaturesSequence = []
            if "DigitalSignaturesSequence" in self._dataset:
                del self._dataset.DigitalSignaturesSequence
        elif not isinstance(value, list) or not all(isinstance(item, DigitalSignaturesSequenceItem) for item in value):
            raise ValueError("DigitalSignaturesSequence must be a list of DigitalSignaturesSequenceItem objects")
        else:
            self._DigitalSignaturesSequence = value
            if "DigitalSignaturesSequence" not in self._dataset:
                self._dataset.DigitalSignaturesSequence = pydicom.Sequence()
            self._dataset.DigitalSignaturesSequence.clear()
            self._dataset.DigitalSignaturesSequence.extend([item.to_dataset() for item in value])

    def add_DigitalSignatures(self, item: DigitalSignaturesSequenceItem):
        if not isinstance(item, DigitalSignaturesSequenceItem):
            raise ValueError("Item must be an instance of DigitalSignaturesSequenceItem")
        self._DigitalSignaturesSequence.append(item)
        if "DigitalSignaturesSequence" not in self._dataset:
            self._dataset.DigitalSignaturesSequence = pydicom.Sequence()
        self._dataset.DigitalSignaturesSequence.append(item.to_dataset())

    @property
    def DeviceSequence(self) -> Optional[List[DeviceSequenceItem]]:
        if "DeviceSequence" in self._dataset:
            if len(self._DeviceSequence) == len(self._dataset.DeviceSequence):
                return self._DeviceSequence
            else:
                return [DeviceSequenceItem(x) for x in self._dataset.DeviceSequence]
        return None

    @DeviceSequence.setter
    def DeviceSequence(self, value: Optional[List[DeviceSequenceItem]]):
        if value is None:
            self._DeviceSequence = []
            if "DeviceSequence" in self._dataset:
                del self._dataset.DeviceSequence
        elif not isinstance(value, list) or not all(isinstance(item, DeviceSequenceItem) for item in value):
            raise ValueError("DeviceSequence must be a list of DeviceSequenceItem objects")
        else:
            self._DeviceSequence = value
            if "DeviceSequence" not in self._dataset:
                self._dataset.DeviceSequence = pydicom.Sequence()
            self._dataset.DeviceSequence.clear()
            self._dataset.DeviceSequence.extend([item.to_dataset() for item in value])

    def add_Device(self, item: DeviceSequenceItem):
        if not isinstance(item, DeviceSequenceItem):
            raise ValueError("Item must be an instance of DeviceSequenceItem")
        self._DeviceSequence.append(item)
        if "DeviceSequence" not in self._dataset:
            self._dataset.DeviceSequence = pydicom.Sequence()
        self._dataset.DeviceSequence.append(item.to_dataset())

    @property
    def AcquisitionUID(self) -> Optional[str]:
        if "AcquisitionUID" in self._dataset:
            return self._dataset.AcquisitionUID
        return None

    @AcquisitionUID.setter
    def AcquisitionUID(self, value: Optional[str]):
        if value is None:
            if "AcquisitionUID" in self._dataset:
                del self._dataset.AcquisitionUID
        else:
            self._dataset.AcquisitionUID = value

    @property
    def AcquisitionDate(self) -> Optional[str]:
        if "AcquisitionDate" in self._dataset:
            return self._dataset.AcquisitionDate
        return None

    @AcquisitionDate.setter
    def AcquisitionDate(self, value: Optional[str]):
        if value is None:
            if "AcquisitionDate" in self._dataset:
                del self._dataset.AcquisitionDate
        else:
            self._dataset.AcquisitionDate = value

    @property
    def AcquisitionDateTime(self) -> Optional[str]:
        if "AcquisitionDateTime" in self._dataset:
            return self._dataset.AcquisitionDateTime
        return None

    @AcquisitionDateTime.setter
    def AcquisitionDateTime(self, value: Optional[str]):
        if value is None:
            if "AcquisitionDateTime" in self._dataset:
                del self._dataset.AcquisitionDateTime
        else:
            self._dataset.AcquisitionDateTime = value

    @property
    def AcquisitionTime(self) -> Optional[str]:
        if "AcquisitionTime" in self._dataset:
            return self._dataset.AcquisitionTime
        return None

    @AcquisitionTime.setter
    def AcquisitionTime(self, value: Optional[str]):
        if value is None:
            if "AcquisitionTime" in self._dataset:
                del self._dataset.AcquisitionTime
        else:
            self._dataset.AcquisitionTime = value

    @property
    def IrradiationEventUID(self) -> Optional[List[str]]:
        if "IrradiationEventUID" in self._dataset:
            return self._dataset.IrradiationEventUID
        return None

    @IrradiationEventUID.setter
    def IrradiationEventUID(self, value: Optional[List[str]]):
        if value is None:
            if "IrradiationEventUID" in self._dataset:
                del self._dataset.IrradiationEventUID
        else:
            self._dataset.IrradiationEventUID = value

    @property
    def AcquisitionDuration(self) -> Optional[float]:
        if "AcquisitionDuration" in self._dataset:
            return self._dataset.AcquisitionDuration
        return None

    @AcquisitionDuration.setter
    def AcquisitionDuration(self, value: Optional[float]):
        if value is None:
            if "AcquisitionDuration" in self._dataset:
                del self._dataset.AcquisitionDuration
        else:
            self._dataset.AcquisitionDuration = value

    @property
    def AcquisitionNumber(self) -> Optional[int]:
        if "AcquisitionNumber" in self._dataset:
            return self._dataset.AcquisitionNumber
        return None

    @AcquisitionNumber.setter
    def AcquisitionNumber(self, value: Optional[int]):
        if value is None:
            if "AcquisitionNumber" in self._dataset:
                del self._dataset.AcquisitionNumber
        else:
            self._dataset.AcquisitionNumber = value

    @property
    def ImagesInAcquisition(self) -> Optional[int]:
        if "ImagesInAcquisition" in self._dataset:
            return self._dataset.ImagesInAcquisition
        return None

    @ImagesInAcquisition.setter
    def ImagesInAcquisition(self, value: Optional[int]):
        if value is None:
            if "ImagesInAcquisition" in self._dataset:
                del self._dataset.ImagesInAcquisition
        else:
            self._dataset.ImagesInAcquisition = value

    @property
    def SeriesDate(self) -> Optional[str]:
        if "SeriesDate" in self._dataset:
            return self._dataset.SeriesDate
        return None

    @SeriesDate.setter
    def SeriesDate(self, value: Optional[str]):
        if value is None:
            if "SeriesDate" in self._dataset:
                del self._dataset.SeriesDate
        else:
            self._dataset.SeriesDate = value

    @property
    def SeriesTime(self) -> Optional[str]:
        if "SeriesTime" in self._dataset:
            return self._dataset.SeriesTime
        return None

    @SeriesTime.setter
    def SeriesTime(self, value: Optional[str]):
        if value is None:
            if "SeriesTime" in self._dataset:
                del self._dataset.SeriesTime
        else:
            self._dataset.SeriesTime = value

    @property
    def Modality(self) -> Optional[str]:
        if "Modality" in self._dataset:
            return self._dataset.Modality
        return None

    @Modality.setter
    def Modality(self, value: Optional[str]):
        if value is None:
            if "Modality" in self._dataset:
                del self._dataset.Modality
        else:
            self._dataset.Modality = value

    @property
    def SeriesDescription(self) -> Optional[str]:
        if "SeriesDescription" in self._dataset:
            return self._dataset.SeriesDescription
        return None

    @SeriesDescription.setter
    def SeriesDescription(self, value: Optional[str]):
        if value is None:
            if "SeriesDescription" in self._dataset:
                del self._dataset.SeriesDescription
        else:
            self._dataset.SeriesDescription = value

    @property
    def SeriesDescriptionCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "SeriesDescriptionCodeSequence" in self._dataset:
            if len(self._SeriesDescriptionCodeSequence) == len(self._dataset.SeriesDescriptionCodeSequence):
                return self._SeriesDescriptionCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.SeriesDescriptionCodeSequence]
        return None

    @SeriesDescriptionCodeSequence.setter
    def SeriesDescriptionCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._SeriesDescriptionCodeSequence = []
            if "SeriesDescriptionCodeSequence" in self._dataset:
                del self._dataset.SeriesDescriptionCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("SeriesDescriptionCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SeriesDescriptionCodeSequence = value
            if "SeriesDescriptionCodeSequence" not in self._dataset:
                self._dataset.SeriesDescriptionCodeSequence = pydicom.Sequence()
            self._dataset.SeriesDescriptionCodeSequence.clear()
            self._dataset.SeriesDescriptionCodeSequence.extend([item.to_dataset() for item in value])

    def add_SeriesDescriptionCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._SeriesDescriptionCodeSequence.append(item)
        if "SeriesDescriptionCodeSequence" not in self._dataset:
            self._dataset.SeriesDescriptionCodeSequence = pydicom.Sequence()
        self._dataset.SeriesDescriptionCodeSequence.append(item.to_dataset())

    @property
    def PerformingPhysicianName(self) -> Optional[List[str]]:
        if "PerformingPhysicianName" in self._dataset:
            return self._dataset.PerformingPhysicianName
        return None

    @PerformingPhysicianName.setter
    def PerformingPhysicianName(self, value: Optional[List[str]]):
        if value is None:
            if "PerformingPhysicianName" in self._dataset:
                del self._dataset.PerformingPhysicianName
        else:
            self._dataset.PerformingPhysicianName = value

    @property
    def PerformingPhysicianIdentificationSequence(self) -> Optional[List[PerformingPhysicianIdentificationSequenceItem]]:
        if "PerformingPhysicianIdentificationSequence" in self._dataset:
            if len(self._PerformingPhysicianIdentificationSequence) == len(
                self._dataset.PerformingPhysicianIdentificationSequence
            ):
                return self._PerformingPhysicianIdentificationSequence
            else:
                return [
                    PerformingPhysicianIdentificationSequenceItem(x)
                    for x in self._dataset.PerformingPhysicianIdentificationSequence
                ]
        return None

    @PerformingPhysicianIdentificationSequence.setter
    def PerformingPhysicianIdentificationSequence(self, value: Optional[List[PerformingPhysicianIdentificationSequenceItem]]):
        if value is None:
            self._PerformingPhysicianIdentificationSequence = []
            if "PerformingPhysicianIdentificationSequence" in self._dataset:
                del self._dataset.PerformingPhysicianIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PerformingPhysicianIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                "PerformingPhysicianIdentificationSequence must be a list of PerformingPhysicianIdentificationSequenceItem"
                " objects"
            )
        else:
            self._PerformingPhysicianIdentificationSequence = value
            if "PerformingPhysicianIdentificationSequence" not in self._dataset:
                self._dataset.PerformingPhysicianIdentificationSequence = pydicom.Sequence()
            self._dataset.PerformingPhysicianIdentificationSequence.clear()
            self._dataset.PerformingPhysicianIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_PerformingPhysicianIdentification(self, item: PerformingPhysicianIdentificationSequenceItem):
        if not isinstance(item, PerformingPhysicianIdentificationSequenceItem):
            raise ValueError("Item must be an instance of PerformingPhysicianIdentificationSequenceItem")
        self._PerformingPhysicianIdentificationSequence.append(item)
        if "PerformingPhysicianIdentificationSequence" not in self._dataset:
            self._dataset.PerformingPhysicianIdentificationSequence = pydicom.Sequence()
        self._dataset.PerformingPhysicianIdentificationSequence.append(item.to_dataset())

    @property
    def OperatorsName(self) -> Optional[List[str]]:
        if "OperatorsName" in self._dataset:
            return self._dataset.OperatorsName
        return None

    @OperatorsName.setter
    def OperatorsName(self, value: Optional[List[str]]):
        if value is None:
            if "OperatorsName" in self._dataset:
                del self._dataset.OperatorsName
        else:
            self._dataset.OperatorsName = value

    @property
    def OperatorIdentificationSequence(self) -> Optional[List[OperatorIdentificationSequenceItem]]:
        if "OperatorIdentificationSequence" in self._dataset:
            if len(self._OperatorIdentificationSequence) == len(self._dataset.OperatorIdentificationSequence):
                return self._OperatorIdentificationSequence
            else:
                return [OperatorIdentificationSequenceItem(x) for x in self._dataset.OperatorIdentificationSequence]
        return None

    @OperatorIdentificationSequence.setter
    def OperatorIdentificationSequence(self, value: Optional[List[OperatorIdentificationSequenceItem]]):
        if value is None:
            self._OperatorIdentificationSequence = []
            if "OperatorIdentificationSequence" in self._dataset:
                del self._dataset.OperatorIdentificationSequence
        elif not isinstance(value, list) or not all(isinstance(item, OperatorIdentificationSequenceItem) for item in value):
            raise ValueError("OperatorIdentificationSequence must be a list of OperatorIdentificationSequenceItem objects")
        else:
            self._OperatorIdentificationSequence = value
            if "OperatorIdentificationSequence" not in self._dataset:
                self._dataset.OperatorIdentificationSequence = pydicom.Sequence()
            self._dataset.OperatorIdentificationSequence.clear()
            self._dataset.OperatorIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_OperatorIdentification(self, item: OperatorIdentificationSequenceItem):
        if not isinstance(item, OperatorIdentificationSequenceItem):
            raise ValueError("Item must be an instance of OperatorIdentificationSequenceItem")
        self._OperatorIdentificationSequence.append(item)
        if "OperatorIdentificationSequence" not in self._dataset:
            self._dataset.OperatorIdentificationSequence = pydicom.Sequence()
        self._dataset.OperatorIdentificationSequence.append(item.to_dataset())

    @property
    def ReferencedPerformedProcedureStepSequence(self) -> Optional[List[ReferencedPerformedProcedureStepSequenceItem]]:
        if "ReferencedPerformedProcedureStepSequence" in self._dataset:
            if len(self._ReferencedPerformedProcedureStepSequence) == len(
                self._dataset.ReferencedPerformedProcedureStepSequence
            ):
                return self._ReferencedPerformedProcedureStepSequence
            else:
                return [
                    ReferencedPerformedProcedureStepSequenceItem(x)
                    for x in self._dataset.ReferencedPerformedProcedureStepSequence
                ]
        return None

    @ReferencedPerformedProcedureStepSequence.setter
    def ReferencedPerformedProcedureStepSequence(self, value: Optional[List[ReferencedPerformedProcedureStepSequenceItem]]):
        if value is None:
            self._ReferencedPerformedProcedureStepSequence = []
            if "ReferencedPerformedProcedureStepSequence" in self._dataset:
                del self._dataset.ReferencedPerformedProcedureStepSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedPerformedProcedureStepSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferencedPerformedProcedureStepSequence must be a list of ReferencedPerformedProcedureStepSequenceItem"
                " objects"
            )
        else:
            self._ReferencedPerformedProcedureStepSequence = value
            if "ReferencedPerformedProcedureStepSequence" not in self._dataset:
                self._dataset.ReferencedPerformedProcedureStepSequence = pydicom.Sequence()
            self._dataset.ReferencedPerformedProcedureStepSequence.clear()
            self._dataset.ReferencedPerformedProcedureStepSequence.extend([item.to_dataset() for item in value])

    def RelatedSeriesSequence(self) -> Optional[List[RelatedSeriesSequenceItem]]:
        if "RelatedSeriesSequence" in self._dataset:
            if len(self._RelatedSeriesSequence) == len(self._dataset.RelatedSeriesSequence):
                return self._RelatedSeriesSequence
            else:
                return [RelatedSeriesSequenceItem(x) for x in self._dataset.RelatedSeriesSequence]
        return None

    @RelatedSeriesSequence.setter
    def RelatedSeriesSequence(self, value: Optional[List[RelatedSeriesSequenceItem]]):
        if value is None:
            self._RelatedSeriesSequence = []
            if "RelatedSeriesSequence" in self._dataset:
                del self._dataset.RelatedSeriesSequence
        elif not isinstance(value, list) or not all(isinstance(item, RelatedSeriesSequenceItem) for item in value):
            raise ValueError("RelatedSeriesSequence must be a list of RelatedSeriesSequenceItem objects")
        else:
            self._RelatedSeriesSequence = value
            if "RelatedSeriesSequence" not in self._dataset:
                self._dataset.RelatedSeriesSequence = pydicom.Sequence()
            self._dataset.RelatedSeriesSequence.clear()
            self._dataset.RelatedSeriesSequence.extend([item.to_dataset() for item in value])

    def add_RelatedSeries(self, item: RelatedSeriesSequenceItem):
        if not isinstance(item, RelatedSeriesSequenceItem):
            raise ValueError("Item must be an instance of RelatedSeriesSequenceItem")
        self._RelatedSeriesSequence.append(item)
        if "RelatedSeriesSequence" not in self._dataset:
            self._dataset.RelatedSeriesSequence = pydicom.Sequence()
        self._dataset.RelatedSeriesSequence.append(item.to_dataset())

    @property
    def AnatomicalOrientationType(self) -> Optional[str]:
        if "AnatomicalOrientationType" in self._dataset:
            return self._dataset.AnatomicalOrientationType
        return None

    @AnatomicalOrientationType.setter
    def AnatomicalOrientationType(self, value: Optional[str]):
        if value is None:
            if "AnatomicalOrientationType" in self._dataset:
                del self._dataset.AnatomicalOrientationType
        else:
            self._dataset.AnatomicalOrientationType = value

    @property
    def BodyPartExamined(self) -> Optional[str]:
        if "BodyPartExamined" in self._dataset:
            return self._dataset.BodyPartExamined
        return None

    @BodyPartExamined.setter
    def BodyPartExamined(self, value: Optional[str]):
        if value is None:
            if "BodyPartExamined" in self._dataset:
                del self._dataset.BodyPartExamined
        else:
            self._dataset.BodyPartExamined = value

    @property
    def ProtocolName(self) -> Optional[str]:
        if "ProtocolName" in self._dataset:
            return self._dataset.ProtocolName
        return None

    @ProtocolName.setter
    def ProtocolName(self, value: Optional[str]):
        if value is None:
            if "ProtocolName" in self._dataset:
                del self._dataset.ProtocolName
        else:
            self._dataset.ProtocolName = value

    @property
    def PatientPosition(self) -> Optional[str]:
        if "PatientPosition" in self._dataset:
            return self._dataset.PatientPosition
        return None

    @PatientPosition.setter
    def PatientPosition(self, value: Optional[str]):
        if value is None:
            if "PatientPosition" in self._dataset:
                del self._dataset.PatientPosition
        else:
            self._dataset.PatientPosition = value

    @property
    def SeriesInstanceUID(self) -> Optional[str]:
        if "SeriesInstanceUID" in self._dataset:
            return self._dataset.SeriesInstanceUID
        return None

    @SeriesInstanceUID.setter
    def SeriesInstanceUID(self, value: Optional[str]):
        if value is None:
            if "SeriesInstanceUID" in self._dataset:
                del self._dataset.SeriesInstanceUID
        else:
            self._dataset.SeriesInstanceUID = value

    @property
    def SeriesNumber(self) -> Optional[int]:
        if "SeriesNumber" in self._dataset:
            return self._dataset.SeriesNumber
        return None

    @SeriesNumber.setter
    def SeriesNumber(self, value: Optional[int]):
        if value is None:
            if "SeriesNumber" in self._dataset:
                del self._dataset.SeriesNumber
        else:
            self._dataset.SeriesNumber = value

    @property
    def Laterality(self) -> Optional[str]:
        if "Laterality" in self._dataset:
            return self._dataset.Laterality
        return None

    @Laterality.setter
    def Laterality(self, value: Optional[str]):
        if value is None:
            if "Laterality" in self._dataset:
                del self._dataset.Laterality
        else:
            self._dataset.Laterality = value

    @property
    def SmallestPixelValueInSeries(self) -> Optional[int]:
        if "SmallestPixelValueInSeries" in self._dataset:
            return self._dataset.SmallestPixelValueInSeries
        return None

    @SmallestPixelValueInSeries.setter
    def SmallestPixelValueInSeries(self, value: Optional[int]):
        if value is None:
            if "SmallestPixelValueInSeries" in self._dataset:
                del self._dataset.SmallestPixelValueInSeries
        else:
            self._dataset.SmallestPixelValueInSeries = value

    @property
    def LargestPixelValueInSeries(self) -> Optional[int]:
        if "LargestPixelValueInSeries" in self._dataset:
            return self._dataset.LargestPixelValueInSeries
        return None

    @LargestPixelValueInSeries.setter
    def LargestPixelValueInSeries(self, value: Optional[int]):
        if value is None:
            if "LargestPixelValueInSeries" in self._dataset:
                del self._dataset.LargestPixelValueInSeries
        else:
            self._dataset.LargestPixelValueInSeries = value

    @property
    def PerformedProcedureStepStartDate(self) -> Optional[str]:
        if "PerformedProcedureStepStartDate" in self._dataset:
            return self._dataset.PerformedProcedureStepStartDate
        return None

    @PerformedProcedureStepStartDate.setter
    def PerformedProcedureStepStartDate(self, value: Optional[str]):
        if value is None:
            if "PerformedProcedureStepStartDate" in self._dataset:
                del self._dataset.PerformedProcedureStepStartDate
        else:
            self._dataset.PerformedProcedureStepStartDate = value

    @property
    def PerformedProcedureStepStartTime(self) -> Optional[str]:
        if "PerformedProcedureStepStartTime" in self._dataset:
            return self._dataset.PerformedProcedureStepStartTime
        return None

    @PerformedProcedureStepStartTime.setter
    def PerformedProcedureStepStartTime(self, value: Optional[str]):
        if value is None:
            if "PerformedProcedureStepStartTime" in self._dataset:
                del self._dataset.PerformedProcedureStepStartTime
        else:
            self._dataset.PerformedProcedureStepStartTime = value

    @property
    def PerformedProcedureStepEndDate(self) -> Optional[str]:
        if "PerformedProcedureStepEndDate" in self._dataset:
            return self._dataset.PerformedProcedureStepEndDate
        return None

    @PerformedProcedureStepEndDate.setter
    def PerformedProcedureStepEndDate(self, value: Optional[str]):
        if value is None:
            if "PerformedProcedureStepEndDate" in self._dataset:
                del self._dataset.PerformedProcedureStepEndDate
        else:
            self._dataset.PerformedProcedureStepEndDate = value

    @property
    def PerformedProcedureStepEndTime(self) -> Optional[str]:
        if "PerformedProcedureStepEndTime" in self._dataset:
            return self._dataset.PerformedProcedureStepEndTime
        return None

    @PerformedProcedureStepEndTime.setter
    def PerformedProcedureStepEndTime(self, value: Optional[str]):
        if value is None:
            if "PerformedProcedureStepEndTime" in self._dataset:
                del self._dataset.PerformedProcedureStepEndTime
        else:
            self._dataset.PerformedProcedureStepEndTime = value

    @property
    def PerformedProcedureStepID(self) -> Optional[str]:
        if "PerformedProcedureStepID" in self._dataset:
            return self._dataset.PerformedProcedureStepID
        return None

    @PerformedProcedureStepID.setter
    def PerformedProcedureStepID(self, value: Optional[str]):
        if value is None:
            if "PerformedProcedureStepID" in self._dataset:
                del self._dataset.PerformedProcedureStepID
        else:
            self._dataset.PerformedProcedureStepID = value

    @property
    def PerformedProcedureStepDescription(self) -> Optional[str]:
        if "PerformedProcedureStepDescription" in self._dataset:
            return self._dataset.PerformedProcedureStepDescription
        return None

    @PerformedProcedureStepDescription.setter
    def PerformedProcedureStepDescription(self, value: Optional[str]):
        if value is None:
            if "PerformedProcedureStepDescription" in self._dataset:
                del self._dataset.PerformedProcedureStepDescription
        else:
            self._dataset.PerformedProcedureStepDescription = value

    @property
    def PerformedProtocolCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PerformedProtocolCodeSequence" in self._dataset:
            if len(self._PerformedProtocolCodeSequence) == len(self._dataset.PerformedProtocolCodeSequence):
                return self._PerformedProtocolCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PerformedProtocolCodeSequence]
        return None

    @PerformedProtocolCodeSequence.setter
    def PerformedProtocolCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PerformedProtocolCodeSequence = []
            if "PerformedProtocolCodeSequence" in self._dataset:
                del self._dataset.PerformedProtocolCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("PerformedProtocolCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PerformedProtocolCodeSequence = value
            if "PerformedProtocolCodeSequence" not in self._dataset:
                self._dataset.PerformedProtocolCodeSequence = pydicom.Sequence()
            self._dataset.PerformedProtocolCodeSequence.clear()
            self._dataset.PerformedProtocolCodeSequence.extend([item.to_dataset() for item in value])

    def add_PerformedProtocolCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._PerformedProtocolCodeSequence.append(item)
        if "PerformedProtocolCodeSequence" not in self._dataset:
            self._dataset.PerformedProtocolCodeSequence = pydicom.Sequence()
        self._dataset.PerformedProtocolCodeSequence.append(item.to_dataset())

    @property
    def RequestAttributesSequence(self) -> Optional[List[RequestAttributesSequenceItem]]:
        if "RequestAttributesSequence" in self._dataset:
            if len(self._RequestAttributesSequence) == len(self._dataset.RequestAttributesSequence):
                return self._RequestAttributesSequence
            else:
                return [RequestAttributesSequenceItem(x) for x in self._dataset.RequestAttributesSequence]
        return None

    @RequestAttributesSequence.setter
    def RequestAttributesSequence(self, value: Optional[List[RequestAttributesSequenceItem]]):
        if value is None:
            self._RequestAttributesSequence = []
            if "RequestAttributesSequence" in self._dataset:
                del self._dataset.RequestAttributesSequence
        elif not isinstance(value, list) or not all(isinstance(item, RequestAttributesSequenceItem) for item in value):
            raise ValueError("RequestAttributesSequence must be a list of RequestAttributesSequenceItem objects")
        else:
            self._RequestAttributesSequence = value
            if "RequestAttributesSequence" not in self._dataset:
                self._dataset.RequestAttributesSequence = pydicom.Sequence()
            self._dataset.RequestAttributesSequence.clear()
            self._dataset.RequestAttributesSequence.extend([item.to_dataset() for item in value])

    def add_RequestAttributes(self, item: RequestAttributesSequenceItem):
        if not isinstance(item, RequestAttributesSequenceItem):
            raise ValueError("Item must be an instance of RequestAttributesSequenceItem")
        self._RequestAttributesSequence.append(item)
        if "RequestAttributesSequence" not in self._dataset:
            self._dataset.RequestAttributesSequence = pydicom.Sequence()
        self._dataset.RequestAttributesSequence.append(item.to_dataset())

    @property
    def CommentsOnThePerformedProcedureStep(self) -> Optional[str]:
        if "CommentsOnThePerformedProcedureStep" in self._dataset:
            return self._dataset.CommentsOnThePerformedProcedureStep
        return None

    @CommentsOnThePerformedProcedureStep.setter
    def CommentsOnThePerformedProcedureStep(self, value: Optional[str]):
        if value is None:
            if "CommentsOnThePerformedProcedureStep" in self._dataset:
                del self._dataset.CommentsOnThePerformedProcedureStep
        else:
            self._dataset.CommentsOnThePerformedProcedureStep = value

    @property
    def TreatmentSessionUID(self) -> Optional[str]:
        if "TreatmentSessionUID" in self._dataset:
            return self._dataset.TreatmentSessionUID
        return None

    @TreatmentSessionUID.setter
    def TreatmentSessionUID(self, value: Optional[str]):
        if value is None:
            if "TreatmentSessionUID" in self._dataset:
                del self._dataset.TreatmentSessionUID
        else:
            self._dataset.TreatmentSessionUID = value

    @property
    def ShutterShape(self) -> Optional[List[str]]:
        if "ShutterShape" in self._dataset:
            return self._dataset.ShutterShape
        return None

    @ShutterShape.setter
    def ShutterShape(self, value: Optional[List[str]]):
        if value is None:
            if "ShutterShape" in self._dataset:
                del self._dataset.ShutterShape
        else:
            self._dataset.ShutterShape = value

    @property
    def ShutterLeftVerticalEdge(self) -> Optional[int]:
        if "ShutterLeftVerticalEdge" in self._dataset:
            return self._dataset.ShutterLeftVerticalEdge
        return None

    @ShutterLeftVerticalEdge.setter
    def ShutterLeftVerticalEdge(self, value: Optional[int]):
        if value is None:
            if "ShutterLeftVerticalEdge" in self._dataset:
                del self._dataset.ShutterLeftVerticalEdge
        else:
            self._dataset.ShutterLeftVerticalEdge = value

    @property
    def ShutterRightVerticalEdge(self) -> Optional[int]:
        if "ShutterRightVerticalEdge" in self._dataset:
            return self._dataset.ShutterRightVerticalEdge
        return None

    @ShutterRightVerticalEdge.setter
    def ShutterRightVerticalEdge(self, value: Optional[int]):
        if value is None:
            if "ShutterRightVerticalEdge" in self._dataset:
                del self._dataset.ShutterRightVerticalEdge
        else:
            self._dataset.ShutterRightVerticalEdge = value

    @property
    def ShutterUpperHorizontalEdge(self) -> Optional[int]:
        if "ShutterUpperHorizontalEdge" in self._dataset:
            return self._dataset.ShutterUpperHorizontalEdge
        return None

    @ShutterUpperHorizontalEdge.setter
    def ShutterUpperHorizontalEdge(self, value: Optional[int]):
        if value is None:
            if "ShutterUpperHorizontalEdge" in self._dataset:
                del self._dataset.ShutterUpperHorizontalEdge
        else:
            self._dataset.ShutterUpperHorizontalEdge = value

    @property
    def ShutterLowerHorizontalEdge(self) -> Optional[int]:
        if "ShutterLowerHorizontalEdge" in self._dataset:
            return self._dataset.ShutterLowerHorizontalEdge
        return None

    @ShutterLowerHorizontalEdge.setter
    def ShutterLowerHorizontalEdge(self, value: Optional[int]):
        if value is None:
            if "ShutterLowerHorizontalEdge" in self._dataset:
                del self._dataset.ShutterLowerHorizontalEdge
        else:
            self._dataset.ShutterLowerHorizontalEdge = value

    @property
    def CenterOfCircularShutter(self) -> Optional[List[int]]:
        if "CenterOfCircularShutter" in self._dataset:
            return self._dataset.CenterOfCircularShutter
        return None

    @CenterOfCircularShutter.setter
    def CenterOfCircularShutter(self, value: Optional[List[int]]):
        if value is None:
            if "CenterOfCircularShutter" in self._dataset:
                del self._dataset.CenterOfCircularShutter
        else:
            self._dataset.CenterOfCircularShutter = value

    @property
    def RadiusOfCircularShutter(self) -> Optional[int]:
        if "RadiusOfCircularShutter" in self._dataset:
            return self._dataset.RadiusOfCircularShutter
        return None

    @RadiusOfCircularShutter.setter
    def RadiusOfCircularShutter(self, value: Optional[int]):
        if value is None:
            if "RadiusOfCircularShutter" in self._dataset:
                del self._dataset.RadiusOfCircularShutter
        else:
            self._dataset.RadiusOfCircularShutter = value

    @property
    def VerticesOfThePolygonalShutter(self) -> Optional[List[int]]:
        if "VerticesOfThePolygonalShutter" in self._dataset:
            return self._dataset.VerticesOfThePolygonalShutter
        return None

    @VerticesOfThePolygonalShutter.setter
    def VerticesOfThePolygonalShutter(self, value: Optional[List[int]]):
        if value is None:
            if "VerticesOfThePolygonalShutter" in self._dataset:
                del self._dataset.VerticesOfThePolygonalShutter
        else:
            self._dataset.VerticesOfThePolygonalShutter = value

    @property
    def ShutterPresentationValue(self) -> Optional[int]:
        if "ShutterPresentationValue" in self._dataset:
            return self._dataset.ShutterPresentationValue
        return None

    @ShutterPresentationValue.setter
    def ShutterPresentationValue(self, value: Optional[int]):
        if value is None:
            if "ShutterPresentationValue" in self._dataset:
                del self._dataset.ShutterPresentationValue
        else:
            self._dataset.ShutterPresentationValue = value

    @property
    def ShutterPresentationColorCIELabValue(self) -> Optional[List[int]]:
        if "ShutterPresentationColorCIELabValue" in self._dataset:
            return self._dataset.ShutterPresentationColorCIELabValue
        return None

    @ShutterPresentationColorCIELabValue.setter
    def ShutterPresentationColorCIELabValue(self, value: Optional[List[int]]):
        if value is None:
            if "ShutterPresentationColorCIELabValue" in self._dataset:
                del self._dataset.ShutterPresentationColorCIELabValue
        else:
            self._dataset.ShutterPresentationColorCIELabValue = value

    @property
    def ImageType(self) -> Optional[List[str]]:
        if "ImageType" in self._dataset:
            return self._dataset.ImageType
        return None

    @ImageType.setter
    def ImageType(self, value: Optional[List[str]]):
        if value is None:
            if "ImageType" in self._dataset:
                del self._dataset.ImageType
        else:
            self._dataset.ImageType = value

    @property
    def DerivationDescription(self) -> Optional[str]:
        if "DerivationDescription" in self._dataset:
            return self._dataset.DerivationDescription
        return None

    @DerivationDescription.setter
    def DerivationDescription(self, value: Optional[str]):
        if value is None:
            if "DerivationDescription" in self._dataset:
                del self._dataset.DerivationDescription
        else:
            self._dataset.DerivationDescription = value

    @property
    def AcquisitionDeviceProcessingDescription(self) -> Optional[str]:
        if "AcquisitionDeviceProcessingDescription" in self._dataset:
            return self._dataset.AcquisitionDeviceProcessingDescription
        return None

    @AcquisitionDeviceProcessingDescription.setter
    def AcquisitionDeviceProcessingDescription(self, value: Optional[str]):
        if value is None:
            if "AcquisitionDeviceProcessingDescription" in self._dataset:
                del self._dataset.AcquisitionDeviceProcessingDescription
        else:
            self._dataset.AcquisitionDeviceProcessingDescription = value

    @property
    def AcquisitionDeviceProcessingCode(self) -> Optional[str]:
        if "AcquisitionDeviceProcessingCode" in self._dataset:
            return self._dataset.AcquisitionDeviceProcessingCode
        return None

    @AcquisitionDeviceProcessingCode.setter
    def AcquisitionDeviceProcessingCode(self, value: Optional[str]):
        if value is None:
            if "AcquisitionDeviceProcessingCode" in self._dataset:
                del self._dataset.AcquisitionDeviceProcessingCode
        else:
            self._dataset.AcquisitionDeviceProcessingCode = value

    @property
    def PatientOrientation(self) -> Optional[List[str]]:
        if "PatientOrientation" in self._dataset:
            return self._dataset.PatientOrientation
        return None

    @PatientOrientation.setter
    def PatientOrientation(self, value: Optional[List[str]]):
        if value is None:
            if "PatientOrientation" in self._dataset:
                del self._dataset.PatientOrientation
        else:
            self._dataset.PatientOrientation = value

    @property
    def SamplesPerPixel(self) -> Optional[int]:
        if "SamplesPerPixel" in self._dataset:
            return self._dataset.SamplesPerPixel
        return None

    @SamplesPerPixel.setter
    def SamplesPerPixel(self, value: Optional[int]):
        if value is None:
            if "SamplesPerPixel" in self._dataset:
                del self._dataset.SamplesPerPixel
        else:
            self._dataset.SamplesPerPixel = value

    @property
    def PhotometricInterpretation(self) -> Optional[str]:
        if "PhotometricInterpretation" in self._dataset:
            return self._dataset.PhotometricInterpretation
        return None

    @PhotometricInterpretation.setter
    def PhotometricInterpretation(self, value: Optional[str]):
        if value is None:
            if "PhotometricInterpretation" in self._dataset:
                del self._dataset.PhotometricInterpretation
        else:
            self._dataset.PhotometricInterpretation = value

    @property
    def BitsAllocated(self) -> Optional[int]:
        if "BitsAllocated" in self._dataset:
            return self._dataset.BitsAllocated
        return None

    @BitsAllocated.setter
    def BitsAllocated(self, value: Optional[int]):
        if value is None:
            if "BitsAllocated" in self._dataset:
                del self._dataset.BitsAllocated
        else:
            self._dataset.BitsAllocated = value

    @property
    def BitsStored(self) -> Optional[int]:
        if "BitsStored" in self._dataset:
            return self._dataset.BitsStored
        return None

    @BitsStored.setter
    def BitsStored(self, value: Optional[int]):
        if value is None:
            if "BitsStored" in self._dataset:
                del self._dataset.BitsStored
        else:
            self._dataset.BitsStored = value

    @property
    def HighBit(self) -> Optional[int]:
        if "HighBit" in self._dataset:
            return self._dataset.HighBit
        return None

    @HighBit.setter
    def HighBit(self, value: Optional[int]):
        if value is None:
            if "HighBit" in self._dataset:
                del self._dataset.HighBit
        else:
            self._dataset.HighBit = value

    @property
    def PixelRepresentation(self) -> Optional[int]:
        if "PixelRepresentation" in self._dataset:
            return self._dataset.PixelRepresentation
        return None

    @PixelRepresentation.setter
    def PixelRepresentation(self, value: Optional[int]):
        if value is None:
            if "PixelRepresentation" in self._dataset:
                del self._dataset.PixelRepresentation
        else:
            self._dataset.PixelRepresentation = value

    @property
    def BurnedInAnnotation(self) -> Optional[str]:
        if "BurnedInAnnotation" in self._dataset:
            return self._dataset.BurnedInAnnotation
        return None

    @BurnedInAnnotation.setter
    def BurnedInAnnotation(self, value: Optional[str]):
        if value is None:
            if "BurnedInAnnotation" in self._dataset:
                del self._dataset.BurnedInAnnotation
        else:
            self._dataset.BurnedInAnnotation = value

    @property
    def PixelIntensityRelationship(self) -> Optional[str]:
        if "PixelIntensityRelationship" in self._dataset:
            return self._dataset.PixelIntensityRelationship
        return None

    @PixelIntensityRelationship.setter
    def PixelIntensityRelationship(self, value: Optional[str]):
        if value is None:
            if "PixelIntensityRelationship" in self._dataset:
                del self._dataset.PixelIntensityRelationship
        else:
            self._dataset.PixelIntensityRelationship = value

    @property
    def PixelIntensityRelationshipSign(self) -> Optional[int]:
        if "PixelIntensityRelationshipSign" in self._dataset:
            return self._dataset.PixelIntensityRelationshipSign
        return None

    @PixelIntensityRelationshipSign.setter
    def PixelIntensityRelationshipSign(self, value: Optional[int]):
        if value is None:
            if "PixelIntensityRelationshipSign" in self._dataset:
                del self._dataset.PixelIntensityRelationshipSign
        else:
            self._dataset.PixelIntensityRelationshipSign = value

    @property
    def WindowCenter(self) -> Optional[List[Decimal]]:
        if "WindowCenter" in self._dataset:
            return self._dataset.WindowCenter
        return None

    @WindowCenter.setter
    def WindowCenter(self, value: Optional[List[Decimal]]):
        if value is None:
            if "WindowCenter" in self._dataset:
                del self._dataset.WindowCenter
        else:
            self._dataset.WindowCenter = value

    @property
    def WindowWidth(self) -> Optional[List[Decimal]]:
        if "WindowWidth" in self._dataset:
            return self._dataset.WindowWidth
        return None

    @WindowWidth.setter
    def WindowWidth(self, value: Optional[List[Decimal]]):
        if value is None:
            if "WindowWidth" in self._dataset:
                del self._dataset.WindowWidth
        else:
            self._dataset.WindowWidth = value

    @property
    def RescaleIntercept(self) -> Optional[Decimal]:
        if "RescaleIntercept" in self._dataset:
            return self._dataset.RescaleIntercept
        return None

    @RescaleIntercept.setter
    def RescaleIntercept(self, value: Optional[Decimal]):
        if value is None:
            if "RescaleIntercept" in self._dataset:
                del self._dataset.RescaleIntercept
        else:
            self._dataset.RescaleIntercept = value

    @property
    def RescaleSlope(self) -> Optional[Decimal]:
        if "RescaleSlope" in self._dataset:
            return self._dataset.RescaleSlope
        return None

    @RescaleSlope.setter
    def RescaleSlope(self, value: Optional[Decimal]):
        if value is None:
            if "RescaleSlope" in self._dataset:
                del self._dataset.RescaleSlope
        else:
            self._dataset.RescaleSlope = value

    @property
    def RescaleType(self) -> Optional[str]:
        if "RescaleType" in self._dataset:
            return self._dataset.RescaleType
        return None

    @RescaleType.setter
    def RescaleType(self, value: Optional[str]):
        if value is None:
            if "RescaleType" in self._dataset:
                del self._dataset.RescaleType
        else:
            self._dataset.RescaleType = value

    @property
    def WindowCenterWidthExplanation(self) -> Optional[List[str]]:
        if "WindowCenterWidthExplanation" in self._dataset:
            return self._dataset.WindowCenterWidthExplanation
        return None

    @WindowCenterWidthExplanation.setter
    def WindowCenterWidthExplanation(self, value: Optional[List[str]]):
        if value is None:
            if "WindowCenterWidthExplanation" in self._dataset:
                del self._dataset.WindowCenterWidthExplanation
        else:
            self._dataset.WindowCenterWidthExplanation = value

    @property
    def LossyImageCompression(self) -> Optional[str]:
        if "LossyImageCompression" in self._dataset:
            return self._dataset.LossyImageCompression
        return None

    @LossyImageCompression.setter
    def LossyImageCompression(self, value: Optional[str]):
        if value is None:
            if "LossyImageCompression" in self._dataset:
                del self._dataset.LossyImageCompression
        else:
            self._dataset.LossyImageCompression = value

    @property
    def LossyImageCompressionRatio(self) -> Optional[List[Decimal]]:
        if "LossyImageCompressionRatio" in self._dataset:
            return self._dataset.LossyImageCompressionRatio
        return None

    @LossyImageCompressionRatio.setter
    def LossyImageCompressionRatio(self, value: Optional[List[Decimal]]):
        if value is None:
            if "LossyImageCompressionRatio" in self._dataset:
                del self._dataset.LossyImageCompressionRatio
        else:
            self._dataset.LossyImageCompressionRatio = value

    @property
    def VOILUTSequence(self) -> Optional[List[VOILUTSequenceItem]]:
        if "VOILUTSequence" in self._dataset:
            if len(self._VOILUTSequence) == len(self._dataset.VOILUTSequence):
                return self._VOILUTSequence
            else:
                return [VOILUTSequenceItem(x) for x in self._dataset.VOILUTSequence]
        return None

    @VOILUTSequence.setter
    def VOILUTSequence(self, value: Optional[List[VOILUTSequenceItem]]):
        if value is None:
            self._VOILUTSequence = []
            if "VOILUTSequence" in self._dataset:
                del self._dataset.VOILUTSequence
        elif not isinstance(value, list) or not all(isinstance(item, VOILUTSequenceItem) for item in value):
            raise ValueError("VOILUTSequence must be a list of VOILUTSequenceItem objects")
        else:
            self._VOILUTSequence = value
            if "VOILUTSequence" not in self._dataset:
                self._dataset.VOILUTSequence = pydicom.Sequence()
            self._dataset.VOILUTSequence.clear()
            self._dataset.VOILUTSequence.extend([item.to_dataset() for item in value])

    def CalibrationImage(self) -> Optional[str]:
        if "CalibrationImage" in self._dataset:
            return self._dataset.CalibrationImage
        return None

    @CalibrationImage.setter
    def CalibrationImage(self, value: Optional[str]):
        if value is None:
            if "CalibrationImage" in self._dataset:
                del self._dataset.CalibrationImage
        else:
            self._dataset.CalibrationImage = value

    @property
    def PresentationLUTShape(self) -> Optional[str]:
        if "PresentationLUTShape" in self._dataset:
            return self._dataset.PresentationLUTShape
        return None

    @PresentationLUTShape.setter
    def PresentationLUTShape(self, value: Optional[str]):
        if value is None:
            if "PresentationLUTShape" in self._dataset:
                del self._dataset.PresentationLUTShape
        else:
            self._dataset.PresentationLUTShape = value

    @property
    def CollimatorShape(self) -> Optional[List[str]]:
        if "CollimatorShape" in self._dataset:
            return self._dataset.CollimatorShape
        return None

    @CollimatorShape.setter
    def CollimatorShape(self, value: Optional[List[str]]):
        if value is None:
            if "CollimatorShape" in self._dataset:
                del self._dataset.CollimatorShape
        else:
            self._dataset.CollimatorShape = value

    @property
    def CollimatorLeftVerticalEdge(self) -> Optional[int]:
        if "CollimatorLeftVerticalEdge" in self._dataset:
            return self._dataset.CollimatorLeftVerticalEdge
        return None

    @CollimatorLeftVerticalEdge.setter
    def CollimatorLeftVerticalEdge(self, value: Optional[int]):
        if value is None:
            if "CollimatorLeftVerticalEdge" in self._dataset:
                del self._dataset.CollimatorLeftVerticalEdge
        else:
            self._dataset.CollimatorLeftVerticalEdge = value

    @property
    def CollimatorRightVerticalEdge(self) -> Optional[int]:
        if "CollimatorRightVerticalEdge" in self._dataset:
            return self._dataset.CollimatorRightVerticalEdge
        return None

    @CollimatorRightVerticalEdge.setter
    def CollimatorRightVerticalEdge(self, value: Optional[int]):
        if value is None:
            if "CollimatorRightVerticalEdge" in self._dataset:
                del self._dataset.CollimatorRightVerticalEdge
        else:
            self._dataset.CollimatorRightVerticalEdge = value

    @property
    def CollimatorUpperHorizontalEdge(self) -> Optional[int]:
        if "CollimatorUpperHorizontalEdge" in self._dataset:
            return self._dataset.CollimatorUpperHorizontalEdge
        return None

    @CollimatorUpperHorizontalEdge.setter
    def CollimatorUpperHorizontalEdge(self, value: Optional[int]):
        if value is None:
            if "CollimatorUpperHorizontalEdge" in self._dataset:
                del self._dataset.CollimatorUpperHorizontalEdge
        else:
            self._dataset.CollimatorUpperHorizontalEdge = value

    @property
    def CollimatorLowerHorizontalEdge(self) -> Optional[int]:
        if "CollimatorLowerHorizontalEdge" in self._dataset:
            return self._dataset.CollimatorLowerHorizontalEdge
        return None

    @CollimatorLowerHorizontalEdge.setter
    def CollimatorLowerHorizontalEdge(self, value: Optional[int]):
        if value is None:
            if "CollimatorLowerHorizontalEdge" in self._dataset:
                del self._dataset.CollimatorLowerHorizontalEdge
        else:
            self._dataset.CollimatorLowerHorizontalEdge = value

    @property
    def CenterOfCircularCollimator(self) -> Optional[List[int]]:
        if "CenterOfCircularCollimator" in self._dataset:
            return self._dataset.CenterOfCircularCollimator
        return None

    @CenterOfCircularCollimator.setter
    def CenterOfCircularCollimator(self, value: Optional[List[int]]):
        if value is None:
            if "CenterOfCircularCollimator" in self._dataset:
                del self._dataset.CenterOfCircularCollimator
        else:
            self._dataset.CenterOfCircularCollimator = value

    @property
    def RadiusOfCircularCollimator(self) -> Optional[int]:
        if "RadiusOfCircularCollimator" in self._dataset:
            return self._dataset.RadiusOfCircularCollimator
        return None

    @RadiusOfCircularCollimator.setter
    def RadiusOfCircularCollimator(self, value: Optional[int]):
        if value is None:
            if "RadiusOfCircularCollimator" in self._dataset:
                del self._dataset.RadiusOfCircularCollimator
        else:
            self._dataset.RadiusOfCircularCollimator = value

    @property
    def VerticesOfThePolygonalCollimator(self) -> Optional[List[int]]:
        if "VerticesOfThePolygonalCollimator" in self._dataset:
            return self._dataset.VerticesOfThePolygonalCollimator
        return None

    @VerticesOfThePolygonalCollimator.setter
    def VerticesOfThePolygonalCollimator(self, value: Optional[List[int]]):
        if value is None:
            if "VerticesOfThePolygonalCollimator" in self._dataset:
                del self._dataset.VerticesOfThePolygonalCollimator
        else:
            self._dataset.VerticesOfThePolygonalCollimator = value

    @property
    def ClinicalTrialTimePointID(self) -> Optional[str]:
        if "ClinicalTrialTimePointID" in self._dataset:
            return self._dataset.ClinicalTrialTimePointID
        return None

    @ClinicalTrialTimePointID.setter
    def ClinicalTrialTimePointID(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialTimePointID" in self._dataset:
                del self._dataset.ClinicalTrialTimePointID
        else:
            self._dataset.ClinicalTrialTimePointID = value

    @property
    def ClinicalTrialTimePointDescription(self) -> Optional[str]:
        if "ClinicalTrialTimePointDescription" in self._dataset:
            return self._dataset.ClinicalTrialTimePointDescription
        return None

    @ClinicalTrialTimePointDescription.setter
    def ClinicalTrialTimePointDescription(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialTimePointDescription" in self._dataset:
                del self._dataset.ClinicalTrialTimePointDescription
        else:
            self._dataset.ClinicalTrialTimePointDescription = value

    @property
    def LongitudinalTemporalOffsetFromEvent(self) -> Optional[float]:
        if "LongitudinalTemporalOffsetFromEvent" in self._dataset:
            return self._dataset.LongitudinalTemporalOffsetFromEvent
        return None

    @LongitudinalTemporalOffsetFromEvent.setter
    def LongitudinalTemporalOffsetFromEvent(self, value: Optional[float]):
        if value is None:
            if "LongitudinalTemporalOffsetFromEvent" in self._dataset:
                del self._dataset.LongitudinalTemporalOffsetFromEvent
        else:
            self._dataset.LongitudinalTemporalOffsetFromEvent = value

    @property
    def LongitudinalTemporalEventType(self) -> Optional[str]:
        if "LongitudinalTemporalEventType" in self._dataset:
            return self._dataset.LongitudinalTemporalEventType
        return None

    @LongitudinalTemporalEventType.setter
    def LongitudinalTemporalEventType(self, value: Optional[str]):
        if value is None:
            if "LongitudinalTemporalEventType" in self._dataset:
                del self._dataset.LongitudinalTemporalEventType
        else:
            self._dataset.LongitudinalTemporalEventType = value

    @property
    def ClinicalTrialTimePointTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ClinicalTrialTimePointTypeCodeSequence" in self._dataset:
            if len(self._ClinicalTrialTimePointTypeCodeSequence) == len(self._dataset.ClinicalTrialTimePointTypeCodeSequence):
                return self._ClinicalTrialTimePointTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ClinicalTrialTimePointTypeCodeSequence]
        return None

    @ClinicalTrialTimePointTypeCodeSequence.setter
    def ClinicalTrialTimePointTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ClinicalTrialTimePointTypeCodeSequence = []
            if "ClinicalTrialTimePointTypeCodeSequence" in self._dataset:
                del self._dataset.ClinicalTrialTimePointTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("ClinicalTrialTimePointTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ClinicalTrialTimePointTypeCodeSequence = value
            if "ClinicalTrialTimePointTypeCodeSequence" not in self._dataset:
                self._dataset.ClinicalTrialTimePointTypeCodeSequence = pydicom.Sequence()
            self._dataset.ClinicalTrialTimePointTypeCodeSequence.clear()
            self._dataset.ClinicalTrialTimePointTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_ClinicalTrialTimePointTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ClinicalTrialTimePointTypeCodeSequence.append(item)
        if "ClinicalTrialTimePointTypeCodeSequence" not in self._dataset:
            self._dataset.ClinicalTrialTimePointTypeCodeSequence = pydicom.Sequence()
        self._dataset.ClinicalTrialTimePointTypeCodeSequence.append(item.to_dataset())

    @property
    def IssuerOfClinicalTrialTimePointID(self) -> Optional[str]:
        if "IssuerOfClinicalTrialTimePointID" in self._dataset:
            return self._dataset.IssuerOfClinicalTrialTimePointID
        return None

    @IssuerOfClinicalTrialTimePointID.setter
    def IssuerOfClinicalTrialTimePointID(self, value: Optional[str]):
        if value is None:
            if "IssuerOfClinicalTrialTimePointID" in self._dataset:
                del self._dataset.IssuerOfClinicalTrialTimePointID
        else:
            self._dataset.IssuerOfClinicalTrialTimePointID = value

    @property
    def ConsentForClinicalTrialUseSequence(self) -> Optional[List[ConsentForClinicalTrialUseSequenceItem]]:
        if "ConsentForClinicalTrialUseSequence" in self._dataset:
            if len(self._ConsentForClinicalTrialUseSequence) == len(self._dataset.ConsentForClinicalTrialUseSequence):
                return self._ConsentForClinicalTrialUseSequence
            else:
                return [ConsentForClinicalTrialUseSequenceItem(x) for x in self._dataset.ConsentForClinicalTrialUseSequence]
        return None

    @ConsentForClinicalTrialUseSequence.setter
    def ConsentForClinicalTrialUseSequence(self, value: Optional[List[ConsentForClinicalTrialUseSequenceItem]]):
        if value is None:
            self._ConsentForClinicalTrialUseSequence = []
            if "ConsentForClinicalTrialUseSequence" in self._dataset:
                del self._dataset.ConsentForClinicalTrialUseSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ConsentForClinicalTrialUseSequenceItem) for item in value
        ):
            raise ValueError(
                "ConsentForClinicalTrialUseSequence must be a list of ConsentForClinicalTrialUseSequenceItem objects"
            )
        else:
            self._ConsentForClinicalTrialUseSequence = value
            if "ConsentForClinicalTrialUseSequence" not in self._dataset:
                self._dataset.ConsentForClinicalTrialUseSequence = pydicom.Sequence()
            self._dataset.ConsentForClinicalTrialUseSequence.clear()
            self._dataset.ConsentForClinicalTrialUseSequence.extend([item.to_dataset() for item in value])

    def add_ConsentForClinicalTrialUse(self, item: ConsentForClinicalTrialUseSequenceItem):
        if not isinstance(item, ConsentForClinicalTrialUseSequenceItem):
            raise ValueError("Item must be an instance of ConsentForClinicalTrialUseSequenceItem")
        self._ConsentForClinicalTrialUseSequence.append(item)
        if "ConsentForClinicalTrialUseSequence" not in self._dataset:
            self._dataset.ConsentForClinicalTrialUseSequence = pydicom.Sequence()
        self._dataset.ConsentForClinicalTrialUseSequence.append(item.to_dataset())
