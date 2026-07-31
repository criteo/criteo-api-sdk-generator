

# InMarketCreateV1

Settings to target users based on high shopping intents and demographics.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brandIds** | **Set&lt;String&gt;** | Choose the brands your segment might be interested in |  [optional] |
|**buyingPower** | [**Set&lt;BuyingPowerEnum&gt;**](#Set&lt;BuyingPowerEnum&gt;) | Reach people who frequently purchase high price range items to lower price range items |  [optional] |
|**country** | **String** | Reach people of a specific country |  |
|**gender** | [**GenderEnum**](#GenderEnum) | Reach people who’ve shown interest in products made for a specific gender |  [optional] |
|**interestIds** | **Set&lt;String&gt;** | Reach new people based on their interests |  [optional] |
|**priceRange** | [**Set&lt;PriceRangeEnum&gt;**](#Set&lt;PriceRangeEnum&gt;) | Reach people who’ve shown interest in products within a specific price range |  [optional] |



## Enum: Set&lt;BuyingPowerEnum&gt;

| Name | Value |
|---- | -----|
| LOW | &quot;Low&quot; |
| MEDIUM | &quot;Medium&quot; |
| HIGH | &quot;High&quot; |
| VERYHIGH | &quot;VeryHigh&quot; |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| MALE | &quot;Male&quot; |
| FEMALE | &quot;Female&quot; |



## Enum: Set&lt;PriceRangeEnum&gt;

| Name | Value |
|---- | -----|
| LOW | &quot;Low&quot; |
| MEDIUM | &quot;Medium&quot; |
| HIGH | &quot;High&quot; |



