

# AdaptiveReadAttributes

The attributes specific to Adaptive creatives read

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callsToAction** | **List&lt;String&gt;** | A Call-to-Action (CTA) is an action-driven instruction to your audience intended to provoke an immediate  response, such as “Buy now” or “Go!”. |  [optional] |
|**colors** | [**AdaptiveColors**](AdaptiveColors.md) |  |  [optional] |
|**descriptionFont** | **String** | Font of the description  Valid supported font like \&quot;Arial\&quot; |  [optional] |
|**descriptionText** | **String** | The description text of the banner |  [optional] |
|**headlineFont** | **String** | Font of the headline  Valid supported font like \&quot;Arial\&quot; |  [optional] |
|**headlineText** | **String** | The headline text of the banner |  [optional] |
|**imageDisplay** | [**ImageDisplayEnum**](#ImageDisplayEnum) | Value can be \&quot;ShowFullImage\&quot; or \&quot;ZoomOnImage\&quot;. Choose whether your image set should fit inside the allocated  space (\&quot;ShowFullImage\&quot;) or whether it should fill that space (\&quot;ZoomOnImage\&quot;). If you choose ZoomOnImage, there may be some  image cropping. |  [optional] |
|**imageSets** | [**List&lt;ImageSet&gt;**](ImageSet.md) | Multiple image sets, each image set consists of multiple images and a headline text. |  [optional] |
|**landingPageUrl** | **URI** | Web redirection of the landing page url |  [optional] |
|**layouts** | [**List&lt;LayoutsEnum&gt;**](#List&lt;LayoutsEnum&gt;) | The Adaptive layouts that are enabled.  It can contain any of the following values: \&quot;Editorial\&quot;, “Montage“, \&quot;InBannerVideo\&quot;. |  [optional] |
|**logos** | [**List&lt;ImageShape&gt;**](ImageShape.md) | Logo images uploaded on demostatic.criteo.com when deploying and then static.criteo.net |  [optional] |
|**videos** | [**List&lt;VideoDetail&gt;**](VideoDetail.md) | Multiple videos potentially in different shapes. |  [optional] |



## Enum: ImageDisplayEnum

| Name | Value |
|---- | -----|
| SHOWFULLIMAGE | &quot;ShowFullImage&quot; |
| ZOOMONIMAGE | &quot;ZoomOnImage&quot; |



## Enum: List&lt;LayoutsEnum&gt;

| Name | Value |
|---- | -----|
| EDITORIAL | &quot;Editorial&quot; |
| MONTAGE | &quot;Montage&quot; |
| INBANNERVIDEO | &quot;InBannerVideo&quot; |



