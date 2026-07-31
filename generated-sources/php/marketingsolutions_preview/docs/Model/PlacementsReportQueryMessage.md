# # PlacementsReportQueryMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adset_ids** | **string** | Optional list of ad set IDs to filter on. The ad sets must already exist. If empty, all ad sets will be included. | [optional]
**advertiser_ids** | **string** | List of advertiser IDs to report on, provided as a single comma-separated string (e.g., \&quot;123,456,789\&quot;). The advertisers must already exist. If empty, all advertisers will be used. |
**campaign_ids** | **string** | Optional list of campaign IDs to filter on. The campaigns must already exist. If empty, all campaigns will be included. | [optional]
**currency** | **string** | The currency used for the report. ISO 4217 code (three-letter capitals). |
**dimensions** | **string[]** | List of dimensions for the report. At least one dimension should be provided. |
**disclosed** | **bool** | Optionally returns disclosed or undisclosed placements. | [optional] [default to true]
**end_date** | **\DateTime** | End date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. |
**environment** | **string** | Optional type of environment to filter on. If empty, all environments will be included. | [optional]
**format** | **string** | Optional file format of the generated report. | [optional] [default to 'json']
**metrics** | **string[]** | List of metrics for the report. At least one dimension should be provided. |
**placement** | **string** | Optional filter on a specific placement domain name. If empty, all placements will be included. | [optional]
**start_date** | **\DateTime** | Start date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. Must be ≤ endDate. |
**timezone** | **string** | Optional timezone used for the report. Timezone Database format (Tz). | [optional] [default to 'UTC']

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
