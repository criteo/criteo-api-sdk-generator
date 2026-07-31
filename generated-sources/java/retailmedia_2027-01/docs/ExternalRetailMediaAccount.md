

# ExternalRetailMediaAccount

The details for a newly created account

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**companyName** | **String** | Paying entity name of ads for the Digital Services Act |  [optional] |
|**countryIds** | **List&lt;String&gt;** | list of countries associated with the account |  [optional] |
|**currencyId** | **String** | the currency for the account |  [optional] |
|**name** | **String** | account name |  [optional] |
|**onBehalfCompanyName** | **String** | On behalf entity name of ads for the Digital Services Act |  [optional] |
|**parentAccountLabel** | **String** | parent account label for the account |  [optional] |
|**subType** | [**SubTypeEnum**](#SubTypeEnum) | subtype for the account |  [optional] |
|**timeZone** | **String** | the timezone for the account |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type for the account |  [optional] |



## Enum: SubTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| BRAND | &quot;Brand&quot; |
| SELLER | &quot;Seller&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| SUPPLY | &quot;Supply&quot; |
| DEMAND | &quot;Demand&quot; |



