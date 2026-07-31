

# StatsReportMessage

A tabular stats report with column headers and data rows. Each row in 'data' is an array of values matching the order of 'columns'.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columns** | **List&lt;String&gt;** | List of column names for the report (e.g. campaignId, sellerId, day, impressions, clicks, cost, etc.) |  [optional] |
|**data** | **List&lt;List&lt;Object&gt;&gt;** | Array of data rows, each row is an array of values matching the columns order |  [optional] |
|**links** | **Object** | Pagination links (empty object if no pagination) |  [optional] |
|**rows** | **Integer** | Total number of data rows in the report |  [optional] |



