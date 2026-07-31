

# AdLevelReportRequestAttributes

Query parameters for the Ad-Level Report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adsetIds** | **List&lt;String&gt;** | Optional filter on ad set IDs. Also satisfies the ad-set-scope requirement for the AdGroupName, ProductId, and AdId breakdown dimensions: if any of those are requested, either adsetIds must be non-empty or AdsetId must also be included in dimensions. |  [optional] |
|**advertiserIds** | **List&lt;String&gt;** | List of advertiser IDs to report on. Between 1 and 5 advertiser IDs can be provided. |  |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) | List of breakdown dimensions for the report. At least one dimension must be provided; nothing is added to the response unless explicitly requested here. |  |
|**endDate** | **OffsetDateTime** | End date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. |  |
|**format** | [**FormatEnum**](#FormatEnum) | Optional file format of the generated report. Only csv and json are currently supported by this endpoint — excel and xml requests are rejected with a 400 error. |  [optional] |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) | List of metrics to return. At least one metric must be provided. AdGroupContextHint and AdGroupDescription require AdGroupName in dimensions; ProductName requires ProductId; AdTitle and AdCopy require AdId. |  |
|**startDate** | **OffsetDateTime** | Start date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. Must be less than or equal to endDate. |  |
|**timezone** | **String** | Optional timezone used for the report. Timezone Database (Tz) format. |  [optional] |



## Enum: List&lt;DimensionsEnum&gt;

| Name | Value |
|---- | -----|
| ADVERTISERID | &quot;AdvertiserId&quot; |
| ADVERTISERNAME | &quot;AdvertiserName&quot; |
| ADSETID | &quot;AdsetId&quot; |
| ADSETNAME | &quot;AdsetName&quot; |
| MEDIACHANNEL | &quot;MediaChannel&quot; |
| PLATFORM | &quot;Platform&quot; |
| ADGROUPNAME | &quot;AdGroupName&quot; |
| PRODUCTID | &quot;ProductId&quot; |
| ADID | &quot;AdId&quot; |



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
| IMPRESSIONS | &quot;Impressions&quot; |
| CLICKS | &quot;Clicks&quot; |
| SPEND | &quot;Spend&quot; |
| CTR | &quot;Ctr&quot; |
| CPC | &quot;Cpc&quot; |
| CPM | &quot;Cpm&quot; |
| ADGROUPCONTEXTHINT | &quot;AdGroupContextHint&quot; |
| ADGROUPDESCRIPTION | &quot;AdGroupDescription&quot; |
| PRODUCTNAME | &quot;ProductName&quot; |
| ADTITLE | &quot;AdTitle&quot; |
| ADCOPY | &quot;AdCopy&quot; |



