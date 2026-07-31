

# CampaignAttributesV202301

An object that represents the available options to set when creating a Retail Media Campaign

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budget** | **Double** |  |  [optional] |
|**clickAttributionScope** | [**ClickAttributionScopeEnum**](#ClickAttributionScopeEnum) |  |  [optional] |
|**clickAttributionWindow** | [**ClickAttributionWindowEnum**](#ClickAttributionWindowEnum) |  |  [optional] |
|**companyName** | **String** |  |  [optional] |
|**dailyPacing** | **Double** |  |  [optional] |
|**drawableBalanceIds** | **List&lt;String&gt;** |  |  [optional] |
|**endDate** | **OffsetDateTime** |  |  [optional] |
|**isAutoDailyPacing** | **Boolean** |  |  |
|**monthlyPacing** | **Double** |  |  [optional] |
|**name** | **String** |  |  |
|**onBehalfCompanyName** | **String** |  |  [optional] |
|**retailerId** | **Integer** |  |  [optional] |
|**startDate** | **OffsetDateTime** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
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



