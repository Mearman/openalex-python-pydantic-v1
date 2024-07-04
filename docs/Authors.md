# Authors


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | [**List[GroupByResultInner]**](GroupByResultInner.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 
**results** | [**List[Author]**](Author.md) |  | [optional] 

## Example

```python
from openalex_api.models.authors import Authors

# TODO update the JSON string below
json = "{}"
# create an instance of Authors from a JSON string
authors_instance = Authors.from_json(json)
# print the JSON string representation of the object
print Authors.to_json()

# convert the object into a dict
authors_dict = authors_instance.to_dict()
# create an instance of Authors from a dict
authors_from_dict = Authors.from_dict(authors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


