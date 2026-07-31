

# CreativeSearchResponse

Creative search response model

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brandId** | **String** | Brand Id of the search filter |  [optional] |
|**createdAt** | **OffsetDateTime** | Time search is created |  [optional] |
|**creativeType** | [**CreativeTypeEnum**](#CreativeTypeEnum) | Creative type |  [optional] |
|**lineItems** | **List&lt;String&gt;** | The list of lineitems |  [optional] |
|**modifiedAt** | **OffsetDateTime** | Time it&#39;s modified |  [optional] |
|**name** | **String** | Name of the creative |  [optional] |
|**pageType** | [**List&lt;PageTypeEnum&gt;**](#List&lt;PageTypeEnum&gt;) | Page type |  [optional] |
|**preview** | **String** | Preview url of the creative |  [optional] |
|**retailerId** | **String** | RetailerId of the search filter |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The search status |  [optional] |
|**templateId** | **String** | Template Id |  [optional] |



## Enum: CreativeTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| COMMERCEDISPLAY | &quot;CommerceDisplay&quot; |
| COMMERCEVIDEO | &quot;CommerceVideo&quot; |
| STANDARDVIDEO | &quot;StandardVideo&quot; |
| STANDARDDISPLAY | &quot;StandardDisplay&quot; |



## Enum: List&lt;PageTypeEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| SEARCH | &quot;Search&quot; |
| HOME | &quot;Home&quot; |
| BROWSE | &quot;Browse&quot; |
| CHECKOUT | &quot;Checkout&quot; |
| CATEGORY | &quot;Category&quot; |
| PRODUCTDETAIL | &quot;ProductDetail&quot; |
| CONFIRMATION | &quot;Confirmation&quot; |
| MERCHANDISING | &quot;Merchandising&quot; |
| DEALS | &quot;Deals&quot; |
| FAVORITES | &quot;Favorites&quot; |
| SEARCHBAR | &quot;SearchBar&quot; |
| CATEGORYMENU | &quot;CategoryMenu&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| READY | &quot;Ready&quot; |
| IN_USE | &quot;In Use&quot; |
| ARCHIVED | &quot;Archived&quot; |



