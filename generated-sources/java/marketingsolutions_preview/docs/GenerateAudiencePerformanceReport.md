

# GenerateAudiencePerformanceReport

Request attributes for async audience performance report

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adSetIds** | **List&lt;String&gt;** | The list of adSets ids. If empty, all the adSets will be fetched. |  [optional] |
|**advertiserId** | **String** | The advertiser id |  |
|**audienceIds** | **List&lt;String&gt;** | The list of Audiences ids. If empty, all the Audiences will be fetched. |  [optional] |
|**currency** | **String** | The currency used for the report. ISO 4217 code (three-letter capitals). |  [optional] |
|**dimension** | [**DimensionEnum**](#DimensionEnum) | The dimension for the report. |  |
|**endDate** | **OffsetDateTime** | End date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. |  |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) | The list of metrics to report. |  |
|**segmentsIds** | **List&lt;String&gt;** | The list of Segments ids. If empty, all the segments will be fetched. |  [optional] |
|**startDate** | **OffsetDateTime** | Start date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. |  |
|**timezone** | **String** | Optional timezone used for the report. Timezone Database format (Tz). |  [optional] |



## Enum: DimensionEnum

| Name | Value |
|---- | -----|
| TOP30BRANDSBYDISPLAYS | &quot;Top30BrandsByDisplays&quot; |
| TOP30BRANDSBYCLICKS | &quot;Top30BrandsByClicks&quot; |
| TOP30BRANDSBYSALES | &quot;Top30BrandsBySales&quot; |
| TOP30INTERESTSBYDISPLAYS | &quot;Top30InterestsByDisplays&quot; |
| TOP30INTERESTSBYCLICKS | &quot;Top30InterestsByClicks&quot; |
| TOP30INTERESTSBYSALES | &quot;Top30InterestsBySales&quot; |



## Enum: List&lt;MetricsEnum&gt;

| Name | Value |
|---- | -----|
| CLICKS | &quot;Clicks&quot; |
| DISPLAYS | &quot;Displays&quot; |
| VISITS | &quot;Visits&quot; |
| SALES | &quot;Sales&quot; |
| REVENUE | &quot;Revenue&quot; |
| COSTPERVISIT | &quot;CostPerVisit&quot; |
| EXPOSEDUSERS | &quot;ExposedUsers&quot; |



