

# TemplateVariable

A variable in a creative template

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**choiceVariableSpecification** | [**ChoiceVariableSpecification**](ChoiceVariableSpecification.md) |  |  [optional] |
|**filesVariablesSpecification** | [**FilesVariablesSpecification**](FilesVariablesSpecification.md) |  |  [optional] |
|**id** | **String** | The id of the variable |  |
|**required** | **Boolean** | Whether the variable is required |  |
|**textVariableSpecification** | [**TextVariableSpecification**](TextVariableSpecification.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the variable |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TEXT | &quot;Text&quot; |
| CHOICE | &quot;Choice&quot; |
| COLOR | &quot;Color&quot; |
| FILES | &quot;Files&quot; |
| HYPERLINK | &quot;Hyperlink&quot; |
| VIDEO | &quot;Video&quot; |



