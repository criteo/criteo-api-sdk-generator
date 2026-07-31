

# PartnerBillingReportRequestV1

The request object of a Partner Billing Report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountIds** | **List&lt;String&gt;** | On which accounts the report is created. |  [optional] |
|**endDate** | **LocalDate** | End date of the report (ISO 8601 format, e.g. YYYY-MM-DD). |  |
|**format** | [**FormatEnum**](#FormatEnum) | Format type of the report. |  [optional] |
|**retailerIds** | **List&lt;Integer&gt;** | On which retailers the report is created. |  [optional] |
|**startDate** | **LocalDate** | Start date of the report (ISO 8601 format, e.g. YYYY-MM-DD). |  |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| JSON | &quot;json&quot; |
| CSV | &quot;csv&quot; |



