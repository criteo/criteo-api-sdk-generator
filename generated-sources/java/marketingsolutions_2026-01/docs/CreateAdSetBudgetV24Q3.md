

# CreateAdSetBudgetV24Q3

ad set budget create model

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budgetAmount** | **Double** |  |  [optional] |
|**budgetDeliverySmoothing** | [**BudgetDeliverySmoothingEnum**](#BudgetDeliverySmoothingEnum) |  |  [optional] |
|**budgetDeliveryWeek** | [**BudgetDeliveryWeekEnum**](#BudgetDeliveryWeekEnum) |  |  [optional] |
|**budgetRenewal** | [**BudgetRenewalEnum**](#BudgetRenewalEnum) |  |  [optional] |
|**budgetStrategy** | [**BudgetStrategyEnum**](#BudgetStrategyEnum) |  |  |



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



