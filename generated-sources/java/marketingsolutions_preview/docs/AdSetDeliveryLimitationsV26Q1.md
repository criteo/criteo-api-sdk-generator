

# AdSetDeliveryLimitationsV26Q1

Delivery limitations for an ad set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**devices** | [**List&lt;DevicesEnum&gt;**](#List&lt;DevicesEnum&gt;) | List of devices which the ad set should target.                No limitation if the list is empty. |  [optional] |
|**environments** | [**List&lt;EnvironmentsEnum&gt;**](#List&lt;EnvironmentsEnum&gt;) | List of environments which the ad set should target.                No limitation if the list is empty. |  [optional] |
|**operatingSystems** | [**List&lt;OperatingSystemsEnum&gt;**](#List&lt;OperatingSystemsEnum&gt;) | List of operating systems which the ad set should target.                No limitation if the list is empty. |  [optional] |



## Enum: List&lt;DevicesEnum&gt;

| Name | Value |
|---- | -----|
| OTHER | &quot;other&quot; |
| DESKTOP | &quot;desktop&quot; |
| MOBILE | &quot;mobile&quot; |
| TABLET | &quot;tablet&quot; |



## Enum: List&lt;EnvironmentsEnum&gt;

| Name | Value |
|---- | -----|
| WEB | &quot;web&quot; |
| INAPP | &quot;inApp&quot; |



## Enum: List&lt;OperatingSystemsEnum&gt;

| Name | Value |
|---- | -----|
| ANDROID | &quot;android&quot; |
| IOS | &quot;ios&quot; |
| UNKNOWN | &quot;unknown&quot; |



