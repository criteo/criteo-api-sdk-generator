# # ProductsCustomBatchRequestEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **int** | An entry ID, unique within the batch request. | [optional]
**feed_id** | **string** | Not used by Criteo. | [optional]
**item_group_id** | **string** | Deprecated (providing this information is no more needed, this field will be removed in next release). The itemGroupId of the product to delete. To be defined when the method is delete and the product is a variant. | [optional]
**merchant_id** | **int** | The ID of the managing account. Criteo: the partnerId. |
**method** | **string** | The method of the batch entry. |
**product** | [**\criteo\api\marketingsolutions\experimental\Model\Product**](Product.md) |  | [optional]
**product_id** | **string** | The Product ID to delete. Only defined if the method is delete. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
