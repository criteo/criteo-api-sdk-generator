

# PreferredLineItemCreateModelV2

Model used to create a preferred line item

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budget** | **Double** |  |  |
|**capping** | [**LineItemCappingV2**](LineItemCappingV2.md) |  |  [optional] |
|**creativeId** | **String** |  |  [optional] |
|**endDate** | **LocalDate** | Represents the Date as a year, month, and day in the format YYYY-MM-DD |  |
|**name** | **String** |  |  |
|**pacing** | [**PacingEnum**](#PacingEnum) | Line Item Pacing Enum |  |
|**page** | [**LineItemPageV2**](LineItemPageV2.md) |  |  |
|**startDate** | **LocalDate** | Represents the Date as a year, month, and day in the format YYYY-MM-DD |  |
|**status** | [**StatusEnum**](#StatusEnum) | Line Item Status Enum |  [optional] |
|**targetRetailerId** | **String** |  |  |



## Enum: PacingEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| STANDARD | &quot;standard&quot; |
| ACCELERATED | &quot;accelerated&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| ACTIVE | &quot;active&quot; |
| SCHEDULED | &quot;scheduled&quot; |
| DRAFT | &quot;draft&quot; |
| PAUSED | &quot;paused&quot; |
| BUDGETHIT | &quot;budgetHit&quot; |
| ENDED | &quot;ended&quot; |
| ARCHIVED | &quot;archived&quot; |
| NOFUNDS | &quot;noFunds&quot; |



