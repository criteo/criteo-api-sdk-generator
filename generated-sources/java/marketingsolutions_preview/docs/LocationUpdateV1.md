

# LocationUpdateV1

Settings to target users based on their location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pointsOfInterest** | [**List&lt;PointOfInterestV1&gt;**](PointOfInterestV1.md) | Reach users which have been historically located in the given coordinates |  [optional] |
|**radiusInKm** | **Integer** | Radius in kilometers |  [optional] |
|**registryType** | [**RegistryTypeEnum**](#RegistryTypeEnum) | The kind of Location audience |  [optional] |



## Enum: RegistryTypeEnum

| Name | Value |
|---- | -----|
| POINTOFINTEREST | &quot;PointOfInterest&quot; |



