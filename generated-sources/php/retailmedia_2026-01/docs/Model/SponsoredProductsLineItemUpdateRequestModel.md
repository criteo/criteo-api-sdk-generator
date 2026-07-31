# # SponsoredProductsLineItemUpdateRequestModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bid_strategy** | **string** | The bid strategy for the line item. | [optional] [default to 'manual']
**budget** | **float** | The total budget allocated for this line item. | [optional]
**daily_pacing** | **float** | The daily pacing amount for the line item. | [optional]
**end_date** | **\DateTime** | The date and time when the line item stops running. | [optional]
**flight_schedule** | [**\criteo\api\retailmedia\v2026_01\Model\FlightSchedule**](FlightSchedule.md) |  | [optional]
**is_auto_daily_pacing** | **bool** | True if daily pacing is automatic, false if manual. |
**max_bid** | **float** | The maximum bid amount for the line item. | [optional]
**monthly_pacing** | **float** | The monthly pacing amount for the line item. | [optional]
**name** | **string** | The name of this line item. |
**optimization_strategy** | **string** | The optimization strategy for the line item. | [optional] [default to 'conversion']
**start_date** | **\DateTime** | The date and time when the line item starts running. |
**status** | **string** | The current status of the line item. |
**target_bid** | **float** | The target bid amount for the line item. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
