# # CreateSellerBudgetMapiMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **string** | Budget amount as a string (e.g. &#39;100.50&#39;) | [optional]
**budget_type** | **string** | Type of budget: &#39;Daily&#39; (daily cap), &#39;Capped&#39; (lifetime with fixed amount), or &#39;Uncapped&#39; (lifetime with no limit) | [optional]
**campaign_ids** | **int[]** | List of campaign IDs this budget applies to | [optional]
**end_date** | **string** | Budget end date as a string (format: YYYY-MM-DD), or empty string for open-ended | [optional]
**seller_id** | **string** | Identifier of the seller this budget is for | [optional]
**start_date** | **\DateTime** | Budget start date. Time component is ignored. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
