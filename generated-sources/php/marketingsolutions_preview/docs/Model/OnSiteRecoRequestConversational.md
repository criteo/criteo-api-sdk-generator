# # OnSiteRecoRequestConversational

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_id** | **int** | Id of the Ad. This field is optional, it allows to setup Reco controls at Ad level. | [optional]
**ad_set_id** | **int** | Id of the AdSet. This field is optional and is resolved automatically for adsets previously configured. |
**conversation** | [**\criteo\api\marketingsolutions\preview\Model\OnSiteRecoChatMessage[]**](OnSiteRecoChatMessage.md) | Conversation between the user and the agent. |
**nb_requested_products** | **int** | Amount of products to recommend. |
**partner_id** | **int** | Id of the partner. |
**product** | [**\criteo\api\marketingsolutions\preview\Model\ProductContext**](ProductContext.md) |  | [optional]
**user_id** | **string** | Used to retrieve user events from Criteo trackers. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
