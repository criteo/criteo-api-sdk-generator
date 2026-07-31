# # Ad

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_set_id** | **string** | The id of the Ad Set binded to this Ad | [optional]
**creative_id** | **string** | The id of the Creative binded to this Ad | [optional]
**description** | **string** | The description of the ad | [optional]
**end_date** | **string** | The date when when we will stop to show this ad. If the end date is not specified (i.e. null) then the ad will go on forever  String must be in ISO8601 format | [optional]
**id** | **string** | Unique identifier (duplicate of the parent id). | [optional]
**inventory_type** | **string** | The inventory the Ad belongs to. Possible values are \&quot;Display\&quot; and \&quot;Native\&quot;. This is optional since this doesn&#39;t make sense for every creative type but will throw an error if not set for a dynamic creative. | [optional]
**name** | **string** | The name of the ad | [optional]
**start_date** | **string** | The date when the ad will be launched  String must be in ISO8601 format | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
