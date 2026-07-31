

# ReadAdSetV24Q3

ad set read model

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserId** | **String** |  |  [optional] |
|**attributionConfiguration** | [**ReadAdSetAttributionConfigurationV24Q3**](ReadAdSetAttributionConfigurationV24Q3.md) |  |  [optional] |
|**bidding** | [**ReadAdSetBiddingV24Q3**](ReadAdSetBiddingV24Q3.md) |  |  [optional] |
|**budget** | [**ReadAdSetBudgetV24Q3**](ReadAdSetBudgetV24Q3.md) |  |  [optional] |
|**campaignId** | **String** |  |  [optional] |
|**datasetId** | **String** |  |  [optional] |
|**destinationEnvironment** | [**DestinationEnvironmentEnum**](#DestinationEnvironmentEnum) |  |  [optional] |
|**mediaType** | [**MediaTypeEnum**](#MediaTypeEnum) |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**objective** | [**ObjectiveEnum**](#ObjectiveEnum) |  |  [optional] |
|**schedule** | [**ReadAdSetScheduleV24Q3**](ReadAdSetScheduleV24Q3.md) |  |  [optional] |
|**targeting** | [**AdSetTargetingV24Q3**](AdSetTargetingV24Q3.md) |  |  [optional] |
|**videoChannel** | [**VideoChannelEnum**](#VideoChannelEnum) |  |  [optional] |



## Enum: DestinationEnvironmentEnum

| Name | Value |
|---- | -----|
| UNDEFINED | &quot;undefined&quot; |
| WEB | &quot;web&quot; |
| APP | &quot;app&quot; |



## Enum: MediaTypeEnum

| Name | Value |
|---- | -----|
| DISPLAY | &quot;display&quot; |
| VIDEO | &quot;video&quot; |



## Enum: ObjectiveEnum

| Name | Value |
|---- | -----|
| CUSTOMACTION | &quot;customAction&quot; |
| CLICKS | &quot;clicks&quot; |
| CONVERSIONS | &quot;conversions&quot; |
| DISPLAYS | &quot;displays&quot; |
| APPPROMOTION | &quot;appPromotion&quot; |
| REVENUE | &quot;revenue&quot; |
| STORECONVERSIONS | &quot;storeConversions&quot; |
| VALUE | &quot;value&quot; |
| REACH | &quot;reach&quot; |
| VISITS | &quot;visits&quot; |
| VIDEOVIEWS | &quot;videoViews&quot; |



## Enum: VideoChannelEnum

| Name | Value |
|---- | -----|
| OLV | &quot;olv&quot; |
| CTV | &quot;ctv&quot; |



