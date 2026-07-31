

# CampaignV202301

A Retail Media Campaign used to represent an advertiser's marketing objective

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**budget** | **Double** |  |  [optional] |
|**budgetRemaining** | **Double** |  |  [optional] |
|**budgetSpent** | **Double** |  |  [optional] |
|**clickAttributionScope** | [**ClickAttributionScopeEnum**](#ClickAttributionScopeEnum) |  |  [optional] |
|**clickAttributionWindow** | [**ClickAttributionWindowEnum**](#ClickAttributionWindowEnum) |  |  [optional] |
|**companyName** | **String** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  |
|**dailyPacing** | **Double** |  |  [optional] |
|**drawableBalanceIds** | **List&lt;String&gt;** |  |  [optional] |
|**endDate** | **OffsetDateTime** |  |  [optional] |
|**isAutoDailyPacing** | **Boolean** |  |  |
|**monthlyPacing** | **Double** |  |  [optional] |
|**name** | **String** |  |  |
|**onBehalfCompanyName** | **String** |  |  [optional] |
|**promotedBrandIds** | **List&lt;String&gt;** |  |  [optional] |
|**retailerId** | **Integer** |  |  [optional] |
|**startDate** | **OffsetDateTime** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  |
|**viewAttributionScope** | [**ViewAttributionScopeEnum**](#ViewAttributionScopeEnum) |  |  [optional] |
|**viewAttributionWindow** | [**ViewAttributionWindowEnum**](#ViewAttributionWindowEnum) |  |  [optional] |



## Enum: ClickAttributionScopeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| SAMESKU | &quot;sameSku&quot; |
| SAMESKUCATEGORY | &quot;sameSkuCategory&quot; |
| SAMESKUCATEGORYBRAND | &quot;sameSkuCategoryBrand&quot; |



## Enum: ClickAttributionWindowEnum

| Name | Value |
|---- | -----|
| _7D | &quot;7D&quot; |
| _14D | &quot;14D&quot; |
| _30D | &quot;30D&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |
| SCHEDULED | &quot;scheduled&quot; |
| ENDED | &quot;ended&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| AUCTION | &quot;auction&quot; |
| PREFERRED | &quot;preferred&quot; |



## Enum: ViewAttributionScopeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| SAMESKU | &quot;sameSku&quot; |
| SAMESKUCATEGORY | &quot;sameSkuCategory&quot; |
| SAMESKUCATEGORYBRAND | &quot;sameSkuCategoryBrand&quot; |



## Enum: ViewAttributionWindowEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| _1D | &quot;1D&quot; |
| _7D | &quot;7D&quot; |
| _14D | &quot;14D&quot; |
| _30D | &quot;30D&quot; |
| UNKNOWN | &quot;unknown&quot; |



