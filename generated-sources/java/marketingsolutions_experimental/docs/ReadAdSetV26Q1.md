

# ReadAdSetV26Q1

Ad set read model.                The ad set is the configuration unit that defines ads delivery. Its binds together the objective, budget,  scheduling, targeting options and ads.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserId** | **String** | Advertiser id of the campaign this ad set belongs to  This value is a string-encoded integer. |  [optional] |
|**attributionConfiguration** | [**ReadAdSetAttributionConfigurationV26Q1**](ReadAdSetAttributionConfigurationV26Q1.md) |  |  [optional] |
|**bidding** | [**ReadAdSetBiddingV26Q1**](ReadAdSetBiddingV26Q1.md) |  |  [optional] |
|**budget** | [**ReadAdSetBudgetV26Q1**](ReadAdSetBudgetV26Q1.md) |  |  [optional] |
|**campaignId** | **String** | Campaign id this ad set belongs to.                This is a key to a MarketingCampaign entity, which can be retrieved using the MarketingCampaigns endpoints.  This value is a string-encoded integer. |  [optional] |
|**datasetId** | **String** | Dataset id of this ad set  This value is a string-encoded integer. |  [optional] |
|**destinationEnvironment** | [**DestinationEnvironmentEnum**](#DestinationEnvironmentEnum) | The environment that an ad click will lead a user to.                Possible values:  - undefined: the ad set does not specify its destination environment  - web: the ad set lead users to a web page  - app: the ad set lead users to an app |  [optional] |
|**mediaType** | [**MediaTypeEnum**](#MediaTypeEnum) |  |  [optional] |
|**name** | **String** | Name of the ad set |  [optional] |
|**objective** | [**ObjectiveEnum**](#ObjectiveEnum) | Ad set objective.                Possible values:  - customAction (previously \&quot;Actions\&quot;)  - clicks  - conversions  - displays  - appPromotion (previously \&quot;Installs\&quot;)  - revenue  - storeConversions  - value  - reach (previously \&quot;ViewedImpressions\&quot;)  - visits  - videoViews (previously \&quot;CompletedVideoViews\&quot;) |  [optional] |
|**schedule** | [**ReadAdSetScheduleV26Q1**](ReadAdSetScheduleV26Q1.md) |  |  [optional] |
|**targeting** | [**AdSetTargetingV26Q1**](AdSetTargetingV26Q1.md) |  |  [optional] |
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



