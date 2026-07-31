# # CampaignSpendLimitV23Q1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spend_limit_amount** | [**\criteo\api\marketingsolutions\preview\Model\NillableDecimal**](NillableDecimal.md) |  | [optional]
**spend_limit_renewal** | **string** | The period over which the campaign spend limit is applied.  When spendLimitType is \&quot;capped\&quot;, this is \&quot;daily\&quot;, \&quot;monthly\&quot;, or \&quot;lifetime\&quot;.  When spendLimitType is \&quot;uncapped\&quot;, this is \&quot;undefined\&quot;. | [optional]
**spend_limit_type** | **string** | Controls whether the campaign has a spend limit.  \&quot;capped\&quot; returns a non-null spendLimitAmount.value and a spendLimitRenewal of \&quot;daily\&quot;, \&quot;monthly\&quot;, or \&quot;lifetime\&quot;.  \&quot;uncapped\&quot; returns spendLimitAmount.value as null and spendLimitRenewal as \&quot;undefined\&quot;. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
