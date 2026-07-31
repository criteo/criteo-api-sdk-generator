# # AsyncCampaignsReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_platforms** | **string[]** | Filter on the activation platform: CommerceMax, PrivateMarket | [optional]
**budget_models** | **string[]** | Filter on the budget model: CriteoBudget, RetailerBudget | [optional]
**buy_types** | **string[]** | Filter on the buy type: auction, preferredDeals, sponsorship | [optional]
**campaign_type** | **string** | Filter the type of campaigns to report on: sponsoredProducts or onSiteDisplays | [optional] [default to 'all']
**click_attribution_window** | **string** | Click attribution window | [optional] [default to 'none']
**dimensions** | **string[]** | List of dimensions to report on | [optional]
**end_date** | **\DateTime** | End date |
**format** | **string** | Format of the output | [optional] [default to 'json-compact']
**id** | **string** | Campaign id to report on | [optional]
**ids** | **string[]** | Campaign ids to report on | [optional]
**media_type** | **string** | Filter on the type of media: unknown, display, video | [optional] [default to 'all']
**metrics** | **string[]** | List of metrics to report on | [optional]
**report_type** | **string** | Type of report, if no dimensions and metrics are provided, falls back to summary reportType | [optional] [default to 'summary']
**sales_channel** | **string** | Filter on specific sales channel: offline or online | [optional] [default to 'all']
**search_term_targetings** | **string[]** | Filter on the type of search term targeting: unknown, automatic, manual | [optional]
**search_term_types** | **string[]** | Filter on the type of search term type: unknown, searched, entered | [optional]
**start_date** | **\DateTime** | Start date |
**targeted_keyword_types** | **string[]** | Filter on targeted keyword type: unknown, generic, branded, conquesting | [optional]
**timezone** | **string** | Time zone : see criteo developer portal for supported time zones | [optional] [default to 'UTC']
**view_attribution_window** | **string** | View attribution window | [optional] [default to 'none']

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
