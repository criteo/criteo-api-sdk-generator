

# AsyncOffsiteReport

Async Offsite report body request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountIds** | **List&lt;String&gt;** | Account ids to report on |  |
|**buyType** | [**BuyTypeEnum**](#BuyTypeEnum) | Filter on buy type: Auction, Preferred Deals or Sponsorship |  [optional] |
|**campaignIds** | **List&lt;String&gt;** | Campaign ids to filter |  [optional] |
|**campaignType** | [**CampaignTypeEnum**](#CampaignTypeEnum) | Filter the type of campaigns to report on: sponsoredProducts or onSiteDisplays |  [optional] |
|**clickAttributionWindow** | [**ClickAttributionWindowEnum**](#ClickAttributionWindowEnum) | Click attribution window |  [optional] |
|**creativeIds** | **List&lt;String&gt;** | Creative ids to filter |  [optional] |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) | List of dimensions to report on |  |
|**endDate** | **OffsetDateTime** | End date |  |
|**format** | [**FormatEnum**](#FormatEnum) | Format of the output |  [optional] |
|**lineItemIds** | **List&lt;String&gt;** | Line item ids to filter |  [optional] |
|**mediaType** | [**MediaTypeEnum**](#MediaTypeEnum) | Filter on the type of media: unknown, display, video |  [optional] |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) | List of metrics to report on |  |
|**retailerIds** | **List&lt;String&gt;** | Retailer ids to filter |  [optional] |
|**salesChannel** | [**SalesChannelEnum**](#SalesChannelEnum) | Filter on specific sales channel: offline or online |  [optional] |
|**startDate** | **OffsetDateTime** | Start date |  |
|**timezone** | **String** | Time zone : see criteo developer portal for supported time zones |  [optional] |
|**viewAttributionWindow** | [**ViewAttributionWindowEnum**](#ViewAttributionWindowEnum) | View attribution window |  [optional] |



## Enum: BuyTypeEnum

| Name | Value |
|---- | -----|
| AUCTION | &quot;auction&quot; |
| PREFERREDDEALS | &quot;preferredDeals&quot; |
| SPONSORSHIP | &quot;sponsorship&quot; |



## Enum: CampaignTypeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| SPONSOREDPRODUCTS | &quot;sponsoredProducts&quot; |
| ONSITEDISPLAYS | &quot;onSiteDisplays&quot; |



## Enum: ClickAttributionWindowEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| _7D | &quot;7D&quot; |
| _14D | &quot;14D&quot; |
| _30D | &quot;30D&quot; |



## Enum: List&lt;DimensionsEnum&gt;

| Name | Value |
|---- | -----|
| DATE | &quot;date&quot; |
| HOUR | &quot;hour&quot; |
| DAYSDIFFERENCE | &quot;daysDifference&quot; |
| ADVDATE | &quot;advDate&quot; |
| ADVHOUR | &quot;advHour&quot; |
| CAMPAIGNID | &quot;campaignId&quot; |
| CAMPAIGNNAME | &quot;campaignName&quot; |
| LINEITEMID | &quot;lineItemId&quot; |
| LINEITEMNAME | &quot;lineItemName&quot; |
| RETAILERID | &quot;retailerId&quot; |
| RETAILERNAME | &quot;retailerName&quot; |
| BILLINGTYPE | &quot;billingType&quot; |
| ENVIRONMENT | &quot;environment&quot; |
| ADFORMATSIZE | &quot;adFormatSize&quot; |
| SSP | &quot;ssp&quot; |
| PUBLISHER | &quot;publisher&quot; |
| INVENTORYTYPE | &quot;inventoryType&quot; |
| MEDIATYPE | &quot;mediaType&quot; |
| BUYTYPE | &quot;buyType&quot; |
| SALESCHANNEL | &quot;salesChannel&quot; |
| CREATIVEID | &quot;creativeId&quot; |
| CREATIVENAME | &quot;creativeName&quot; |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| JSON | &quot;json&quot; |
| JSON_COMPACT | &quot;json-compact&quot; |
| JSON_NEWLINE | &quot;json-newline&quot; |
| CSV | &quot;csv&quot; |



## Enum: MediaTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| VIDEO | &quot;video&quot; |
| DISPLAY | &quot;display&quot; |
| ALL | &quot;all&quot; |



## Enum: List&lt;MetricsEnum&gt;

| Name | Value |
|---- | -----|
| AUDIENCE | &quot;audience&quot; |
| UNIQUEVISITORS | &quot;uniqueVisitors&quot; |
| REACHRATE | &quot;reachRate&quot; |
| IMPRESSIONS | &quot;impressions&quot; |
| FREQUENCY | &quot;frequency&quot; |
| WINRATE | &quot;winRate&quot; |
| CLICKS | &quot;clicks&quot; |
| CTR | &quot;ctr&quot; |
| VIEWABILITY | &quot;viewability&quot; |
| CPC | &quot;cpc&quot; |
| ECPM | &quot;ecpm&quot; |
| CPM | &quot;cpm&quot; |
| SPEND | &quot;spend&quot; |
| ATTRIBUTEDUNITS | &quot;attributedUnits&quot; |
| ATTRIBUTEDSALES | &quot;attributedSales&quot; |
| ROAS | &quot;roas&quot; |
| VIDEOSTARTS | &quot;videoStarts&quot; |
| VIDEOSPLAYEDTO25 | &quot;videosPlayedTo25&quot; |
| VIDEOSPLAYEDTO50 | &quot;videosPlayedTo50&quot; |
| VIDEOSPLAYEDTO75 | &quot;videosPlayedTo75&quot; |
| VIDEOSPLAYEDTO100 | &quot;videosPlayedTo100&quot; |
| VIDEOSTARTINGRATE | &quot;videoStartingRate&quot; |
| VIDEOCOMPLETIONRATE | &quot;videoCompletionRate&quot; |
| VIDEOCPC | &quot;videoCPC&quot; |
| VIDEOCPCV | &quot;videoCPCV&quot; |
| VISITS | &quot;visits&quot; |
| QUALIFIEDVISITS | &quot;qualifiedVisits&quot; |
| LANDINGRATE | &quot;landingRate&quot; |



## Enum: SalesChannelEnum

| Name | Value |
|---- | -----|
| ONLINE | &quot;online&quot; |
| OFFLINE | &quot;offline&quot; |
| ALL | &quot;all&quot; |



## Enum: ViewAttributionWindowEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| _1D | &quot;1D&quot; |
| _7D | &quot;7D&quot; |
| _14D | &quot;14D&quot; |
| _30D | &quot;30D&quot; |



