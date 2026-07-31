# # AdaptiveReadAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calls_to_action** | **string[]** | A Call-to-Action (CTA) is an action-driven instruction to your audience intended to provoke an immediate  response, such as “Buy now” or “Go!”. | [optional]
**colors** | [**\criteo\api\marketingsolutions\experimental\Model\AdaptiveColors**](AdaptiveColors.md) |  | [optional]
**description_font** | **string** | Font of the description  Valid supported font like \&quot;Arial\&quot; | [optional]
**description_text** | **string** | The description text of the banner | [optional]
**headline_font** | **string** | Font of the headline  Valid supported font like \&quot;Arial\&quot; | [optional]
**headline_text** | **string** | The headline text of the banner | [optional]
**image_display** | **string** | Value can be \&quot;ShowFullImage\&quot; or \&quot;ZoomOnImage\&quot;. Choose whether your image set should fit inside the allocated  space (\&quot;ShowFullImage\&quot;) or whether it should fill that space (\&quot;ZoomOnImage\&quot;). If you choose ZoomOnImage, there may be some  image cropping. | [optional]
**image_sets** | [**\criteo\api\marketingsolutions\experimental\Model\ImageSet[]**](ImageSet.md) | Multiple image sets, each image set consists of multiple images and a headline text. | [optional]
**landing_page_url** | **string** | Web redirection of the landing page url | [optional]
**layouts** | **string[]** | The Adaptive layouts that are enabled.  It can contain any of the following values: \&quot;Editorial\&quot;, “Montage“, \&quot;InBannerVideo\&quot;. | [optional]
**logos** | [**\criteo\api\marketingsolutions\experimental\Model\ImageShape[]**](ImageShape.md) | Logo images uploaded on demostatic.criteo.com when deploying and then static.criteo.net | [optional]
**videos** | [**\criteo\api\marketingsolutions\experimental\Model\VideoDetail[]**](VideoDetail.md) | Multiple videos potentially in different shapes. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
