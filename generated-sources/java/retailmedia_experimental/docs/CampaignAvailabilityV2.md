

# CampaignAvailabilityV2

Information about the budget model availability for a specific campaign type and buy type combination, and page types and environments supported for that combination

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budgetModelAvailabilities** | [**List&lt;BudgetModelAvailabilitiesEnum&gt;**](#List&lt;BudgetModelAvailabilitiesEnum&gt;) | The budget models available for this campaign type and buy type combination. Presence of a value indicates that budget model is available. |  [optional] |
|**buyType** | [**BuyTypeEnum**](#BuyTypeEnum) | The buy type this object represents availability for |  [optional] |
|**campaignType** | [**CampaignTypeEnum**](#CampaignTypeEnum) | The type of campaign this object represents availability for |  [optional] |
|**validCombinations** | [**List&lt;PageTypeCombinationV2&gt;**](PageTypeCombinationV2.md) | PageType-PageEnvironmentType pairs which are supported for this campaign-buy type combination |  [optional] |



## Enum: List&lt;BudgetModelAvailabilitiesEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| CRITEOBUDGET | &quot;criteoBudget&quot; |
| RETAILERBUDGET | &quot;retailerBudget&quot; |



## Enum: BuyTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| AUCTION | &quot;auction&quot; |
| PREFERREDDEALS | &quot;preferredDeals&quot; |
| SPONSORSHIP | &quot;sponsorship&quot; |
| OFFSITE | &quot;offsite&quot; |



## Enum: CampaignTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| SPONSOREDPRODUCTS | &quot;sponsoredProducts&quot; |
| ONSITEDISPLAY | &quot;onsiteDisplay&quot; |
| OFFSITE | &quot;offsite&quot; |



