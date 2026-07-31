

# GenerateTopProductsReportRequestAttributes

This is the message defining the query for TopProducts report

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adSetIds** | **List&lt;String&gt;** | Optional list of ad set IDs to filter on. The ad sets must already exist. If empty, all ad sets will be included. |  [optional] |
|**adSetStatus** | [**List&lt;AdSetStatusEnum&gt;**](#List&lt;AdSetStatusEnum&gt;) | Optional list of ad set statuses to filter on. If empty, all ad sets will be included. |  [optional] |
|**advertiserId** | **String** | The advertiser ID to report on. The advertiser must already exist. At least one advertiser ID should be provided |  |
|**brands** | **List&lt;String&gt;** | Optional list of brand names to filter on. If empty, all brands will be included. |  [optional] |
|**campaignIds** | **List&lt;String&gt;** | Optional list of campaign IDs to filter on. The campaigns must already exist. If empty, all campaigns will be included. |  [optional] |
|**categoryIds** | **List&lt;String&gt;** | Optional list of product catalog category IDs to filter on. If empty, all categories will be included. |  [optional] |
|**currency** | **String** | The currency used for the report. ISO 4217 code (three-letter capitals). |  |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) | Optional list of dimensions for the report. If not provided, defaults to [ProductId, Product, ProductUrl]. When an ID dimension is requested (e.g., CampaignId), the corresponding name dimension (e.g., Campaign) is automatically included, and vice versa. This applies to the following pairs: CampaignId/Campaign, AdSetId/AdSet, ProductId/Product, CategoryId/Category, AdvertiserId/Advertiser. |  [optional] |
|**endDate** | **OffsetDateTime** | End date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. |  |
|**limit** | **Integer** | Optional maximum number of top products returned. Must be between 1 and 200. |  [optional] |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) | Optional list of metrics to report. If not provided, defaults to the metric specified in rankProductsBy. |  [optional] |
|**rankProductsBy** | [**RankProductsByEnum**](#RankProductsByEnum) | Optional metric used to rank the top products. Allowed values: &#39;Clicks&#39;, &#39;Displays&#39;, &#39;Sales&#39;. |  |
|**startDate** | **OffsetDateTime** | Start date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. Must be ≤ endDate. |  |
|**timezone** | **String** | Optional timezone used for the report. Timezone Database format (Tz). |  [optional] |



## Enum: List&lt;AdSetStatusEnum&gt;

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| NOTRUNNING | &quot;NotRunning&quot; |
| DEAD | &quot;Dead&quot; |



## Enum: List&lt;DimensionsEnum&gt;

| Name | Value |
|---- | -----|
| CAMPAIGN | &quot;Campaign&quot; |
| CAMPAIGNID | &quot;CampaignId&quot; |
| ADSET | &quot;AdSet&quot; |
| ADSETID | &quot;AdSetId&quot; |
| PRODUCT | &quot;Product&quot; |
| PRODUCTID | &quot;ProductId&quot; |
| CATEGORY | &quot;Category&quot; |
| CATEGORYID | &quot;CategoryId&quot; |
| ADVERTISER | &quot;Advertiser&quot; |
| ADVERTISERID | &quot;AdvertiserId&quot; |
| PRODUCTURL | &quot;ProductUrl&quot; |
| BRAND | &quot;Brand&quot; |



## Enum: List&lt;MetricsEnum&gt;

| Name | Value |
|---- | -----|
| CLICKS | &quot;Clicks&quot; |
| CTR | &quot;Ctr&quot; |
| VISITS | &quot;Visits&quot; |
| SALES | &quot;Sales&quot; |
| COST | &quot;Cost&quot; |
| REVENUE | &quot;Revenue&quot; |
| DISPLAYS | &quot;Displays&quot; |



## Enum: RankProductsByEnum

| Name | Value |
|---- | -----|
| CLICKS | &quot;Clicks&quot; |
| DISPLAYS | &quot;Displays&quot; |
| SALES | &quot;Sales&quot; |



