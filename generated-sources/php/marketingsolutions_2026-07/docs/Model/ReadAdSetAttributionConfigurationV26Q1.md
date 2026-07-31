# # ReadAdSetAttributionConfigurationV26Q1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribution_method** | **string** | Ad set attribution method.  This defines how certain events (visits, clicks, sales...) are attributed to the ad set.                Possible values:  - unknown  - criteoAttribution (default attribution method)  - lastClick  - postClick  - sftp  - googleAnalytics (requires Google Analytics integration) | [optional]
**lookback_window** | **string** | The lookback window. Optional, should be specified only for attribution methods PostClick and LastClick. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
