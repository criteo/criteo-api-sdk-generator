

# SyncAttributedTransactionsReport

Attributed Transactions report body request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Account id to report on |  |
|**campaignIds** | **List&lt;String&gt;** | Campaign ids to filter |  [optional] |
|**campaignType** | [**CampaignTypeEnum**](#CampaignTypeEnum) | Filter the type of campaigns to report on: sponsoredProducts or onSiteDisplays |  [optional] |
|**clickAttributionWindow** | [**ClickAttributionWindowEnum**](#ClickAttributionWindowEnum) | Click attribution window |  [optional] |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) | List of dimensions to report on |  [optional] |
|**endDate** | **OffsetDateTime** | End date |  |
|**lineItemIds** | **List&lt;String&gt;** | Line item ids to filter |  [optional] |
|**mediaType** | [**MediaTypeEnum**](#MediaTypeEnum) | Filter on the type of media: unknown, display, video |  [optional] |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) | List of metrics to report on |  [optional] |
|**salesChannel** | [**SalesChannelEnum**](#SalesChannelEnum) | Filter on specific sales channel: offline or online |  [optional] |
|**startDate** | **OffsetDateTime** | Start date |  |
|**timezone** | **String** | Time zone : see criteo developer portal for supported time zones |  [optional] |
|**viewAttributionWindow** | [**ViewAttributionWindowEnum**](#ViewAttributionWindowEnum) | View attribution window |  [optional] |



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
| PURCHASEDDATE | &quot;purchasedDate&quot; |
| PURCHASEDHOUR | &quot;purchasedHour&quot; |
| ADVDATE | &quot;advDate&quot; |
| ADVHOUR | &quot;advHour&quot; |
| DAYSDIFFERENCE | &quot;daysDifference&quot; |
| CAMPAIGNID | &quot;campaignId&quot; |
| CAMPAIGNNAME | &quot;campaignName&quot; |
| LINEITEMID | &quot;lineItemId&quot; |
| LINEITEMNAME | &quot;lineItemName&quot; |
| ADVPRODUCTID | &quot;advProductId&quot; |
| ADVPRODUCTGTIN | &quot;advProductGtin&quot; |
| ADVPRODUCTMPN | &quot;advProductMpn&quot; |
| ADVPRODUCTNAME | &quot;advProductName&quot; |
| ADVPRODUCTCATEGORY | &quot;advProductCategory&quot; |
| PURCHASEDPRODUCTID | &quot;purchasedProductId&quot; |
| PURCHASEDPRODUCTGTIN | &quot;purchasedProductGtin&quot; |
| PURCHASEDPRODUCTMPN | &quot;purchasedProductMpn&quot; |
| PURCHASEDPRODUCTNAME | &quot;purchasedProductName&quot; |
| PURCHASEDPRODUCTCATEGORY | &quot;purchasedProductCategory&quot; |
| ADVENGAGEMENT | &quot;advEngagement&quot; |
| ADVTOPURCHASEDPRODUCTRELATIONSHIP | &quot;advToPurchasedProductRelationship&quot; |
| SALESCHANNEL | &quot;salesChannel&quot; |
| RETAILERNAME | &quot;retailerName&quot; |
| PAGETYPENAME | &quot;pageTypeName&quot; |
| KEYWORD | &quot;keyword&quot; |
| ATTRIBUTIONWINDOW | &quot;attributionWindow&quot; |
| SALESELLERID | &quot;saleSellerId&quot; |
| SALESELLERNAME | &quot;saleSellerName&quot; |
| ACTIVITYSELLERID | &quot;activitySellerId&quot; |
| ACTIVITYSELLERNAME | &quot;activitySellerName&quot; |



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
| ATTRIBUTEDUNITS | &quot;attributedUnits&quot; |
| ATTRIBUTEDSALES | &quot;attributedSales&quot; |



## Enum: SalesChannelEnum

| Name | Value |
|---- | -----|
| ONLINE | &quot;online&quot; |
| OFFLINE | &quot;offline&quot; |
| ALL | &quot;all&quot; |



## Enum: ViewAttributionWindowEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| _1D | &quot;1D&quot; |
| _7D | &quot;7D&quot; |
| _14D | &quot;14D&quot; |
| _30D | &quot;30D&quot; |



