

# ExternalRetailMediaAccountV2

The details for a newly created account

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countryIds** | **List&lt;String&gt;** | list of countries associated with the account |  [optional] |
|**currencyId** | **String** | the currency for the account |  [optional] |
|**name** | **String** | account name |  [optional] |
|**onBehalfCompanyName** | **String** | On behalf entity name of ads for the Digital Services Act |  [optional] |
|**parentAccountLabel** | **String** | parent account label for the account |  [optional] |
|**payingCompanyName** | **String** | Paying entity name of ads for the Digital Services Act |  [optional] |
|**subType** | [**SubTypeEnum**](#SubTypeEnum) | subtype for the account |  [optional] |
|**timeZone** | **String** | the timezone for the account |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type for the account |  [optional] |



## Enum: SubTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| BRAND | &quot;brand&quot; |
| SELLER | &quot;seller&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| SUPPLY | &quot;supply&quot; |
| DEMAND | &quot;demand&quot; |



