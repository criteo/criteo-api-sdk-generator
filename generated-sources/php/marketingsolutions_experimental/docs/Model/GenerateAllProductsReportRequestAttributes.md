# # GenerateAllProductsReportRequestAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_set_ids** | **string[]** | The list of ad set ids. | [optional]
**advertiser_ids** | **string[]** | The list of advertiser account IDs. |
**campaign_ids** | **string[]** | The list of campaign ids. | [optional]
**currency** | **string** | The currency used for the report. ISO 4217 code (three-letter capitals). | [optional] [default to 'EUR']
**dimensions** | **string[]** | The dimensions for the report. | [optional]
**end_date** | **\DateTime** | End date of the report. ISO 8601 date-time (UTC). Defaults to Now if not provided. | [optional]
**file_format** | **string** | The output file format. Supported: csv, json. | [optional] [default to 'csv']
**metrics** | **string[]** | The list of metrics to report. | [optional]
**seller_ids** | **string[]** | The list of seller ids. | [optional]
**start_date** | **\DateTime** | Start date of the report. ISO 8601 date-time (UTC). |
**timezone** | **string** | The timezone used for the report. Timezone Database format (Tz). | [optional] [default to 'UTC']

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
