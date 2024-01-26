# Location


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_accepted** | **object** |  | [optional] 
**is_oa** | **object** |  | [optional] 
**is_published** | **object** |  | [optional] 
**landing_page_url** | **object** |  | [optional] 
**license** | **object** |  | [optional] 
**pdf_url** | **object** |  | [optional] 
**source** | [**LocationSource**](LocationSource.md) |  | [optional] 
**version** | **object** |  | [optional] 

## Example

```python
from openalex_api_pydantic_v1.models.location import Location

# TODO update the JSON string below
json = "{}"
# create an instance of Location from a JSON string
location_instance = Location.from_json(json)
# print the JSON string representation of the object
print Location.to_json()

# convert the object into a dict
location_dict = location_instance.to_dict()
# create an instance of Location from a dict
location_form_dict = location.from_dict(location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


