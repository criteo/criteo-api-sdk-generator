# # TransactionsReportQueryMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_ids** | **string** | List of advertiser IDs to report on, provided as a single comma-separated string (e.g., \&quot;123,456,789\&quot;). The advertisers must already exist. If empty, all advertisers will be used. |
**currency** | **string** | The currency used for the report. ISO 4217 code (three-letter capitals). |
**end_date** | **\DateTime** | End date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. |
**event_type** | **string** | Optional event type to filter on. If empty, all event types will be included. | [optional]
**format** | **string** | Optional file format of the generated report. | [optional] [default to 'json']
**start_date** | **\DateTime** | Start date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. Must be ≤ endDate. |
**timezone** | **string** | Optional timezone used for the report. Timezone Database format (Tz). | [optional] [default to 'UTC']

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
