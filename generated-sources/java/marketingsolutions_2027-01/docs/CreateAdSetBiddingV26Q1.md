

# CreateAdSetBiddingV26Q1

ad set bidding create model

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bidAmount** | **Double** | Decimal value target relating to the &#x60;bidStrategy&#x60; specified. May be &#x60;null&#x60; for strategies that do not require a target value. At most 4 decimals are supported. Additional decimals are rounded. |  [optional] |
|**costController** | [**CostControllerEnum**](#CostControllerEnum) | How spend is controlled |  |



## Enum: CostControllerEnum

| Name | Value |
|---- | -----|
| COS | &quot;COS&quot; |
| MAXCPC | &quot;maxCPC&quot; |
| CPI | &quot;CPI&quot; |
| CPM | &quot;CPM&quot; |
| CPO | &quot;CPO&quot; |
| CPSV | &quot;CPSV&quot; |
| CPV | &quot;CPV&quot; |
| DAILYBUDGET | &quot;dailyBudget&quot; |
| TARGETCPM | &quot;targetCPM&quot; |



