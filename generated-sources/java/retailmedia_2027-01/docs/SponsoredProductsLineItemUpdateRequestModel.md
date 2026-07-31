

# SponsoredProductsLineItemUpdateRequestModel

A request to update a Sponsored Products Line Item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bidStrategy** | [**BidStrategyEnum**](#BidStrategyEnum) | The bid strategy for the line item. |  [optional] |
|**budget** | **Double** | The total budget allocated for this line item. |  [optional] |
|**dailyPacing** | **Double** | The daily pacing amount for the line item. |  [optional] |
|**endDate** | **OffsetDateTime** | The date and time when the line item stops running. |  [optional] |
|**flightSchedule** | [**FlightSchedule**](FlightSchedule.md) |  |  [optional] |
|**isAutoDailyPacing** | **Boolean** | True if daily pacing is automatic, false if manual. |  |
|**maxBid** | **Double** | The maximum bid amount for the line item. |  [optional] |
|**monthlyPacing** | **Double** | The monthly pacing amount for the line item. |  [optional] |
|**name** | **String** | The name of this line item. |  |
|**optimizationStrategy** | [**OptimizationStrategyEnum**](#OptimizationStrategyEnum) | The optimization strategy for the line item. |  [optional] |
|**startDate** | **OffsetDateTime** | The date and time when the line item starts running. |  |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the line item. |  |
|**targetBid** | **Double** | The target bid amount for the line item. |  [optional] |



## Enum: BidStrategyEnum

| Name | Value |
|---- | -----|
| MANUAL | &quot;manual&quot; |
| AUTOMATED | &quot;automated&quot; |



## Enum: OptimizationStrategyEnum

| Name | Value |
|---- | -----|
| CONVERSION | &quot;conversion&quot; |
| CLICKS | &quot;clicks&quot; |
| REVENUE | &quot;revenue&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |
| DRAFT | &quot;draft&quot; |



