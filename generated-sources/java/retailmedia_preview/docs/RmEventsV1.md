

# RmEventsV1

Settings to target users based on their behavior

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brandIds** | **List&lt;String&gt;** | The list of brand ids |  [optional] |
|**categoryIds** | **List&lt;String&gt;** | The list of category ids |  [optional] |
|**lookbackDays** | [**LookbackDaysEnum**](#LookbackDaysEnum) | The number of days to look back |  [optional] |
|**maxPrice** | **Double** | Maximum price of the products |  [optional] |
|**minPrice** | **Double** | Minimum price of the products |  [optional] |
|**shopperActivity** | [**ShopperActivityEnum**](#ShopperActivityEnum) | Reach people who performed specific action |  [optional] |



## Enum: LookbackDaysEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
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
| UNKNOWN | &quot;Unknown&quot; |
| VIEW | &quot;View&quot; |
| BUY | &quot;Buy&quot; |
| ADDTOCART | &quot;AddToCart&quot; |



