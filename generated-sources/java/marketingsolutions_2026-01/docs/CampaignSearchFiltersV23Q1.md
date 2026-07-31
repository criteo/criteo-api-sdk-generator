

# CampaignSearchFiltersV23Q1

Filters for searching campaigns.                Multiple filters are combined with an implicit AND operation.  Identifiers are string-encoded integers; invalid values are ignored.  If no filter is provided (both arrays are null or empty), the search returns all accessible campaigns.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserIds** | **List&lt;String&gt;** | Advertiser IDs to filter on (string-encoded integers). |  [optional] |
|**campaignIds** | **List&lt;String&gt;** | Campaign IDs to filter on (string-encoded integers). |  [optional] |



