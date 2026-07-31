

# CgAudienceSegmentEntityV1

Set of rules that defines specific people to target.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contactList** | **Object** | Settings to target users with your contact lists. |  [optional] |
|**createdAt** | **OffsetDateTime** | ISO-8601 timestamp in UTC of segment creation (read-only) |  [optional] |
|**dataProviderId** | **String** | Data provider associated to the segment (read-only) |  [optional] |
|**description** | **String** | Description of the segment |  [optional] |
|**name** | **String** | Name of the segment |  [optional] |
|**remoteId** | **String** | The ID used to identify the segment in the data provider&#39;s system (read-only) |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of segment (read-only) |  [optional] |
|**updatedAt** | **OffsetDateTime** | ISO-8601 timestamp in UTC of segment update (read-only) |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| CONTACTLIST | &quot;ContactList&quot; |



