

# RetargetingCreateV1

Settings to target users based on its type and days since last visit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**daysSinceLastVisitMax** | **Integer** | Maximum number of days since last visit to partner. |  |
|**daysSinceLastVisitMin** | **Integer** | Minimum number of days since last visit to partner. |  |
|**visitorsType** | [**VisitorsTypeEnum**](#VisitorsTypeEnum) | Types of visitors. |  |



## Enum: VisitorsTypeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;All&quot; |
| BUYERS | &quot;Buyers&quot; |
| NONBUYERS | &quot;NonBuyers&quot; |



