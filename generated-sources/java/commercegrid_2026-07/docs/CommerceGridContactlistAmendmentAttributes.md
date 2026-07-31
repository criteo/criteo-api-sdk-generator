

# CommerceGridContactlistAmendmentAttributes

Attributes of Commerce Grid contact list amendment

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**identifiers** | **List&lt;String&gt;** | The users to add or remove, each in the schema specified |  |
|**identifierType** | [**IdentifierTypeEnum**](#IdentifierTypeEnum) | What type of identifiers are used |  [optional] |
|**operation** | [**OperationEnum**](#OperationEnum) | Whether to add or remove users |  |



## Enum: IdentifierTypeEnum

| Name | Value |
|---- | -----|
| EMAIL | &quot;Email&quot; |
| MADID | &quot;MadId&quot; |
| USERIDENTIFIER | &quot;UserIdentifier&quot; |
| IDENTITYLINK | &quot;IdentityLink&quot; |
| BIDSWITCHID | &quot;BidSwitchId&quot; |
| FTRACKID | &quot;FTrackId&quot; |
| PANORAMAID | &quot;PanoramaId&quot; |
| HADRONID | &quot;HadronId&quot; |
| IPADDRESSV4 | &quot;IpAddressV4&quot; |
| PAGEURL | &quot;PageUrl&quot; |
| PAGEDOMAIN | &quot;PageDomain&quot; |
| APPID | &quot;AppId&quot; |



## Enum: OperationEnum

| Name | Value |
|---- | -----|
| ADD | &quot;Add&quot; |
| REMOVE | &quot;Remove&quot; |



