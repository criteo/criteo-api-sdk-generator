

# BalanceV1

A Retail Media Balance used to determine the funds available for any or all campaigns in an account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**balanceType** | [**BalanceTypeEnum**](#BalanceTypeEnum) | Type of the balance. |  |
|**createdAt** | **OffsetDateTime** | Creation time of the balance. |  |
|**criteoPoNumber** | **String** | Criteo purchase order number. |  [optional] |
|**deposited** | **Double** | Amount of billable funds allotted to the balance. |  |
|**endDate** | **String** | End date of the balance in the format YYYY-MM-DD. |  [optional] |
|**memo** | **String** | Memo. |  [optional] |
|**name** | **String** | Name of the balance. |  |
|**privateMarketBillingType** | [**PrivateMarketBillingTypeEnum**](#PrivateMarketBillingTypeEnum) | Billing type for Private Market of the balance. |  |
|**remaining** | **Double** | Amount of remaining funds of the balance. |  |
|**retailerId** | **String** | The billing retailer id. |  [optional] |
|**retailerPoNumber** | **String** | Retailer purchase order number. |  [optional] |
|**spendType** | [**SpendTypeEnum**](#SpendTypeEnum) | Spend Type of the balance. |  |
|**spent** | **Double** | Amount of spent funds of the balance. |  |
|**startDate** | **String** | Start date of the balance in the format YYYY-MM-DD. |  |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the balance. |  |
|**updatedAt** | **OffsetDateTime** | Update time of the balance. |  |



## Enum: BalanceTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| CAPPED | &quot;capped&quot; |
| UNCAPPED | &quot;uncapped&quot; |



## Enum: PrivateMarketBillingTypeEnum

| Name | Value |
|---- | -----|
| NOTAPPLICABLE | &quot;notApplicable&quot; |
| BILLBYRETAILER | &quot;billByRetailer&quot; |
| BILLBYCRITEO | &quot;billByCriteo&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: SpendTypeEnum

| Name | Value |
|---- | -----|
| ONSITE | &quot;onsite&quot; |
| OFFSITE | &quot;offsite&quot; |
| OFFSITEAWARENESS | &quot;offsiteAwareness&quot; |
| LOCKOUT | &quot;lockout&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| SCHEDULED | &quot;scheduled&quot; |
| ACTIVE | &quot;active&quot; |
| ENDED | &quot;ended&quot; |



