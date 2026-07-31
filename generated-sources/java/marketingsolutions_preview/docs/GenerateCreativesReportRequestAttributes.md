

# GenerateCreativesReportRequestAttributes

This is the message defining the query for Creatives report

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adFormats** | [**List&lt;AdFormatsEnum&gt;**](#List&lt;AdFormatsEnum&gt;) | Optional list of ad formats to filter on. If empty, all ad formats will be included. |  [optional] |
|**adIds** | **List&lt;String&gt;** | Optional list of ad IDs to filter on. If empty, all ads will be included. |  [optional] |
|**adNames** | **List&lt;String&gt;** | Optional list of ad names to filter on. If empty, all ads will be included. |  [optional] |
|**adSetIds** | **List&lt;String&gt;** | Optional list of ad set IDs to filter on. If empty, all ad sets will be included. |  [optional] |
|**adSetStatus** | [**List&lt;AdSetStatusEnum&gt;**](#List&lt;AdSetStatusEnum&gt;) | Optional list of ad set statuses to filter on. If empty, all ad sets will be included. |  [optional] |
|**advertiserIds** | **List&lt;String&gt;** | List of advertiser IDs to report on. The advertisers must already exist. At least one advertiser ID should be provided. |  |
|**campaignIds** | **List&lt;String&gt;** | Optional list of marketing campaign IDs to filter on. If empty, all campaigns will be included. |  [optional] |
|**couponIds** | **List&lt;String&gt;** | Optional list of coupon IDs to filter on. If empty, all coupons will be included. |  [optional] |
|**couponNames** | **List&lt;String&gt;** | Optional list of coupon names to filter on. If empty, all coupons will be included. |  [optional] |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) | List of dimensions for the report. At least one dimension should be provided. |  |
|**displaySizes** | **List&lt;String&gt;** | Optional list of display sizes to filter on. If empty, all display sizes will be included. &lt;br /&gt;&lt;br /&gt; Most common values: &#39;Native&#39;, &#39;Skyscraper&#39;, &#39;HalfPage&#39;, &#39;MediumBanner&#39;, &#39;LargeBanner&#39;, &#39;LeaderBoard&#39;, &#39;WideLeaderBoard&#39;, &#39;Other placements&#39;, &#39;Others&#39;. |  [optional] |
|**endDate** | **OffsetDateTime** | End date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. |  |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) | List of metrics for the report. At least one metric should be provided. |  |
|**startDate** | **OffsetDateTime** | Start date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. Must be ≤ endDate. |  |
|**timezone** | **String** | Optional timezone used for the report. Timezone Database format (Tz). |  [optional] |



## Enum: List&lt;AdFormatsEnum&gt;

| Name | Value |
|---- | -----|
| DYNAMIC | &quot;Dynamic&quot; |
| ADAPTIVE | &quot;Adaptive&quot; |
| RICHMEDIA | &quot;RichMedia&quot; |
| SHOWCASE | &quot;Showcase&quot; |
| VIDEO | &quot;Video&quot; |
| IMAGE | &quot;Image&quot; |
| HTML5 | &quot;HTML5&quot; |
| HTML_AD_TAGS | &quot;Html Ad Tags&quot; |
| VAST_VPAID_TAGS | &quot;VAST/VPAID Tags&quot; |
| OTHER_FORMATS | &quot;Other formats&quot; |



## Enum: List&lt;AdSetStatusEnum&gt;

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| NOTRUNNING | &quot;NotRunning&quot; |
| DEAD | &quot;Dead&quot; |



## Enum: List&lt;DimensionsEnum&gt;

| Name | Value |
|---- | -----|
| ADFORMAT | &quot;AdFormat&quot; |
| COUPON | &quot;Coupon&quot; |
| COUPONID | &quot;CouponId&quot; |
| DISPLAYSIZE | &quot;DisplaySize&quot; |
| SIZECATEGORY | &quot;SizeCategory&quot; |
| AD | &quot;Ad&quot; |
| ADID | &quot;AdId&quot; |
| DAY | &quot;Day&quot; |
| HOUR | &quot;Hour&quot; |



## Enum: List&lt;MetricsEnum&gt;

| Name | Value |
|---- | -----|
| CLICKS | &quot;Clicks&quot; |
| CTR | &quot;Ctr&quot; |
| DISPLAYS | &quot;Displays&quot; |



