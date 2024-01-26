# ErrorMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **object** |  | 
**message** | **object** |  | 

## Example

```python
from openalex_api.models.error_message import ErrorMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorMessage from a JSON string
error_message_instance = ErrorMessage.from_json(json)
# print the JSON string representation of the object
print ErrorMessage.to_json()

# convert the object into a dict
error_message_dict = error_message_instance.to_dict()
# create an instance of ErrorMessage from a dict
error_message_form_dict = error_message.from_dict(error_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


