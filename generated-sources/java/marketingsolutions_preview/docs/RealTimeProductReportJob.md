

# RealTimeProductReportJob

Represents a request to create a real-time product export.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserIds** | **List&lt;String&gt;** | List of advertiser IDs to include in the export. Required. |  [optional] |
|**campaignIds** | **List&lt;String&gt;** | Optional list of campaign IDs to filter the export. |  [optional] |
|**currency** | **String** | Currency for the export. Default is _local currency_. |  [optional] |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) | List of dimensions to include in the export. Default: [\&quot;advertiserId\&quot;, \&quot;campaignId\&quot;, \&quot;sellerId\&quot;, \&quot;productId\&quot;, \&quot;day\&quot;]. |  [optional] |
|**endDate** | **OffsetDateTime** | End of the reporting interval, in ISO‑8601 date‑time format (UTC). Mutually exclusive with lookbackWindow.  If omitted while startDate is provided, defaults to the current time. |  [optional] |
|**fileFormat** | [**FileFormatEnum**](#FileFormatEnum) | The file format for the export. Allowed values: \&quot;csv\&quot;, \&quot;json\&quot;. Default is \&quot;csv\&quot;. |  [optional] |
|**lookbackWindow** | **Integer** | Lookback window in minutes. Default is 60. |  [optional] |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) | List of metrics to include in the export. Default: [\&quot;clicks\&quot;, \&quot;displays\&quot;, \&quot;cost\&quot;]. |  [optional] |
|**partnerIds** | **List&lt;String&gt;** | Optional list of partner IDs to filter the export. |  [optional] |
|**sellerIds** | **List&lt;String&gt;** | Optional list of seller IDs to filter the export. |  [optional] |
|**startDate** | **OffsetDateTime** | Start of the reporting interval, in ISO‑8601 date‑time format (UTC). Mutually exclusive with lookbackWindow. |  [optional] |
|**timezone** | **String** | Timezone for the export. Default is \&quot;UTC\&quot;. |  [optional] |



## Enum: List&lt;DimensionsEnum&gt;

| Name | Value |
|---- | -----|
| ADVERTISERID | &quot;AdvertiserId&quot; |
| PARTNERID | &quot;PartnerId&quot; |
| CAMPAIGNID | &quot;CampaignId&quot; |
| SELLERID | &quot;SellerId&quot; |
| PRODUCTID | &quot;ProductId&quot; |
| SELLERNAME | &quot;SellerName&quot; |
| YEAR | &quot;Year&quot; |
| MONTH | &quot;Month&quot; |
| WEEK | &quot;Week&quot; |
| DAY | &quot;Day&quot; |
| HOUR | &quot;Hour&quot; |
| MINUTE | &quot;Minute&quot; |



## Enum: FileFormatEnum

| Name | Value |
|---- | -----|
| CSV | &quot;Csv&quot; |
| JSON | &quot;Json&quot; |



## Enum: List&lt;MetricsEnum&gt;

| Name | Value |
|---- | -----|
| CLICKS | &quot;Clicks&quot; |
| DISPLAYS | &quot;Displays&quot; |
| COST | &quot;Cost&quot; |



