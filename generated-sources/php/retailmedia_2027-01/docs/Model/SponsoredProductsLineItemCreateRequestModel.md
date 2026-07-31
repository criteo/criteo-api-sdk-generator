# # SponsoredProductsLineItemCreateRequestModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bid_strategy** | **string** | The bidding strategy for this line item.  Default value is manual. | [optional] [default to 'manual']
**budget** | **float** | The total budget allocated for this line item. | [optional]
**daily_pacing** | **float** | The daily pacing limit for budget spending. | [optional]
**end_date** | **\DateTime** | The date and time when the line item stops running. | [optional]
**flight_schedule** | [**\criteo\api\retailmedia\v2027_01\Model\FlightSchedule**](FlightSchedule.md) |  | [optional]
**is_auto_daily_pacing** | **bool** | Indicates whether automatic daily pacing is enabled.  Default value is false. | [optional] [default to false]
**keyword_strategy** | **string** | The keyword targeting strategy for this line item. | [optional]
**max_bid** | **float** | The maximum bid amount allowed for this line item. | [optional]
**monthly_pacing** | **float** | The monthly pacing limit for budget spending. | [optional]
**name** | **string** | The name of the line item. |
**optimization_strategy** | **string** | The optimization strategy to use for this line item.  Default value is Conversion. | [optional] [default to 'conversion']
**start_date** | **\DateTime** | The date and time when the line item starts running. |
**target_bid** | **float** | The target bid amount for the line item. | [optional]
**target_retailer_id** | **string** | The ID of the retailer to target for this line item. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
