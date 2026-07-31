

# SellerBudgetMessage

A budget defines spending constraints for a seller across one or more campaigns. Each seller can have one active budget per time period.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Double** | Budget amount in the advertiser&#39;s currency |  [optional] |
|**budgetType** | **String** | Type of budget: &#39;Daily&#39; (daily cap), &#39;Capped&#39; (lifetime with fixed amount), or &#39;Uncapped&#39; (lifetime with no limit) |  [optional] |
|**campaignIds** | **List&lt;Integer&gt;** | List of campaign IDs this budget applies to |  [optional] |
|**endDate** | **String** | End date of the budget period (format: YYYY-MM-DD), or empty string if open-ended |  [optional] |
|**id** | **String** | Unique budget identifier |  [optional] |
|**isSuspended** | **Boolean** | Whether the budget has been manually suspended by the partner |  [optional] |
|**sellerId** | **String** | Identifier of the seller this budget belongs to |  [optional] |
|**spend** | **Double** | Amount spent against this budget so far, or null if not available |  [optional] |
|**startDate** | **LocalDate** | Start date of the budget period (format: YYYY-MM-DD) |  [optional] |
|**status** | **SellerBudgetStatusV2** |  |  [optional] |



