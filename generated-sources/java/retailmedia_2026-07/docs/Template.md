

# Template

A template for creating creatives.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allCollectionsMandatory** | **Boolean** | Marks whether or not all collections are mandatory |  |
|**createdAt** | **OffsetDateTime** | The time at which the template was created |  |
|**creativeFormat** | [**CreativeFormatEnum**](#CreativeFormatEnum) | The kind of creative this template can be used to build. |  |
|**displayableSkusMax** | **Integer** | Maximum number of displayable skus |  [optional] |
|**id** | **String** |  |  [optional] |
|**name** | **String** | The name of the template |  |
|**sections** | [**List&lt;Section&gt;**](Section.md) | The sections holding various template variables |  |
|**skuCollectionMax** | **Integer** | Maximum number of skus in the collection |  [optional] |
|**skuCollectionMin** | **Integer** | Minimum number of skus in the collection |  |
|**skuPerCollectionMax** | **Integer** | Maximum number of skus per collection |  [optional] |
|**skuPerCollectionMin** | **Integer** | Minimum number of skus per collection |  |
|**updatedAt** | **OffsetDateTime** | The time at which the template was updated |  |



## Enum: CreativeFormatEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| FLAGSHIP | &quot;FlagShip&quot; |
| SHOWCASE | &quot;Showcase&quot; |
| SPONSOREDPRODUCTS | &quot;SponsoredProducts&quot; |
| BUTTERFLY | &quot;Butterfly&quot; |
| BUNDLEBOOST | &quot;BundleBoost&quot; |
| IAB | &quot;IAB&quot; |
| CUSTOM | &quot;CUSTOM&quot; |
| DISPLAYPANEL | &quot;DisplayPanel&quot; |
| DIGITALSHELFTALKER | &quot;DigitalShelfTalker&quot; |
| COMMERCEVIDEOSPOTLIGHT | &quot;CommerceVideoSpotlight&quot; |
| BRANDINGVIDEOSTANDOUT | &quot;BrandingVideoStandout&quot; |
| COMMERCEDISPLAYSPOTLIGHT | &quot;CommerceDisplaySpotlight&quot; |
| BRANDINGDISPLAYSPOTLIGHTSOLO | &quot;BrandingDisplaySpotlightSolo&quot; |
| COMMERCEDISPLAYGRIDSHELF | &quot;CommerceDisplayGridShelf&quot; |
| COMMERCEDISPLAYGRIDDUET | &quot;CommerceDisplayGridDuet&quot; |
| BRANDINGDISPLAYGRIDSOLO | &quot;BrandingDisplayGridSolo&quot; |
| COMMERCEVIDEOGRIDDUET | &quot;CommerceVideoGridDuet&quot; |



