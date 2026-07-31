

# GenerateStatisticsReport

Request attributes for async statistics report

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adSetIds** | **List&lt;String&gt;** | List of advertiser IDs to report on, provided as a single comma-separated string (e.g., \&quot;123,456,789\&quot;). The advertisers must already exist. If empty, all advertisers will be used. |  [optional] |
|**adSetNames** | **List&lt;String&gt;** | The list of ad sets names. If empty, all the adSets will be fetched. |  [optional] |
|**adSetStatus** | **List&lt;String&gt;** | The list of ad sets status. If empty, all the adSets will be fetched. |  [optional] |
|**advertiserIds** | **List&lt;String&gt;** | The list of advertiser ids |  |
|**currency** | **String** | The currency used for the report. ISO 4217 code (three-letter capitals). |  [optional] |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) | The dimensions for the report. |  |
|**endDate** | **OffsetDateTime** | End date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. |  |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) | The list of metrics to report. |  |
|**startDate** | **OffsetDateTime** | Start date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. |  |
|**timezone** | **String** | Optional timezone used for the report. Timezone Database format (Tz). |  [optional] |



## Enum: List&lt;DimensionsEnum&gt;

| Name | Value |
|---- | -----|
| ADVERTISERID | &quot;AdvertiserId&quot; |
| ADVERTISER | &quot;Advertiser&quot; |
| CAMPAIGNID | &quot;CampaignId&quot; |
| CAMPAIGN | &quot;Campaign&quot; |
| ADSETID | &quot;AdSetId&quot; |
| ADSET | &quot;AdSet&quot; |
| CHANNELID | &quot;ChannelId&quot; |
| CHANNEL | &quot;Channel&quot; |
| CATEGORYID | &quot;CategoryId&quot; |
| CATEGORY | &quot;Category&quot; |
| DEVICE | &quot;Device&quot; |
| OS | &quot;Os&quot; |
| ADID | &quot;AdId&quot; |
| AD | &quot;Ad&quot; |
| COUPONID | &quot;CouponId&quot; |
| COUPON | &quot;Coupon&quot; |
| YEAR | &quot;Year&quot; |
| MONTH | &quot;Month&quot; |
| WEEK | &quot;Week&quot; |
| DAY | &quot;Day&quot; |
| HOUR | &quot;Hour&quot; |
| MARKETINGCAMPAIGNGOAL | &quot;MarketingCampaignGoal&quot; |
| MARKETINGOBJECTIVE | &quot;MarketingObjective&quot; |
| MARKETINGOBJECTIVEID | &quot;MarketingObjectiveId&quot; |
| VIDEOPLAYERSIZE | &quot;VideoPlayerSize&quot; |
| VIDEOPLACEMENT | &quot;VideoPlacement&quot; |
| VIDEOPLAYBACKMETHOD | &quot;VideoPlaybackMethod&quot; |
| SSP | &quot;SSP&quot; |
| VIDEODURATIONINSECONDS | &quot;VideoDurationInSeconds&quot; |
| MEDIATYPE | &quot;MediaType&quot; |
| ADFORMAT | &quot;AdFormat&quot; |
| DISPLAYSIZE | &quot;DisplaySize&quot; |
| VIDEOPLAYERRATIO | &quot;VideoPlayerRatio&quot; |
| COUNTRY | &quot;Country&quot; |
| REGION | &quot;Region&quot; |
| POSTALCODE | &quot;PostalCode&quot; |
| USERBEHAVIOR | &quot;UserBehavior&quot; |
| ENVIRONMENT | &quot;Environment&quot; |
| ADCHANNEL | &quot;AdChannel&quot; |
| SOCIALPLATFORM | &quot;SocialPlatform&quot; |



## Enum: List&lt;MetricsEnum&gt;

| Name | Value |
|---- | -----|
| CLICKS | &quot;Clicks&quot; |
| DISPLAYS | &quot;Displays&quot; |
| ADVERTISERCOST | &quot;AdvertiserCost&quot; |
| SALESPC30DCLIENTATTRIBUTION | &quot;SalesPc30dClientAttribution&quot; |
| SALESALLPC30DCLIENTATTRIBUTION | &quot;SalesAllPc30dClientAttribution&quot; |
| SALESCLIENTATTRIBUTION | &quot;SalesClientAttribution&quot; |
| SALESALLCLIENTATTRIBUTION | &quot;SalesAllClientAttribution&quot; |
| SALESPC30D | &quot;SalesPc30d&quot; |
| SALESALLPC30D | &quot;SalesAllPc30d&quot; |
| SALESPC1D | &quot;SalesPc1d&quot; |
| SALESALLPC1D | &quot;SalesAllPc1d&quot; |
| SALESPC7D | &quot;SalesPc7d&quot; |
| SALESALLPC7D | &quot;SalesAllPc7d&quot; |
| SALESPC7DPV24 | &quot;SalesPc7dPv24&quot; |
| SALESALLPC7DPV24 | &quot;SalesAllPc7dPv24&quot; |
| SALESPV24H | &quot;SalesPv24h&quot; |
| SALESALLPV24H | &quot;SalesAllPv24h&quot; |
| SALESPC30PV24 | &quot;SalesPc30Pv24&quot; |
| SALESALLPC30PV24 | &quot;SalesAllPc30Pv24&quot; |
| SALESPC30DPV24H | &quot;SalesPc30dPv24h&quot; |
| SALESALLPC30DPV24H | &quot;SalesAllPc30dPv24h&quot; |
| SALESPIPC | &quot;SalesPiPc&quot; |
| SALESPIPV | &quot;SalesPiPv&quot; |
| SALESPIPCPV | &quot;SalesPiPcPv&quot; |
| POSTINSTALLSALES | &quot;PostInstallSales&quot; |
| SALESOFFLINEPC | &quot;SalesOfflinePc&quot; |
| SALESOFFLINEPV | &quot;SalesOfflinePv&quot; |
| SALESOFFLINEPC30D | &quot;SalesOfflinePc30d&quot; |
| SALESOFFLINEPV24H | &quot;SalesOfflinePv24h&quot; |
| REVENUEGENERATEDPC30DCLIENTATTRIBUTION | &quot;RevenueGeneratedPc30dClientAttribution&quot; |
| REVENUEGENERATEDALLPC30DCLIENTATTRIBUTION | &quot;RevenueGeneratedAllPc30dClientAttribution&quot; |
| REVENUEGENERATEDCLIENTATTRIBUTION | &quot;RevenueGeneratedClientAttribution&quot; |
| REVENUEGENERATEDALLCLIENTATTRIBUTION | &quot;RevenueGeneratedAllClientAttribution&quot; |
| REVENUEGENERATEDPC30D | &quot;RevenueGeneratedPc30d&quot; |
| REVENUEGENERATEDALLPC30D | &quot;RevenueGeneratedAllPc30d&quot; |
| REVENUEGENERATEDPC1D | &quot;RevenueGeneratedPc1d&quot; |
| REVENUEGENERATEDALLPC1D | &quot;RevenueGeneratedAllPc1d&quot; |
| REVENUEGENERATEDPC7D | &quot;RevenueGeneratedPc7d&quot; |
| REVENUEGENERATEDALLPC7D | &quot;RevenueGeneratedAllPc7d&quot; |
| REVENUEGENERATEDPV24H | &quot;RevenueGeneratedPv24h&quot; |
| REVENUEGENERATEDALLPV24H | &quot;RevenueGeneratedAllPv24h&quot; |
| REVENUEGENERATEDPC30PV24 | &quot;RevenueGeneratedPc30Pv24&quot; |
| REVENUEGENERATEDALLPC30PV24 | &quot;RevenueGeneratedAllPc30Pv24&quot; |
| REVENUEGENERATEDPC30DPV24H | &quot;RevenueGeneratedPc30dPv24h&quot; |
| REVENUEGENERATEDALLPC30DPV24H | &quot;RevenueGeneratedAllPc30dPv24h&quot; |
| REVENUEGENERATEDPC7DPV24 | &quot;RevenueGeneratedPc7dPv24&quot; |
| REVENUEGENERATEDALLPC7DPV24 | &quot;RevenueGeneratedAllPc7dPv24&quot; |
| REVENUEGENERATEDOFFLINEPC | &quot;RevenueGeneratedOfflinePc&quot; |
| REVENUEGENERATEDOFFLINEPV | &quot;RevenueGeneratedOfflinePv&quot; |
| REVENUEGENERATEDOFFLINEPC30D | &quot;RevenueGeneratedOfflinePc30d&quot; |
| REVENUEGENERATEDOFFLINEPV24H | &quot;RevenueGeneratedOfflinePv24h&quot; |
| CONVERSIONRATEPC30DCLIENTATTRIBUTION | &quot;ConversionRatePc30dClientAttribution&quot; |
| CONVERSIONRATEALLPC30DCLIENTATTRIBUTION | &quot;ConversionRateAllPc30dClientAttribution&quot; |
| CONVERSIONRATECLIENTATTRIBUTION | &quot;ConversionRateClientAttribution&quot; |
| CONVERSIONRATEALLCLIENTATTRIBUTION | &quot;ConversionRateAllClientAttribution&quot; |
| CONVERSIONRATEPC30D | &quot;ConversionRatePc30d&quot; |
| CONVERSIONRATEALLPC30D | &quot;ConversionRateAllPc30d&quot; |
| CONVERSIONRATEPC1D | &quot;ConversionRatePc1d&quot; |
| CONVERSIONRATEALLPC1D | &quot;ConversionRateAllPc1d&quot; |
| CONVERSIONRATEPC7D | &quot;ConversionRatePc7d&quot; |
| CONVERSIONRATEALLPC7D | &quot;ConversionRateAllPc7d&quot; |
| CONVERSIONRATEPV24H | &quot;ConversionRatePv24h&quot; |
| CONVERSIONRATEALLPV24H | &quot;ConversionRateAllPv24h&quot; |
| CONVERSIONRATEPC30PV24 | &quot;ConversionRatePc30Pv24&quot; |
| CONVERSIONRATEALLPC30PV24 | &quot;ConversionRateAllPc30Pv24&quot; |
| CONVERSIONRATEPC30DPV24H | &quot;ConversionRatePc30dPv24h&quot; |
| CONVERSIONRATEALLPC30DPV24H | &quot;ConversionRateAllPc30dPv24h&quot; |
| CONVERSIONRATEPC7DPV24 | &quot;ConversionRatePc7dPv24&quot; |
| CONVERSIONRATEALLPC7DPV24 | &quot;ConversionRateAllPc7dPv24&quot; |
| CONVERSIONRATEPIPCPV | &quot;ConversionRatePiPcPv&quot; |
| POSTINSTALLCONVERSIONRATE | &quot;PostInstallConversionRate&quot; |
| ECOSPC30DCLIENTATTRIBUTION | &quot;ECosPc30dClientAttribution&quot; |
| ECOSALLPC30DCLIENTATTRIBUTION | &quot;ECosAllPc30dClientAttribution&quot; |
| ECOSCLIENTATTRIBUTION | &quot;ECosClientAttribution&quot; |
| ECOSALLCLIENTATTRIBUTION | &quot;ECosAllClientAttribution&quot; |
| ECOSPC30D | &quot;ECosPc30d&quot; |
| ECOSALLPC30D | &quot;ECosAllPc30d&quot; |
| ECOSPC1D | &quot;ECosPc1d&quot; |
| ECOSALLPC1D | &quot;ECosAllPc1d&quot; |
| ECOSPC7D | &quot;ECosPc7d&quot; |
| ECOSALLPC7D | &quot;ECosAllPc7d&quot; |
| ECOSPV24H | &quot;ECosPv24h&quot; |
| ECOSALLPV24H | &quot;ECosAllPv24h&quot; |
| ECOSPC30PV24 | &quot;ECosPc30Pv24&quot; |
| ECOSALLPC30PV24 | &quot;ECosAllPc30Pv24&quot; |
| ECOSPC30DPV24H | &quot;ECosPc30dPv24h&quot; |
| ECOSALLPC30DPV24H | &quot;ECosAllPc30dPv24h&quot; |
| ECOSPC7DPV24 | &quot;ECosPc7dPv24&quot; |
| ECOSALLPC7DPV24 | &quot;ECosAllPc7dPv24&quot; |
| COSTPERORDERPC30DCLIENTATTRIBUTION | &quot;CostPerOrderPc30dClientAttribution&quot; |
| COSTPERORDERALLPC30DCLIENTATTRIBUTION | &quot;CostPerOrderAllPc30dClientAttribution&quot; |
| COSTPERORDERCLIENTATTRIBUTION | &quot;CostPerOrderClientAttribution&quot; |
| COSTPERORDERALLCLIENTATTRIBUTION | &quot;CostPerOrderAllClientAttribution&quot; |
| COSTPERORDERPC30D | &quot;CostPerOrderPc30d&quot; |
| COSTPERORDERALLPC30D | &quot;CostPerOrderAllPc30d&quot; |
| COSTPERORDERPC1D | &quot;CostPerOrderPc1d&quot; |
| COSTPERORDERALLPC1D | &quot;CostPerOrderAllPc1d&quot; |
| COSTPERORDERPC7D | &quot;CostPerOrderPc7d&quot; |
| COSTPERORDERALLPC7D | &quot;CostPerOrderAllPc7d&quot; |
| COSTPERORDERPV24H | &quot;CostPerOrderPv24h&quot; |
| COSTPERORDERALLPV24H | &quot;CostPerOrderAllPv24h&quot; |
| COSTPERORDERPC30PV24 | &quot;CostPerOrderPc30Pv24&quot; |
| COSTPERORDERALLPC30PV24 | &quot;CostPerOrderAllPc30Pv24&quot; |
| COSTPERORDERPC30DPV24H | &quot;CostPerOrderPc30dPv24h&quot; |
| COSTPERORDERALLPC30DPV24H | &quot;CostPerOrderAllPc30dPv24h&quot; |
| COSTPERORDERPC7DPV24 | &quot;CostPerOrderPc7dPv24&quot; |
| COSTPERORDERALLPC7DPV24 | &quot;CostPerOrderAllPc7dPv24&quot; |
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
| ORDERVALUEPI | &quot;OrderValuePi&quot; |
| POSTINSTALLORDERVALUE | &quot;PostInstallOrderValue&quot; |
| BOUNCERATE | &quot;BounceRate&quot; |
| COSTPERINSTALLPCPV | &quot;CostPerInstallPcPv&quot; |
| COSTPERINSTALL | &quot;CostPerInstall&quot; |
| COSTPERVISIT | &quot;CostPerVisit&quot; |
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
| INVALIDCLICKS | &quot;InvalidClicks&quot; |
| INVALIDDISPLAYS | &quot;InvalidDisplays&quot; |
| RESULTTYPE | &quot;ResultType&quot; |
| COSTPERQUALIFIEDVISIT | &quot;CostPerQualifiedVisit&quot; |
| COSTPERVISITPV1D | &quot;CostPerVisitPV1D&quot; |
| VISITSPV1D | &quot;VisitsPV1D&quot; |
| ASSISTSPC30DCLIENTATTRIBUTION | &quot;AssistsPc30dClientAttribution&quot; |
| ASSISTSALLPC30DCLIENTATTRIBUTION | &quot;AssistsAllPc30dClientAttribution&quot; |
| ASSISTSCLIENTATTRIBUTION | &quot;AssistsClientAttribution&quot; |
| ASSISTSALLCLIENTATTRIBUTION | &quot;AssistsAllClientAttribution&quot; |
| ASSISTSPC30D | &quot;AssistsPc30d&quot; |
| ASSISTSALLPC30D | &quot;AssistsAllPc30d&quot; |
| ASSISTSPC1D | &quot;AssistsPc1d&quot; |
| ASSISTSALLPC1D | &quot;AssistsAllPc1d&quot; |
| ASSISTSPC7D | &quot;AssistsPc7d&quot; |
| ASSISTSALLPC7D | &quot;AssistsAllPc7d&quot; |
| ASSISTSPC7DPV24 | &quot;AssistsPc7dPv24&quot; |
| ASSISTSALLPC7DPV24 | &quot;AssistsAllPc7dPv24&quot; |
| ASSISTSPC7DPV24H | &quot;AssistsPc7dPv24h&quot; |
| ASSISTSALLPC7DPV24H | &quot;AssistsAllPc7dPv24h&quot; |
| ASSISTSPV24H | &quot;AssistsPv24h&quot; |
| ASSISTSALLPV24H | &quot;AssistsAllPv24h&quot; |
| ASSISTSPC30PV24 | &quot;AssistsPc30Pv24&quot; |
| ASSISTSALLPC30PV24 | &quot;AssistsAllPc30Pv24&quot; |
| ASSISTSPC30DPV24H | &quot;AssistsPc30dPv24h&quot; |
| ASSISTSALLPC30DPV24H | &quot;AssistsAllPc30dPv24h&quot; |
| ASSISTSPIPC | &quot;AssistsPiPc&quot; |
| ASSISTSPIPV | &quot;AssistsPiPv&quot; |
| ASSISTSPIPCPV | &quot;AssistsPiPcPv&quot; |
| ASSISTSSALESRATIOPC30DCLIENTATTRIBUTION | &quot;AssistsSalesRatioPc30dClientAttribution&quot; |
| ASSISTSSALESRATIOALLPC30DCLIENTATTRIBUTION | &quot;AssistsSalesRatioAllPc30dClientAttribution&quot; |
| ASSISTSSALESRATIOCLIENTATTRIBUTION | &quot;AssistsSalesRatioClientAttribution&quot; |
| ASSISTSSALESRATIOALLCLIENTATTRIBUTION | &quot;AssistsSalesRatioAllClientAttribution&quot; |
| ASSISTSSALESRATIOPC30D | &quot;AssistsSalesRatioPc30d&quot; |
| ASSISTSSALESRATIOALLPC30D | &quot;AssistsSalesRatioAllPc30d&quot; |
| ASSISTSSALESRATIOPC1D | &quot;AssistsSalesRatioPc1d&quot; |
| ASSISTSSALESRATIOALLPC1D | &quot;AssistsSalesRatioAllPc1d&quot; |
| ASSISTSSALESRATIOPC7D | &quot;AssistsSalesRatioPc7d&quot; |
| ASSISTSSALESRATIOALLPC7D | &quot;AssistsSalesRatioAllPc7d&quot; |
| ASSISTSSALESRATIOPC7DPV24 | &quot;AssistsSalesRatioPc7dPv24&quot; |
| ASSISTSSALESRATIOALLPC7DPV24 | &quot;AssistsSalesRatioAllPc7dPv24&quot; |
| ASSISTSSALESRATIOPC7DPV24H | &quot;AssistsSalesRatioPc7dPv24h&quot; |
| ASSISTSSALESRATIOALLPC7DPV24H | &quot;AssistsSalesRatioAllPc7dPv24h&quot; |
| ASSISTSSALESRATIOPV24H | &quot;AssistsSalesRatioPv24h&quot; |
| ASSISTSSALESRATIOALLPV24H | &quot;AssistsSalesRatioAllPv24h&quot; |
| ASSISTSSALESRATIOPC30PV24 | &quot;AssistsSalesRatioPc30Pv24&quot; |
| ASSISTSSALESRATIOALLPC30PV24 | &quot;AssistsSalesRatioAllPc30Pv24&quot; |
| ASSISTSSALESRATIOPC30DPV24H | &quot;AssistsSalesRatioPc30dPv24h&quot; |
| ASSISTSSALESRATIOALLPC30DPV24H | &quot;AssistsSalesRatioAllPc30dPv24h&quot; |
| ASSISTSSALESRATIOPIPC | &quot;AssistsSalesRatioPiPc&quot; |
| ASSISTSSALESRATIOPIPV | &quot;AssistsSalesRatioPiPv&quot; |
| ASSISTSSALESRATIOPIPCPV | &quot;AssistsSalesRatioPiPcPv&quot; |
| SALESLC | &quot;SalesLc&quot; |
| SALESALLLC | &quot;SalesAllLc&quot; |
| REVENUEGENERATEDLC | &quot;RevenueGeneratedLc&quot; |
| REVENUEGENERATEDALLLC | &quot;RevenueGeneratedAllLc&quot; |



