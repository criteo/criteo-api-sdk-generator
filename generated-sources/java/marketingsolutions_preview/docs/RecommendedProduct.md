

# RecommendedProduct

Represents a recommended product.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alternativeClickUrl** | **String** | Url leading to product details page and also used to track user click. It&#39;s relying on a custom product URL field in the catalog. |  [optional] |
|**brand** | **String** | Product brand. |  [optional] |
|**clickUrl** | **String** | Url leading to product details page and also used to track user click |  [optional] |
|**description** | **String** | Product description. |  [optional] |
|**googleCategory** | **String** | Product google category. |  [optional] |
|**hasVariants** | **Boolean** | Whether the product has variants available. |  [optional] |
|**imageUrl** | **String** | Product image. |  [optional] |
|**name** | **String** | Product name |  [optional] |
|**price** | **Double** | Product price. |  [optional] |
|**productExternalId** | **String** | Product external id. Same id than what is used in user events |  [optional] |
|**relevanceLabel** | [**RelevanceLabelEnum**](#RelevanceLabelEnum) | Product Relevance label |  [optional] |
|**relevancyScore** | **Double** | Product Relevancy score |  [optional] |
|**retailPrice** | **Double** | Product retail price. |  [optional] |



## Enum: RelevanceLabelEnum

| Name | Value |
|---- | -----|
| SIMILAR | &quot;Similar&quot; |
| RELEVANT | &quot;Relevant&quot; |



