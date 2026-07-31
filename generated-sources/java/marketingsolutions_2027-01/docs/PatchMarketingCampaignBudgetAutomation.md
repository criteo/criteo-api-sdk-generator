

# PatchMarketingCampaignBudgetAutomation

Budget automation, lets users configure budgets once at the campaign level while Criteo dynamically routes spend toward the best-performing ad sets.  Only provided fields are updated; omitted fields are left unchanged.  If \"enabled\" is omitted and only \"budgetConfiguration\" is provided, \"enabled\" defaults to false — budget automation will not be activated.  To activate budget automation, \"enabled\" must be explicitly set to true along with a valid \"budgetConfiguration\".  To deactivate, set \"enabled\" to false; \"budgetConfiguration\" can be omitted.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budgetConfiguration** | [**BudgetAutomationConfiguration**](BudgetAutomationConfiguration.md) |  |  [optional] |
|**enabled** | **Boolean** | Whether budget automation is enabled for this campaign. This field is always present in the response. |  [optional] |



