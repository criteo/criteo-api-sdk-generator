

# CampaignSpendLimitV23Q1

Campaign spend-limit configuration. A capped spend limit restricts campaign spending per renewal period. An uncapped spend limit does not impose a spending ceiling.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**spendLimitAmount** | [**NillableDecimal**](NillableDecimal.md) |  |  [optional] |
|**spendLimitRenewal** | [**SpendLimitRenewalEnum**](#SpendLimitRenewalEnum) | The period over which the campaign spend limit is applied.  When spendLimitType is \&quot;capped\&quot;, this is \&quot;daily\&quot;, \&quot;monthly\&quot;, or \&quot;lifetime\&quot;.  When spendLimitType is \&quot;uncapped\&quot;, this is \&quot;undefined\&quot;. |  [optional] |
|**spendLimitType** | [**SpendLimitTypeEnum**](#SpendLimitTypeEnum) | Controls whether the campaign has a spend limit.  \&quot;capped\&quot; returns a non-null spendLimitAmount.value and a spendLimitRenewal of \&quot;daily\&quot;, \&quot;monthly\&quot;, or \&quot;lifetime\&quot;.  \&quot;uncapped\&quot; returns spendLimitAmount.value as null and spendLimitRenewal as \&quot;undefined\&quot;. |  [optional] |



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



