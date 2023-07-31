# gooddata_api_client.model.json_api_analytical_dashboard_out_document.JsonApiAnalyticalDashboardOutDocument

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**data** | [**JsonApiAnalyticalDashboardOut**](JsonApiAnalyticalDashboardOut.md) | [**JsonApiAnalyticalDashboardOut**](JsonApiAnalyticalDashboardOut.md) |  | 
**[included](#included)** | list, tuple,  | tuple,  | Included resources | [optional] 
**links** | [**ObjectLinks**](ObjectLinks.md) | [**ObjectLinks**](ObjectLinks.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# included

Included resources

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Included resources | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**JsonApiAnalyticalDashboardOutIncludes**](JsonApiAnalyticalDashboardOutIncludes.md) | [**JsonApiAnalyticalDashboardOutIncludes**](JsonApiAnalyticalDashboardOutIncludes.md) | [**JsonApiAnalyticalDashboardOutIncludes**](JsonApiAnalyticalDashboardOutIncludes.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
