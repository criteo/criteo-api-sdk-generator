

# PlacementsReportQueryMessage

This is the message defining the query for Placements report

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adsetIds** | **String** | Optional list of ad set IDs to filter on. The ad sets must already exist. If empty, all ad sets will be included. |  [optional] |
|**advertiserIds** | **String** | List of advertiser IDs to report on, provided as a single comma-separated string (e.g., \&quot;123,456,789\&quot;). The advertisers must already exist. If empty, all advertisers will be used. |  |
|**campaignIds** | **String** | Optional list of campaign IDs to filter on. The campaigns must already exist. If empty, all campaigns will be included. |  [optional] |
|**currency** | **String** | The currency used for the report. ISO 4217 code (three-letter capitals). |  |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) | List of dimensions for the report. At least one dimension should be provided. |  |
|**disclosed** | **Boolean** | Optionally returns disclosed or undisclosed placements. |  [optional] |
|**endDate** | **OffsetDateTime** | End date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. |  |
|**environment** | [**EnvironmentEnum**](#EnvironmentEnum) | Optional type of environment to filter on. If empty, all environments will be included. |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | Optional file format of the generated report. |  [optional] |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) | List of metrics for the report. At least one dimension should be provided. |  |
|**placement** | **String** | Optional filter on a specific placement domain name. If empty, all placements will be included. |  [optional] |
|**startDate** | **OffsetDateTime** | Start date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. Must be ≤ endDate. |  |
|**timezone** | **String** | Optional timezone used for the report. Timezone Database format (Tz). |  [optional] |



## Enum: List&lt;DimensionsEnum&gt;

| Name | Value |
|---- | -----|
| ADSETID | &quot;AdsetId&quot; |
| ADVERTISERID | &quot;AdvertiserId&quot; |
| PLACEMENT | &quot;Placement&quot; |
| ENVIRONMENT | &quot;Environment&quot; |
| ADSETNAME | &quot;AdsetName&quot; |
| ADVERTISERNAME | &quot;AdvertiserName&quot; |
| CAMPAIGNID | &quot;CampaignId&quot; |
| CAMPAIGNNAME | &quot;CampaignName&quot; |
| ADCHANNEL | &quot;AdChannel&quot; |
| SOCIALPLATFORM | &quot;SocialPlatform&quot; |
| CATEGORYID | &quot;CategoryId&quot; |
| CATEGORYNAME | &quot;CategoryName&quot; |



## Enum: EnvironmentEnum

| Name | Value |
|---- | -----|
| WEB | &quot;Web&quot; |
| ANDROID | &quot;Android&quot; |
| IOS | &quot;Ios&quot; |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| CSV | &quot;csv&quot; |
| EXCEL | &quot;excel&quot; |
| XML | &quot;xml&quot; |
| JSON | &quot;json&quot; |



## Enum: List&lt;MetricsEnum&gt;

| Name | Value |
|---- | -----|
| CLICKS | &quot;Clicks&quot; |
| DISPLAYS | &quot;Displays&quot; |
| COST | &quot;Cost&quot; |
| SALESPC30D | &quot;SalesPc30d&quot; |
| REVENUEPC30D | &quot;RevenuePc30d&quot; |
| COSPC30D | &quot;CosPc30d&quot; |
| ROASPC30D | &quot;RoasPc30d&quot; |
| CPOPC30D | &quot;CpoPc30d&quot; |
| CVRPC30D | &quot;CvrPc30d&quot; |
| SALESPV1D | &quot;SalesPv1d&quot; |
| REVENUEPV1D | &quot;RevenuePv1d&quot; |
| COSPV1D | &quot;CosPv1d&quot; |
| ROASPV1D | &quot;RoasPv1d&quot; |
| CPOPV1D | &quot;CpoPv1d&quot; |
| CVRPV1D | &quot;CvrPv1d&quot; |



