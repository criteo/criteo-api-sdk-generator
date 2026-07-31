

# GenerateRealtimeStatisticsReportRequestAttributes

This is the message defining the query for Realtime report

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adsetIds** | **List&lt;String&gt;** | Optional list of ad set IDs to filter on. The ad sets must already exist. If empty, all ad sets will be included. |  [optional] |
|**advertiserIds** | **List&lt;String&gt;** | List of advertiser IDs to report on. The advertisers must already exist. Between 1 and 10 advertiser IDs can be provided. |  |
|**campaignIds** | **List&lt;String&gt;** | Optional list of campaign IDs to filter on. The campaigns must already exist. If empty, all campaigns will be included. |  [optional] |
|**currency** | **String** | The currency used for the report. ISO 4217 code (three-letter capitals). |  [optional] |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) | List of dimensions for the report. If not included, the default list of dimensions will be used. |  [optional] |
|**lookbackWindow** | **Integer** | Optional number of hours to consider in the past. |  [optional] |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) | List of metrics for the report. If included, at least one metric should be provided. |  [optional] |
|**timezone** | **String** | Optional timezone used for the report. |  [optional] |



## Enum: List&lt;DimensionsEnum&gt;

| Name | Value |
|---- | -----|
| ADVERTISER | &quot;Advertiser&quot; |
| ADVERTISERID | &quot;AdvertiserId&quot; |
| CAMPAIGN | &quot;Campaign&quot; |
| CAMPAIGNID | &quot;CampaignId&quot; |
| ADSET | &quot;Adset&quot; |
| ADSETID | &quot;AdsetId&quot; |
| YEAR | &quot;Year&quot; |
| MONTH | &quot;Month&quot; |
| WEEK | &quot;Week&quot; |
| DAY | &quot;Day&quot; |
| HOUR | &quot;Hour&quot; |



## Enum: List&lt;MetricsEnum&gt;

| Name | Value |
|---- | -----|
| CLICKS | &quot;Clicks&quot; |
| COST | &quot;Cost&quot; |
| DISPLAYS | &quot;Displays&quot; |



