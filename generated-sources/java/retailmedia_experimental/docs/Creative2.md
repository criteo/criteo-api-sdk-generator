

# Creative2

A creative entity

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**associatedLineItemIds** | **List&lt;String&gt;** | Associated Line Item Ids |  [optional] |
|**brandId** | **Long** | Brand Id |  [optional] |
|**creativeFormatV2Type** | [**CreativeFormatV2TypeEnum**](#CreativeFormatV2TypeEnum) | Creative format type |  |
|**environments** | [**List&lt;PageTypeEnvironment2&gt;**](PageTypeEnvironment2.md) | Environment type (e.g. mobile, web, app) |  |
|**formatId** | **Integer** | Format Id |  |
|**id** | **String** |  |  [optional] |
|**name** | **String** | Name |  |
|**retailerId** | **Integer** | Retailer Id |  |
|**status** | [**StatusEnum**](#StatusEnum) | Creative Status |  |
|**templateId** | **Integer** | Template Id |  |
|**templateName** | **String** | Template Name |  |
|**templateVariableValues** | [**List&lt;TemplateVariableValue&gt;**](TemplateVariableValue.md) | The template chosen values |  |
|**updatedAt** | **OffsetDateTime** | Updated at time |  [optional] |



## Enum: CreativeFormatV2TypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| FLAGSHIP | &quot;FlagShip&quot; |
| SHOWCASE | &quot;Showcase&quot; |
| SPONSOREDPRODUCTS | &quot;SponsoredProducts&quot; |
| BUTTERFLY | &quot;Butterfly&quot; |
| BUNDLEBOOST | &quot;BundleBoost&quot; |
| IAB | &quot;IAB&quot; |
| CUSTOM | &quot;Custom&quot; |
| DISPLAYPANEL | &quot;DisplayPanel&quot; |
| DIGITALSHELFTALKER | &quot;DigitalShelfTalker&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| READY | &quot;Ready&quot; |
| INUSE | &quot;InUse&quot; |
| ARCHIVED | &quot;Archived&quot; |
| DELETED | &quot;Deleted&quot; |



