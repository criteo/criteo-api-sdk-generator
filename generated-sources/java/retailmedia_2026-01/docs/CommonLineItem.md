

# CommonLineItem

A common line item to hold line item information shared between preferred and auction line items

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budget** | **Double** |  |  [optional] |
|**budgetRemaining** | **Double** |  |  [optional] |
|**budgetSpent** | **Double** |  |  [optional] |
|**campaignId** | **String** |  |  |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**endDate** | **LocalDate** | Represents the Date as a year, month, and day in the format YYYY-MM-DD |  [optional] |
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  |
|**startDate** | **LocalDate** | Represents the Date as a year, month, and day in the format YYYY-MM-DD |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**targetRetailerId** | **String** |  |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |



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



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| AUCTION | &quot;auction&quot; |
| PREFERRED | &quot;preferred&quot; |



