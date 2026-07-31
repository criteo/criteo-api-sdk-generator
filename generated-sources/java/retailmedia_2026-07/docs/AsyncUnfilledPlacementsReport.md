

# AsyncUnfilledPlacementsReport

Async Unfilled Placements report body request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adServerType** | [**AdServerTypeEnum**](#AdServerTypeEnum) | Filter on the type of the ad server: criteo, gam, all |  [optional] |
|**campaignType** | [**CampaignTypeEnum**](#CampaignTypeEnum) | Filter on the type of the campaign: onsite display, onsite sponsored products, all |  [optional] |
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



## Enum: CampaignTypeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| SPONSOREDPRODUCTS | &quot;sponsoredProducts&quot; |
| ONSITEDISPLAYS | &quot;onSiteDisplays&quot; |



## Enum: List&lt;DimensionsEnum&gt;

| Name | Value |
|---- | -----|
| DATE | &quot;date&quot; |
| RETAILERID | &quot;retailerId&quot; |
| RETAILERNAME | &quot;retailerName&quot; |
| PLACEMENTID | &quot;placementId&quot; |
| PLACEMENTNAME | &quot;placementName&quot; |
| PAGETYPENAME | &quot;pageTypeName&quot; |
| SERVEDCATEGORY | &quot;servedCategory&quot; |
| ENVIRONMENT | &quot;environment&quot; |
| RETAILERCATEGORYID | &quot;retailerCategoryId&quot; |
| RETAILERCATEGORYNAME | &quot;retailerCategoryName&quot; |
| ADSERVERTYPE | &quot;adServerType&quot; |
| CAMPAIGNTYPE | &quot;campaignType&quot; |



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
| TOTALUNFILLEDPLACEMENTS | &quot;totalUnfilledPlacements&quot; |
| UNFILLEDUSEROPTOUT | &quot;unfilledUserOptOut&quot; |
| UNFILLEDNOTENOUGHDEMAND | &quot;unfilledNotEnoughDemand&quot; |
| UNFILLEDTOTALAUCTIONSETTINGS | &quot;unfilledTotalAuctionSettings&quot; |
| UNFILLEDTOTALAUCTIONCONSIDERATIONS | &quot;unfilledTotalAuctionConsiderations&quot; |
| UNFILLEDADVERTISERAUCTIONSETTINGS | &quot;unfilledAdvertiserAuctionSettings&quot; |
| UNFILLEDRETAILERAUCTIONSETTINGS | &quot;unfilledRetailerAuctionSettings&quot; |
| UNFILLEDCRITEOAUCTIONSETTINGS | &quot;unfilledCriteoAuctionSettings&quot; |
| UNFILLEDRETURNEDBUTNOTPAINTED | &quot;unfilledReturnedButNotPainted&quot; |
| NONDELIVERABLEUNMAPPEDCATEGORIES | &quot;nonDeliverableUnmappedCategories&quot; |
| NONDELIVERABLEPAGESWITHUNKNOWNPRODUCTS | &quot;nonDeliverablePagesWithUnknownProducts&quot; |
| NONDELIVERABLEBLOCKEDOPTOUT | &quot;nonDeliverableBlockedOptOut&quot; |
| NONDELIVERABLEBLOCKEDPAGECATEGORY | &quot;nonDeliverableBlockedPageCategory&quot; |
| NONDELIVERABLEINACTIVEPLACEMENT | &quot;nonDeliverableInactivePlacement&quot; |
| NONDELIVERABLEINSUFFICIENTORGANICRESULTS | &quot;nonDeliverableInsufficientOrganicResults&quot; |
| NONDELIVERABLEINVALIDTRAFFIC | &quot;nonDeliverableInvalidTraffic&quot; |
| NONDELIVERABLETESTPLACEMENT | &quot;nonDeliverableTestPlacement&quot; |
| UNCOVEREDUNUSEDFORMATS | &quot;uncoveredUnusedFormats&quot; |
| UNCOVEREDSEARCHTERMWITHOUTCATEGORY | &quot;uncoveredSearchTermWithoutCategory&quot; |
| UNCOVEREDNODEMANDBRANDEDKEYWORDCONQUESTINGENABLED | &quot;uncoveredNoDemandBrandedKeywordConquestingEnabled&quot; |
| UNCOVEREDNODEMANDBRANDEDKEYWORDCONQUESTINGDISABLED | &quot;uncoveredNoDemandBrandedKeywordConquestingDisabled&quot; |
| UNCOVEREDNODEMANDUNBRANDEDINVENTORY | &quot;uncoveredNoDemandUnbrandedInventory&quot; |
| UNCOVEREDNODEMANDOPTOUT | &quot;uncoveredNoDemandOptOut&quot; |
| UNCOVEREDFILTEREDOUTDEMAND | &quot;uncoveredFilteredOutDemand&quot; |
| UNCOVEREDBROKENPLACEMENT | &quot;uncoveredBrokenPlacement&quot; |
| UNCOVEREDNOTPAINTED | &quot;uncoveredNotPainted&quot; |
| AVAILABLEPLACEMENTS | &quot;availablePlacements&quot; |
| FILLRATE | &quot;fillRate&quot; |
| PLACEMENTIMPRESSIONS | &quot;placementImpressions&quot; |
| PRODUCTIMPRESSIONS | &quot;productImpressions&quot; |
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
| NONDELIVERABLEPLACEMENTS | &quot;nonDeliverablePlacements&quot; |
| DELIVERABLEPLACEMENTS | &quot;deliverablePlacements&quot; |
| PLACEMENTSWITHCANDIDATES | &quot;placementsWithCandidates&quot; |
| COVEREDPLACEMENTS | &quot;coveredPlacements&quot; |
| COVERAGERATE | &quot;coverageRate&quot; |



