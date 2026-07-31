

# DynamicWriteAttributes

The attributes specific to create or update a Dynamic creative

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bodyTextColor** | **String** | Color of the creative&#39;s body text  Valid hexadecimal color (e.g. \&quot;AB00FF\&quot;) |  |
|**callsToAction** | **List&lt;String&gt;** | A Call-to-Action (CTA) is an action-driven instruction to your audience intended to provoke an immediate  response, such as “Buy now” or “Go!”. |  |
|**creativeBackgroundColor** | **String** | Color of the creative&#39;s background  Valid hexadecimal color (e.g. \&quot;AB00FF\&quot;) |  [optional] |
|**logoBase64String** | **String** | Logo image as a base-64 encoded string |  |
|**pricesColor** | **String** | Color of the creative&#39;s prices  Valid hexadecimal color (e.g. \&quot;AB00FF\&quot;) |  |
|**primaryFont** | **String** | Font of the primary font  Valid supported font like \&quot;Arial\&quot; |  [optional] |
|**productImageDisplay** | [**ProductImageDisplayEnum**](#ProductImageDisplayEnum) | Value can be \&quot;ShowFullImage\&quot; or \&quot;ZoomOnImage\&quot;. Choose whether your product catalog images should fit inside the allocated  space (\&quot;ShowFullImage\&quot;) or whether they should fill that space (\&quot;ZoomOnImage\&quot;). If you choose ZoomOnImage, there may be some  image cropping. |  |



## Enum: ProductImageDisplayEnum

| Name | Value |
|---- | -----|
| SHOWFULLIMAGE | &quot;ShowFullImage&quot; |
| ZOOMONIMAGE | &quot;ZoomOnImage&quot; |



