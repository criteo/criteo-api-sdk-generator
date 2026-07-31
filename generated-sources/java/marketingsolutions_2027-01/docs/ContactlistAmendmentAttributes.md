

# ContactlistAmendmentAttributes

the name of the entity type

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gumCallerId** | **Integer** | The Gum caller id of the advertiser patching identifiers of type Gum |  [optional] |
|**identifiers** | **List&lt;String&gt;** | The users to add or remove, each in the schema specified |  |
|**identifierType** | [**IdentifierTypeEnum**](#IdentifierTypeEnum) | What type of identifiers are used |  [optional] |
|**operation** | [**OperationEnum**](#OperationEnum) | Operation to add or remove users |  |



## Enum: IdentifierTypeEnum

| Name | Value |
|---- | -----|
| EMAIL | &quot;email&quot; |
| MADID | &quot;madid&quot; |
| IDENTITYLINK | &quot;identityLink&quot; |
| GUM | &quot;gum&quot; |
| PHONENUMBER | &quot;phoneNumber&quot; |



## Enum: OperationEnum

| Name | Value |
|---- | -----|
| ADD | &quot;add&quot; |
| REMOVE | &quot;remove&quot; |



