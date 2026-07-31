

# ProductsCustomBatchRequestEntry

A product event for a batch request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batchId** | **Long** | An entry ID, unique within the batch request. |  [optional] |
|**feedId** | **String** | Not used by Criteo. |  [optional] |
|**itemGroupId** | **String** | Deprecated (providing this information is no more needed, this field will be removed in next release). The itemGroupId of the product to delete. To be defined when the method is delete and the product is a variant. |  [optional] |
|**merchantId** | **Integer** | The ID of the managing account. Criteo: the partnerId. |  |
|**method** | [**MethodEnum**](#MethodEnum) | The method of the batch entry. |  |
|**product** | [**Product**](Product.md) |  |  [optional] |
|**productId** | **String** | The Product ID to delete. Only defined if the method is delete. |  [optional] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| DELETE | &quot;delete&quot; |
| INSERT | &quot;insert&quot; |



