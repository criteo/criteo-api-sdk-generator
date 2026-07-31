# # AsyncRevenueReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **string[]** | Account ids to filter | [optional]
**activation_platforms** | **string[]** | Filter on the activation platform: CommerceMax, PrivateMarket | [optional]
**advertiser_types** | **string[]** | Filter on the type of advertiser: retailer, brand, seller | [optional]
**budget_models** | **string[]** | Filter on the budget model: CriteoBudget, RetailerBudget | [optional]
**buy_type** | **string** | Filter on buy type: Auction, Preferred Deals or Sponsorship | [optional]
**campaign_ids** | **string[]** | Campaign ids to filter | [optional]
**campaign_type** | **string** | Filter the type of campaigns to report on: sponsoredProducts or onSiteDisplays | [optional] [default to 'all']
**click_attribution_window** | **string** | Click attribution window | [optional] [default to 'none']
**click_match_level** | **string** | Click Match Level: Campaign, Same SKU, Same Category or Same Brand | [optional] [default to 'campaign']
**dimensions** | **string[]** | List of dimensions to report on | [optional]
**end_date** | **\DateTime** | End date |
**format** | **string** | Format of the output | [optional] [default to 'json']
**id** | **string** | Supply account id to report on | [optional]
**ids** | **string[]** | Supply account ids to report on | [optional]
**line_item_ids** | **string[]** | Line item ids to filter | [optional]
**media_type** | **string** | Filter on the type of media: unknown, display, video | [optional] [default to 'all']
**metrics** | **string[]** | List of metrics to report on | [optional]
**report_type** | **string** | Type of report, if no dimensions and metrics are provided, falls back to advertiser reportType | [optional]
**retailer_ids** | **string[]** | Retailer ids to filter | [optional]
**revenue_type** | **string** | Type of revenue | [optional]
**sales_channel** | **string** | Filter on specific sales channel: offline or online | [optional] [default to 'all']
**sku_relations** | **string[]** | Filter on sku relations: Same SKU, Same Parent SKU, Same Category, Same Brand or Same Seller | [optional]
**sold_by** | **string** | Filter on the seller: Indirect Sold, Direct Sold, Authorized Buyer or Private Market | [optional]
**start_date** | **\DateTime** | Start date |
**targeted_keyword_types** | **string[]** | Filter on targeted keyword type: unknown, generic, branded, conquesting | [optional]
**timezone** | **string** | Time zone : see criteo developer portal for supported time zones | [optional] [default to 'UTC']
**view_attribution_window** | **string** | View attribution window | [optional] [default to 'none']
**view_match_level** | **string** | View Match Level: Campaign, Same SKU, Same Category or Same Brand | [optional] [default to 'campaign']

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
