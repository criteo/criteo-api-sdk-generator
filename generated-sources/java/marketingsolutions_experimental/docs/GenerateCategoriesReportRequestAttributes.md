

# GenerateCategoriesReportRequestAttributes

This is the message defining the query for Categories report

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adsetId** | **String** | Optional adset id to filter on. The adset must already exist. If empty, all adsets will be fetched. |  [optional] |
|**advertiserIds** | **List&lt;String&gt;** | List of advertiser IDs to report on. The advertisers must already exist. At least one advertiser ID should be provided. |  |
|**campaignId** | **String** | Optional campaign id to filter on. The campaign must already exist. If empty, all campaign will be fetched. |  [optional] |
|**category** | **String** | Optional category to filter on. If empty, all categories will be fetched. |  [optional] |
|**domain** | **String** | Optional domain to filter on. If empty, all domains will be fetched. |  [optional] |
|**endDate** | **OffsetDateTime** | End date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. |  |
|**format** | [**FormatEnum**](#FormatEnum) | Optional file format of the generated report. |  [optional] |
|**shouldDisplayDomainDimension** | **Boolean** | Optionally specify if the domain dimension is displayed in the report. |  [optional] |
|**startDate** | **OffsetDateTime** | Start date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. Must be ≤ endDate. |  |
|**timezone** | **String** | Optional timezone used for the report. Timezone Database format (Tz). |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| CSV | &quot;csv&quot; |
| EXCEL | &quot;excel&quot; |
| XML | &quot;xml&quot; |
| JSON | &quot;json&quot; |



