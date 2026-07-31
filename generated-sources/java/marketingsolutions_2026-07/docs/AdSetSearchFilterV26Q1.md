

# AdSetSearchFilterV26Q1

Filter on ad set ids.                Multiple filters are combined with an implicit AND operation.  Identifiers are string-encoded integers; invalid values are ignored.  If no filter is provided (both arrays are null or empty), the search returns all accessible campaigns.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adSetIds** | **List&lt;String&gt;** | Ad set ids to filter on. Ids are string-encoded integers. |  [optional] |
|**advertiserIds** | **List&lt;String&gt;** | Advertiser ids which ad sets belongs to (indirectly via their marketing campaign).  Ids are string-encoded integers. |  [optional] |
|**campaignIds** | **List&lt;String&gt;** | Campaign ids to filter on. Ids are string-encoded integers. |  [optional] |



