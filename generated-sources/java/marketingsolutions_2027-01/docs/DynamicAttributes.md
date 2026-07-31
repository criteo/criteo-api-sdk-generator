

# DynamicAttributes

The attributes specific to Dynamic creatives

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bodyTextColor** | **String** | Color of the creative&#39;s body text  Valid hexadecimal color (e.g. \&quot;AB00FF\&quot;) |  [optional] |
|**callsToAction** | **List&lt;String&gt;** | A Call-to-Action (CTA) is an action-driven instruction to your audience intended to provoke an immediate  response, such as “Buy now” or “Go!”. |  [optional] |
|**creativeBackgroundColor** | **String** | Color of the creative&#39;s background  Valid hexadecimal color (e.g. \&quot;AB00FF\&quot;) |  [optional] |
|**logos** | [**List&lt;ImageShape&gt;**](ImageShape.md) | Logo images uploaded on demostatic.criteo.com when deploying and then static.criteo.net |  [optional] |
|**pricesColor** | **String** | Color of the creative&#39;s prices  Valid hexadecimal color (e.g. \&quot;AB00FF\&quot;) |  [optional] |
|**primaryFont** | **String** | Font of the primary font  Valid supported font like \&quot;Arial\&quot; |  [optional] |
|**productImageDisplay** | [**ProductImageDisplayEnum**](#ProductImageDisplayEnum) | Value can be \&quot;ShowFullImage\&quot; or \&quot;ZoomOnImage\&quot;. Choose whether your product catalog images should fit inside the allocated  space (\&quot;ShowFullImage\&quot;) or whether they should fill that space (\&quot;ZoomOnImage\&quot;). If you choose ZoomOnImage, there may be some  image cropping. |  [optional] |



## Enum: ProductImageDisplayEnum

| Name | Value |
|---- | -----|
| SHOWFULLIMAGE | &quot;ShowFullImage&quot; |
| ZOOMONIMAGE | &quot;ZoomOnImage&quot; |



