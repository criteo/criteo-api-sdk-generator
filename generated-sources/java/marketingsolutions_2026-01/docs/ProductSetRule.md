

# ProductSetRule

Encapsulate a product rule

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**field** | [**FieldEnum**](#FieldEnum) | The field on which we want to apply the rule |  [optional] |
|**operator** | [**OperatorEnum**](#OperatorEnum) | The operator used with the field |  [optional] |
|**values** | **List&lt;String&gt;** | The values on which we want to apply the rule |  [optional] |



## Enum: FieldEnum

| Name | Value |
|---- | -----|
| OBSOLETE_EXTRADATA | &quot;OBSOLETE_Extradata&quot; |
| CATEGORY1 | &quot;Category1&quot; |
| CATEGORY2 | &quot;Category2&quot; |
| CATEGORY3 | &quot;Category3&quot; |
| EXTERNALITEMID | &quot;ExternalItemId&quot; |
| SALEPRICE | &quot;SalePrice&quot; |
| BRAND | &quot;Brand&quot; |
| CUSTOMLABEL0 | &quot;CustomLabel0&quot; |
| CUSTOMLABEL1 | &quot;CustomLabel1&quot; |
| CUSTOMLABEL2 | &quot;CustomLabel2&quot; |
| CUSTOMLABEL3 | &quot;CustomLabel3&quot; |
| CUSTOMLABEL4 | &quot;CustomLabel4&quot; |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| ISIN | &quot;IsIn&quot; |
| ISNOTIN | &quot;IsNotIn&quot; |
| BETWEEN | &quot;Between&quot; |
| NOTBETWEEN | &quot;NotBetween&quot; |
| LESSTHAN | &quot;LessThan&quot; |
| GREATERTHAN | &quot;GreaterThan&quot; |



