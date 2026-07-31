# # AdLevelReportRequestAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adset_ids** | **string[]** | Optional filter on ad set IDs. Also satisfies the ad-set-scope requirement for the AdGroupName, ProductId, and AdId breakdown dimensions: if any of those are requested, either adsetIds must be non-empty or AdsetId must also be included in dimensions. | [optional]
**advertiser_ids** | **string[]** | List of advertiser IDs to report on. Between 1 and 5 advertiser IDs can be provided. |
**dimensions** | **string[]** | List of breakdown dimensions for the report. At least one dimension must be provided; nothing is added to the response unless explicitly requested here. |
**end_date** | **\DateTime** | End date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. |
**format** | **string** | Optional file format of the generated report. Only csv and json are currently supported by this endpoint — excel and xml requests are rejected with a 400 error. | [optional] [default to 'json']
**metrics** | **string[]** | List of metrics to return. At least one metric must be provided. AdGroupContextHint and AdGroupDescription require AdGroupName in dimensions; ProductName requires ProductId; AdTitle and AdCopy require AdId. |
**start_date** | **\DateTime** | Start date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. Must be less than or equal to endDate. |
**timezone** | **string** | Optional timezone used for the report. Timezone Database (Tz) format. | [optional] [default to 'UTC']

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
