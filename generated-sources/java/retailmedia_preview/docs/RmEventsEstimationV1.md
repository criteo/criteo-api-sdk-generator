

# RmEventsEstimationV1

Settings to target users based on the shopping events

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brandIds** | **Set&lt;String&gt;** |  |  [optional] |
|**categoryIds** | **Set&lt;String&gt;** |  |  [optional] |
|**lookbackDays** | [**LookbackDaysEnum**](#LookbackDaysEnum) |  |  |
|**maxPrice** | **Double** |  |  [optional] |
|**minPrice** | **Double** |  |  [optional] |
|**shopperActivity** | [**ShopperActivityEnum**](#ShopperActivityEnum) |  |  |



## Enum: LookbackDaysEnum

| Name | Value |
|---- | -----|
| LAST7DAYS | &quot;Last7Days&quot; |
| LAST14DAYS | &quot;Last14Days&quot; |
| LAST30DAYS | &quot;Last30Days&quot; |
| LAST45DAYS | &quot;Last45Days&quot; |
| LAST60DAYS | &quot;Last60Days&quot; |
| LAST90DAYS | &quot;Last90Days&quot; |
| LAST120DAYS | &quot;Last120Days&quot; |
| LAST150DAYS | &quot;Last150Days&quot; |
| LAST180DAYS | &quot;Last180Days&quot; |



## Enum: ShopperActivityEnum

| Name | Value |
|---- | -----|
| VIEW | &quot;View&quot; |
| BUY | &quot;Buy&quot; |
| ADDTOCART | &quot;AddToCart&quot; |



