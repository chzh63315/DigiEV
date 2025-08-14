
ORION_URL = "http://localhost:1026"

NGSI_LD_ENDPOINT = f"{ORION_URL}/ngsi-ld/v1/entities"
MINTAKA_URL = "http://localhost:8080"

headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/ld+json',
        'Link': '<https://raw.githubusercontent.com/chzh63315/DigiEV/refs/heads/main/contexts/datamodels.context-ngsi.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'
    }

QL_NOTIFY="http://localhost:8668/ngsi-ld/v1/notify"