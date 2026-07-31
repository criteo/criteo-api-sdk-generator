# # GenerateStatisticsReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_set_ids** | **string[]** | List of advertiser IDs to report on, provided as a single comma-separated string (e.g., \&quot;123,456,789\&quot;). The advertisers must already exist. If empty, all advertisers will be used. | [optional]
**ad_set_names** | **string[]** | The list of ad sets names. If empty, all the adSets will be fetched. | [optional]
**ad_set_status** | **string[]** | The list of ad sets status. If empty, all the adSets will be fetched. | [optional]
**advertiser_ids** | **string[]** | The list of advertiser ids |
**currency** | **string** | The currency used for the report. ISO 4217 code (three-letter capitals). | [optional]
**dimensions** | **string[]** | The dimensions for the report. |
**end_date** | **\DateTime** | End date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. |
**metrics** | **string[]** | The list of metrics to report. |
**start_date** | **\DateTime** | Start date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. |
**timezone** | **string** | Optional timezone used for the report. Timezone Database format (Tz). | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
