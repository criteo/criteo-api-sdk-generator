

# RmAudienceEntityV1

Audience of people of interest for a marketer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Account associated to the audience |  [optional] |
|**algebra** | [**RmAlgebraNodeV1**](RmAlgebraNodeV1.md) |  |  [optional] |
|**channels** | [**List&lt;ChannelsEnum&gt;**](#List&lt;ChannelsEnum&gt;) | Channels associated to the audience (read-only) |  [optional] |
|**createdAt** | **OffsetDateTime** | ISO-8601 timestamp in UTC of audience creation (read-only) |  [optional] |
|**createdById** | **String** | User that created the audience |  [optional] |
|**description** | **String** | Description of the audience |  [optional] |
|**name** | **String** | Name of the audience |  [optional] |
|**retailerId** | **String** | Retailer  associated to the audience |  [optional] |
|**updatedAt** | **OffsetDateTime** | ISO-8601 timestamp in UTC of audience update (read-only) |  [optional] |



## Enum: List&lt;ChannelsEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| ONSITE | &quot;Onsite&quot; |
| OFFSITE | &quot;Offsite&quot; |



