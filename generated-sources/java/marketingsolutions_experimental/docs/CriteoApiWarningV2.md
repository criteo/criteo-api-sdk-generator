

# CriteoApiWarningV2

Criteo API response warning

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | A machine-readable error code string in kabab-case. Unique across Criteo |  [optional] |
|**detail** | **String** | A human-readable explanation specific to this occurrence of the problem. |  [optional] |
|**instance** | **String** | A URI reference that identifies the specific occurrence of the problem |  [optional] |
|**title** | **String** | A short, human-readable remarks of the problem type. |  [optional] |
|**traceId** | **String** | The correlation ID provided by the gateway |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | A machine-readable code specifying error category |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| INTERNAL_ERROR | &quot;internal-error&quot; |
| DEPRECATED_FIELD | &quot;deprecated-field&quot; |
| ENDPOINT_DEPRECATED | &quot;endpoint-deprecated&quot; |
| REQUIRED_FIELD | &quot;required-field&quot; |
| INVALID_DATE_FORMAT | &quot;invalid-date-format&quot; |
| INVALID | &quot;invalid&quot; |
| INVALID_RANGED | &quot;invalid-ranged&quot; |
| INVALID_TIMESPAN | &quot;invalid-timespan&quot; |
| PERMISSION_DENIED | &quot;permission-denied&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACCESS_CONTROL | &quot;access-control&quot; |
| AUTHENTICATION | &quot;authentication&quot; |
| AUTHORIZATION | &quot;authorization&quot; |
| AVAILABILITY | &quot;availability&quot; |
| DEPRECATION | &quot;deprecation&quot; |
| QUOTA | &quot;quota&quot; |
| VALIDATION | &quot;validation&quot; |



