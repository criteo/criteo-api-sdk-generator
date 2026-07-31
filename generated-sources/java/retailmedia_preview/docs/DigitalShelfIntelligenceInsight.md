

# DigitalShelfIntelligenceInsight

Description of a Digital Shelf Intelligence insight

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**aggregationLevel** | [**AggregationLevelEnum**](#AggregationLevelEnum) |  |  |
|**brandIds** | **List&lt;String&gt;** |  |  [optional] |
|**categories** | **List&lt;String&gt;** |  |  [optional] |
|**endDate** | **OffsetDateTime** |  |  |
|**format** | [**FormatEnum**](#FormatEnum) |  |  [optional] |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) |  |  |
|**retailerIds** | **List&lt;String&gt;** |  |  [optional] |
|**skuIds** | [**List&lt;SkuFilter&gt;**](SkuFilter.md) |  |  [optional] |
|**startDate** | **OffsetDateTime** |  |  |



## Enum: AggregationLevelEnum

| Name | Value |
|---- | -----|
| BRAND | &quot;brand&quot; |
| SKU | &quot;sku&quot; |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| JSON | &quot;json&quot; |
| JSON_COMPACT | &quot;json-compact&quot; |
| JSON_NEWLINE | &quot;json-newline&quot; |
| CSV | &quot;csv&quot; |



## Enum: List&lt;MetricsEnum&gt;

| Name | Value |
|---- | -----|
| CONSIDERATIONINDEX | &quot;considerationIndex&quot; |
| LISTINGPRICE | &quot;listingPrice&quot; |
| PDPVIEWRANK | &quot;pdpViewRank&quot; |
| SALESINDEX | &quot;salesIndex&quot; |
| SALESRANK | &quot;salesRank&quot; |
| TOTALPDPPAGEVIEWS | &quot;totalPdpPageViews&quot; |
| TOTALSALESONLINE | &quot;totalSalesOnline&quot; |
| TOTALSOLDUNITSONLINE | &quot;totalSoldUnitsOnline&quot; |



