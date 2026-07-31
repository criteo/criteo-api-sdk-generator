

# GenerateAllProductsReportRequestAttributes

This is the message defining the query for AllProducts report (async export)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adSetIds** | **List&lt;String&gt;** | The list of ad set ids. |  [optional] |
|**advertiserIds** | **List&lt;String&gt;** | The list of advertiser account IDs. |  |
|**campaignIds** | **List&lt;String&gt;** | The list of campaign ids. |  [optional] |
|**currency** | **String** | The currency used for the report. ISO 4217 code (three-letter capitals). |  [optional] |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) | The dimensions for the report. |  [optional] |
|**endDate** | **OffsetDateTime** | End date of the report. ISO 8601 date-time (UTC). Defaults to Now if not provided. |  [optional] |
|**fileFormat** | **String** | The output file format. Supported: csv, json. |  [optional] |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) | The list of metrics to report. |  [optional] |
|**sellerIds** | **List&lt;String&gt;** | The list of seller ids. |  [optional] |
|**startDate** | **OffsetDateTime** | Start date of the report. ISO 8601 date-time (UTC). |  |
|**timezone** | **String** | The timezone used for the report. Timezone Database format (Tz). |  [optional] |



## Enum: List&lt;DimensionsEnum&gt;

| Name | Value |
|---- | -----|
| ADVERTISERID | &quot;AdvertiserId&quot; |
| PARTNERID | &quot;PartnerId&quot; |
| CAMPAIGNID | &quot;CampaignId&quot; |
| ADSETID | &quot;AdSetId&quot; |
| PRODUCTID | &quot;ProductId&quot; |
| SELLERID | &quot;SellerId&quot; |



## Enum: List&lt;MetricsEnum&gt;

| Name | Value |
|---- | -----|
| CLICKS | &quot;Clicks&quot; |
| DISPLAYS | &quot;Displays&quot; |
| CTR | &quot;Ctr&quot; |
| VISITS | &quot;Visits&quot; |
| SALES | &quot;Sales&quot; |
| COST | &quot;Cost&quot; |
| REVENUE | &quot;Revenue&quot; |



