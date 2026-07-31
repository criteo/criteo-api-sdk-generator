

# AdSetSearchRequestMetadataV26Q1

Optional metadata for searching ad sets

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fields** | [**List&lt;FieldsEnum&gt;**](#List&lt;FieldsEnum&gt;) | List of fields to include in the response. If null or omitted, all fields are returned.  When only a subset of fields is projected, non-projected fields will have default values (e.g. null, 0, or enum defaults) which may not reflect the actual ad set state. Do not interpret non-projected fields as meaningful data. |  [optional] |



## Enum: List&lt;FieldsEnum&gt;

| Name | Value |
|---- | -----|
| NAME | &quot;Name&quot; |
| ADVERTISERID | &quot;AdvertiserId&quot; |
| DATASETID | &quot;DatasetId&quot; |
| CAMPAIGNID | &quot;CampaignId&quot; |
| DESTINATIONENVIRONMENT | &quot;DestinationEnvironment&quot; |
| OBJECTIVE | &quot;Objective&quot; |
| SCHEDULE | &quot;Schedule&quot; |
| BIDDING | &quot;Bidding&quot; |
| TARGETING | &quot;Targeting&quot; |
| BUDGET | &quot;Budget&quot; |
| MEDIATYPE | &quot;MediaType&quot; |
| VIDEOCHANNEL | &quot;VideoChannel&quot; |
| ATTRIBUTIONCONFIGURATION | &quot;AttributionConfiguration&quot; |



