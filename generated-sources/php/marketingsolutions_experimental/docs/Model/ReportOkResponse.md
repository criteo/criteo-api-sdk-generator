# # ReportOkResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_details** | [**\criteo\api\marketingsolutions\experimental\Model\ReportDetailErrors[]**](ReportDetailErrors.md) | The list of errors with details. |
**import_request_timestamp** | **string** | The date when the original batch request was sent. |
**number_of_products_deleted** | **string** | The number of products deleted. |
**number_of_products_in_the_batch** | **string** | The number of products present in the batch. |
**number_of_products_upserted** | **string** | The number of products upserted. |
**number_of_products_with_errors** | **string** | The number of products with errors. |
**number_of_products_with_warnings** | **string** | The number of products with Warnings. |
**status** | **string** | The status of the operation. The operation is completed when the status is one of (VALIDATED,VALIDATED_WITH_ERRORS,FAILED) |
**warning_details** | [**\criteo\api\marketingsolutions\experimental\Model\ReportDetailWarnings[]**](ReportDetailWarnings.md) | The list of Warnings with details. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
