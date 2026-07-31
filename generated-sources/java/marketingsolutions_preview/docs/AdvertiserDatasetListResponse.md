

# AdvertiserDatasetListResponse

Get datasets response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**List&lt;EntityV2OfDataset&gt;**](EntityV2OfDataset.md) | The response’s primary data |  [optional] |
|**errors** | [**List&lt;CommonProblem&gt;**](CommonProblem.md) | Error list returned by the Criteo API  For successful requests it is empty |  [optional] |
|**warnings** | [**List&lt;CriteoApiWarningV2&gt;**](CriteoApiWarningV2.md) | Warnings list returned by the Criteo API  In some situations the operations are successful but it may be useful to issue warnings to the API consumer.  For example the endpoint, entity or field is deprecated. Warnings are like compiler warnings, they indicate that problems may occur in the future. |  [optional] |



