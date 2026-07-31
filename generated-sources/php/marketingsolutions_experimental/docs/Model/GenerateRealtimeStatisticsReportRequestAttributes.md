# # GenerateRealtimeStatisticsReportRequestAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adset_ids** | **string[]** | Optional list of ad set IDs to filter on. The ad sets must already exist. If empty, all ad sets will be included. | [optional]
**advertiser_ids** | **string[]** | List of advertiser IDs to report on. The advertisers must already exist. Between 1 and 10 advertiser IDs can be provided. |
**campaign_ids** | **string[]** | Optional list of campaign IDs to filter on. The campaigns must already exist. If empty, all campaigns will be included. | [optional]
**currency** | **string** | The currency used for the report. ISO 4217 code (three-letter capitals). | [optional] [default to 'EUR']
**dimensions** | **string[]** | List of dimensions for the report. If not included, the default list of dimensions will be used. | [optional]
**lookback_window** | **int** | Optional number of hours to consider in the past. | [optional] [default to 12]
**metrics** | **string[]** | List of metrics for the report. If included, at least one metric should be provided. | [optional]
**timezone** | **string** | Optional timezone used for the report. | [optional] [default to 'UTC']

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
