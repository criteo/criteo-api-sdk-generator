

# RealTimeProductReportJobStatus

Represents the status of a real-time product report export job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exportId** | **String** | Unique ID (UUID) of the export job. |  [optional] |
|**message** | **String** | Optional informational message (e.g. rows_count&#x3D;1232). |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Export job status: PENDING, DONE, FAILURE, EXPIRED. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| PENDING | &quot;Pending&quot; |
| DONE | &quot;Done&quot; |
| FAILURE | &quot;Failure&quot; |
| EXPIRED | &quot;Expired&quot; |



