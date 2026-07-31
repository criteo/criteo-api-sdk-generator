

# RmAudienceSegmentEntityV1

Set of rules that defines specific people to target.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Account associated to the segment |  [optional] |
|**channels** | [**List&lt;ChannelsEnum&gt;**](#List&lt;ChannelsEnum&gt;) | Channels associated to the segment (read-only) |  [optional] |
|**contactList** | [**RmContactListV1**](RmContactListV1.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | ISO-8601 timestamp in UTC of segment creation (read-only) |  [optional] |
|**createdById** | **String** | User that created the segment |  [optional] |
|**description** | **String** | Description of the segment |  [optional] |
|**events** | [**RmEventsV1**](RmEventsV1.md) |  |  [optional] |
|**name** | **String** | Name of the segment |  [optional] |
|**retailerId** | **String** | Retailer  associated to the segment |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of segment (read-only) |  [optional] |
|**updatedAt** | **OffsetDateTime** | ISO-8601 timestamp in UTC of segment update (read-only) |  [optional] |



## Enum: List&lt;ChannelsEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| ONSITE | &quot;Onsite&quot; |
| OFFSITE | &quot;Offsite&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| CONTACTLIST | &quot;ContactList&quot; |
| EVENTS | &quot;Events&quot; |



