

# AdWrite

Entity to create or update an ad

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adSetId** | **String** | The id of the Ad Set bound to this Ad |  |
|**creativeId** | **String** | The id of the Creative bound to this Ad |  |
|**description** | **String** | The description of the ad |  [optional] |
|**endDate** | **String** | The date when when we will stop to show this ad. If the end date is not specified (i.e. null) then the ad will go on forever  String must be in ISO8601 format |  [optional] |
|**inventoryType** | [**InventoryTypeEnum**](#InventoryTypeEnum) | The inventory the Ad to be created or updated belongs to. Possible values are \&quot;Display\&quot; and \&quot;Native\&quot;. This is optional since this doesn&#39;t make sense for every creative type but will throw an error if not set for a dynamic creative. |  [optional] |
|**name** | **String** | The name of the ad |  |
|**startDate** | **String** | The date when the ad will be launched  String must be in ISO8601 format |  |



## Enum: InventoryTypeEnum

| Name | Value |
|---- | -----|
| DISPLAY | &quot;Display&quot; |
| NATIVE | &quot;Native&quot; |



