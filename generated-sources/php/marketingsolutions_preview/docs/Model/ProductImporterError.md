# # ProductImporterError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **string** | A MACHINE-READABLE error code string in kebab-case. Unique across Criteo |
**detail** | **string** | A HUMAN-READABLE detailed explanation specific to this occurrence of the problem. This should not be more that 1 paragraph |
**instance** | **string** | A MACHINE-READABLE URI reference that identifies the specific occurrence of the problem. This could be useful when we want to the return the API Endpoint identifying the exact resource related to the error. |
**title** | **string** | A short, HUMAN-READABLE summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
**trace_id** | **string** | The MACHINE-READABLE correlation ID provided by the gateway |
**type** | **string** | A MACHINE-READABLE code specifying error category. This information is used on client side to focus on certain type of error, to either retry some processing or display only certain type of errors. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
