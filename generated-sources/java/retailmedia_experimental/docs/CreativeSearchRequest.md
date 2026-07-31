

# CreativeSearchRequest

Creative search request model

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brandIds** | **List&lt;String&gt;** | Brand Id of the search filter |  [optional] |
|**creativeIds** | **List&lt;String&gt;** | Search Id |  [optional] |
|**creativeName** | **String** | Name to search |  [optional] |
|**creativeTypes** | [**List&lt;CreativeTypesEnum&gt;**](#List&lt;CreativeTypesEnum&gt;) | Creative type |  [optional] |
|**pageTypes** | [**List&lt;PageTypesEnum&gt;**](#List&lt;PageTypesEnum&gt;) | Page type |  [optional] |
|**retailerIds** | **List&lt;String&gt;** | RetailerId of the search filter |  [optional] |
|**templateIds** | **List&lt;String&gt;** | Id of the template this creative was created on |  [optional] |



## Enum: List&lt;CreativeTypesEnum&gt;

| Name | Value |
|---- | -----|
| COMMERCEDISPLAY | &quot;CommerceDisplay&quot; |
| COMMERCEVIDEO | &quot;CommerceVideo&quot; |
| STANDARDVIDEO | &quot;StandardVideo&quot; |
| STANDARDDISPLAY | &quot;StandardDisplay&quot; |



## Enum: List&lt;PageTypesEnum&gt;

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



