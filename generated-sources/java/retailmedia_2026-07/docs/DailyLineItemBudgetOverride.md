

# DailyLineItemBudgetOverride

The details for a daily budget override

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**duration** | **String** | The number of DAYs that the override is active from StartDate, e.g. \&quot;1D\&quot;. Must end with &#39;D&#39; or &#39;d&#39;. |  |
|**maxDailySpend** | **Double** | Daily budget override maximum daily spend amount. |  [optional] |
|**startDate** | **OffsetDateTime** | Daily budget override start date, format \&quot;yyyy-MM-dd\&quot;. If it is null, the StartDate would be the following date of the last item in the override sequence. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Daily budget override computed status. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| EXPIRED | &quot;Expired&quot; |
| ACTIVE | &quot;Active&quot; |
| UPCOMING | &quot;Upcoming&quot; |



