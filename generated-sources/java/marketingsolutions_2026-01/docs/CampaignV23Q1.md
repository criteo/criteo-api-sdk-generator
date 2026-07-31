

# CampaignV23Q1

Campaign read model                The {id} field is the campaign identifier (string-encoded integer).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserId** | **String** | Advertiser id of the campaign (string-encoded integer) |  [optional] |
|**budgetAutomation** | [**CampaignBudgetAutomationV23Q1**](CampaignBudgetAutomationV23Q1.md) |  |  [optional] |
|**goal** | [**GoalEnum**](#GoalEnum) | Goal of the campaign                Serialized values are {unspecified}, {acquisition} and {retention}.                Acquisition and retention are defined as follows:  - Acquisition: campaign with the goal of acquiring new customers. The success of an acquisition campaign is measured by the number of new customers it brings.  - Retention: campaign with the goal of retaining existing customers. The success of a retention campaign is measured by the number of existing customers it retains. |  [optional] |
|**id** | **String** | Id of the entity (duplicate of the parent id). |  [optional] |
|**name** | **String** | Name of the campaign |  [optional] |
|**spendLimit** | [**CampaignSpendLimitV23Q1**](CampaignSpendLimitV23Q1.md) |  |  [optional] |



## Enum: GoalEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;unspecified&quot; |
| ACQUISITION | &quot;acquisition&quot; |
| RETENTION | &quot;retention&quot; |



