

# OnSiteRecoRequestConversational

Conversational recommendation request parameters

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adId** | **Integer** | Id of the Ad. This field is optional, it allows to setup Reco controls at Ad level. |  [optional] |
|**adSetId** | **Integer** | Id of the AdSet. This field is optional and is resolved automatically for adsets previously configured. |  |
|**conversation** | [**List&lt;OnSiteRecoChatMessage&gt;**](OnSiteRecoChatMessage.md) | Conversation between the user and the agent. |  |
|**nbRequestedProducts** | **Integer** | Amount of products to recommend. |  |
|**partnerId** | **Integer** | Id of the partner. |  |
|**product** | [**ProductContext**](ProductContext.md) |  |  [optional] |
|**userId** | **String** | Used to retrieve user events from Criteo trackers. |  |



