

# ReadAdSetScheduleV24Q3

ad set schedule read model

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activationStatus** | [**ActivationStatusEnum**](#ActivationStatusEnum) |  |  [optional] |
|**deliveryStatus** | [**DeliveryStatusEnum**](#DeliveryStatusEnum) |  |  [optional] |
|**endDate** | [**NillableDateTime**](NillableDateTime.md) |  |  [optional] |
|**startDate** | [**NillableDateTime**](NillableDateTime.md) |  |  [optional] |



## Enum: ActivationStatusEnum

| Name | Value |
|---- | -----|
| ON | &quot;on&quot; |
| OFF | &quot;off&quot; |



## Enum: DeliveryStatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| INACTIVE | &quot;inactive&quot; |
| LIVE | &quot;live&quot; |
| NOTLIVE | &quot;notLive&quot; |
| PAUSING | &quot;pausing&quot; |
| PAUSED | &quot;paused&quot; |
| SCHEDULED | &quot;scheduled&quot; |
| ENDED | &quot;ended&quot; |
| NOTDELIVERING | &quot;notDelivering&quot; |
| ARCHIVED | &quot;archived&quot; |



