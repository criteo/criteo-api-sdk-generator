

# LocationV1

Settings to target users based on their location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pointsOfInterest** | [**List&lt;PointOfInterestV1&gt;**](PointOfInterestV1.md) | Reach users which have been historically located in the given coordinates |  [optional] |
|**radiusInKm** | **Integer** | The expected maximum distance in kilometers between a user and a point of interest |  [optional] |
|**registryType** | [**RegistryTypeEnum**](#RegistryTypeEnum) | The kind of Location audience |  [optional] |



## Enum: RegistryTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| POINTOFINTEREST | &quot;PointOfInterest&quot; |



