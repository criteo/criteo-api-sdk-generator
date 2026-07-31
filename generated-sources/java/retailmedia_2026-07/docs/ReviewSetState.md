

# ReviewSetState

A Phrase-ReviewState pair describing an update to a keyword review

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**phrase** | **String** | Normalized key phrase for keyword review to update |  |
|**reviewState** | [**ReviewStateEnum**](#ReviewStateEnum) | Keyword review state to set for a phrase |  |



## Enum: ReviewStateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| INREVIEW | &quot;InReview&quot; |
| RECOMMENDED | &quot;Recommended&quot; |
| APPROVED | &quot;Approved&quot; |
| AUTOAPPROVED | &quot;AutoApproved&quot; |
| REJECTED | &quot;Rejected&quot; |
| AUTOREJECTED | &quot;AutoRejected&quot; |



