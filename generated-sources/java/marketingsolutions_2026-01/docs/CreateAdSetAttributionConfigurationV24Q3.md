

# CreateAdSetAttributionConfigurationV24Q3

Create model for an ad set's attribution configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributionMethod** | [**AttributionMethodEnum**](#AttributionMethodEnum) | The attribution method. |  [optional] |
|**lookbackWindow** | [**LookbackWindowEnum**](#LookbackWindowEnum) | The lookback window. Optional, should be specified only for attribution methods PostClick and LastClick. |  [optional] |



## Enum: AttributionMethodEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| CRITEOATTRIBUTION | &quot;criteoAttribution&quot; |
| GOOGLEANALYTICSLASTCLICK | &quot;googleAnalyticsLastClick&quot; |
| GOOGLEANALYTICSDATADRIVEN | &quot;googleAnalyticsDataDriven&quot; |
| LASTCLICK | &quot;lastClick&quot; |
| POSTCLICK | &quot;postClick&quot; |



## Enum: LookbackWindowEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| _30M | &quot;30M&quot; |
| _24H | &quot;24H&quot; |
| _7D | &quot;7D&quot; |
| _30D | &quot;30D&quot; |



