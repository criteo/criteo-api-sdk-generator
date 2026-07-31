# # SponsoredProductsLineItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bid_strategy** | **string** | Bid strategy for the line item. | [optional]
**budget** | **float** | The total budget allocated for this line item. | [optional]
**budget_remaining** | **float** | The amount of the budget that remains available. |
**budget_spent** | **float** | The amount of the budget that has been spent so far. | [optional]
**campaign_id** | **string** | The ID of the campaign this line item belongs to. |
**created_at** | **\DateTime** | The date and time when the line item was created. |
**daily_pacing** | **float** | The daily pacing limit for budget spending. | [optional]
**end_date** | **\DateTime** | The date and time when the line item stops running. | [optional]
**flight_schedule** | [**\criteo\api\retailmedia\v2027_01\Model\FlightSchedule**](FlightSchedule.md) |  | [optional]
**is_auto_daily_pacing** | **bool** | Indicates whether automatic daily pacing is enabled. | [optional]
**keyword_strategy** | **string** | The keyword targeting strategy for this line item. | [optional]
**max_bid** | **float** | The maximum bid amount allowed for this line item. | [optional]
**monthly_pacing** | **float** | The monthly pacing limit for budget spending. | [optional]
**name** | **string** | The name of the line item. |
**optimization_strategy** | **string** | The optimization strategy for this line item. | [optional]
**start_date** | **\DateTime** | The date and time when the line item starts running. |
**status** | **string** | The current status of the line item. | [optional]
**target_bid** | **float** | The target bid amount for the line item. | [optional]
**target_retailer_id** | **string** | The ID of the retailer targeted by this line item. |
**updated_at** | **\DateTime** | The date and time when the line item was last updated. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
