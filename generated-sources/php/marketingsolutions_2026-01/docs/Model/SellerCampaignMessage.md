# # SellerCampaignMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bid** | **float** | Cost-per-click bid in the advertiser&#39;s currency. Null means no CPC is defined (seller-campaign will be suspended with NoCpcDefined). Set to 0 to stop delivery. | [optional]
**campaign_id** | **int** | Identifier of the campaign this seller participates in | [optional]
**id** | **string** | Composite identifier in format {sellerId}.{campaignId} | [optional] [readonly]
**product_set** | [**\criteo\api\marketingsolutions\v2026_01\Model\SellerCampaignProductSet**](SellerCampaignProductSet.md) |  | [optional]
**seller_id** | **string** | Unique identifier of the seller (merchant) | [optional]
**suspended_since** | **\DateTime** | Timestamp when the seller-campaign was suspended. Null means the seller-campaign is active. | [optional]
**suspension_reasons** | [**\criteo\api\marketingsolutions\v2026_01\Model\SellerCampaignSuspensionReason[]**](SellerCampaignSuspensionReason.md) | List of reasons why the seller-campaign is suspended. Null means the seller-campaign is active. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
