# # ProductShipping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **string** | The CLDR territory code of the country to which an item will ship. | [optional]
**location_group_name** | **string** | The location where the shipping is applicable, represented by a location group name. | [optional]
**location_id** | **int** | The numeric ID of a location that the shipping rate applies to as defined in the AdWords API. | [optional]
**postal_code** | **string** | The postal code range that the shipping rate applies to, represented by a postal code, a postal code prefix followed by a * wildcard, a range between two postal codes or two postal code prefixes of equal length. | [optional]
**price** | [**\criteo\api\marketingsolutions\preview\Model\Price**](Price.md) |  | [optional]
**region** | **string** | The geographic region to which a shipping rate applies. | [optional]
**service** | **string** | A free-form description of the service class or delivery speed. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
