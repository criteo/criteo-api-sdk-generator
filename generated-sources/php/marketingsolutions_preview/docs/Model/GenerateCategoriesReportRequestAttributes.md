# # GenerateCategoriesReportRequestAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adset_id** | **string** | Optional adset id to filter on. The adset must already exist. If empty, all adsets will be fetched. | [optional]
**advertiser_ids** | **string[]** | List of advertiser IDs to report on. The advertisers must already exist. At least one advertiser ID should be provided. |
**campaign_id** | **string** | Optional campaign id to filter on. The campaign must already exist. If empty, all campaign will be fetched. | [optional]
**category** | **string** | Optional category to filter on. If empty, all categories will be fetched. | [optional]
**domain** | **string** | Optional domain to filter on. If empty, all domains will be fetched. | [optional]
**end_date** | **\DateTime** | End date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. |
**format** | **string** | Optional file format of the generated report. | [optional] [default to 'json']
**should_display_domain_dimension** | **bool** | Optionally specify if the domain dimension is displayed in the report. | [optional] [default to true]
**start_date** | **\DateTime** | Start date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. Must be ≤ endDate. |
**timezone** | **string** | Optional timezone used for the report. Timezone Database format (Tz). | [optional] [default to 'UTC']

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
