

# CreateAdSetBudgetV26Q1

Budget create model for an ad set.  For \"capped\": budgetAmount (required, non-null), budgetRenewal (required, not \"undefined\"), and budgetDeliverySmoothing (required) must all be provided.  pacingBehavior is optional; \"targetAverageDailyBudget\" is only supported for capped, standard, monthly budgets.  For \"uncapped\": budgetAmount must be null, budgetRenewal must be \"undefined\", budgetDeliverySmoothing, budgetDeliveryWeek, and pacingBehavior must be omitted or \"undefined\".  For marketing campaigns with budget automation enabled, omit this object.  In that case, the ad set budget is initialized from the marketing campaign spend limit amount and renewal period.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budgetAmount** | **Double** | Maximum budget amount in the advertiser&#39;s currency per renewal period. Required non-null when capped. Must be null when uncapped. |  [optional] |
|**budgetDeliverySmoothing** | [**BudgetDeliverySmoothingEnum**](#BudgetDeliverySmoothingEnum) | Pacing strategy for spending the budget within a renewal period. Only applicable when budgetStrategy is \&quot;capped\&quot;.  - \&quot;accelerated\&quot;: spend pacing is based on delivery efficiency rather than the full budget period.  - \&quot;standard\&quot;: spread spending evenly over the renewal period.  When budgetStrategy is \&quot;uncapped\&quot;, this field is not set (null in read responses, omit in create/patch requests). |  [optional] |
|**budgetDeliveryWeek** | [**BudgetDeliveryWeekEnum**](#BudgetDeliveryWeekEnum) | Defines which day-of-week boundaries are used for weekly budget renewal. Only applicable when budgetStrategy is \&quot;capped\&quot;, budgetRenewal is \&quot;weekly\&quot;, and budgetDeliverySmoothing is \&quot;standard\&quot;.  - \&quot;mondayToSunday\&quot;, \&quot;tuesdayToMonday\&quot;, etc.: the day range over which the weekly budget is paced. Changing this value on the active budget also propagates to all scheduled budgets of the same ad set.  - \&quot;undefined\&quot;: used when budgetStrategy is \&quot;uncapped\&quot;, when budgetRenewal is not \&quot;weekly\&quot;, or when budgetDeliverySmoothing is \&quot;accelerated\&quot;. |  [optional] |
|**budgetRenewal** | [**BudgetRenewalEnum**](#BudgetRenewalEnum) | The period over which the budget is spent.  - \&quot;daily\&quot;, \&quot;monthly\&quot;, \&quot;weekly\&quot;: budget resets at the start of each period.  - \&quot;lifetime\&quot;: budget covers the entire ad set duration without resetting.  - \&quot;undefined\&quot;: only used when budgetStrategy is \&quot;uncapped\&quot; (no renewal applies). Required for capped budgets (must not be \&quot;undefined\&quot;). |  [optional] |
|**budgetStrategy** | [**BudgetStrategyEnum**](#BudgetStrategyEnum) | Controls whether the ad set has a spending limit.  - \&quot;capped\&quot;: spending is limited to budgetAmount. Requires budgetAmount (non-null), budgetRenewal (not \&quot;undefined\&quot;), and budgetDeliverySmoothing (not null).  - \&quot;uncapped\&quot;: no spending limit. budgetAmount is null, budgetRenewal is \&quot;undefined\&quot;, and budgetDeliverySmoothing is null. |  |
|**pacingBehavior** | [**PacingBehaviorEnum**](#PacingBehaviorEnum) | Controls how a standard capped budget is paced.  - \&quot;targetFullBudget\&quot;: spend toward the full budget amount within the renewal period.  - \&quot;targetAverageDailyBudget\&quot;: spend toward an average daily amount. Only supported for capped, standard, monthly budgets.  - \&quot;undefined\&quot;: no explicit pacing behavior. Required for uncapped budgets and accelerated budgets. |  [optional] |



## Enum: BudgetDeliverySmoothingEnum

| Name | Value |
|---- | -----|
| ACCELERATED | &quot;accelerated&quot; |
| STANDARD | &quot;standard&quot; |



## Enum: BudgetDeliveryWeekEnum

| Name | Value |
|---- | -----|
| UNDEFINED | &quot;undefined&quot; |
| MONDAYTOSUNDAY | &quot;mondayToSunday&quot; |
| TUESDAYTOMONDAY | &quot;tuesdayToMonday&quot; |
| WEDNESDAYTOTUESDAY | &quot;wednesdayToTuesday&quot; |
| THURSDAYTOWEDNESDAY | &quot;thursdayToWednesday&quot; |
| FRIDAYTOTHURSDAY | &quot;fridayToThursday&quot; |
| SATURDAYTOFRIDAY | &quot;saturdayToFriday&quot; |
| SUNDAYTOSATURDAY | &quot;sundayToSaturday&quot; |



## Enum: BudgetRenewalEnum

| Name | Value |
|---- | -----|
| UNDEFINED | &quot;undefined&quot; |
| DAILY | &quot;daily&quot; |
| MONTHLY | &quot;monthly&quot; |
| LIFETIME | &quot;lifetime&quot; |
| WEEKLY | &quot;weekly&quot; |



## Enum: BudgetStrategyEnum

| Name | Value |
|---- | -----|
| CAPPED | &quot;capped&quot; |
| UNCAPPED | &quot;uncapped&quot; |



## Enum: PacingBehaviorEnum

| Name | Value |
|---- | -----|
| UNDEFINED | &quot;undefined&quot; |
| TARGETFULLBUDGET | &quot;targetFullBudget&quot; |
| TARGETAVERAGEDAILYBUDGET | &quot;targetAverageDailyBudget&quot; |



