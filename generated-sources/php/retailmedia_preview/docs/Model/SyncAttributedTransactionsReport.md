# # SyncAttributedTransactionsReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **string** | Account id to report on |
**campaign_ids** | **string[]** | Campaign ids to filter | [optional]
**campaign_type** | **string** | Filter the type of campaigns to report on: sponsoredProducts or onSiteDisplays | [optional] [default to 'all']
**click_attribution_window** | **string** | Click attribution window | [optional] [default to 'none']
**dimensions** | **string[]** | List of dimensions to report on | [optional]
**end_date** | **\DateTime** | End date |
**line_item_ids** | **string[]** | Line item ids to filter | [optional]
**media_type** | **string** | Filter on the type of media: unknown, display, video | [optional] [default to 'all']
**metrics** | **string[]** | List of metrics to report on | [optional]
**sales_channel** | **string** | Filter on specific sales channel: offline or online | [optional] [default to 'all']
**start_date** | **\DateTime** | Start date |
**timezone** | **string** | Time zone : see criteo developer portal for supported time zones | [optional] [default to 'UTC']
**view_attribution_window** | **string** | View attribution window | [optional] [default to 'none']

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
