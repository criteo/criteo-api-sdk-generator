

# CreativeWrite

Entity to create or update a creative

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adaptiveWriteAttributes** | [**AdaptiveWriteAttributes**](AdaptiveWriteAttributes.md) |  |  [optional] |
|**datasetId** | **String** | Dataset linked to the Creative |  |
|**description** | **String** | The description of the creative |  [optional] |
|**dynamicWriteAttributes** | [**DynamicWriteAttributes**](DynamicWriteAttributes.md) |  |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | The format of the creative  You can use \&quot;Image\&quot;, \&quot; HtmlTag\&quot;, \&quot;Dynamic\&quot; or \&quot;Adaptive\&quot; |  |
|**htmlTagWriteAttributes** | [**HtmlTagWriteAttributes**](HtmlTagWriteAttributes.md) |  |  [optional] |
|**imageWriteAttributes** | [**ImageWriteAttributes**](ImageWriteAttributes.md) |  |  [optional] |
|**name** | **String** | The name of the creative |  |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;Image&quot; |
| HTMLTAG | &quot;HtmlTag&quot; |
| DYNAMIC | &quot;Dynamic&quot; |
| ADAPTIVE | &quot;Adaptive&quot; |



