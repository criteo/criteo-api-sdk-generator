

# TargetingEntity

Represents either an allowlisting or a blocklisting rule

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**Set&lt;EntityFilter&gt;**](EntityFilter.md) |  |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | Can be either BLOCKLIST or ALLOWLIST |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Can be either DOMAIN or BUNDLE |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| BLOCKLIST | &quot;BLOCKLIST&quot; |
| ALLOWLIST | &quot;ALLOWLIST&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DOMAIN | &quot;DOMAIN&quot; |
| BUNDLE | &quot;BUNDLE&quot; |



