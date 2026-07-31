

# BudgetAutomationConfiguration

Configuration for budget automation. Only meaningful when \"enabled\" is true.  When \"enabled\" is false or omitted, this field is ignored.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adSetObjectives** | [**AdSetObjectivesEnum**](#AdSetObjectivesEnum) | The ad set optimization objective for budget automation. Determines how the automated budget allocates spend across ad sets in the campaign.  - \&quot;conversions\&quot;: optimize for conversion events.  - \&quot;revenue\&quot;: optimize for revenue.  - \&quot;visits\&quot;: optimize for site visits.  - \&quot;videoViews\&quot;: optimize for completed video views. |  [optional] |



## Enum: AdSetObjectivesEnum

| Name | Value |
|---- | -----|
| CONVERSIONS | &quot;conversions&quot; |
| REVENUE | &quot;revenue&quot; |
| VISITS | &quot;visits&quot; |
| VIDEOVIEWS | &quot;videoViews&quot; |



