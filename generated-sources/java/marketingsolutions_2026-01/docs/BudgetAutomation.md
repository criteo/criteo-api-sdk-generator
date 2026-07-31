

# BudgetAutomation

Budget automation, lets users configure budgets once at the campaign level while Criteo dynamically routes spend toward the best-performing ad sets.  If \"enabled\" is omitted and only \"budgetConfiguration\" is provided, \"enabled\" defaults to false — budget automation will not be activated.  To activate budget automation at creation, \"enabled\" must be explicitly set to true along with a valid \"budgetConfiguration\".  If the entire \"budgetAutomation\" object is omitted from the create request, the campaign is created with budget automation disabled.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budgetConfiguration** | [**BudgetAutomationConfiguration**](BudgetAutomationConfiguration.md) |  |  [optional] |
|**enabled** | **Boolean** | Whether budget automation is active for this marketing campaign.  - true: budget automation is enabled and \&quot;budgetConfiguration\&quot; must be provided with a valid objective.  - false (default when omitted): budget automation is disabled; \&quot;budgetConfiguration\&quot; is ignored if provided. |  [optional] |



