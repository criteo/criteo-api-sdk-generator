# # CampaignV23Q1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_id** | **string** | Advertiser id of the campaign (string-encoded integer) | [optional]
**budget_automation** | [**\criteo\api\marketingsolutions\experimental\Model\CampaignBudgetAutomationV23Q1**](CampaignBudgetAutomationV23Q1.md) |  | [optional]
**goal** | **string** | Goal of the campaign                Serialized values are {unspecified}, {acquisition} and {retention}.                Acquisition and retention are defined as follows:  - Acquisition: campaign with the goal of acquiring new customers. The success of an acquisition campaign is measured by the number of new customers it brings.  - Retention: campaign with the goal of retaining existing customers. The success of a retention campaign is measured by the number of existing customers it retains. | [optional]
**id** | **string** | Id of the entity (duplicate of the parent id). | [optional]
**name** | **string** | Name of the campaign | [optional]
**spend_limit** | [**\criteo\api\marketingsolutions\experimental\Model\CampaignSpendLimitV23Q1**](CampaignSpendLimitV23Q1.md) |  | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
