

# ExternalCatalogStatus

The status of an asynchronous request to generate a catalog

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The time this catalog was created. Represented as a UTC ISO8601 string. |  |
|**currency** | **String** | An ISO4217 representation of the currency products are listed under in this catalog. |  |
|**fileSizeBytes** | **Integer** | The size of this catalog in bytes. Available when this catalog reaches a success status. |  |
|**md5Checksum** | **String** | An MD5 checksum of the catalog for use in confirming complete and uncorrupted retrieval.  Available when this catalog reaches a success status. |  |
|**message** | **String** | An optional information message intended for developer consumption. |  |
|**rowCount** | **Integer** | An indication of the number of products contained in this catalog. Available when  this catalog reaches a success status. |  |
|**status** | [**StatusEnum**](#StatusEnum) | An enumeration of the status of the catalog. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| PENDING | &quot;pending&quot; |
| SUCCESS | &quot;success&quot; |
| FAILURE | &quot;failure&quot; |
| EXPIRED | &quot;expired&quot; |



