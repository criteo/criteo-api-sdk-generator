# # SellerBudgetMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Budget amount in the advertiser&#39;s currency | [optional]
**budget_type** | **string** | Type of budget: &#39;Daily&#39; (daily cap), &#39;Capped&#39; (lifetime with fixed amount), or &#39;Uncapped&#39; (lifetime with no limit) | [optional]
**campaign_ids** | **int[]** | List of campaign IDs this budget applies to | [optional]
**end_date** | **string** | End date of the budget period (format: YYYY-MM-DD), or empty string if open-ended | [optional]
**id** | **string** | Unique budget identifier | [optional]
**is_suspended** | **bool** | Whether the budget has been manually suspended by the partner | [optional]
**seller_id** | **string** | Identifier of the seller this budget belongs to | [optional]
**spend** | **float** | Amount spent against this budget so far, or null if not available | [optional]
**start_date** | **\DateTime** | Start date of the budget period (format: YYYY-MM-DD) | [optional]
**status** | [**\criteo\api\marketingsolutions\v2027_01\Model\SellerBudgetStatusV2**](SellerBudgetStatusV2.md) |  | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
