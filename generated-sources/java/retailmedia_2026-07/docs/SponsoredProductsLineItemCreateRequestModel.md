

# SponsoredProductsLineItemCreateRequestModel

Model to create a retail media auction line item

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bidStrategy** | [**BidStrategyEnum**](#BidStrategyEnum) | The bidding strategy for this line item.  Default value is manual. |  [optional] |
|**budget** | **Double** | The total budget allocated for this line item. |  [optional] |
|**dailyPacing** | **Double** | The daily pacing limit for budget spending. |  [optional] |
|**endDate** | **OffsetDateTime** | The date and time when the line item stops running. |  [optional] |
|**flightSchedule** | [**FlightSchedule**](FlightSchedule.md) |  |  [optional] |
|**isAutoDailyPacing** | **Boolean** | Indicates whether automatic daily pacing is enabled.  Default value is false. |  [optional] |
|**keywordStrategy** | [**KeywordStrategyEnum**](#KeywordStrategyEnum) | The keyword targeting strategy for this line item. |  [optional] |
|**maxBid** | **Double** | The maximum bid amount allowed for this line item. |  [optional] |
|**monthlyPacing** | **Double** | The monthly pacing limit for budget spending. |  [optional] |
|**name** | **String** | The name of the line item. |  |
|**optimizationStrategy** | [**OptimizationStrategyEnum**](#OptimizationStrategyEnum) | The optimization strategy to use for this line item.  Default value is Conversion. |  [optional] |
|**startDate** | **OffsetDateTime** | The date and time when the line item starts running. |  |
|**targetBid** | **Double** | The target bid amount for the line item. |  [optional] |
|**targetRetailerId** | **String** | The ID of the retailer to target for this line item. |  |



## Enum: BidStrategyEnum

| Name | Value |
|---- | -----|
| MANUAL | &quot;manual&quot; |
| AUTOMATED | &quot;automated&quot; |



## Enum: KeywordStrategyEnum

| Name | Value |
|---- | -----|
| CONQUESTING | &quot;conquesting&quot; |
| GENERICANDBRANDED | &quot;genericAndBranded&quot; |
| GENERICBRANDEDANDCONQUESTING | &quot;genericBrandedAndConquesting&quot; |



## Enum: OptimizationStrategyEnum

| Name | Value |
|---- | -----|
| CONVERSION | &quot;conversion&quot; |
| CLICKS | &quot;clicks&quot; |
| REVENUE | &quot;revenue&quot; |



