
import requests
from src.config import ORION_URL, NGSI_LD_ENDPOINT, headers

# Check Orion Context Broker version
def test_connection():
    """Check if Orion Context Broker is accessible"""
    try:
        # Send GET request to version endpoint
        response = requests.get(f"{ORION_URL}/version")
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            version_info = response.json()
            print(f"Orion Version: {version_info.get('orion version', 'Unknown')}")
            print(f"Orion-LD Version: {version_info.get('orionld version', 'Unknown')}")
        else:
            print("Failed to connect to Orion")
            
    except Exception as e:
        print(f"Connection error: {e}")


# def function for entity query test

def get_entity_types():
    """Get all available entity types"""
    try:
        response = requests.get(f"{ORION_URL}/ngsi-ld/v1/types", headers=headers)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            types_data = response.json()
                         
            return types_data
        else:
            print(f"Failed: {response.text}")
            return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def get_all_entities():
    """Get all entities from Orion Context Broker"""
    try:
        # Add local=true to avoid "too broad query" error
        params = {
            "limit": 1000,
            "local": "true"
        }
        
        response = requests.get(f"{ORION_URL}/ngsi-ld/v1/entities", 
                              headers=headers, 
                              params=params)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            entities = response.json()
            print(f"Retrieved {len(entities)} entities")
            
            # Display basic info about each entity
            for i, entity in enumerate(entities):
                print(f"\nEntity {i+1}:")
                print(f"  ID: {entity.get('id')}")
                
                # Handle type field in NGSI-LD format
                entity_type = entity.get('type')
                if isinstance(entity_type, list):
                    entity_type = entity_type[0] if entity_type else 'Unknown'
                print(f"  Type: {entity_type}")
                
                # Count attributes (exclude @context, id, type)
                excluded_keys = ['@context', 'id', 'type']
                attr_count = len([k for k in entity.keys() if k not in excluded_keys])
                print(f"  Attributes: {attr_count}")
                
                # Show @context if present
                if '@context' in entity:
                    print(f"  Context: {entity.get('@context')}")
            
            return entities
        else:
            print("Failed to get entities")
            print(f"Response: {response.text}")
            return []
            
    except Exception as e:
        print(f"Error: {e}")
        return []
    
def query_entity_by_id(entity_id):
    """Query entity by exact ID"""
    try:
        response = requests.get(f"{ORION_URL}/ngsi-ld/v1/entities/{entity_id}", 
                              headers=headers)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            entity = response.json()          
            return entity
        else:
            print(f"Entity not found: {response.text}")
            return None
            
    except Exception as e:
        print(f"Error: {e}")
        return None

def query_entities_by_type(entity_type):
    """Query entities by type"""
    try:
        params = {
            "type": entity_type,
            "limit": 10     # limit 10 outputs
        }
        
        response = requests.get(f"{ORION_URL}/ngsi-ld/v1/entities", 
                              headers=headers, 
                              params=params)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            entities = response.json()
            print(f"Found {len(entities)} entities of type '{entity_type}'")
            
            for i, entity in enumerate(entities):
                print(f"\nEntity {i+1}:")
                print(f"  ID: {entity.get('id')}")
                print(f"  Type: {entity.get('type')}")
            
            return entities
        else:
            print(f"Query failed: {response.text}")
            return []
            
    except Exception as e:
        print(f"Error: {e}")
        return []

def query_entities_by_attribute(attribute_name, attribute_value):
    """Query entities by attribute value"""
    try:
        params = {
            "q": f'{attribute_name}=="{attribute_value}"',
            "limit": 10
        }
        
        response = requests.get(f"{ORION_URL}/ngsi-ld/v1/entities", 
                              headers=headers, 
                              params=params)
        print(f"Status Code: {response.status_code}")
        print(f"Query: {params['q']}")
        
        if response.status_code == 200:
            entities = response.json()
            print(f"Found {len(entities)} entities with {attribute_name}={attribute_value}")
            
            for i, entity in enumerate(entities):
                print(f"\nEntity {i+1}:")
                print(f"  ID: {entity.get('id')}")
                print(f"  Type: {entity.get('type')}")
                if attribute_name in entity:
                    attr_value = entity[attribute_name]
                    if isinstance(attr_value, dict) and 'value' in attr_value:
                        print(f"  {attribute_name}: {attr_value['value']}")
                    else:
                        print(f"  {attribute_name}: {attr_value}")
            
            return entities
        else:
            print(f"Query failed: {response.text}")
            return []
            
    except Exception as e:
        print(f"Error: {e}")
        return []

