# # CampaignAvailabilityV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_model_availabilities** | **string[]** | The budget models available for this campaign type and buy type combination. Presence of a value indicates that budget model is available. | [optional]
**buy_type** | **string** | The buy type this object represents availability for | [optional]
**campaign_type** | **string** | The type of campaign this object represents availability for | [optional]
**valid_combinations** | [**\criteo\api\retailmedia\experimental\Model\PageTypeCombinationV2[]**](PageTypeCombinationV2.md) | PageType-PageEnvironmentType pairs which are supported for this campaign-buy type combination | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
