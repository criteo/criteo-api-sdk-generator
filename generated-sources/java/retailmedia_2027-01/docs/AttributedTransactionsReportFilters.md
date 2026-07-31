

# AttributedTransactionsReportFilters

Array-valued constraints for attributed-transactions reporting. Exactly one of accountIds, campaignIds, or lineItemIds is required.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountIds** | **List&lt;String&gt;** |  |  [optional] |
|**campaignIds** | **List&lt;String&gt;** |  |  [optional] |
|**lineItemIds** | **List&lt;String&gt;** |  |  [optional] |
|**mediaTypes** | [**List&lt;MediaTypesEnum&gt;**](#List&lt;MediaTypesEnum&gt;) |  |  [optional] |



## Enum: List&lt;MediaTypesEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| VIDEO | &quot;video&quot; |
| DISPLAY | &quot;display&quot; |
| ALL | &quot;all&quot; |



