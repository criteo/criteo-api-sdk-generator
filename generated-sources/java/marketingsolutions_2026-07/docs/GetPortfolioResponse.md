

# GetPortfolioResponse

Portfolio fetch Response

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**List&lt;EntityOfPortfolioMessage&gt;**](EntityOfPortfolioMessage.md) | The response�s primary data |  [optional] |
|**errors** | [**List&lt;CriteoApiError&gt;**](CriteoApiError.md) | Error list returned by the Criteo API  For successful requests it is empty |  [optional] |
|**warnings** | [**List&lt;CriteoApiWarning&gt;**](CriteoApiWarning.md) | Warnings list returned by the Criteo API  In some situations the operations are successful but it may be useful to issue warnings to the API consumer.  For example the endpoint, entity or field is deprecated. Warnings are like compiler warnings, they indicate that problems may occur in the future. |  [optional] |



