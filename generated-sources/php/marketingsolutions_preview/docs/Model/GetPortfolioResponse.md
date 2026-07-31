# # GetPortfolioResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**\criteo\api\marketingsolutions\preview\Model\EntityOfPortfolioMessage[]**](EntityOfPortfolioMessage.md) | The response�s primary data | [optional]
**errors** | [**\criteo\api\marketingsolutions\preview\Model\CriteoApiError[]**](CriteoApiError.md) | Error list returned by the Criteo API  For successful requests it is empty | [optional]
**warnings** | [**\criteo\api\marketingsolutions\preview\Model\CriteoApiWarning[]**](CriteoApiWarning.md) | Warnings list returned by the Criteo API  In some situations the operations are successful but it may be useful to issue warnings to the API consumer.  For example the endpoint, entity or field is deprecated. Warnings are like compiler warnings, they indicate that problems may occur in the future. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
