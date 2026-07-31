# # GenerateCreativesReportRequestAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_formats** | **string[]** | Optional list of ad formats to filter on. If empty, all ad formats will be included. | [optional]
**ad_ids** | **string[]** | Optional list of ad IDs to filter on. If empty, all ads will be included. | [optional]
**ad_names** | **string[]** | Optional list of ad names to filter on. If empty, all ads will be included. | [optional]
**ad_set_ids** | **string[]** | Optional list of ad set IDs to filter on. If empty, all ad sets will be included. | [optional]
**ad_set_status** | **string[]** | Optional list of ad set statuses to filter on. If empty, all ad sets will be included. | [optional]
**advertiser_ids** | **string[]** | List of advertiser IDs to report on. The advertisers must already exist. At least one advertiser ID should be provided. |
**campaign_ids** | **string[]** | Optional list of marketing campaign IDs to filter on. If empty, all campaigns will be included. | [optional]
**coupon_ids** | **string[]** | Optional list of coupon IDs to filter on. If empty, all coupons will be included. | [optional]
**coupon_names** | **string[]** | Optional list of coupon names to filter on. If empty, all coupons will be included. | [optional]
**dimensions** | **string[]** | List of dimensions for the report. At least one dimension should be provided. |
**display_sizes** | **string[]** | Optional list of display sizes to filter on. If empty, all display sizes will be included. &lt;br /&gt;&lt;br /&gt; Most common values: &#39;Native&#39;, &#39;Skyscraper&#39;, &#39;HalfPage&#39;, &#39;MediumBanner&#39;, &#39;LargeBanner&#39;, &#39;LeaderBoard&#39;, &#39;WideLeaderBoard&#39;, &#39;Other placements&#39;, &#39;Others&#39;. | [optional]
**end_date** | **\DateTime** | End date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. |
**metrics** | **string[]** | List of metrics for the report. At least one metric should be provided. |
**start_date** | **\DateTime** | Start date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. Must be ≤ endDate. |
**timezone** | **string** | Optional timezone used for the report. Timezone Database format (Tz). | [optional] [default to 'UTC']

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
