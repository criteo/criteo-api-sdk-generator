

# AdvertiserCampaignMessage

Data representing a campaign for an advertiser. A campaign groups seller-campaigns and defines delivery settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adSetDeliveryStatus** | [**AdSetDeliveryStatusEnum**](#AdSetDeliveryStatusEnum) | Human-readable delivery status of the campaign&#39;s ad set |  [optional] [readonly] |
|**campaignName** | **String** | Display name of the campaign |  [optional] |
|**id** | **Integer** | Unique campaign identifier |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Numeric delivery status: 0 &#x3D; Running, 1 &#x3D; Archived, 2 &#x3D; NotRunning |  [optional] |



## Enum: AdSetDeliveryStatusEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;Running&quot; |
| ARCHIVED | &quot;Archived&quot; |
| NOTRUNNING | &quot;NotRunning&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



