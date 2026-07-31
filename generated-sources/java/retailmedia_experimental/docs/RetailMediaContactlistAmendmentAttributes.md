

# RetailMediaContactlistAmendmentAttributes

Attributes of retail media contact list amendment

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
| USERIDENTIFIER | &quot;UserIdentifier&quot; |
| IDENTITYLINK | &quot;IdentityLink&quot; |
| GUM | &quot;Gum&quot; |
| CUSTOMERID | &quot;CustomerId&quot; |
| PHONENUMBER | &quot;PhoneNumber&quot; |



## Enum: OperationEnum

| Name | Value |
|---- | -----|
| ADD | &quot;add&quot; |
| REMOVE | &quot;remove&quot; |



