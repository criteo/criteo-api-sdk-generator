

# CampaignAvailability

Information about the availability of a specific campaign type and buy type combination, and page types and environments supported for that combination

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**buyType** | [**BuyTypeEnum**](#BuyTypeEnum) | The buy type this object represents availability for |  [optional] |
|**campaignType** | [**CampaignTypeEnum**](#CampaignTypeEnum) | The type of campaign this object represents availability for |  [optional] |
|**isAvailable** | **Boolean** | Indicates whether the campaign type and buy type combination is available for the retailer |  [optional] |
|**validCombinations** | [**List&lt;PageTypeCombination&gt;**](PageTypeCombination.md) | PageType-PageEnvironmentType pairs which are supported for this campaign-buy type combination |  [optional] |



## Enum: BuyTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| AUCTION | &quot;auction&quot; |
| PREFERREDDEALS | &quot;preferredDeals&quot; |
| SPONSORSHIP | &quot;sponsorship&quot; |
| OFFSITE | &quot;offsite&quot; |



## Enum: CampaignTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| SPONSOREDPRODUCTS | &quot;sponsoredProducts&quot; |
| ONSITEDISPLAY | &quot;onsiteDisplay&quot; |
| OFFSITE | &quot;offsite&quot; |



