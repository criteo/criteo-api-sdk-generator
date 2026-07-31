

# ExportStatusModel

Status returned for an asynchronous export job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exportId** | **String** | Export id (UUID), ex.: \&quot;e0893b6b-be25-477f-9ca3-e6e8c8ec9e30\&quot; |  [optional] |
|**message** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| PENDING | &quot;Pending&quot; |
| DONE | &quot;Done&quot; |
| FAILURE | &quot;Failure&quot; |
| EXPIRED | &quot;Expired&quot; |



