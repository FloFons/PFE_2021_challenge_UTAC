
"use strict";

let DeltaReferencePosition = require('./DeltaReferencePosition.js');
let BasicVehicleContainerLowFrequency = require('./BasicVehicleContainerLowFrequency.js');
let ManagementContainer = require('./ManagementContainer.js');
let CurvatureCalculationMode = require('./CurvatureCalculationMode.js');
let BasicVehicleContainerHighFrequency = require('./BasicVehicleContainerHighFrequency.js');
let SPAT = require('./SPAT.js');
let DriveDirection = require('./DriveDirection.js');
let PositionConfidenceEllipse = require('./PositionConfidenceEllipse.js');
let Heading = require('./Heading.js');
let PathPoint = require('./PathPoint.js');
let PathHistory = require('./PathHistory.js');
let VehicleWidth = require('./VehicleWidth.js');
let ItsPduHeader = require('./ItsPduHeader.js');
let ActionID = require('./ActionID.js');
let Altitude = require('./Altitude.js');
let CauseCode = require('./CauseCode.js');
let YawRate = require('./YawRate.js');
let LongitudinalAcceleration = require('./LongitudinalAcceleration.js');
let InformationQuality = require('./InformationQuality.js');
let ExteriorLights = require('./ExteriorLights.js');
let RelevanceTrafficDirection = require('./RelevanceTrafficDirection.js');
let VehicleRole = require('./VehicleRole.js');
let VehicleLength = require('./VehicleLength.js');
let EventPoint = require('./EventPoint.js');
let ReferencePosition = require('./ReferencePosition.js');
let RelevanceDistance = require('./RelevanceDistance.js');
let DENM = require('./DENM.js');
let SituationContainer = require('./SituationContainer.js');
let Curvature = require('./Curvature.js');
let PathDeltaTime = require('./PathDeltaTime.js');
let AccelerationControl = require('./AccelerationControl.js');
let Speed = require('./Speed.js');
let StationType = require('./StationType.js');
let CAM = require('./CAM.js');
let LocationContainer = require('./LocationContainer.js');

module.exports = {
  DeltaReferencePosition: DeltaReferencePosition,
  BasicVehicleContainerLowFrequency: BasicVehicleContainerLowFrequency,
  ManagementContainer: ManagementContainer,
  CurvatureCalculationMode: CurvatureCalculationMode,
  BasicVehicleContainerHighFrequency: BasicVehicleContainerHighFrequency,
  SPAT: SPAT,
  DriveDirection: DriveDirection,
  PositionConfidenceEllipse: PositionConfidenceEllipse,
  Heading: Heading,
  PathPoint: PathPoint,
  PathHistory: PathHistory,
  VehicleWidth: VehicleWidth,
  ItsPduHeader: ItsPduHeader,
  ActionID: ActionID,
  Altitude: Altitude,
  CauseCode: CauseCode,
  YawRate: YawRate,
  LongitudinalAcceleration: LongitudinalAcceleration,
  InformationQuality: InformationQuality,
  ExteriorLights: ExteriorLights,
  RelevanceTrafficDirection: RelevanceTrafficDirection,
  VehicleRole: VehicleRole,
  VehicleLength: VehicleLength,
  EventPoint: EventPoint,
  ReferencePosition: ReferencePosition,
  RelevanceDistance: RelevanceDistance,
  DENM: DENM,
  SituationContainer: SituationContainer,
  Curvature: Curvature,
  PathDeltaTime: PathDeltaTime,
  AccelerationControl: AccelerationControl,
  Speed: Speed,
  StationType: StationType,
  CAM: CAM,
  LocationContainer: LocationContainer,
};
