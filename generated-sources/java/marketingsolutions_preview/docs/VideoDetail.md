

# VideoDetail

Entity consists of the url of the video, its duration and its shape.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**duration** | **Double** | The duration of the video in milliseconds, the video could be trimmed if it is longer than 30000 ms. |  |
|**shape** | [**ShapeEnum**](#ShapeEnum) | Shape of the video |  |
|**url** | **URI** | URL of the video uploaded on demostatic.criteo.com when deploying and then static.criteo.net |  |



## Enum: ShapeEnum

| Name | Value |
|---- | -----|
| HORIZONTAL | &quot;Horizontal&quot; |
| VERTICAL | &quot;Vertical&quot; |
| SQUARE | &quot;Square&quot; |



