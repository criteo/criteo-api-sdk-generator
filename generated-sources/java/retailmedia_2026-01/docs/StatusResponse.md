

# StatusResponse

Status of an async report request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** |  |  [optional] |
|**expiresAt** | **String** |  |  [optional] |
|**fileSizeBytes** | **Long** |  |  [optional] |
|**id** | **String** |  |  [optional] |
|**md5CheckSum** | **String** |  |  [optional] |
|**message** | **String** |  |  [optional] |
|**rowCount** | **Integer** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| SUCCESS | &quot;success&quot; |
| FAILURE | &quot;failure&quot; |
| EXPIRED | &quot;expired&quot; |



