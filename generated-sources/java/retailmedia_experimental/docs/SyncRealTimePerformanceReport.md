

# SyncRealTimePerformanceReport

Real Time Performance report body request (one sheeter: startDate, endDate (optional), RetailerIds, accountIds, campaignIds, lineItemIds, dimensions, metrics, timezones).  Extends SyncReport only (no default filters); adds entry filter arrays.  Dimensions and metrics are restricted to their supported enumerated values; invalid values cause deserialization to fail.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountIds** | **List&lt;String&gt;** | Account ids to filter (plural; base has AccountId for single account). |  [optional] |
|**campaignIds** | **List&lt;String&gt;** | Campaign ids to filter. |  [optional] |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) | List of dimensions to report on (real-time: at least one required). Only the supported dimension values are valid. |  [optional] |
|**endDate** | **OffsetDateTime** | Optional end date/time (inclusive in the request timezone). If empty or not provided, no end date filter is applied.  When provided, used as the inclusive upper bound for the report range.  Hides base Report.EndDate so this report can treat end date as optional (no [Required]). |  [optional] |
|**lineItemIds** | **List&lt;String&gt;** | Line item ids to filter. |  [optional] |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) | List of metrics to report on (real-time: at least one required). Only the supported metric values are valid. |  [optional] |
|**retailerIds** | **List&lt;String&gt;** | Retailer ids to filter. This is not used for security, so no need to check for &gt; 0 elements |  [optional] |
|**startDate** | **OffsetDateTime** | Start date (real-time: must be within the last 7 days). |  |
|**timezone** | **String** | Time zone : see criteo developer portal for supported time zones |  [optional] |



## Enum: List&lt;DimensionsEnum&gt;

| Name | Value |
|---- | -----|
| DATE | &quot;date&quot; |
| HOUR | &quot;hour&quot; |
| ACCOUNTID | &quot;accountId&quot; |
| ACCOUNTNAME | &quot;accountName&quot; |
| CAMPAIGNID | &quot;campaignId&quot; |
| CAMPAIGNNAME | &quot;campaignName&quot; |
| LINEITEMID | &quot;lineItemId&quot; |
| LINEITEMNAME | &quot;lineItemName&quot; |
| RETAILERID | &quot;retailerId&quot; |
| RETAILERNAME | &quot;retailerName&quot; |



## Enum: List&lt;MetricsEnum&gt;

| Name | Value |
|---- | -----|
| IMPRESSIONS | &quot;impressions&quot; |
| CLICKS | &quot;clicks&quot; |
| SPEND | &quot;spend&quot; |



