# # CreateCampaignSpendLimit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spend_limit_amount** | **float** | Maximum spend amount in the advertiser&#39;s currency per renewal period. Non-null when capped. null when uncapped. | [optional]
**spend_limit_renewal** | **string** | The period over which the spend limit is consumed.  - \&quot;daily\&quot;, \&quot;monthly\&quot;: spend limit resets at the start of each period.  - \&quot;lifetime\&quot;: spend limit covers the entire campaign duration without resetting.  - \&quot;undefined\&quot;: only used when spendLimitType is \&quot;uncapped\&quot; (no renewal applies). | [optional]
**spend_limit_type** | **string** | Controls whether the campaign has a spending limit.  - \&quot;capped\&quot;: spending is limited to spendLimitAmount. Requires spendLimitAmount (non-null) and spendLimitRenewal (not \&quot;undefined\&quot;).  - \&quot;uncapped\&quot;: no spending limit. spendLimitAmount is null and spendLimitRenewal is \&quot;undefined\&quot;. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
