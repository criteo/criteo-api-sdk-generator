

# SellerCampaignMessage

A seller-campaign links a seller to a campaign, defining the CPC bid. A seller can participate in multiple campaigns, and a campaign can have multiple sellers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bid** | **Double** | Cost-per-click bid in the advertiser&#39;s currency. Null means no CPC is defined (seller-campaign will be suspended with NoCpcDefined). Set to 0 to stop delivery. |  [optional] |
|**campaignId** | **Integer** | Identifier of the campaign this seller participates in |  [optional] |
|**id** | **String** | Composite identifier in format {sellerId}.{campaignId} |  [optional] [readonly] |
|**productSet** | [**SellerCampaignProductSet**](SellerCampaignProductSet.md) |  |  [optional] |
|**sellerId** | **String** | Unique identifier of the seller (merchant) |  [optional] |
|**suspendedSince** | **OffsetDateTime** | Timestamp when the seller-campaign was suspended. Null means the seller-campaign is active. |  [optional] |
|**suspensionReasons** | **List&lt;SellerCampaignSuspensionReason&gt;** | List of reasons why the seller-campaign is suspended. Null means the seller-campaign is active. |  [optional] |



