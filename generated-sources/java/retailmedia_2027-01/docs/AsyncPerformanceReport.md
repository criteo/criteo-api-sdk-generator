

# AsyncPerformanceReport

Create payload attributes for a performance DSP analytics async report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clickAttributionWindow** | [**ClickAttributionWindowEnum**](#ClickAttributionWindowEnum) |  |  [optional] |
|**clickMatchLevel** | [**ClickMatchLevelEnum**](#ClickMatchLevelEnum) |  |  [optional] |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) |  |  |
|**endDate** | **OffsetDateTime** |  |  |
|**filters** | [**PerformanceReportFilters**](PerformanceReportFilters.md) |  |  |
|**format** | [**FormatEnum**](#FormatEnum) |  |  [optional] |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) |  |  |
|**startDate** | **OffsetDateTime** |  |  |
|**timezone** | **String** |  |  [optional] |
|**viewAttributionWindow** | [**ViewAttributionWindowEnum**](#ViewAttributionWindowEnum) |  |  [optional] |
|**viewMatchLevel** | [**ViewMatchLevelEnum**](#ViewMatchLevelEnum) |  |  [optional] |



## Enum: ClickAttributionWindowEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| _7D | &quot;7D&quot; |
| _14D | &quot;14D&quot; |
| _30D | &quot;30D&quot; |



## Enum: ClickMatchLevelEnum

| Name | Value |
|---- | -----|
| SAMESKU | &quot;sameSku&quot; |
| SAMECATEGORY | &quot;sameCategory&quot; |
| SAMEBRAND | &quot;sameBrand&quot; |
| CAMPAIGN | &quot;campaign&quot; |



## Enum: List&lt;DimensionsEnum&gt;

| Name | Value |
|---- | -----|
| DATE | &quot;date&quot; |
| HOUR | &quot;hour&quot; |
| ACCOUNTID | &quot;accountId&quot; |
| ACCOUNTNAME | &quot;accountName&quot; |
| CAMPAIGNID | &quot;campaignId&quot; |
| CAMPAIGNNAME | &quot;campaignName&quot; |
| CAMPAIGNTYPE | &quot;campaignType&quot; |
| LINEITEMID | &quot;lineItemId&quot; |
| LINEITEMNAME | &quot;lineItemName&quot; |
| RETAILERID | &quot;retailerId&quot; |
| RETAILERNAME | &quot;retailerName&quot; |
| BRANDID | &quot;brandId&quot; |
| BRANDNAME | &quot;brandName&quot; |
| PRODUCTCATEGORY | &quot;productCategory&quot; |
| PRODUCTID | &quot;productId&quot; |
| PRODUCTNAME | &quot;productName&quot; |
| SALESCHANNEL | &quot;salesChannel&quot; |
| MEDIATYPE | &quot;mediaType&quot; |
| BUYTYPE | &quot;buyType&quot; |
| BUDGETMODEL | &quot;budgetModel&quot; |
| ACTIVATIONPLATFORM | &quot;activationPlatform&quot; |
| ENVIRONMENT | &quot;environment&quot; |
| PAGETYPE | &quot;pageType&quot; |
| PAGECATEGORY | &quot;pageCategory&quot; |
| SERVEDCATEGORY | &quot;servedCategory&quot; |
| KEYWORD | &quot;keyword&quot; |
| SEARCHTERM | &quot;searchTerm&quot; |
| SEARCHTERMTYPE | &quot;searchTermType&quot; |
| SEARCHTERMTARGETING | &quot;searchTermTargeting&quot; |
| CREATIVEID | &quot;creativeId&quot; |
| CREATIVENAME | &quot;creativeName&quot; |
| CREATIVETYPE | &quot;creativeType&quot; |
| CREATIVETEMPLATEID | &quot;creativeTemplateId&quot; |
| CREATIVETEMPLATENAME | &quot;creativeTemplateName&quot; |
| TARGETEDKEYWORDTYPE | &quot;targetedKeywordType&quot; |



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
| IMPRESSIONS | &quot;impressions&quot; |
| CLICKS | &quot;clicks&quot; |
| SPEND | &quot;spend&quot; |
| ATTRIBUTEDSALES | &quot;attributedSales&quot; |
| ATTRIBUTEDUNITS | &quot;attributedUnits&quot; |
| ATTRIBUTEDORDERS | &quot;attributedOrders&quot; |
| ASSISTEDSALES | &quot;assistedSales&quot; |
| ASSISTEDUNITS | &quot;assistedUnits&quot; |
| CTR | &quot;ctr&quot; |
| CPC | &quot;cpc&quot; |
| CPO | &quot;cpo&quot; |
| CPM | &quot;cpm&quot; |
| ROAS | &quot;roas&quot; |
| VIDEOVIEWS | &quot;videoViews&quot; |
| VIDEOSSTARTED | &quot;videosStarted&quot; |
| VIDEOSPLAYEDTO25 | &quot;videosPlayedTo25&quot; |
| VIDEOSPLAYEDTO50 | &quot;videosPlayedTo50&quot; |
| VIDEOSPLAYEDTO75 | &quot;videosPlayedTo75&quot; |
| VIDEOSPLAYEDTO100 | &quot;videosPlayedTo100&quot; |
| VIDEOPLAYINGRATE | &quot;videoPlayingRate&quot; |
| VIDEOCOMPLETIONRATE | &quot;videoCompletionRate&quot; |
| VIDEOIMPRESSIONS | &quot;videoImpressions&quot; |
| VIDEOMUTED | &quot;videoMuted&quot; |
| VIDEOUNMUTED | &quot;videoUnmuted&quot; |
| VIDEOPAUSED | &quot;videoPaused&quot; |
| VIDEORESUMED | &quot;videoResumed&quot; |
| VIDEOAVGINTERACTIONRATE | &quot;videoAvgInteractionRate&quot; |
| VIDEOVIEWABILITY | &quot;videoViewability&quot; |
| VIDEOSTARTINGRATE | &quot;videoStartingRate&quot; |
| VIDEOCPC | &quot;videoCPC&quot; |
| VIDEOCPCV | &quot;videoCPCV&quot; |
| NEWTOBRANDATTRIBUTEDSALES | &quot;newToBrandAttributedSales&quot; |
| NEWTOBRANDATTRIBUTEDSALESRATE | &quot;newToBrandAttributedSalesRate&quot; |
| NEWTOBRANDATTRIBUTEDUNITS | &quot;newToBrandAttributedUnits&quot; |
| NEWTOBRANDATTRIBUTEDUNITSRATE | &quot;newToBrandAttributedUnitsRate&quot; |
| UNIQUEVISITORS | &quot;uniqueVisitors&quot; |
| FREQUENCY | &quot;frequency&quot; |
| WINRATE | &quot;winRate&quot; |
| SAMPLEDBIDSWON | &quot;sampledBidsWon&quot; |
| SAMPLEDBIDSPARTICIPATED | &quot;sampledBidsParticipated&quot; |



## Enum: ViewAttributionWindowEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| _1D | &quot;1D&quot; |
| _7D | &quot;7D&quot; |
| _14D | &quot;14D&quot; |
| _30D | &quot;30D&quot; |



## Enum: ViewMatchLevelEnum

| Name | Value |
|---- | -----|
| SAMESKU | &quot;sameSku&quot; |
| SAMECATEGORY | &quot;sameCategory&quot; |
| SAMEBRAND | &quot;sameBrand&quot; |
| CAMPAIGN | &quot;campaign&quot; |



