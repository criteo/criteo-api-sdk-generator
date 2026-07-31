# # AsyncUnfilledPlacementsReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_server_type** | **string** | Filter on the type of the ad server: criteo, gam, all | [optional] [default to 'all']
**campaign_type** | **string** | Filter on the type of the campaign: onsite display, onsite sponsored products, all | [optional] [default to 'all']
**dimensions** | **string[]** | List of dimensions to report on |
**end_date** | **\DateTime** | End date |
**format** | **string** | Format of the output | [optional] [default to 'json']
**metrics** | **string[]** | List of metrics to report on |
**start_date** | **\DateTime** | Start date |
**supply_account_ids** | **string[]** | Supply account ids to report on |
**timezone** | **string** | Time zone : see criteo developer portal for supported time zones | [optional] [default to 'UTC']

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
