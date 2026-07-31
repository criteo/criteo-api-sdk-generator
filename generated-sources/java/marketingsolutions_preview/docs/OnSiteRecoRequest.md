

# OnSiteRecoRequest

Recommendation request parameters

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adId** | **Integer** | Id of the Ad. This field is optional, it allows to setup Reco controls at Ad level. |  [optional] |
|**adSetId** | **Integer** | Id of the AdSet. This field is optional and is resolved automatically for adsets previously configured. |  [optional] |
|**identityType** | [**IdentityTypeEnum**](#IdentityTypeEnum) | Type of the user identifier (CtoBundle, Idfa, Gaid...) Optional if its type is CtoBundle |  [optional] |
|**nbRequestedProducts** | **Integer** | Amount of products to recommend. |  |
|**partnerId** | **Integer** | Id of the partner. |  |
|**userId** | **String** | Used to retrieve user events from Criteo trackers. |  [optional] |



## Enum: IdentityTypeEnum

| Name | Value |
|---- | -----|
| CTOBUNDLE | &quot;CtoBundle&quot; |
| IDFA | &quot;Idfa&quot; |
| GAID | &quot;Gaid&quot; |
| INTERNALUSERID | &quot;InternalUserId&quot; |



