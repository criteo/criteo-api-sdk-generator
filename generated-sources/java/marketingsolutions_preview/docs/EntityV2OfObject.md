

# EntityV2OfObject

Generic Criteo API successful data model

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | **Object** | Generic Criteo API successful data model  While others may be computed e.g. lastChangedDate.  Computed attributes are only part of the read model and not part of the write model. |  [optional] |
|**id** | **String** | A opaque string containing the unique Id of the entity |  |
|**meta** | **Object** | A meta object that contains application-specific metadata |  [optional] |
|**relationships** | **Object** | Relationships with this entity |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | A string containing the entity type |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CAMPAIGN | &quot;campaign&quot; |
| ADSET | &quot;adset&quot; |
| AD | &quot;ad&quot; |
| ADVERTISER | &quot;advertiser&quot; |
| AGENCY | &quot;agency&quot; |
| AGENCYADVERTISERLINK | &quot;agencyAdvertiserLink&quot; |
| AGENCYADVERTISERTRANSFERREQUEST | &quot;AgencyAdvertiserTransferRequest&quot; |
| PUBLISHER | &quot;publisher&quot; |
| ADDRESS | &quot;address&quot; |
| CLIENT | &quot;client&quot; |
| CONTACT | &quot;contact&quot; |
| INDUSTRY | &quot;industry&quot; |



