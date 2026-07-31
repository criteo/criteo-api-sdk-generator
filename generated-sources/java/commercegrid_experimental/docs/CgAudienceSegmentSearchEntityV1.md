

# CgAudienceSegmentSearchEntityV1

Available filters to perform a search on audience segments. If present, the filters are AND'ed together when applied.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audienceSegmentIds** | **List&lt;String&gt;** | List of segment ids |  [optional] |
|**audienceSegmentTypes** | [**List&lt;AudienceSegmentTypesEnum&gt;**](#List&lt;AudienceSegmentTypesEnum&gt;) | List of segment types |  [optional] |
|**dataProviderIds** | **List&lt;String&gt;** | List of data provider ids |  [optional] |
|**remoteIds** | **List&lt;String&gt;** | List of ids used to identify the segment in the data provider&#39;s system |  [optional] |



## Enum: List&lt;AudienceSegmentTypesEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| CONTACTLIST | &quot;ContactList&quot; |



