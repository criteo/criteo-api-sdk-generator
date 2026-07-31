

# AdSetFrequencyCappingV26Q1

Ad set frequency capping.                Settings that can limit the number of impression by viewer and by period.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**frequency** | [**FrequencyEnum**](#FrequencyEnum) | Period on which impression limitation is calculated.                Possible values:  - hourly  - daily  - lifetime  - advanced |  [optional] |
|**maximumImpressions** | **Integer** | Maximum impressions for the specified period. |  [optional] |



## Enum: FrequencyEnum

| Name | Value |
|---- | -----|
| HOURLY | &quot;hourly&quot; |
| DAILY | &quot;daily&quot; |
| LIFETIME | &quot;lifetime&quot; |
| ADVANCED | &quot;advanced&quot; |



