

# SellerCatalogRequestV2

Used to request a catalog of seller SKUs

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**includeFields** | [**List&lt;IncludeFieldsEnum&gt;**](#List&lt;IncludeFieldsEnum&gt;) | Out of the optional fields, only the ones specified will be included in the catalog generated. |  [optional] |
|**modifiedAfter** | **OffsetDateTime** | Only products modified after this time will be returned. |  [optional] |
|**sellers** | [**List&lt;SellerIdentifierV2&gt;**](SellerIdentifierV2.md) | A list of sellers to restrict the catalog to. |  [optional] |



## Enum: List&lt;IncludeFieldsEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| DESCRIPTION | &quot;Description&quot; |
| IMAGEURL | &quot;ImageUrl&quot; |
| GOOGLECATEGORY | &quot;GoogleCategory&quot; |
| RETAILERNAME | &quot;RetailerName&quot; |
| CATEGORY | &quot;Category&quot; |
| BRANDNAME | &quot;BrandName&quot; |



