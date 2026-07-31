

# CreateCampaign

Campaign create model.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserId** | **String** | Advertiser ID this campaign belongs to (string-encoded integer). |  |
|**budgetAutomation** | [**BudgetAutomation**](BudgetAutomation.md) |  |  [optional] |
|**goal** | [**GoalEnum**](#GoalEnum) | Goal of the campaign                Serialized values are {Unspecified}, {Acquisition} and {Retention}.                Acquisition and retention are defined as follows:  - Acquisition: campaign with the goal of acquiring new customers. The success of an acquisition campaign is measured by the number of new customers it brings.  - Retention: campaign with the goal of retaining existing customers. The success of a retention campaign is measured by the number of existing customers it retains. |  |
|**name** | **String** | Name of the campaign |  |
|**spendLimit** | [**CreateCampaignSpendLimit**](CreateCampaignSpendLimit.md) |  |  |



## Enum: GoalEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;Unspecified&quot; |
| ACQUISITION | &quot;Acquisition&quot; |
| RETENTION | &quot;Retention&quot; |



