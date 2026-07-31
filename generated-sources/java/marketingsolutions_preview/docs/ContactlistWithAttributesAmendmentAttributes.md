

# ContactlistWithAttributesAmendmentAttributes

the name of the entity type

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gumCallerId** | **Object** | The Gum caller id of the advertiser patching identifiers of type Gum |  [optional] [readonly] |
|**identifiers** | [**List&lt;UserDef&gt;**](UserDef.md) | The users to add or remove, each in the schema specified, defined with attributes |  |
|**identifierType** | [**IdentifierTypeEnum**](#IdentifierTypeEnum) | What type of identifiers are used |  |
|**operation** | [**OperationEnum**](#OperationEnum) | Whether to add or remove users |  |



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



