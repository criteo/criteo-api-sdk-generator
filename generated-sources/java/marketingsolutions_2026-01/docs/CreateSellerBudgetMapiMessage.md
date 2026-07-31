

# CreateSellerBudgetMapiMessage

Data used to create a seller's budget

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **String** | Budget amount as a string (e.g. &#39;100.50&#39;) |  [optional] |
|**budgetType** | **String** | Type of budget: &#39;Daily&#39; (daily cap), &#39;Capped&#39; (lifetime with fixed amount), or &#39;Uncapped&#39; (lifetime with no limit) |  [optional] |
|**campaignIds** | **List&lt;Integer&gt;** | List of campaign IDs this budget applies to |  [optional] |
|**endDate** | **String** | Budget end date as a string (format: YYYY-MM-DD), or empty string for open-ended |  [optional] |
|**sellerId** | **String** | Identifier of the seller this budget is for |  [optional] |
|**startDate** | **OffsetDateTime** | Budget start date. Time component is ignored. |  [optional] |



