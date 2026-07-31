

# CreateCampaignSpendLimit

Spend limit configuration for a marketing campaign. Controls how much can be spent and the renewal cadence.  When spendLimitType is \"capped\": spendLimitAmount and spendLimitRenewal are required.  When spendLimitType is \"uncapped\": spendLimitAmount is null and spendLimitRenewal is \"undefined\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**spendLimitAmount** | **Double** | Maximum spend amount in the advertiser&#39;s currency per renewal period. Non-null when capped. null when uncapped. |  [optional] |
|**spendLimitRenewal** | [**SpendLimitRenewalEnum**](#SpendLimitRenewalEnum) | The period over which the spend limit is consumed.  - \&quot;daily\&quot;, \&quot;monthly\&quot;: spend limit resets at the start of each period.  - \&quot;lifetime\&quot;: spend limit covers the entire campaign duration without resetting.  - \&quot;undefined\&quot;: only used when spendLimitType is \&quot;uncapped\&quot; (no renewal applies). |  [optional] |
|**spendLimitType** | [**SpendLimitTypeEnum**](#SpendLimitTypeEnum) | Controls whether the campaign has a spending limit.  - \&quot;capped\&quot;: spending is limited to spendLimitAmount. Requires spendLimitAmount (non-null) and spendLimitRenewal (not \&quot;undefined\&quot;).  - \&quot;uncapped\&quot;: no spending limit. spendLimitAmount is null and spendLimitRenewal is \&quot;undefined\&quot;. |  |



## Enum: SpendLimitRenewalEnum

| Name | Value |
|---- | -----|
| UNDEFINED | &quot;undefined&quot; |
| DAILY | &quot;daily&quot; |
| MONTHLY | &quot;monthly&quot; |
| LIFETIME | &quot;lifetime&quot; |



## Enum: SpendLimitTypeEnum

| Name | Value |
|---- | -----|
| CAPPED | &quot;capped&quot; |
| UNCAPPED | &quot;uncapped&quot; |



