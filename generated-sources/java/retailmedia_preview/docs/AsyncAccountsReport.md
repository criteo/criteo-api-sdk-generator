

# AsyncAccountsReport

Async Accounts report body request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountIds** | **List&lt;String&gt;** | Account Ids to report on |  |
|**activationPlatforms** | [**List&lt;ActivationPlatformsEnum&gt;**](#List&lt;ActivationPlatformsEnum&gt;) | Filter on the activation platform: CommerceMax, PrivateMarket |  [optional] |
|**aggregationLevel** | [**AggregationLevelEnum**](#AggregationLevelEnum) | Level of aggregation, if no dimensions and metrics are provided, falls back to campaign aggregationLevel |  [optional] |
|**budgetModels** | [**List&lt;BudgetModelsEnum&gt;**](#List&lt;BudgetModelsEnum&gt;) | Filter on the budget model: CriteoBudget, RetailerBudget |  [optional] |
|**buyTypes** | [**List&lt;BuyTypesEnum&gt;**](#List&lt;BuyTypesEnum&gt;) | Filter on the buy type: auction, preferredDeals, sponsorship |  [optional] |
|**campaignType** | [**CampaignTypeEnum**](#CampaignTypeEnum) | Filter the type of campaigns to report on: sponsoredProducts or onSiteDisplays |  [optional] |
|**clickAttributionWindow** | [**ClickAttributionWindowEnum**](#ClickAttributionWindowEnum) | Click attribution window |  [optional] |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) | List of dimensions to report on |  [optional] |
|**endDate** | **OffsetDateTime** | End date |  |
|**format** | [**FormatEnum**](#FormatEnum) | Format of the output |  [optional] |
|**mediaType** | [**MediaTypeEnum**](#MediaTypeEnum) | Filter on the type of media: unknown, display, video |  [optional] |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) | List of metrics to report on |  [optional] |
|**reportType** | [**ReportTypeEnum**](#ReportTypeEnum) | Type of report, if no dimensions and metrics are provided, falls back to summary reportType |  [optional] |
|**salesChannel** | [**SalesChannelEnum**](#SalesChannelEnum) | Filter on specific sales channel: offline or online |  [optional] |
|**searchTermTargetings** | [**List&lt;SearchTermTargetingsEnum&gt;**](#List&lt;SearchTermTargetingsEnum&gt;) | Filter on the type of search term targeting: unknown, automatic, manual |  [optional] |
|**searchTermTypes** | [**List&lt;SearchTermTypesEnum&gt;**](#List&lt;SearchTermTypesEnum&gt;) | Filter on the type of search term type: unknown, searched, entered |  [optional] |
|**startDate** | **OffsetDateTime** | Start date |  |
|**targetedKeywordTypes** | [**List&lt;TargetedKeywordTypesEnum&gt;**](#List&lt;TargetedKeywordTypesEnum&gt;) | Filter on targeted keyword type: unknown, generic, branded, conquesting |  [optional] |
|**timezone** | **String** | Time zone : see criteo developer portal for supported time zones |  [optional] |
|**viewAttributionWindow** | [**ViewAttributionWindowEnum**](#ViewAttributionWindowEnum) | View attribution window |  [optional] |



## Enum: List&lt;ActivationPlatformsEnum&gt;

| Name | Value |
|---- | -----|
| COMMERCEMAX | &quot;CommerceMax&quot; |
| PRIVATEMARKET | &quot;PrivateMarket&quot; |



## Enum: AggregationLevelEnum

| Name | Value |
|---- | -----|
| CAMPAIGN | &quot;campaign&quot; |
| LINEITEM | &quot;lineItem&quot; |



## Enum: List&lt;BudgetModelsEnum&gt;

| Name | Value |
|---- | -----|
| CRITEOBUDGET | &quot;CriteoBudget&quot; |
| RETAILERBUDGET | &quot;RetailerBudget&quot; |



## Enum: List&lt;BuyTypesEnum&gt;

| Name | Value |
|---- | -----|
| AUCTION | &quot;auction&quot; |
| PREFERREDDEALS | &quot;preferredDeals&quot; |
| SPONSORSHIP | &quot;sponsorship&quot; |



## Enum: CampaignTypeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| SPONSOREDPRODUCTS | &quot;sponsoredProducts&quot; |
| ONSITEDISPLAYS | &quot;onSiteDisplays&quot; |



## Enum: ClickAttributionWindowEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| _7D | &quot;7D&quot; |
| _14D | &quot;14D&quot; |
| _30D | &quot;30D&quot; |



## Enum: List&lt;DimensionsEnum&gt;

| Name | Value |
|---- | -----|
| DATE | &quot;date&quot; |
| HOUR | &quot;hour&quot; |
| ACCOUNTID | &quot;accountId&quot; |
| ACCOUNTNAME | &quot;accountName&quot; |
| CAMPAIGNID | &quot;campaignId&quot; |
| CAMPAIGNNAME | &quot;campaignName&quot; |
| CAMPAIGNTYPENAME | &quot;campaignTypeName&quot; |
| LINEITEMID | &quot;lineItemId&quot; |
| LINEITEMNAME | &quot;lineItemName&quot; |
| RETAILERID | &quot;retailerId&quot; |
| RETAILERNAME | &quot;retailerName&quot; |
| BRANDID | &quot;brandId&quot; |
| BRANDNAME | &quot;brandName&quot; |
| ADVPRODUCTCATEGORY | &quot;advProductCategory&quot; |
| ADVPRODUCTID | &quot;advProductId&quot; |
| ADVPRODUCTNAME | &quot;advProductName&quot; |
| SALESCHANNEL | &quot;salesChannel&quot; |
| MEDIATYPE | &quot;mediaType&quot; |
| BUYTYPE | &quot;buyType&quot; |
| BUDGETMODEL | &quot;budgetModel&quot; |
| ACTIVATIONPLATFORM | &quot;activationPlatform&quot; |
| ENVIRONMENT | &quot;environment&quot; |
| PAGETYPENAME | &quot;pageTypeName&quot; |
| PAGECATEGORY | &quot;pageCategory&quot; |
| SERVEDCATEGORY | &quot;servedCategory&quot; |
| TAXONOMYBREADCRUMB | &quot;taxonomyBreadcrumb&quot; |
| KEYWORD | &quot;keyword&quot; |
| SEARCHTERM | &quot;searchTerm&quot; |
| SEARCHTERMTYPE | &quot;searchTermType&quot; |
| SEARCHTERMTARGETING | &quot;searchTermTargeting&quot; |
| CREATIVEID | &quot;creativeId&quot; |
| CREATIVENAME | &quot;creativeName&quot; |
| CREATIVETYPEID | &quot;creativeTypeId&quot; |
| CREATIVETYPENAME | &quot;creativeTypeName&quot; |
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



## Enum: MediaTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| VIDEO | &quot;video&quot; |
| DISPLAY | &quot;display&quot; |
| ALL | &quot;all&quot; |



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



## Enum: ReportTypeEnum

| Name | Value |
|---- | -----|
| SUMMARY | &quot;summary&quot; |
| PAGETYPE | &quot;pageType&quot; |
| KEYWORD | &quot;keyword&quot; |
| PRODUCTCATEGORY | &quot;productCategory&quot; |
| PRODUCT | &quot;product&quot; |
| ATTRIBUTEDTRANSACTIONS | &quot;attributedTransactions&quot; |
| ENVIRONMENT | &quot;environment&quot; |
| SERVEDCATEGORY | &quot;servedCategory&quot; |
| CAPOUT | &quot;capout&quot; |



## Enum: SalesChannelEnum

| Name | Value |
|---- | -----|
| ONLINE | &quot;online&quot; |
| OFFLINE | &quot;offline&quot; |
| ALL | &quot;all&quot; |



## Enum: List&lt;SearchTermTargetingsEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| AUTOMATIC | &quot;automatic&quot; |
| MANUAL | &quot;manual&quot; |



## Enum: List&lt;SearchTermTypesEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| SEARCHED | &quot;searched&quot; |
| ENTERED | &quot;entered&quot; |



## Enum: List&lt;TargetedKeywordTypesEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| GENERIC | &quot;generic&quot; |
| BRANDED | &quot;branded&quot; |
| CONQUESTING | &quot;conquesting&quot; |



## Enum: ViewAttributionWindowEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| _1D | &quot;1D&quot; |
| _7D | &quot;7D&quot; |
| _14D | &quot;14D&quot; |
| _30D | &quot;30D&quot; |



