

# AsyncRevenueReport

Async Revenue report body request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountIds** | **List&lt;String&gt;** | Account ids to filter |  [optional] |
|**activationPlatforms** | [**List&lt;ActivationPlatformsEnum&gt;**](#List&lt;ActivationPlatformsEnum&gt;) | Filter on the activation platform: CommerceMax, PrivateMarket |  [optional] |
|**advertiserTypes** | [**List&lt;AdvertiserTypesEnum&gt;**](#List&lt;AdvertiserTypesEnum&gt;) | Filter on the type of advertiser: retailer, brand, seller |  [optional] |
|**budgetModels** | [**List&lt;BudgetModelsEnum&gt;**](#List&lt;BudgetModelsEnum&gt;) | Filter on the budget model: CriteoBudget, RetailerBudget |  [optional] |
|**buyType** | [**BuyTypeEnum**](#BuyTypeEnum) | Filter on buy type: Auction, Preferred Deals or Sponsorship |  [optional] |
|**campaignIds** | **List&lt;String&gt;** | Campaign ids to filter |  [optional] |
|**campaignType** | [**CampaignTypeEnum**](#CampaignTypeEnum) | Filter the type of campaigns to report on: sponsoredProducts or onSiteDisplays |  [optional] |
|**clickAttributionWindow** | [**ClickAttributionWindowEnum**](#ClickAttributionWindowEnum) | Click attribution window |  [optional] |
|**clickMatchLevel** | [**ClickMatchLevelEnum**](#ClickMatchLevelEnum) | Click Match Level: Campaign, Same SKU, Same Category or Same Brand |  [optional] |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) | List of dimensions to report on |  [optional] |
|**endDate** | **OffsetDateTime** | End date |  |
|**format** | [**FormatEnum**](#FormatEnum) | Format of the output |  [optional] |
|**id** | **String** | Supply account id to report on |  [optional] |
|**ids** | **List&lt;String&gt;** | Supply account ids to report on |  [optional] |
|**lineItemIds** | **List&lt;String&gt;** | Line item ids to filter |  [optional] |
|**mediaType** | [**MediaTypeEnum**](#MediaTypeEnum) | Filter on the type of media: unknown, display, video |  [optional] |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) | List of metrics to report on |  [optional] |
|**reportType** | [**ReportTypeEnum**](#ReportTypeEnum) | Type of report, if no dimensions and metrics are provided, falls back to advertiser reportType |  [optional] |
|**retailerIds** | **List&lt;String&gt;** | Retailer ids to filter |  [optional] |
|**revenueType** | [**RevenueTypeEnum**](#RevenueTypeEnum) | Type of revenue |  [optional] |
|**salesChannel** | [**SalesChannelEnum**](#SalesChannelEnum) | Filter on specific sales channel: offline or online |  [optional] |
|**skuRelations** | [**List&lt;SkuRelationsEnum&gt;**](#List&lt;SkuRelationsEnum&gt;) | Filter on sku relations: Same SKU, Same Parent SKU, Same Category, Same Brand or Same Seller |  [optional] |
|**soldBy** | [**SoldByEnum**](#SoldByEnum) | Filter on the seller: Indirect Sold, Direct Sold, Authorized Buyer or Private Market |  [optional] |
|**startDate** | **OffsetDateTime** | Start date |  |
|**targetedKeywordTypes** | [**List&lt;TargetedKeywordTypesEnum&gt;**](#List&lt;TargetedKeywordTypesEnum&gt;) | Filter on targeted keyword type: unknown, generic, branded, conquesting |  [optional] |
|**timezone** | **String** | Time zone : see criteo developer portal for supported time zones |  [optional] |
|**viewAttributionWindow** | [**ViewAttributionWindowEnum**](#ViewAttributionWindowEnum) | View attribution window |  [optional] |
|**viewMatchLevel** | [**ViewMatchLevelEnum**](#ViewMatchLevelEnum) | View Match Level: Campaign, Same SKU, Same Category or Same Brand |  [optional] |



## Enum: List&lt;ActivationPlatformsEnum&gt;

| Name | Value |
|---- | -----|
| COMMERCEMAX | &quot;CommerceMax&quot; |
| PRIVATEMARKET | &quot;PrivateMarket&quot; |



## Enum: List&lt;AdvertiserTypesEnum&gt;

| Name | Value |
|---- | -----|
| RETAILER | &quot;retailer&quot; |
| BRAND | &quot;brand&quot; |
| SELLER | &quot;seller&quot; |



## Enum: List&lt;BudgetModelsEnum&gt;

| Name | Value |
|---- | -----|
| CRITEOBUDGET | &quot;CriteoBudget&quot; |
| RETAILERBUDGET | &quot;RetailerBudget&quot; |



## Enum: BuyTypeEnum

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
| PARENTACCOUNT | &quot;parentAccount&quot; |
| ACCOUNTID | &quot;accountId&quot; |
| ACCOUNTNAME | &quot;accountName&quot; |
| ACCOUNTTYPENAME | &quot;accountTypeName&quot; |
| ADVERTISERTYPE | &quot;advertiserType&quot; |
| CAMPAIGNID | &quot;campaignId&quot; |
| CAMPAIGNNAME | &quot;campaignName&quot; |
| CAMPAIGNTYPENAME | &quot;campaignTypeName&quot; |
| CAMPAIGNSTARTDATE | &quot;campaignStartDate&quot; |
| CAMPAIGNENDDATE | &quot;campaignEndDate&quot; |
| LINEITEMID | &quot;lineItemId&quot; |
| LINEITEMNAME | &quot;lineItemName&quot; |
| LINEITEMSTARTDATE | &quot;lineItemStartDate&quot; |
| LINEITEMENDDATE | &quot;lineItemEndDate&quot; |
| LINEITEMSTATUS | &quot;lineItemStatus&quot; |
| RETAILERID | &quot;retailerId&quot; |
| RETAILERNAME | &quot;retailerName&quot; |
| BRANDID | &quot;brandId&quot; |
| BRANDNAME | &quot;brandName&quot; |
| PLACEMENTID | &quot;placementId&quot; |
| PLACEMENTNAME | &quot;placementName&quot; |
| PAGETYPENAME | &quot;pageTypeName&quot; |
| ENVIRONMENT | &quot;environment&quot; |
| PAGECATEGORY | &quot;pageCategory&quot; |
| ADVPRODUCTID | &quot;advProductId&quot; |
| ADVPRODUCTNAME | &quot;advProductName&quot; |
| ADVPRODUCTGTIN | &quot;advProductGtin&quot; |
| ADVPRODUCTMPN | &quot;advProductMpn&quot; |
| BUYTYPE | &quot;buyType&quot; |
| BUDGETMODEL | &quot;budgetModel&quot; |
| ACTIVATIONPLATFORM | &quot;activationPlatform&quot; |
| SOLDBY | &quot;soldBy&quot; |
| SALECHANNEL | &quot;saleChannel&quot; |
| SALESCHANNEL | &quot;salesChannel&quot; |
| MEDIATYPE | &quot;mediaType&quot; |
| ATTRIBUTIONSETTINGS | &quot;attributionSettings&quot; |
| ACTIVITYTYPE | &quot;activityType&quot; |
| KEYWORD | &quot;keyword&quot; |
| SKURELATION | &quot;skuRelation&quot; |
| RETAILERCATEGORYID | &quot;retailerCategoryId&quot; |
| RETAILERCATEGORYNAME | &quot;retailerCategoryName&quot; |
| TAXONOMYBREADCRUMB | &quot;taxonomyBreadcrumb&quot; |
| TAXONOMY1ID | &quot;taxonomy1Id&quot; |
| TAXONOMY1NAME | &quot;taxonomy1Name&quot; |
| TAXONOMY2ID | &quot;taxonomy2Id&quot; |
| TAXONOMY2NAME | &quot;taxonomy2Name&quot; |
| TAXONOMY3ID | &quot;taxonomy3Id&quot; |
| TAXONOMY3NAME | &quot;taxonomy3Name&quot; |
| TAXONOMY4ID | &quot;taxonomy4Id&quot; |
| TAXONOMY4NAME | &quot;taxonomy4Name&quot; |
| TAXONOMY5ID | &quot;taxonomy5Id&quot; |
| TAXONOMY5NAME | &quot;taxonomy5Name&quot; |
| TAXONOMY6ID | &quot;taxonomy6Id&quot; |
| TAXONOMY6NAME | &quot;taxonomy6Name&quot; |
| TAXONOMY7ID | &quot;taxonomy7Id&quot; |
| TAXONOMY7NAME | &quot;taxonomy7Name&quot; |
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
| NUMBEROFCAMPAIGNS | &quot;numberOfCampaigns&quot; |
| NUMBEROFLINEITEMS | &quot;numberOfLineItems&quot; |
| NUMBEROFSKUS | &quot;numberOfSkus&quot; |
| SKUPRICE | &quot;skuPrice&quot; |
| PAGEVIEWS | &quot;pageViews&quot; |
| IMPRESSIONS | &quot;impressions&quot; |
| PRODUCTCLICKS | &quot;productClicks&quot; |
| PLACEMENTCLICKS | &quot;placementClicks&quot; |
| CLICKS | &quot;clicks&quot; |
| SALES | &quot;sales&quot; |
| UNITS | &quot;units&quot; |
| TRANSACTIONS | &quot;transactions&quot; |
| ASSISTEDSALES | &quot;assistedSales&quot; |
| ASSISTEDUNITS | &quot;assistedUnits&quot; |
| REVENUE | &quot;revenue&quot; |
| OPENAUCTIONREVENUE | &quot;openAuctionRevenue&quot; |
| PREFERREDDEALSREVENUE | &quot;preferredDealsRevenue&quot; |
| CTR | &quot;ctr&quot; |
| CR | &quot;cr&quot; |
| CPC | &quot;cpc&quot; |
| CPM | &quot;cpm&quot; |
| ROAS | &quot;roas&quot; |
| WORKINGMEDIA | &quot;workingMedia&quot; |
| NETREVENUE | &quot;netRevenue&quot; |
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
| VIDEORESUMED | &quot;videoResumed&quot; |
| VIDEOPAUSED | &quot;videoPaused&quot; |
| VIDEOAVGINTERACTIONRATE | &quot;videoAvgInteractionRate&quot; |
| VIDEOVIEWABILITY | &quot;videoViewability&quot; |
| VIDEOSTARTINGRATE | &quot;videoStartingRate&quot; |
| VIDEOCPC | &quot;videoCPC&quot; |
| VIDEOCPCV | &quot;videoCPCV&quot; |
| UNIQUEVISITORS | &quot;uniqueVisitors&quot; |
| FREQUENCY | &quot;frequency&quot; |



## Enum: ReportTypeEnum

| Name | Value |
|---- | -----|
| ADVERTISER | &quot;advertiser&quot; |
| ENVIRONMENT | &quot;environment&quot; |
| PAGETYPE | &quot;pageType&quot; |
| PRODUCTCATEGORY | &quot;productCategory&quot; |
| BRAND | &quot;brand&quot; |



## Enum: RevenueTypeEnum

| Name | Value |
|---- | -----|
| AUCTION | &quot;auction&quot; |
| PREFERRED | &quot;preferred&quot; |



## Enum: SalesChannelEnum

| Name | Value |
|---- | -----|
| ONLINE | &quot;online&quot; |
| OFFLINE | &quot;offline&quot; |
| ALL | &quot;all&quot; |



## Enum: List&lt;SkuRelationsEnum&gt;

| Name | Value |
|---- | -----|
| SAMESKU | &quot;sameSku&quot; |
| SAMEPARENTSKU | &quot;sameParentSku&quot; |
| SAMECATEGORY | &quot;sameCategory&quot; |
| SAMEBRAND | &quot;sameBrand&quot; |
| SAMESELLER | &quot;sameSeller&quot; |



## Enum: SoldByEnum

| Name | Value |
|---- | -----|
| DIRECTSOLD | &quot;directSold&quot; |
| INDIRECTSOLD | &quot;indirectSold&quot; |
| PRIVATEMARKET | &quot;privateMarket&quot; |
| AUTHORIZEDBUYER | &quot;authorizedBuyer&quot; |



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



## Enum: ViewMatchLevelEnum

| Name | Value |
|---- | -----|
| SAMESKU | &quot;sameSku&quot; |
| SAMECATEGORY | &quot;sameCategory&quot; |
| SAMEBRAND | &quot;sameBrand&quot; |
| CAMPAIGN | &quot;campaign&quot; |



