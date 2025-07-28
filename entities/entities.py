from datetime import datetime, timedelta,timezone
import pytz
import pandas as pd

# charging station
CS_001 = {

    # required
    "id": "urn:ngsi-ld:ChargingStation:ParisSaclay30-1",
    "type": "ChargingStation",

    "stationName": {
        "type": "Property",
        "value": "IPP - Drahi - X"
    },

    "location": {
        "type": "Point",
        "coordinates": [2.212206,48.712779]
    },

    # required
    "totalChargingPoints": {
        "type": "Property",
        "value": 1
    },

    "maxPowerCapacity": {
        "type": "Property",
        "value": 22.0,
        "units": "kW"  
    },

    "ratedVoltage": {
        "type": "Property",
        "value": 400.0,
        "units": "V"
    },

    # required
    "socketType": {
        "type": "Property",
        "value": [
            "Type2"
        ]
    },

    "dateCreated": {
        "type": "Property",
        "value": {
            "@type": "DateTime",
            "@value": datetime.now().isoformat() + "Z"
        }
    }
}

CS_002 = {

    # required
    "id": "urn:ngsi-ld:ChargingStation:Building103",
    "type": "ChargingStation",

    "stationName": {
        "type": "Property",
        "value": "IPP - Building103"
    },

    # required
    "totalChargingPoints": {
        "type": "Property",
        "value": 1
    },

    # required
    "socketType": {
        "type": "Property",
        "value": [
            "Type2",
            "Schuko"
        ]
    },

    "dateCreated": {
        "type": "Property",
        "value": {
            "@type": "DateTime",
            "@value": datetime.now().isoformat() + "Z"
        }
    }
}

# charging point
CP_001 = {
    # required
    "id": "urn:ngsi-ld:ChargingPoint:ParisSaclay30-1-P-01",
    "type": "ChargingPoint",

    # required - Relationship to Parent Station
    "refChargingStation": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:ChargingStation:ParisSaclay30-1"
    },

    # required
    "chargingType": {
        "type": "Property",
        "value": "AC-Level2"
    },

    # required
    "connectorTypes": {
        "type": "Property",
        "value": [
            "Type2"
        ]
    },

    "powerCapabilities": {
        "type": "Property",
        "value": {
            "maxACPower": 22.0,
            "maxDCPower": 0,
            "maxVoltage": 400,
            "maxCurrent": 32,
            "phases": 3
        }
    },

    "communicationProtocol": {
        "type": "Property",
        "value": "OCPP1.6J"
    },

    "refChargingPointStatus": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:ChargingPointStatus:ParisSaclay30-1-P-01-status"
    },

    "dateCreated": {
        "type": "Property",
        "value": {
            "@type": "DateTime",
            "@value": datetime.now().isoformat() + "Z"
        }
    }
}

def B103_charging_point(point_number):
    formatted_number = str(point_number)
    
    charging_point = {
        "id": f"urn:ngsi-ld:ChargingPoint:Building103-P-{formatted_number}",
        "type": "ChargingPoint",
        
        "refChargingStation": {
            "type": "Relationship",
            "object": "urn:ngsi-ld:ChargingStation:Building103"
        },
        
        "chargingType": {
            "type": "Property",
            "value": "AC-Level2"
        },
        
        "connectorTypes": {
            "type": "Property",
            "value": ["Type2", "Schuko"]
        },
        
        "powerCapabilities": {
            "type": "Property",
            "value": {
                "maxACPower": 7.0
            }
        },
        
        "refChargingPointStatus": {
            "type": "Relationship",
            "object": f"urn:ngsi-ld:ChargingStation:Building103-P-{formatted_number}-status"
        },
        
        "dateCreated": {
            "type": "Property",
            "value": {
                "@type": "DateTime",
                "@value": datetime.now().isoformat() + "Z"
            }
        }
    }
    
    return charging_point

#EV 
EV_001 = {

    # required
    "id": "urn:ngsi-ld:E-Vehicle:EV-001",
    "type": "E-Vehicle",

    # required
    "vehiclePlateIdentifier": {
        "type": "Property",
        "value": "EE-049-CE"
    },

    # required
    "brand": {
        "type": "Property",
        "value": "Renault"
    },

    "color": {
        "type": "Property",
        "value": "white"
    },

    # required
    "batterySpecifications": {
        "type": "Property",
        "value": {
            "totalCapacity": 52.0,
            "batteryType": "lithium-ion",
            "nominalVoltage": 400
        }
    },

    # required
    "chargingCapabilities": {
        "type": "Property",
        "value": {
            "maxChargingPowerAC": 22.0,
            "maxChargingPowerDC": 130.0,
            "chargingPortTypes": [
                "Type2",
                "CCS2"
            ],
            "chargingStandards": [
                "AC-Level2",
                "DC-FastCharging"
            ]
        }
    },

    # required
    "refVehicleStatus": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:E-VehicleStatus:EV-001-status"
    },

    # required
    "vehicleType": {
        "type": "Property",
        "value": "car"
    },

    "dateCreated": {
        "type": "Property",
        "value": {
            "@type": "DateTime",
            "@value": datetime.now().isoformat() + "Z"
        }
    }
}

#charging satation status
CS_001_S = {
    "id": "urn:ngsi-ld:ChargingStationStatus:ParisSaclay30-1-S",
    "type": "ChargingStationStatus",
    "dateCreated": {
        "type": "Property",
        "value": {
            "@type": "DateTime",
            "@value": datetime.now(timezone.utc).isoformat()
        }
    },
    "refChargingStation": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:ChargingPoint:ParisSaclay30-1"
    },
    "operationalStatus": {
        "type": "Property",
        "value": "operational"
    },
    "totalPoints": {
        "type": "Property",
        "value": 1
    },

    "availablePoints": {
        "type": "Property",
        "value": 1
    },

    "occupiedPoints": {
        "type": "Property",
        "value": 0
    },
    "currentPowerConsumption": {
        "type": "Property",
        "value": 0,
        "units": "kW",
    }
}

CS_002_S = {
    "id": "urn:ngsi-ld:ChargingStationStatus:Building103-S",
    "type": "ChargingStationStatus",
    "dateCreated": {
        "type": "Property",
        "value": {
            "@type": "DateTime",
            "@value": datetime.now(timezone.utc).isoformat()
        }
    },
    "refChargingStation": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:ChargingPoint:ParisSaclay30-1"
    },
    "operationalStatus": {
        "type": "Property",
        "value": "operational"
    },
    "totalPoints": {
        "type": "Property",
        "value": 10
    },

    "availablePoints": {
        "type": "Property",
        "value": 10
    },

    "occupiedPoints": {
        "type": "Property",
        "value": 0
    },
    "currentPowerConsumption": {
        "type": "Property",
        "value": 0,
        "units": "kW",
    }
}

#charging poiont status
CP_001_S = {
    "id": "urn:ngsi-ld:ChargingPointStatus:ParisSaclay30-1-P-01-S",
    "type": "ChargingPointStatus",
    "dateCreated": {
        "type": "Property",
        "value": {
            "@type": "DateTime",
            "@value": datetime.now(timezone.utc).isoformat()
        }
    },
    "refChargingPoint": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:ChargingPoint:ParisSaclay30-1-P-01"
    },
    "pointStatus": {
        "type": "Property",
        "value": "available"
    },
    "currentPowerOutput": {
        "type": "Property",
        "value": 0,
        "units": "kW",
    }    
}

def B103_charging_point_status(point_number):
    formatted_number = str(point_number)
    
    charging_point_status = {
        "id": f"urn:ngsi-ld:ChargingPointStatus:Building103-P-{formatted_number}-S",
        "type": "ChargingPointStatus",
        "dateCreated": {
            "type": "Property",
            "value": {
                "@type": "DateTime",
                "@value": datetime.now().isoformat() + "Z"
            }
        },
        "refChargingPoint": {
            "type": "Relationship",
            "object": f"urn:ngsi-ld:ChargingPointStatus:Building103-P-{formatted_number}"
        },
        "pointStatus": {
        "type": "Property",
        "value": "available"
        },  
        "currentPowerOutput": {
            "type": "Property",
            "value": 0,
            "units": "kW",
        }
    }
    
    return charging_point_status

#charging session
def Drahi_X_charging_session(df_DX_Session):
    Drahi_X_charging_session_entities = []
    
    for index, row in df_DX_Session.iterrows():
        start_time = pd.to_datetime(row['startdate'])
        end_time = pd.to_datetime(row['enddate'])
        
        # Time Europe/Paris
        if start_time.tz is None:
            start_time = start_time.tz_localize(pytz.timezone("Europe/Paris"))
        if end_time.tz is None:
            end_time = end_time.tz_localize(pytz.timezone("Europe/Paris"))
        
        entity = {
            "id": f"urn:ngsi-ld:ChargingSession:session-{row['transaction_id']}",
            "type": "ChargingSession",
            
            "refChargingPoint": {
                "type": "Relationship",
                "object": "urn:ngsi-ld:ChargingPoint:ParisSaclay30-1-P-01"
            },
            
            "sessionId": {
                "type": "Property",
                "value": str(row['transaction_id'])
            },
            
            "sessionStatus": {
                "type": "Property",
                "value": "ended"
            },
            
            "sessionType": {
                "type": "Property",
                "value": "AC-Level2"
            },
            
            "sessionStartTime": {
                "type": "Property",
                "value": {
                    "@type": "DateTime",
                    "@value": start_time.isoformat()
                },
                "observedAt": start_time.isoformat()
            },
                      
            "sessionEndTime": {
                "type": "Property",
                "value": {
                    "@type": "DateTime",
                    "@value": end_time.isoformat()
                },
                "observedAt": end_time.isoformat()
            },
            
            "sessionDuration": {
                "type": "Property",
                "value": float(row['duration']) / 60,
                "units": "MIN",
                "observedAt": end_time.isoformat()
            },
            
            "energyConsumed": {
                "type": "Property",
                "value": float(row['total_volume']),
                "units": "kWh",
                "observedAt": end_time.isoformat()               
            },
            
            "userId": {
                "type": "Property",
                "value": str(row['authorize'])
            },
            
            "authenticationMethod": {
                "type": "Property",
                "value": str(row['auth_method'])
            },
            
            "authenticationId": {
                "type": "Property",
                "value": str(row['rfid'])
            },
            
            "dateCreated": {
                "type": "Property",
                "value": {
                    "@type": "DateTime",
                    "@value": start_time.isoformat()
                }
            },
            
            "lastUpdated": {
                "type": "Property",
                "value": {
                    "@type": "DateTime",
                    "@value": datetime.now().isoformat() + "Z"
                }
            }
        }
        
        Drahi_X_charging_session_entities.append(entity)
    
    return Drahi_X_charging_session_entities

def B103_charging_session(df_B103_Session):
    B103_charging_session_entities = []

    for index, row in df_B103_Session.iterrows():
        try:
            session_start_time = row['session start time']
            session_end_time = row['session end time']
            charging_start_time = row['charging start time']
            charging_end_time = row['charging end time']

            paris = pytz.timezone('Europe/Paris')
            session_start_time = session_start_time.tz_localize(paris) if session_start_time.tzinfo is None else session_start_time
            session_end_time = session_end_time.tz_localize(paris) if session_end_time.tzinfo is None else session_end_time
            charging_start_time = charging_start_time.tz_localize(paris) if charging_start_time.tzinfo is None else charging_start_time
            charging_end_time = charging_end_time.tz_localize(paris) if charging_end_time.tzinfo is None else charging_end_time

            entity = {
                "id": f"urn:ngsi-ld:ChargingSession:{row['uuid']}",
                "type": "ChargingSession",

                "refChargingPoint": {
                    "type": "Relationship",
                    "object": f"urn:ngsi-ld:ChargingPoint:Building103-P-{row['Evse Id']}"
                },

                "sessionId": {
                    "type": "Property",
                    "value": str(row['uuid'])
                },

                "sessionStatus": {
                    "type": "Property",
                    "value": row['compliance']
                },

                "sessionType": {
                    "type": "Property",
                    "value": row['plug type']
                },

                "sessionStartTime": {
                    "type": "Property",
                    "value": {
                        "@type": "DateTime",
                        "@value": session_start_time.isoformat()
                    },
                    "observedAt": session_start_time.isoformat()
                },

                "sessionEndTime": {
                    "type": "Property",
                    "value": {
                        "@type": "DateTime",
                        "@value": session_end_time.isoformat()
                    },
                    "observedAt": session_end_time.isoformat()
                },

                "sessionDuration": {
                    "type": "Property",
                    "value": float(row['session duration']),
                    "units": "MIN",
                    "observedAt": session_end_time.isoformat()
                },

                "chargingStartTime": {
                    "type": "Property",
                    "value": {
                        "@type": "DateTime",
                        "@value": charging_start_time.isoformat()
                    },
                    "observedAt": charging_start_time.isoformat()
                },

                "chargingEndTime": {
                    "type": "Property",
                    "value": {
                        "@type": "DateTime",
                        "@value": charging_end_time.isoformat()
                    },
                    "observedAt": charging_end_time.isoformat()
                },

                "chargingDuration": {
                    "type": "Property",
                    "value": float(row['charging duration']),
                    "units": "MIN",
                    "observedAt": charging_end_time.isoformat()
                },

                "energyConsumed": {
                    "type": "Property",
                    "value": float(row['consumption (kWh)']),
                    "units": "kWh",
                    "observedAt": charging_end_time.isoformat()
                },

                "userId": {
                    "type": "Property",
                    "value": str(row['idTag'])
                },

                "authenticationId": {
                    "type": "Property",
                    "value": str(row['Label RFID'])
                },

                "dateCreated": {
                    "type": "Property",
                    "value": {
                        "@type": "DateTime",
                        "@value": session_start_time.isoformat()
                    }
                },

                "maxChargingPower": {
                    "type": "Property",
                    "value": float(row['max power (kW)']),
                    "units": "kW"
                },
                
                "lastUpdated": {
                    "type": "Property",
                    "value": {
                        "@type": "DateTime",
                        "@value": datetime.now(paris).isoformat()
                    }
                }
            }

            B103_charging_session_entities.append(entity)
        
        except Exception as e:
            print(f"Error at index {index}: {e}")
            continue

    return B103_charging_session_entities

