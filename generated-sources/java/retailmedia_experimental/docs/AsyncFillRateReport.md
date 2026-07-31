

# AsyncFillRateReport

Async FillRate report body request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adServerType** | [**AdServerTypeEnum**](#AdServerTypeEnum) | Filter on the type of the ad server: criteo, gam, all |  [optional] |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) | List of dimensions to report on |  |
|**endDate** | **OffsetDateTime** | End date |  |
|**format** | [**FormatEnum**](#FormatEnum) | Format of the output |  [optional] |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) | List of metrics to report on |  |
|**startDate** | **OffsetDateTime** | Start date |  |
|**supplyAccountIds** | **List&lt;String&gt;** | Supply account ids to report on |  |
|**timezone** | **String** | Time zone : see criteo developer portal for supported time zones |  [optional] |



## Enum: AdServerTypeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| GAM | &quot;gam&quot; |
| CRITEO | &quot;criteo&quot; |



## Enum: List&lt;DimensionsEnum&gt;

| Name | Value |
|---- | -----|
| DATE | &quot;date&quot; |
| RETAILERID | &quot;retailerId&quot; |
| RETAILERNAME | &quot;retailerName&quot; |
| PLACEMENTID | &quot;placementId&quot; |
| PLACEMENTNAME | &quot;placementName&quot; |
| PAGETYPENAME | &quot;pageTypeName&quot; |
| ENVIRONMENT | &quot;environment&quot; |
| SERVEDCATEGORY | &quot;servedCategory&quot; |
| RETAILERCATEGORYID | &quot;retailerCategoryId&quot; |
| RETAILERCATEGORYNAME | &quot;retailerCategoryName&quot; |
| ADSERVERTYPE | &quot;adServerType&quot; |



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
| PAGEVIEWS | &quot;pageViews&quot; |
| AVAILABLEPLACEMENTS | &quot;availablePlacements&quot; |
| UNFILLEDPLACEMENTS | &quot;unfilledPlacements&quot; |
| FILLRATE | &quot;fillRate&quot; |
| PLACEMENTIMPRESSIONS | &quot;placementImpressions&quot; |
| PRODUCTIMPRESSIONS | &quot;productImpressions&quot; |
| IMPRESSIONS | &quot;impressions&quot; |
| PLACEMENTCLICKS | &quot;placementClicks&quot; |
| PRODUCTCLICKS | &quot;productClicks&quot; |
| CLICKS | &quot;clicks&quot; |
| PLACEMENTIMPRESSIONSCTR | &quot;placementImpressionsCTR&quot; |
| PRODUCTIMPRESSIONSCTR | &quot;productImpressionsCTR&quot; |
| CPM | &quot;cpm&quot; |
| CPC | &quot;cpc&quot; |
| PLACEMENTIMPRESSIONSREVENUE | &quot;placementImpressionsRevenue&quot; |
| PRODUCTCLICKSREVENUE | &quot;productClicksRevenue&quot; |
| REVENUE | &quot;revenue&quot; |
| WORKINGMEDIA | &quot;workingMedia&quot; |
| NETREVENUE | &quot;netRevenue&quot; |
| NONDELIVERABLEPLACEMENTS | &quot;nonDeliverablePlacements&quot; |
| DELIVERABLEPLACEMENTS | &quot;deliverablePlacements&quot; |
| PLACEMENTSWITHCANDIDATES | &quot;placementsWithCandidates&quot; |
| COVEREDPLACEMENTS | &quot;coveredPlacements&quot; |
| COVERAGERATE | &quot;coverageRate&quot; |



