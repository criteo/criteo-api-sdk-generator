

# Coupon

Coupons are static images applied on ad set which can be displayed within an ad and link to a landing page.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adSetId** | **String** | The id of the Ad Set on which the Coupon is applied to |  [optional] |
|**advertiserId** | **String** | Advertiser linked to the Coupon |  [optional] |
|**author** | **String** | The login of the person who created this Coupon |  [optional] |
|**description** | **String** | The description of the Coupon |  [optional] |
|**endDate** | **String** | The date when when we will stop to show this Coupon. If the end date is not specified (i.e. null) then the Coupon will go on forever  String must be in ISO8601 format |  [optional] |
|**format** | **String** | Format of the Coupon, it can have two values: \&quot;FullFrame\&quot; or \&quot;LogoZone\&quot; |  [optional] |
|**id** | **String** | Unique identifier (duplicate of the parent id). |  [optional] |
|**images** | [**List&lt;ImageSlide&gt;**](ImageSlide.md) | List of slides containing the image URLs |  [optional] |
|**landingPageUrl** | **String** | Web redirection of the landing page url |  [optional] |
|**name** | **String** | The name of the Coupon |  [optional] |
|**rotationsNumber** | **Integer** | Number of rotations for the Coupons (from 1 to 10 times) |  [optional] |
|**showDuration** | **Integer** | Show Coupon for a duration of N seconds (between 1 and 5) |  [optional] |
|**showEvery** | **Integer** | Show the Coupon every N seconds (between 1 and 10) |  [optional] |
|**startDate** | **String** | The date when the Coupon will be launched  String must be in ISO8601 format |  [optional] |
|**status** | **String** | The status of the Coupon |  [optional] |



