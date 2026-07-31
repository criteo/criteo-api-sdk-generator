

# PartnerBillingReportStatusV1

Status info of a Partner Billing Report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The date when the report request is created. |  |
|**errorMessage** | **String** | Possible error message along with the status. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the report. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| SUCCESS | &quot;success&quot; |
| FAILED | &quot;failed&quot; |
| EXPIRED | &quot;expired&quot; |



