

# ReadAdSetAttributionConfigurationV26Q1

Read model for an ad set's attribution configuration.                The lookback window is only set for ad sets with an attribution method that is postClick or lastClick.  It will be null with any other attribution method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributionMethod** | [**AttributionMethodEnum**](#AttributionMethodEnum) | Ad set attribution method.  This defines how certain events (visits, clicks, sales...) are attributed to the ad set.                Possible values:  - unknown  - criteoAttribution (default attribution method)  - lastClick  - postClick  - sftp  - googleAnalytics (requires Google Analytics integration) |  [optional] |
|**lookbackWindow** | [**LookbackWindowEnum**](#LookbackWindowEnum) | The lookback window. Optional, should be specified only for attribution methods PostClick and LastClick. |  [optional] |



## Enum: AttributionMethodEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| CRITEOATTRIBUTION | &quot;criteoAttribution&quot; |
| LASTCLICK | &quot;lastClick&quot; |
| POSTCLICK | &quot;postClick&quot; |
| SFTP | &quot;sftp&quot; |
| GOOGLEANALYTICS | &quot;googleAnalytics&quot; |



## Enum: LookbackWindowEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| _30M | &quot;30M&quot; |
| _24H | &quot;24H&quot; |
| _7D | &quot;7D&quot; |
| _30D | &quot;30D&quot; |



