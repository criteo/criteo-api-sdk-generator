

# CampaignMonthlyBudgetOverride

Campaign monthly budget override.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**duration** | **String** | The number of MONTHs that the override is active from StartMonth, e.g. \&quot;1M\&quot;. Must end with &#39;M&#39; or &#39;m&#39;. |  |
|**maxMonthlySpend** | **Double** | Monthly budget override maximum monthly spend amount. |  |
|**startMonth** | **OffsetDateTime** | Monthly budget override start month, format \&quot;yyyy-MM\&quot;. If it is null, the StartMonth would be the following month of the last item in the override sequence. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Monthly budget override computed status. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| EXPIRED | &quot;Expired&quot; |
| ACTIVE | &quot;Active&quot; |
| UPCOMING | &quot;Upcoming&quot; |



