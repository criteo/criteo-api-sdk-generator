# # CampaignDailyBudgetOverride

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **string** | The number of DAYs that the override is active from StartDate, e.g. \&quot;1D\&quot;. Must end with &#39;D&#39; or &#39;d&#39;. |
**max_daily_spend** | **float** | Daily budget override maximum daily spend amount. |
**start_date** | **\DateTime** | Daily budget override start date, format \&quot;yyyy-MM-dd\&quot;. If it is null, the StartDate would be the following date of the last item in the override sequence. | [optional]
**status** | **string** | Daily budget override computed status. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
