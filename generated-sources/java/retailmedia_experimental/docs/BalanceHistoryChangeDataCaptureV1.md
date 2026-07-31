

# BalanceHistoryChangeDataCaptureV1

Data model represents the data change capture of balance history.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**changeDetails** | [**ChangeDetailsV1**](ChangeDetailsV1.md) |  |  |
|**changeType** | [**ChangeTypeEnum**](#ChangeTypeEnum) | Represent the type of change states of the history. |  |
|**dateOfModification** | **OffsetDateTime** | Date when data change has occured. |  |
|**memo** | **String** | Memo associate with the insertion order modification. |  [optional] |
|**modifiedByUser** | **String** | Username who modified the insertion order. |  |



## Enum: ChangeTypeEnum

| Name | Value |
|---- | -----|
| BALANCECREATED | &quot;balanceCreated&quot; |
| BALANCEADDED | &quot;balanceAdded&quot; |
| BALANCEREMOVED | &quot;balanceRemoved&quot; |
| BALANCEUNCAPPED | &quot;balanceUncapped&quot; |
| BALANCECAPPED | &quot;balanceCapped&quot; |
| ENDDATE | &quot;endDate&quot; |
| STARTDATE | &quot;startDate&quot; |
| BALANCENAME | &quot;balanceName&quot; |
| RETAILERPONUMBER | &quot;retailerPoNumber&quot; |
| CRITEOPONUMBER | &quot;criteoPoNumber&quot; |
| RETAILERID | &quot;retailerId&quot; |
| VALUEADD | &quot;valueAdd&quot; |
| UNKNOWN | &quot;unknown&quot; |



