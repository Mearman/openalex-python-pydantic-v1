# WorkBiblio


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_page** | **str** |  | [optional] 
**issue** | **str** |  | [optional] 
**last_page** | **str** |  | [optional] 
**volume** | **str** |  | [optional] 

## Example

```python
from openalex_api.models.work_biblio import WorkBiblio

# TODO update the JSON string below
json = "{}"
# create an instance of WorkBiblio from a JSON string
work_biblio_instance = WorkBiblio.from_json(json)
# print the JSON string representation of the object
print WorkBiblio.to_json()

# convert the object into a dict
work_biblio_dict = work_biblio_instance.to_dict()
# create an instance of WorkBiblio from a dict
work_biblio_from_dict = WorkBiblio.from_dict(work_biblio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


