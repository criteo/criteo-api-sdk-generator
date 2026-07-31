

# StoreInventoryUpsert

Defines a store inventory to be upserted. Inspired from google spec.See https://developers.google.com/shopping-content/reference/rest/v2.1/localinventory/custombatch#LocalinventoryCustomBatchRequestEntry

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availability** | [**AvailabilityEnum**](#AvailabilityEnum) | Might be: In stock, Out of stock, Preorder, Backorder |  |
|**batchId** | **String** | Identifies this array entry |  |
|**price** | **String** | Product&#39;s price at this store |  |
|**productId** | **String** |  Identifies a product |  |
|**salePrice** | **String** | The sale price of the product. |  [optional] |
|**storeId** | **String** | Identifies the store, for the customer |  |



## Enum: AvailabilityEnum

| Name | Value |
|---- | -----|
| BACKORDER | &quot;backorder&quot; |
| IN_STOCK | &quot;in_stock&quot; |
| OUT_OF_STOCK | &quot;out_of_stock&quot; |
| PREORDER | &quot;preorder&quot; |



