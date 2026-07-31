

# Creative202210

A creative entity

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**associatedLineItemIds** | **List&lt;String&gt;** | Associated Line Item Ids |  [optional] |
|**brandId** | **Long** | Brand Id |  [optional] |
|**creativeFormatType** | [**CreativeFormatTypeEnum**](#CreativeFormatTypeEnum) | Creative format type |  |
|**environments** | [**List&lt;PageTypeEnvironment202210&gt;**](PageTypeEnvironment202210.md) | Environment type (e.g. mobile, web, app) |  |
|**formatId** | **Integer** | Format Id |  |
|**id** | **String** |  |  [optional] |
|**name** | **String** | Name |  |
|**retailerId** | **Integer** | Retailer Id |  |
|**status** | [**StatusEnum**](#StatusEnum) | Creative Status |  |
|**templateId** | **Integer** | Template Id |  |
|**templateName** | **String** | Template Name |  |
|**templateVariableValues** | [**List&lt;TemplateVariableValue&gt;**](TemplateVariableValue.md) | The template chosen values |  |
|**updatedAt** | **OffsetDateTime** | Updated at time |  [optional] |



## Enum: CreativeFormatTypeEnum

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



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| READY | &quot;Ready&quot; |
| IN_USE | &quot;In_Use&quot; |
| ARCHIVED | &quot;Archived&quot; |
| DELETED | &quot;Deleted&quot; |



