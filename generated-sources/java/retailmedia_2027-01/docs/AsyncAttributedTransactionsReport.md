

# AsyncAttributedTransactionsReport

Create payload attributes for an attributed-transactions async report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clickAttributionWindow** | [**ClickAttributionWindowEnum**](#ClickAttributionWindowEnum) |  |  [optional] |
|**clickMatchLevel** | [**ClickMatchLevelEnum**](#ClickMatchLevelEnum) |  |  [optional] |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) |  |  |
|**endDate** | **OffsetDateTime** |  |  |
|**filters** | [**AttributedTransactionsReportFilters**](AttributedTransactionsReportFilters.md) |  |  |
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
| PURCHASEDDATE | &quot;purchasedDate&quot; |
| PURCHASEDHOUR | &quot;purchasedHour&quot; |
| ADVERTISEDDATE | &quot;advertisedDate&quot; |
| ADVERTISEDHOUR | &quot;advertisedHour&quot; |
| DAYSDIFFERENCE | &quot;daysDifference&quot; |
| ACCOUNTID | &quot;accountId&quot; |
| ACCOUNTNAME | &quot;accountName&quot; |
| CAMPAIGNID | &quot;campaignId&quot; |
| CAMPAIGNNAME | &quot;campaignName&quot; |
| LINEITEMID | &quot;lineItemId&quot; |
| LINEITEMNAME | &quot;lineItemName&quot; |
| ADVERTISEDPRODUCTID | &quot;advertisedProductId&quot; |
| ADVERTISEDPRODUCTGTIN | &quot;advertisedProductGtin&quot; |
| ADVERTISEDPRODUCTMPN | &quot;advertisedProductMpn&quot; |
| ADVERTISEDPRODUCTNAME | &quot;advertisedProductName&quot; |
| ADVERTISEDPRODUCTCATEGORY | &quot;advertisedProductCategory&quot; |
| PURCHASEDPRODUCTID | &quot;purchasedProductId&quot; |
| PURCHASEDPRODUCTGTIN | &quot;purchasedProductGtin&quot; |
| PURCHASEDPRODUCTMPN | &quot;purchasedProductMpn&quot; |
| PURCHASEDPRODUCTNAME | &quot;purchasedProductName&quot; |
| PURCHASEDPRODUCTCATEGORY | &quot;purchasedProductCategory&quot; |
| ADVERTISEDENGAGEMENT | &quot;advertisedEngagement&quot; |
| ADVERTISEDTOPURCHASEDPRODUCTRELATIONSHIP | &quot;advertisedToPurchasedProductRelationship&quot; |
| SALESCHANNEL | &quot;salesChannel&quot; |
| RETAILERID | &quot;retailerId&quot; |
| RETAILERNAME | &quot;retailerName&quot; |
| PAGETYPE | &quot;pageType&quot; |
| KEYWORD | &quot;keyword&quot; |
| ATTRIBUTIONWINDOW | &quot;attributionWindow&quot; |
| SALESELLERID | &quot;saleSellerId&quot; |
| SALESELLERNAME | &quot;saleSellerName&quot; |
| ACTIVITYSELLERID | &quot;activitySellerId&quot; |
| ACTIVITYSELLERNAME | &quot;activitySellerName&quot; |



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
| ATTRIBUTEDUNITS | &quot;attributedUnits&quot; |
| ATTRIBUTEDSALES | &quot;attributedSales&quot; |



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



