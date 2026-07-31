

# TransactionsReportQueryMessage

This is the message defining the query for Transaction report

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserIds** | **String** | List of advertiser IDs to report on, provided as a single comma-separated string (e.g., \&quot;123,456,789\&quot;). The advertisers must already exist. If empty, all advertisers will be used. |  |
|**currency** | **String** | The currency used for the report. ISO 4217 code (three-letter capitals). |  |
|**endDate** | **OffsetDateTime** | End date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. |  |
|**eventType** | [**EventTypeEnum**](#EventTypeEnum) | Optional event type to filter on. If empty, all event types will be included. |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | Optional file format of the generated report. |  [optional] |
|**startDate** | **OffsetDateTime** | Start date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. Must be ≤ endDate. |  |
|**timezone** | **String** | Optional timezone used for the report. Timezone Database format (Tz). |  [optional] |



## Enum: EventTypeEnum

| Name | Value |
|---- | -----|
| CLICK | &quot;Click&quot; |
| DISPLAY | &quot;Display&quot; |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| CSV | &quot;csv&quot; |
| EXCEL | &quot;excel&quot; |
| XML | &quot;xml&quot; |
| JSON | &quot;json&quot; |



