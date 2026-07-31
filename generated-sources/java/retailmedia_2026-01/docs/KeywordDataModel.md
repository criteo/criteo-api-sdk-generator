

# KeywordDataModel

A single keyword and associated bid override.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bid** | **Double** | The bid to use when a positive keyword matches the shopper search phrase. |  [optional] |
|**createdAt** | **OffsetDateTime** | The time at which this keyword was created in UTC. |  [optional] |
|**inputKeywords** | [**InputKeywordsModel**](InputKeywordsModel.md) |  |  [optional] |
|**matchType** | [**MatchTypeEnum**](#MatchTypeEnum) | The matching algorithm to be used when comparing this keyword with the shopper search phrase. |  [optional] |
|**reviewState** | **ReviewStateModel** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** | The time at which this keyword was last modified in UTC. |  [optional] |



## Enum: MatchTypeEnum

| Name | Value |
|---- | -----|
| POSITIVEEXACTMATCH | &quot;PositiveExactMatch&quot; |
| NEGATIVEEXACTMATCH | &quot;NegativeExactMatch&quot; |
| NEGATIVEBROADMATCH | &quot;NegativeBroadMatch&quot; |



