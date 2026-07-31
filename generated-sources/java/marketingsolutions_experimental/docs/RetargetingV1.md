

# RetargetingV1

Settings to target users based on its type and days since last visit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**daysSinceLastVisitMax** | **Integer** | Maximum number of days since last visit to partner. |  [optional] |
|**daysSinceLastVisitMin** | **Integer** | Minimum number of days since last visit to partner. |  [optional] |
|**visitorsType** | [**VisitorsTypeEnum**](#VisitorsTypeEnum) | Types of visitors. |  [optional] |



## Enum: VisitorsTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| ALL | &quot;All&quot; |
| BUYERS | &quot;Buyers&quot; |
| NONBUYERS | &quot;NonBuyers&quot; |



