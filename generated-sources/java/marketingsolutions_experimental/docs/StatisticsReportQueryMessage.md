

# StatisticsReportQueryMessage

This is the message defining the query for Adset report

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adSetIds** | **List&lt;String&gt;** | Optional list of ad set IDs to filter on. The ad sets must already exist. If empty, all ad sets will be fetched. |  [optional] |
|**adSetNames** | **List&lt;String&gt;** | Optional list of ad set names to filter on. If empty, all ad sets will be fetched. |  [optional] |
|**adSetStatus** | [**List&lt;AdSetStatusEnum&gt;**](#List&lt;AdSetStatusEnum&gt;) | Optional list of ad set statuses to filter on. If empty, all ad sets will be fetched. |  [optional] |
|**advertiserIds** | **String** | List of advertiser IDs to report on, provided as a single comma-separated string (e.g., \&quot;123,456,789\&quot;). The advertisers must already exist. If empty, all advertisers will be used. |  |
|**currency** | **String** | The currency used for the report. ISO 4217 code (three-letter capitals). |  |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) | List of dimensions for the report. At least one dimension should be provided. &lt;br/&gt;&lt;br/&gt; When an ID dimension is requested (e.g., AdsetId), the corresponding name dimension (e.g., Adset) is automatically included, and vice versa. This applies to the following pairs: AdsetId/Adset, AdId/Ad, AdvertiserId/Advertiser, CampaignId/Campaign, CategoryId/Category, CouponId/Coupon, MarketingObjectiveId/MarketingObjective, ChannelId/Channel. |  |
|**endDate** | **OffsetDateTime** | End date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. |  |
|**format** | [**FormatEnum**](#FormatEnum) | Optional file format of the generated report. |  [optional] |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) | List of metrics for the report. Provide at least one metric to return performance data; otherwise, the response will include only dimension-related information. |  |
|**startDate** | **OffsetDateTime** | Start date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. Must be ≤ endDate. |  |
|**timezone** | **String** | Optional timezone used for the report. Timezone Database format (Tz). |  [optional] |



## Enum: List&lt;AdSetStatusEnum&gt;

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| NOTRUNNING | &quot;NotRunning&quot; |
| DEAD | &quot;Dead&quot; |



## Enum: List&lt;DimensionsEnum&gt;

| Name | Value |
|---- | -----|
| ADSETID | &quot;AdsetId&quot; |
| ADSET | &quot;Adset&quot; |
| ADVERTISERID | &quot;AdvertiserId&quot; |
| ADVERTISER | &quot;Advertiser&quot; |
| CATEGORYID | &quot;CategoryId&quot; |
| CATEGORY | &quot;Category&quot; |
| HOUR | &quot;Hour&quot; |
| DAY | &quot;Day&quot; |
| WEEK | &quot;Week&quot; |
| MONTH | &quot;Month&quot; |
| YEAR | &quot;Year&quot; |
| OS | &quot;Os&quot; |
| DEVICE | &quot;Device&quot; |
| CAMPAIGNID | &quot;CampaignId&quot; |
| CAMPAIGN | &quot;Campaign&quot; |
| ADID | &quot;AdId&quot; |
| AD | &quot;Ad&quot; |
| COUPONID | &quot;CouponId&quot; |
| COUPON | &quot;Coupon&quot; |
| MARKETINGOBJECTIVEID | &quot;MarketingObjectiveId&quot; |
| MARKETINGOBJECTIVE | &quot;MarketingObjective&quot; |
| CHANNELID | &quot;ChannelId&quot; |
| CHANNEL | &quot;Channel&quot; |
| GOAL | &quot;Goal&quot; |
| ADCHANNEL | &quot;AdChannel&quot; |
| SOCIALPLATFORM | &quot;SocialPlatform&quot; |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| CSV | &quot;csv&quot; |
| EXCEL | &quot;excel&quot; |
| XML | &quot;xml&quot; |
| JSON | &quot;json&quot; |



## Enum: List&lt;MetricsEnum&gt;

| Name | Value |
|---- | -----|
| CLICKS | &quot;Clicks&quot; |
| DISPLAYS | &quot;Displays&quot; |
| ADVERTISERCOST | &quot;AdvertiserCost&quot; |
| SALESPC30DCLIENTATTRIBUTION | &quot;SalesPc30dClientAttribution&quot; |
| SALESCLIENTATTRIBUTION | &quot;SalesClientAttribution&quot; |
| SALESPC30D | &quot;SalesPc30d&quot; |
| SALESALLPC30DCLIENTATTRIBUTION | &quot;SalesAllPc30dClientAttribution&quot; |
| SALESALLCLIENTATTRIBUTION | &quot;SalesAllClientAttribution&quot; |
| SALESALLPC30D | &quot;SalesAllPc30d&quot; |
| SALESPV24H | &quot;SalesPv24h&quot; |
| SALESALLPV24H | &quot;SalesAllPv24h&quot; |
| SALESPC30PV24 | &quot;SalesPc30Pv24&quot; |
| SALESALLPC30PV24 | &quot;SalesAllPc30Pv24&quot; |
| SALESPC30DPV24H | &quot;SalesPc30dPv24h&quot; |
| SALESALLPC30DPV24H | &quot;SalesAllPc30dPv24h&quot; |
| SALESPC7DPV24 | &quot;SalesPc7dPv24&quot; |
| SALESALLPC7DPV24 | &quot;SalesAllPc7dPv24&quot; |
| SALESLC | &quot;SalesLc&quot; |
| SALESALLLC | &quot;SalesAllLc&quot; |
| SALESPC7D | &quot;SalesPc7d&quot; |
| SALESALLPC7D | &quot;SalesAllPc7d&quot; |
| SALESPC1D | &quot;SalesPc1d&quot; |
| SALESALLPC1D | &quot;SalesAllPc1d&quot; |
| SALESPIPC | &quot;SalesPiPc&quot; |
| SALESPIPV | &quot;SalesPiPv&quot; |
| SALESPIPCPV | &quot;SalesPiPcPv&quot; |
| POSTINSTALLSALES | &quot;PostInstallSales&quot; |
| SALESOFFLINEPC | &quot;SalesOfflinePc&quot; |
| SALESOFFLINEPV | &quot;SalesOfflinePv&quot; |
| SALESOFFLINEPC30D | &quot;SalesOfflinePc30d&quot; |
| SALESOFFLINEPV24H | &quot;SalesOfflinePv24h&quot; |
| REVENUEGENERATEDPC30DCLIENTATTRIBUTION | &quot;RevenueGeneratedPc30dClientAttribution&quot; |
| REVENUEGENERATEDCLIENTATTRIBUTION | &quot;RevenueGeneratedClientAttribution&quot; |
| REVENUEGENERATEDPC30D | &quot;RevenueGeneratedPc30d&quot; |
| REVENUEGENERATEDALLPC30DCLIENTATTRIBUTION | &quot;RevenueGeneratedAllPc30dClientAttribution&quot; |
| REVENUEGENERATEDALLCLIENTATTRIBUTION | &quot;RevenueGeneratedAllClientAttribution&quot; |
| REVENUEGENERATEDALLPC30D | &quot;RevenueGeneratedAllPc30d&quot; |
| REVENUEGENERATEDPV24H | &quot;RevenueGeneratedPv24h&quot; |
| REVENUEGENERATEDALLPV24H | &quot;RevenueGeneratedAllPv24h&quot; |
| REVENUEGENERATEDPC30PV24 | &quot;RevenueGeneratedPc30Pv24&quot; |
| REVENUEGENERATEDALLPC30PV24 | &quot;RevenueGeneratedAllPc30Pv24&quot; |
| REVENUEGENERATEDPC30DPV24H | &quot;RevenueGeneratedPc30dPv24h&quot; |
| REVENUEGENERATEDALLPC30DPV24H | &quot;RevenueGeneratedAllPc30dPv24h&quot; |
| REVENUEGENERATEDPC7DPV24 | &quot;RevenueGeneratedPc7dPv24&quot; |
| REVENUEGENERATEDALLPC7DPV24 | &quot;RevenueGeneratedAllPc7dPv24&quot; |
| REVENUEGENERATEDLC | &quot;RevenueGeneratedLc&quot; |
| REVENUEGENERATEDALLLC | &quot;RevenueGeneratedAllLc&quot; |
| REVENUEGENERATEDPC7D | &quot;RevenueGeneratedPc7d&quot; |
| REVENUEGENERATEDALLPC7D | &quot;RevenueGeneratedAllPc7d&quot; |
| REVENUEGENERATEDPC1D | &quot;RevenueGeneratedPc1d&quot; |
| REVENUEGENERATEDALLPC1D | &quot;RevenueGeneratedAllPc1d&quot; |
| REVENUEGENERATEDOFFLINEPC | &quot;RevenueGeneratedOfflinePc&quot; |
| REVENUEGENERATEDOFFLINEPV | &quot;RevenueGeneratedOfflinePv&quot; |
| REVENUEGENERATEDOFFLINEPC30D | &quot;RevenueGeneratedOfflinePc30d&quot; |
| REVENUEGENERATEDOFFLINEPV24H | &quot;RevenueGeneratedOfflinePv24h&quot; |
| CONVERSIONRATEPC30DCLIENTATTRIBUTION | &quot;ConversionRatePc30dClientAttribution&quot; |
| CONVERSIONRATECLIENTATTRIBUTION | &quot;ConversionRateClientAttribution&quot; |
| CONVERSIONRATEPC30D | &quot;ConversionRatePc30d&quot; |
| CONVERSIONRATEALLPC30DCLIENTATTRIBUTION | &quot;ConversionRateAllPc30dClientAttribution&quot; |
| CONVERSIONRATEALLCLIENTATTRIBUTION | &quot;ConversionRateAllClientAttribution&quot; |
| CONVERSIONRATEALLPC30D | &quot;ConversionRateAllPc30d&quot; |
| CONVERSIONRATEPV24H | &quot;ConversionRatePv24h&quot; |
| CONVERSIONRATEALLPV24H | &quot;ConversionRateAllPv24h&quot; |
| CONVERSIONRATEPC30PV24 | &quot;ConversionRatePc30Pv24&quot; |
| CONVERSIONRATEALLPC30PV24 | &quot;ConversionRateAllPc30Pv24&quot; |
| CONVERSIONRATEPC30DPV24H | &quot;ConversionRatePc30dPv24h&quot; |
| CONVERSIONRATEALLPC30DPV24H | &quot;ConversionRateAllPc30dPv24h&quot; |
| CONVERSIONRATEPC7DPV24 | &quot;ConversionRatePc7dPv24&quot; |
| CONVERSIONRATEALLPC7DPV24 | &quot;ConversionRateAllPc7dPv24&quot; |
| CONVERSIONRATEPC7D | &quot;ConversionRatePc7d&quot; |
| CONVERSIONRATEALLPC7D | &quot;ConversionRateAllPc7d&quot; |
| CONVERSIONRATEPC1D | &quot;ConversionRatePc1d&quot; |
| CONVERSIONRATEALLPC1D | &quot;ConversionRateAllPc1d&quot; |
| CONVERSIONRATEPIPCPV | &quot;ConversionRatePiPcPv&quot; |
| POSTINSTALLCONVERSIONRATE | &quot;PostInstallConversionRate&quot; |
| ECOSPC30DCLIENTATTRIBUTION | &quot;ECosPc30dClientAttribution&quot; |
| ECOSCLIENTATTRIBUTION | &quot;ECosClientAttribution&quot; |
| ECOSPC30D | &quot;ECosPc30d&quot; |
| ECOSALLPC30DCLIENTATTRIBUTION | &quot;ECosAllPc30dClientAttribution&quot; |
| ECOSALLCLIENTATTRIBUTION | &quot;ECosAllClientAttribution&quot; |
| ECOSALLPC30D | &quot;ECosAllPc30d&quot; |
| ECOSPV24H | &quot;ECosPv24h&quot; |
| ECOSALLPV24H | &quot;ECosAllPv24h&quot; |
| ECOSPC30PV24 | &quot;ECosPc30Pv24&quot; |
| ECOSALLPC30PV24 | &quot;ECosAllPc30Pv24&quot; |
| ECOSPC30DPV24H | &quot;ECosPc30dPv24h&quot; |
| ECOSALLPC30DPV24H | &quot;ECosAllPc30dPv24h&quot; |
| ECOSPC7DPV24 | &quot;ECosPc7dPv24&quot; |
| ECOSALLPC7DPV24 | &quot;ECosAllPc7dPv24&quot; |
| ECOSPC7D | &quot;ECosPc7d&quot; |
| ECOSALLPC7D | &quot;ECosAllPc7d&quot; |
| ECOSPC1D | &quot;ECosPc1d&quot; |
| ECOSALLPC1D | &quot;ECosAllPc1d&quot; |
| COSTPERORDERPC30DCLIENTATTRIBUTION | &quot;CostPerOrderPc30dClientAttribution&quot; |
| COSTPERORDERCLIENTATTRIBUTION | &quot;CostPerOrderClientAttribution&quot; |
| COSTPERORDERPC30D | &quot;CostPerOrderPc30d&quot; |
| COSTPERORDERALLPC30DCLIENTATTRIBUTION | &quot;CostPerOrderAllPc30dClientAttribution&quot; |
| COSTPERORDERALLCLIENTATTRIBUTION | &quot;CostPerOrderAllClientAttribution&quot; |
| COSTPERORDERALLPC30D | &quot;CostPerOrderAllPc30d&quot; |
| COSTPERORDERPV24H | &quot;CostPerOrderPv24h&quot; |
| COSTPERORDERALLPV24H | &quot;CostPerOrderAllPv24h&quot; |
| COSTPERORDERPC30PV24 | &quot;CostPerOrderPc30Pv24&quot; |
| COSTPERORDERALLPC30PV24 | &quot;CostPerOrderAllPc30Pv24&quot; |
| COSTPERORDERPC30DPV24H | &quot;CostPerOrderPc30dPv24h&quot; |
| COSTPERORDERALLPC30DPV24H | &quot;CostPerOrderAllPc30dPv24h&quot; |
| COSTPERORDERPC7DPV24 | &quot;CostPerOrderPc7dPv24&quot; |
| COSTPERORDERALLPC7DPV24 | &quot;CostPerOrderAllPc7dPv24&quot; |
| COSTPERORDERPC7D | &quot;CostPerOrderPc7d&quot; |
| COSTPERORDERALLPC7D | &quot;CostPerOrderAllPc7d&quot; |
| COSTPERORDERPC1D | &quot;CostPerOrderPc1d&quot; |
| COSTPERORDERALLPC1D | &quot;CostPerOrderAllPc1d&quot; |
| EXPOSEDUSERS | &quot;ExposedUsers&quot; |
| AUDIENCE | &quot;Audience&quot; |
| REACH | &quot;Reach&quot; |
| AVERAGECARTPC30DCLIENTATTRIBUTION | &quot;AverageCartPc30dClientAttribution&quot; |
| AVERAGECARTALLPC30DCLIENTATTRIBUTION | &quot;AverageCartAllPc30dClientAttribution&quot; |
| AVERAGECARTCLIENTATTRIBUTION | &quot;AverageCartClientAttribution&quot; |
| AVERAGECARTALLCLIENTATTRIBUTION | &quot;AverageCartAllClientAttribution&quot; |
| AVERAGECARTPC30D | &quot;AverageCartPc30d&quot; |
| AVERAGECARTALLPC30D | &quot;AverageCartAllPc30d&quot; |
| AVERAGECARTPV24H | &quot;AverageCartPv24h&quot; |
| AVERAGECARTALLPV24H | &quot;AverageCartAllPv24h&quot; |
| AVERAGECARTPC1D | &quot;AverageCartPc1d&quot; |
| AVERAGECARTALLPC1D | &quot;AverageCartAllPc1d&quot; |
| AVERAGECARTPC7D | &quot;AverageCartPc7d&quot; |
| AVERAGECARTALLPC7D | &quot;AverageCartAllPc7d&quot; |
| AVERAGECARTPC30PV24 | &quot;AverageCartPc30Pv24&quot; |
| AVERAGECARTALLPC30PV24 | &quot;AverageCartAllPc30Pv24&quot; |
| AVERAGECARTPC30DPV24H | &quot;AverageCartPc30dPv24h&quot; |
| AVERAGECARTALLPC30DPV24H | &quot;AverageCartAllPc30dPv24h&quot; |
| AVERAGECARTPC7DPV24 | &quot;AverageCartPc7dPv24&quot; |
| AVERAGECARTALLPC7DPV24 | &quot;AverageCartAllPc7dPv24&quot; |
| CLICKTHROUGHRATE | &quot;ClickThroughRate&quot; |
| ECPC | &quot;ECpc&quot; |
| CPC | &quot;Cpc&quot; |
| ECPM | &quot;ECpm&quot; |
| RETURNONADVERTISINGSPENDINGCLIENTATTRIBUTION | &quot;ReturnOnAdvertisingSpendingClientAttribution&quot; |
| RETURNONADVERTISINGSPENDINGALLCLIENTATTRIBUTION | &quot;ReturnOnAdvertisingSpendingAllClientAttribution&quot; |
| ADVERTISERVALUE | &quot;AdvertiserValue&quot; |
| ADVERTISERALLVALUE | &quot;AdvertiserAllValue&quot; |
| COSTOFADVERTISERVALUE | &quot;CostOfAdvertiserValue&quot; |
| COSTOFADVERTISERVALUEALL | &quot;CostOfAdvertiserValueAll&quot; |
| APPINSTALLSPCPV | &quot;AppInstallsPcPv&quot; |
| APPINSTALLS | &quot;AppInstalls&quot; |
| QUALIFIEDVISITS | &quot;QualifiedVisits&quot; |
| VISITS | &quot;Visits&quot; |
| VISITSPV1D | &quot;VisitsPV1D&quot; |
| VISITSALLPV1D | &quot;VisitsAllPv1d&quot; |
| ORDERVALUEPI | &quot;OrderValuePi&quot; |
| POSTINSTALLORDERVALUE | &quot;PostInstallOrderValue&quot; |
| BOUNCERATE | &quot;BounceRate&quot; |
| COSTPERINSTALLPCPV | &quot;CostPerInstallPcPv&quot; |
| COSTPERINSTALL | &quot;CostPerInstall&quot; |
| COSTPERVISIT | &quot;CostPerVisit&quot; |
| COSTPERVISITPV1D | &quot;CostPerVisitPV1D&quot; |
| COSTPERQUALIFIEDVISIT | &quot;CostPerQualifiedVisit&quot; |
| INSTALLRATEPCPV | &quot;InstallRatePcPv&quot; |
| INSTALLRATE | &quot;InstallRate&quot; |
| OMNICHANNELROASPC30D | &quot;OmnichannelRoasPc30d&quot; |
| OMNICHANNELROASALLPC30D | &quot;OmnichannelRoasAllPc30d&quot; |
| OMNICHANNELREVENUEPC30D | &quot;OmnichannelRevenuePc30d&quot; |
| OMNICHANNELREVENUEALLPC30D | &quot;OmnichannelRevenueAllPc30d&quot; |
| OMNICHANNELSALESPC30D | &quot;OmnichannelSalesPc30d&quot; |
| OMNICHANNELSALESALLPC30D | &quot;OmnichannelSalesAllPc30d&quot; |
| OMNICHANNELROASALLPV24H | &quot;OmnichannelRoasAllPv24h&quot; |
| OMNICHANNELROASPV24H | &quot;OmnichannelRoasPv24h&quot; |
| OMNICHANNELREVENUEALLPV24H | &quot;OmnichannelRevenueAllPv24h&quot; |
| OMNICHANNELREVENUEPV24H | &quot;OmnichannelRevenuePv24h&quot; |
| OMNICHANNELSALESALLPV24H | &quot;OmnichannelSalesAllPv24h&quot; |
| OMNICHANNELSALESPV24H | &quot;OmnichannelSalesPv24h&quot; |
| OMNICHANNELROASCLIENTATTRIBUTION | &quot;OmnichannelRoasClientAttribution&quot; |
| OMNICHANNELREVENUECLIENTATTRIBUTION | &quot;OmnichannelRevenueClientAttribution&quot; |
| OMNICHANNELSALESCLIENTATTRIBUTION | &quot;OmnichannelSalesClientAttribution&quot; |
| ROASALLPC30DCLIENTATTRIBUTION | &quot;RoasAllPc30dClientAttribution&quot; |
| ROASPC30DCLIENTATTRIBUTION | &quot;RoasPc30dClientAttribution&quot; |
| ROASALLCLIENTATTRIBUTION | &quot;RoasAllClientAttribution&quot; |
| ROASCLIENTATTRIBUTION | &quot;RoasClientAttribution&quot; |
| ROASALLPC30D | &quot;RoasAllPc30d&quot; |
| ROASPC30D | &quot;RoasPc30d&quot; |
| ROASALLPC7D | &quot;RoasAllPc7d&quot; |
| ROASPC7D | &quot;RoasPc7d&quot; |
| ROASALLPC1D | &quot;RoasAllPc1d&quot; |
| ROASPC1D | &quot;RoasPc1d&quot; |
| ROASALLPV24H | &quot;RoasAllPv24h&quot; |
| ROASPV24H | &quot;RoasPv24h&quot; |
| ROASPC30PV24 | &quot;RoasPc30Pv24&quot; |
| ROASALLPC30PV24 | &quot;RoasAllPc30Pv24&quot; |
| ROASPC30DPV24H | &quot;RoasPc30dPv24h&quot; |
| ROASALLPC30DPV24H | &quot;RoasAllPc30dPv24h&quot; |
| ROASPC7DPV24 | &quot;RoasPc7dPv24&quot; |
| ROASALLPC7DPV24 | &quot;RoasAllPc7dPv24&quot; |
| COSTOFSALEPI | &quot;CostOfSalePi&quot; |
| COSTPERORDERPI | &quot;CostPerOrderPi&quot; |
| POSTINSTALLCOSTOFSALE | &quot;PostInstallCostOfSale&quot; |
| POSTINSTALLCOSTPERORDER | &quot;PostInstallCostPerOrder&quot; |
| RETURNONADVERTISERSPENDINGPI | &quot;ReturnOnAdvertiserSpendingPi&quot; |
| POSTINSTALLROAS | &quot;PostInstallRoas&quot; |
| RETURNONADVERTISERSPENDINGOFFLINEPC | &quot;ReturnOnAdvertiserSpendingOfflinePc&quot; |
| RETURNONADVERTISERSPENDINGOFFLINEPV | &quot;ReturnOnAdvertiserSpendingOfflinePv&quot; |
| ROASOFFLINEPC30D | &quot;RoasOfflinePc30d&quot; |
| ROASOFFLINEPV24H | &quot;RoasOfflinePv24h&quot; |
| POTENTIALDISPLAYS | &quot;PotentialDisplays&quot; |
| OVERALLCOMPETITIONWIN | &quot;OverallCompetitionWin&quot; |
| VIEWABLEDISPLAYS | &quot;ViewableDisplays&quot; |
| NONVIEWABLEDISPLAYS | &quot;NonViewableDisplays&quot; |
| UNTRACKABLEDISPLAYS | &quot;UntrackableDisplays&quot; |
| FREQUENCY | &quot;Frequency&quot; |
| INVALIDDISPLAYS | &quot;InvalidDisplays&quot; |
| INVALIDCLICKS | &quot;InvalidClicks&quot; |
| RESULTTYPE | &quot;ResultType&quot; |
| VIDEOSTARTED | &quot;VideoStarted&quot; |
| VIDEOFIRSTQUARTILE | &quot;VideoFirstQuartile&quot; |
| VIDEOMIDPOINT | &quot;VideoMidpoint&quot; |
| VIDEOTHIRDQUARTILE | &quot;VideoThirdQuartile&quot; |
| VIDEOCOMPLETED | &quot;VideoCompleted&quot; |
| VIDEOAVOC | &quot;VideoAvoc&quot; |
| VIDEOSTARTRATE | &quot;VideoStartRate&quot; |
| VIDEOCOMPLETIONRATE | &quot;VideoCompletionRate&quot; |
| VIDEOAVERAGEVIEWRATE | &quot;VideoAverageViewRate&quot; |
| VIDEOCPV | &quot;VideoCpv&quot; |
| VIDEOCPCV | &quot;VideoCpcv&quot; |
| POTENTIALUSERS | &quot;PotentialUsers&quot; |
| RETAILERMARGINEURO | &quot;RetailerMarginEuro&quot; |
| PLATFORMFEEEURO | &quot;PlatformFeeEuro&quot; |
| ALLINMEDIACOST | &quot;AllInMediaCost&quot; |
| NETMEDIACOST | &quot;NetMediaCost&quot; |
| COS | &quot;Cos&quot; |



