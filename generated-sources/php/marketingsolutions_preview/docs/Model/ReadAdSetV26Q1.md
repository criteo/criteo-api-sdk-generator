# # ReadAdSetV26Q1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_id** | **string** | Advertiser id of the campaign this ad set belongs to  This value is a string-encoded integer. | [optional]
**attribution_configuration** | [**\criteo\api\marketingsolutions\preview\Model\ReadAdSetAttributionConfigurationV26Q1**](ReadAdSetAttributionConfigurationV26Q1.md) |  | [optional]
**bidding** | [**\criteo\api\marketingsolutions\preview\Model\ReadAdSetBiddingV26Q1**](ReadAdSetBiddingV26Q1.md) |  | [optional]
**budget** | [**\criteo\api\marketingsolutions\preview\Model\ReadAdSetBudgetV26Q1**](ReadAdSetBudgetV26Q1.md) |  | [optional]
**campaign_id** | **string** | Campaign id this ad set belongs to.                This is a key to a MarketingCampaign entity, which can be retrieved using the MarketingCampaigns endpoints.  This value is a string-encoded integer. | [optional]
**dataset_id** | **string** | Dataset id of this ad set  This value is a string-encoded integer. | [optional]
**destination_environment** | **string** | The environment that an ad click will lead a user to.                Possible values:  - undefined: the ad set does not specify its destination environment  - web: the ad set lead users to a web page  - app: the ad set lead users to an app | [optional]
**media_type** | **string** |  | [optional]
**name** | **string** | Name of the ad set | [optional]
**objective** | **string** | Ad set objective.                Possible values:  - customAction (previously \&quot;Actions\&quot;)  - clicks  - conversions  - displays  - appPromotion (previously \&quot;Installs\&quot;)  - revenue  - storeConversions  - value  - reach (previously \&quot;ViewedImpressions\&quot;)  - visits  - videoViews (previously \&quot;CompletedVideoViews\&quot;) | [optional]
**schedule** | [**\criteo\api\marketingsolutions\preview\Model\ReadAdSetScheduleV26Q1**](ReadAdSetScheduleV26Q1.md) |  | [optional]
**targeting** | [**\criteo\api\marketingsolutions\preview\Model\AdSetTargetingV26Q1**](AdSetTargetingV26Q1.md) |  | [optional]
**video_channel** | **string** |  | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
