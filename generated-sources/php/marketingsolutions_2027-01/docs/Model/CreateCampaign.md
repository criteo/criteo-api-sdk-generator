# # CreateCampaign

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_id** | **string** | Advertiser ID this campaign belongs to (string-encoded integer). |
**budget_automation** | [**\criteo\api\marketingsolutions\v2027_01\Model\BudgetAutomation**](BudgetAutomation.md) |  | [optional]
**goal** | **string** | Goal of the campaign                Serialized values are {Unspecified}, {Acquisition} and {Retention}.                Acquisition and retention are defined as follows:  - Acquisition: campaign with the goal of acquiring new customers. The success of an acquisition campaign is measured by the number of new customers it brings.  - Retention: campaign with the goal of retaining existing customers. The success of a retention campaign is measured by the number of existing customers it retains. |
**name** | **string** | Name of the campaign |
**spend_limit** | [**\criteo\api\marketingsolutions\v2027_01\Model\CreateCampaignSpendLimit**](CreateCampaignSpendLimit.md) |  |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
