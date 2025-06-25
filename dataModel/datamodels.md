# ChargingStation

E4C charging station that contains multiple charging points for electric vehicles - static configuration data
-  `id`: Unique identifier of the charging station entity
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI-LD Entity type. It must be ChargingStation. One of : `ChargingStation`.
   -  Attribute type: **Property**. 
   -  Required
-  `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform
   -  Attribute type: **Property**. 
   -  Optional
-  `lastUpdated`: Timestamp when data was last updated
   -  Attribute type: **Property**. [DateTime](https://schema.org/DateTime)
   -  Optional
-  `stationName`: Name of the charging station
   -  Attribute type: **Property**. [Text](http://schema.org/Text)
   -  Required
-  `stationId`: External identifier or code for the station
   -  Attribute type: **Property**. [Text](http://schema.org/Text)
   -  Optional
-  `location`: Geojson reference to the item. Point location only
   -  Attribute type: **GeoProperty**. 
   -  Optional
-  `totalChargingPoints`: Total number of charging points installed in this station
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Required
-  `maxPowerCapacity`: Maximum total power capacity of the station in kW
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Optional
-  `ratedVoltage`: The rated voltage offered by the charging station in Volts
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Optional
-  `gridConnection`: Type of electrical grid connection. One of : `lowVoltage`, `mediumVoltage`, `highVoltage`, `directCurrent`.
   -  Attribute type: **Property**. [Text](http://schema.org/Text)
   -  Optional
-  `socketType`: Types of charging sockets/connectors available at this station
   -  Attribute type: **Property**. [Text](http://schema.org/Text)
   -  Required
-  `refChargingPoints`: References to charging points in this station
   -  Attribute type: **Relationship**. [URL](http://schema.org/URL)
   -  Optional
-  `refStationStatus`: Reference to real-time station status information
   -  Attribute type: **Relationship**. [URL](http://schema.org/URL)
   -  Optional



# ChargingStationStatus

Real-time operational status and dynamic data for E4C charging station
-  `id`: Unique identifier of the charging station status entity
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI-LD Entity type. It must be ChargingStationStatus. One of : `ChargingStationStatus`.
   -  Attribute type: **Property**. 
   -  Required
-  `refChargingStation`: Reference to the charging station this status belongs to
   -  Attribute type: **Relationship**. [URL](http://schema.org/URL)
   -  Required
-  `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform
   -  Attribute type: **Property**. 
   -  Required
-  `operationalStatus`: Overall operational status of the charging station. One of : `operational`, `outOfService`, `maintenance`.
   -  Attribute type: **Property**. [Text](http://schema.org/Text)
   -  Optional
-  `totalPoints`: Total number of charging points in the station
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Required
-  `availablePoints`: Number of currently available charging points
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Required
-  `occupiedPoints`: Number of occupied charging points
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Optional
-  `faultedPoints`: Number of faulted charging points
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Optional
-  `maintenancePoints`: Number of points under maintenance
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Optional
-  `reservedPoints`: Number of reserved charging points
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Optional
-  `currentPowerConsumption`: Current total power consumption of all active units in kW
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Optional
-  `currentGridPowerConsumption`: Current power consumption from electrical grid in kW
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Optional
-  `currentRenewablePowerConsumption`: Current power consumption from renewable energy sources in kW
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Optional
-  `activeSessionsCount`: Number of currently active charging sessions
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Optional
-  `queueLength`: Number of vehicles waiting in queue
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Optional
-  `estimatedWaitTime`: Estimated wait time for next available unit in minutes
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Optional
-  `ambientTemperature`: Current ambient temperature in Celsius
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Optional
-  `humidity`: Current relative humidity in percentage
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Optional
-  `weatherConditions`: Current weather conditions. One of : `clear`, `cloudy`, `rainy`, `snowy`, `stormy`, `windy`, `foggy`.
   -  Attribute type: **Property**. [Text](http://schema.org/Text)
   -  Optional
-  `gridVoltage`: Current grid voltage in Volts
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Optional
-  `gridFrequency`: Current grid frequency in Hz
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Optional
-  `powerFactor`: Current power factor
   -  Attribute type: **Property**. [Number](http://schema.org/Number)
   -  Optional
-  `lastMaintenanceDate`: Timestamp of last maintenance performed
   -  Attribute type: **Property**. 
   -  Optional
-  `nextScheduledMaintenance`: Next scheduled maintenance timestamp
   -  Attribute type: **Property**. 
   -  Optional



# ChargingPoint

An E4C charging point within a charging station, containing static configuration and specification data
-  `id`: Unique identifier of the charging point entity
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be ChargingPoint. One of : `ChargingPoint`.
   -  Attribute type: **Property**. 
   -  Required
-  `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform
   -  Attribute type: **Property**. 
   -  Optional
-  `lastUpdated`: Timestamp when data was last updated
   -  Attribute type: **Property**. [DateTime](https://schema.org/DateTime)
   -  Optional
-  `refChargingStation`: Reference to the charging station this point belongs to
   -  Attribute type: **Relationship**. [URL](https://schema.org/URL)
   -  Optional
-  `pointId`: External point identifier from charging management system
   -  Attribute type: **Property**. [Text](https://schema.org/Text)
   -  Optional
-  `chargingType`: Type of charging supported by this point. One of : `AC-Level1`, `AC-Level2`, `DC-FastCharging`, `bidirectional`.
   -  Attribute type: **Property**. [Text](https://schema.org/Text)
   -  Required
-  `connectorTypes`: Types of connectors available on this point
   -  Attribute type: **Property**. [Text](https://schema.org/Text)
   -  Required
-  `numberOfConnectors`: Number of connectors on this point
   -  Attribute type: **Property**. [Number](https://schema.org/Number)
   -  Optional
-  `powerCapabilities`: Detailed power capabilities of the point
   -  Attribute type: **Property**. [Object](https://schema.org/Object)
   -  Optional
-  `refSession`: Reference to current charging session if point is in use
   -  Attribute type: **Relationship**. [URL](https://schema.org/URL)
   -  Optional
-  `refChargingPointStatus`: Reference to the PointStatus
   -  Attribute type: **Relationship**. [URL](https://schema.org/URL)
   -  Optional
-  `communicationProtocol`: Communication protocol used by the point. One of : `OCPP1.6`, `OCPP2.0`, `OCPP2.0.1`, `ISO15118`, `proprietary`, `other`.
   -  Attribute type: **Property**. [Text](https://schema.org/Text)
   -  Optional



# ChargingPointStatus

Real-time operational status and dynamic data for E4C charging point, including current status, operating parameters, and monitoring information
-  `id`: Unique identifier of the charging point status entity
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be ChargingPointStatus. One of : `ChargingPointStatus`.
   -  Attribute type: **Property**. 
   -  Required
-  `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform
   -  Attribute type: **Property**. 
   -  Required
-  `refChargingPoint`: Reference to the charging point this status belongs to
   -  Attribute type: **Relationship**. [URL](https://schema.org/URL)
   -  Required
-  `unitStatus`: Current operational status of the charging point. One of : `available`, `occupied`, `reserved`, `charging`, `finishing`.
   -  Attribute type: **Property**. [Text](https://schema.org/Text)
   -  Required
-  `operatingData`: Current operating parameters of the point
   -  Attribute type: **Property**. [Object](https://schema.org/Object)
   -  Optional



# ChargingSession

E4C charging session represents a complete charging event for an electric vehicle, including session details, energy consumption, duration, and billing information
-  `id`: Unique identifier of the charging session entity
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be ChargingSession. One of : `ChargingSession`.
   -  Attribute type: **Property**. 
   -  Required
-  `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform
   -  Attribute type: **Property**. 
   -  Optional
-  `refVehicleStatus`: Reference to the E-Vehicle Status that is being charged
   -  Attribute type: **Relationship**. [URL](https://schema.org/URL)
   -  Optional
-  `refChargingPoint`: Reference to the charging point being used for this session
   -  Attribute type: **Relationship**. [URL](https://schema.org/URL)
   -  Required
-  `sessionId`: External session identifier from charging management system
   -  Attribute type: **Property**. [Text](https://schema.org/Text)
   -  Optional
-  `sessionStatus`: Current status of the charging session. One of : `initiated`, `authorized`, `started`, `charging`, `suspended`, `ended`, `completed`, `failed`, `cancelled`.
   -  Attribute type: **Property**. [Text](https://schema.org/Text)
   -  Required
-  `sessionType`: Type of charging session. One of : `AC-Level1`, `AC-Level2`, `DC-FastCharging`, `bidirectional`.
   -  Attribute type: **Property**. [Text](https://schema.org/Text)
   -  Optional
-  `sessionStartTime`: Timestamp when the charging session was initiated
   -  Attribute type: **Property**. [DateTime](https://schema.org/DateTime)
   -  Required
-  `sessionEndTime`: Timestamp when the charging session ended
   -  Attribute type: **Property**. [DateTime](https://schema.org/DateTime)
   -  Optional
-  `chargingStartTime`: Timestamp when actual charging (energy transfer) began
   -  Attribute type: **Property**. [DateTime](https://schema.org/DateTime)
   -  Optional
-  `chargingEndTime`: Timestamp when actual charging (energy transfer) ended
   -  Attribute type: **Property**. [DateTime](https://schema.org/DateTime)
   -  Optional
-  `sessionDuration`: Total session duration in minutes (from initiation to completion)
   -  Attribute type: **Property**. [Number](https://schema.org/Number)
   -  Optional
-  `chargingDuration`: Actual charging duration in minutes (energy transfer time)
   -  Attribute type: **Property**. [Number](https://schema.org/Number)
   -  Optional
-  `energyDelivered`: Total energy delivered during the session in kWh
   -  Attribute type: **Property**. [Number](https://schema.org/Number)
   -  Optional
-  `energyConsumed`: Total energy consumed from the grid during the session in kWh
   -  Attribute type: **Property**. [Number](https://schema.org/Number)
   -  Optional
-  `averageChargingPower`: Average charging power during the session in kW
   -  Attribute type: **Property**. [Number](https://schema.org/Number)
   -  Optional
-  `maxChargingPower`: Maximum charging power reached during the session in kW
   -  Attribute type: **Property**. [Number](https://schema.org/Number)
   -  Optional
-  `chargingEfficiency`: Overall charging efficiency as percentage
   -  Attribute type: **Property**. [Number](https://schema.org/Number)
   -  Optional
-  `batteryStatusAtStart`: Battery status when session started
   -  Attribute type: **Property**. [Object](https://schema.org/Object)
   -  Optional
-  `batteryStatusAtEnd`: Battery status when session ended
   -  Attribute type: **Property**. [Object](https://schema.org/Object)
   -  Optional
-  `userId`: Identifier of the user who initiated the session
   -  Attribute type: **Property**. [Text](https://schema.org/Text)
   -  Optional
-  `authenticationMethod`: Method used to authenticate the charging session. One of : `rfid`, `mobileApp`, `qrCode`, `nfc`, `web`.
   -  Attribute type: **Property**. [Text](https://schema.org/Text)
   -  Optional
-  `authenticationId`: Authentication identifier (RFID tag, user ID, etc.)
   -  Attribute type: **Property**. [Text](https://schema.org/Text)
   -  Optional
-  `chargingProtocol`: Communication protocol used for charging. One of : `IEC61851`, `CHAdeMO`, `CCS`, `Tesla`, `GB/T`, `ISO15118`, `OCPP`, `other`.
   -  Attribute type: **Property**. [Text](https://schema.org/Text)
   -  Optional
-  `endReason`: Reason why the charging session ended. One of : `completed`, `userStopped`, `batteryFull`, `timeLimit`, `powerLimit`, `emergency`, `error`, `maintenance`, `deAuthorized`, `other`.
   -  Attribute type: **Property**. [Text](https://schema.org/Text)
   -  Optional
-  `sessionRating`: User rating for the charging session (1-5)
   -  Attribute type: **Property**. [Number](https://schema.org/Number)
   -  Optional
-  `lastUpdated`: Timestamp when data was last updated
   -  Attribute type: **Property**. [DateTime](https://schema.org/DateTime)
   -  Required



# E-Vehicle

Static information and specifications for a E4C electric vehicle, including all properties which are common to the vehicle model and do not change frequently
-  `id`: Unique identifier of the electric vehicle entity
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be E-Vehicle. One of : `E-Vehicle`.
   -  Attribute type: **Property**. 
   -  Required
-  `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform
   -  Attribute type: **Property**. 
   -  Optional
-  `lastUpdated`: Timestamp when data was last updated
   -  Attribute type: **Property**. [DateTime](https://schema.org/DateTime)
   -  Optional
-  `vehiclePlateIdentifier`: An identifier or code displayed on a vehicle registration plate attached to the vehicle used for official identification purposes
   -  Attribute type: **Property**. [Text](https://schema.org/Text)
   -  Required
-  `brand`: Vehicle brand or manufacturer
   -  Attribute type: **Property**. [brand](https://schema.org/brand)
   -  Required
-  `color`: The color of the vehicle
   -  Attribute type: **Property**. [color](https://schema.org/color)
   -  Optional
-  `batterySpecifications`: Battery system specifications
   -  Attribute type: **Property**. [Object](https://schema.org/Object)
   -  Required
-  `chargingCapabilities`: Charging system capabilities and specifications
   -  Attribute type: **Property**. [Object](https://schema.org/Object)
   -  Required
-  `refVehicleStatus`: Reference to current VehicleS tatus
   -  Attribute type: **Relationship**. [URL](https://schema.org/URL)
   -  Required
-  `vehicleType`: Type of vehicle from the point of view of its structural characteristics. One of : `car`, `van`, `motorcycle`.
   -  Attribute type: **Property**. [Text](https://schema.org/Text)
   -  Required



# E-VehicleStatus

Real-time operational status and dynamic data for E4C electric vehicle, including battery status, location, charging state, and other frequently changing properties
-  `id`: Unique identifier of the electric vehicle status entity
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be E-VehicleStatus. One of : `E-VehicleStatus`.
   -  Attribute type: **Property**. 
   -  Required
-  `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform
   -  Attribute type: **Property**. 
   -  Required
-  `refVehicle`: Reference to the E-Vehicle this status belongs to
   -  Attribute type: **Relationship**. [URL](https://schema.org/URL)
   -  Required
-  `batteryStatus`: Current battery status and health information
   -  Attribute type: **Property**. [Object](https://schema.org/Object)
   -  Required
-  `batteryRangeStatus`: Real-time status about driving range, focused on charging/discharging scenarios
   -  Attribute type: **Property**. 
   -  Optional
-  `chargingStatus`: Current charging status and information
   -  Attribute type: **Property**. [Object](https://schema.org/Object)
   -  Optional
-  `refChargingSession`: Reference to current charging session if vehicle is currently charging
   -  Attribute type: **Relationship**. [URL](https://schema.org/URL)
   -  Optional



