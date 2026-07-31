

# AudienceSegmentSearchEntityV1

Available filters to perform a search on audience segments. If present, the filters are AND'ed together when applied.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserIds** | **List&lt;String&gt;** | List of advertiser ids |  [optional] |
|**audienceSegmentIds** | **List&lt;String&gt;** | List of segment ids |  [optional] |
|**audienceSegmentTypes** | [**List&lt;AudienceSegmentTypesEnum&gt;**](#List&lt;AudienceSegmentTypesEnum&gt;) | List of segment types |  [optional] |



## Enum: List&lt;AudienceSegmentTypesEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| INMARKET | &quot;InMarket&quot; |
| PROSPECTING | &quot;Prospecting&quot; |
| CONTACTLIST | &quot;ContactList&quot; |
| LOCATION | &quot;Location&quot; |
| BEHAVIORAL | &quot;Behavioral&quot; |
| RETARGETING | &quot;Retargeting&quot; |
| LOOKALIKE | &quot;Lookalike&quot; |



