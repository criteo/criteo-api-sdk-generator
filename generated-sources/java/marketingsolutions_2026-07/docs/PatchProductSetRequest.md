

# PatchProductSetRequest

Entity to update a product set

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isDraft** | **Boolean** | [optional] New value of product set segment status (draft or active) |  [optional] |
|**minimumNumberOfProducts** | **Integer** | [optional] New minimum number of products of the product set to be patched. This is used to determine if the rules are valid! |  [optional] |
|**name** | **String** | [optional]  New name that will be associated to the product set |  [optional] |
|**rules** | [**List&lt;ProductSetRule&gt;**](ProductSetRule.md) | [optional] New rules that will be associated to the product set |  [optional] |



