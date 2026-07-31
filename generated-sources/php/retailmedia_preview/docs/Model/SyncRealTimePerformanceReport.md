# # SyncRealTimePerformanceReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **string[]** | Account ids to filter (plural; base has AccountId for single account). | [optional]
**campaign_ids** | **string[]** | Campaign ids to filter. | [optional]
**dimensions** | **string[]** | List of dimensions to report on (real-time: at least one required). Only the supported dimension values are valid. | [optional]
**end_date** | **\DateTime** | Optional end date/time (inclusive in the request timezone). If empty or not provided, no end date filter is applied.  When provided, used as the inclusive upper bound for the report range.  Hides base Report.EndDate so this report can treat end date as optional (no [Required]). | [optional]
**line_item_ids** | **string[]** | Line item ids to filter. | [optional]
**metrics** | **string[]** | List of metrics to report on (real-time: at least one required). Only the supported metric values are valid. | [optional]
**retailer_ids** | **string[]** | Retailer ids to filter. This is not used for security, so no need to check for &gt; 0 elements | [optional]
**start_date** | **\DateTime** | Start date (real-time: must be within the last 7 days). |
**timezone** | **string** | Time zone : see criteo developer portal for supported time zones | [optional] [default to 'UTC']

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
