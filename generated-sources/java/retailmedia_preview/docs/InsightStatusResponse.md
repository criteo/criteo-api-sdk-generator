

# InsightStatusResponse

Status of an async insight request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** |  |  [optional] |
|**expiresAt** | **String** |  |  [optional] |
|**fileSizeBytes** | **Long** |  |  [optional] |
|**md5CheckSum** | **String** |  |  [optional] |
|**message** | **String** |  |  [optional] |
|**rowCount** | **Integer** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of an async insight request |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| PENDING | &quot;Pending&quot; |
| SUCCESS | &quot;Success&quot; |
| FAILURE | &quot;Failure&quot; |
| EXPIRED | &quot;Expired&quot; |
| INVALIDATED | &quot;Invalidated&quot; |



