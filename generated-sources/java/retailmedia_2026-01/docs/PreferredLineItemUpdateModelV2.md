

# PreferredLineItemUpdateModelV2

Model used to update a preferred line item

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budget** | **Double** |  |  [optional] |
|**capping** | [**LineItemCappingV2**](LineItemCappingV2.md) |  |  [optional] |
|**creativeId** | **String** |  |  [optional] |
|**endDate** | **LocalDate** | Represents the Date as a year, month, and day in the format YYYY-MM-DD |  |
|**name** | **String** |  |  |
|**pacing** | [**PacingEnum**](#PacingEnum) |  |  [optional] |
|**page** | [**LineItemPageV2**](LineItemPageV2.md) |  |  [optional] |
|**startDate** | **LocalDate** | Represents the Date as a year, month, and day in the format YYYY-MM-DD |  |
|**status** | [**StatusEnum**](#StatusEnum) | Line Item Status Enum |  |



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



