# # RealTimeProductReportJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_ids** | **string[]** | List of advertiser IDs to include in the export. Required. | [optional]
**campaign_ids** | **string[]** | Optional list of campaign IDs to filter the export. | [optional]
**currency** | **string** | Currency for the export. Default is _local currency_. | [optional]
**dimensions** | **string[]** | List of dimensions to include in the export. Default: [\&quot;advertiserId\&quot;, \&quot;campaignId\&quot;, \&quot;sellerId\&quot;, \&quot;productId\&quot;, \&quot;day\&quot;]. | [optional]
**end_date** | **\DateTime** | End of the reporting interval, in ISO‑8601 date‑time format (UTC). Mutually exclusive with lookbackWindow.  If omitted while startDate is provided, defaults to the current time. | [optional]
**file_format** | **string** | The file format for the export. Allowed values: \&quot;csv\&quot;, \&quot;json\&quot;. Default is \&quot;csv\&quot;. | [optional]
**lookback_window** | **int** | Lookback window in minutes. Default is 60. | [optional]
**metrics** | **string[]** | List of metrics to include in the export. Default: [\&quot;clicks\&quot;, \&quot;displays\&quot;, \&quot;cost\&quot;]. | [optional]
**partner_ids** | **string[]** | Optional list of partner IDs to filter the export. | [optional]
**seller_ids** | **string[]** | Optional list of seller IDs to filter the export. | [optional]
**start_date** | **\DateTime** | Start of the reporting interval, in ISO‑8601 date‑time format (UTC). Mutually exclusive with lookbackWindow. | [optional]
**timezone** | **string** | Timezone for the export. Default is \&quot;UTC\&quot;. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
