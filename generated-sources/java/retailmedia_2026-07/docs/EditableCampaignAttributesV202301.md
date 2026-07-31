

# EditableCampaignAttributesV202301

An object that represents the available options to set when editing a Retail Media Campaign

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budget** | **Double** |  |  [optional] |
|**clickAttributionScope** | [**ClickAttributionScopeEnum**](#ClickAttributionScopeEnum) |  |  [optional] |
|**clickAttributionWindow** | [**ClickAttributionWindowEnum**](#ClickAttributionWindowEnum) |  |  |
|**companyName** | **String** |  |  [optional] |
|**dailyPacing** | **Double** |  |  [optional] |
|**endDate** | **OffsetDateTime** |  |  [optional] |
|**isAutoDailyPacing** | **Boolean** |  |  |
|**monthlyPacing** | **Double** |  |  [optional] |
|**name** | **String** |  |  |
|**onBehalfCompanyName** | **String** |  |  [optional] |
|**startDate** | **OffsetDateTime** |  |  [optional] |
|**viewAttributionScope** | [**ViewAttributionScopeEnum**](#ViewAttributionScopeEnum) |  |  [optional] |
|**viewAttributionWindow** | [**ViewAttributionWindowEnum**](#ViewAttributionWindowEnum) |  |  |



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



