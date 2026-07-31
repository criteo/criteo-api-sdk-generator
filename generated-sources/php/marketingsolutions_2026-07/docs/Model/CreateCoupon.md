# # CreateCoupon

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_set_id** | **string** | The id of the Ad Set on which the Coupon is applied to |
**description** | **string** | The description of the Coupon | [optional]
**end_date** | **string** | The date when when we will stop to show this Coupon. If the end date is not specified (i.e. null) then the Coupon will go on forever  String must be in ISO8601 format | [optional]
**format** | **string** | Format of the Coupon, it can have two values: \&quot;FullFrame\&quot; or \&quot;LogoZone\&quot; |
**images** | [**\criteo\api\marketingsolutions\v2026_07\Model\CreateImageSlide[]**](CreateImageSlide.md) | List of slides containing the images as a base-64 encoded string |
**landing_page_url** | **string** | Web redirection of the landing page url |
**name** | **string** | The name of the Coupon |
**rotations_number** | **int** | Number of rotations for the Coupons (from 1 to 10 times) |
**show_duration** | **int** | Show Coupon for a duration of N seconds (between 1 and 5) |
**show_every** | **int** | Show the Coupon every N seconds (between 1 and 10) |
**start_date** | **string** | The date when the coupon will be launched  String must be in ISO8601 format |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
