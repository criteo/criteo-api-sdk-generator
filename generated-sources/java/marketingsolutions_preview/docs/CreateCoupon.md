

# CreateCoupon

Entity to create a Coupon

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adSetId** | **String** | The id of the Ad Set on which the Coupon is applied to |  |
|**description** | **String** | The description of the Coupon |  [optional] |
|**endDate** | **String** | The date when when we will stop to show this Coupon. If the end date is not specified (i.e. null) then the Coupon will go on forever  String must be in ISO8601 format |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | Format of the Coupon, it can have two values: \&quot;FullFrame\&quot; or \&quot;LogoZone\&quot; |  |
|**images** | [**List&lt;CreateImageSlide&gt;**](CreateImageSlide.md) | List of slides containing the images as a base-64 encoded string |  |
|**landingPageUrl** | **String** | Web redirection of the landing page url |  |
|**name** | **String** | The name of the Coupon |  |
|**rotationsNumber** | **Integer** | Number of rotations for the Coupons (from 1 to 10 times) |  |
|**showDuration** | **Integer** | Show Coupon for a duration of N seconds (between 1 and 5) |  |
|**showEvery** | **Integer** | Show the Coupon every N seconds (between 1 and 10) |  |
|**startDate** | **String** | The date when the coupon will be launched  String must be in ISO8601 format |  |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| FULLFRAME | &quot;FullFrame&quot; |
| LOGOZONE | &quot;LogoZone&quot; |



