

# FlightLeg

A leg of a flight schedule outlining which days and times the line item will run.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dayOfWeek** | [**DayOfWeekEnum**](#DayOfWeekEnum) | Enum for the days of the week. |  |
|**endTime** | **String** | Wall-clock time of day in HH:mm, 24-hour. No timezone. |  |
|**startTime** | **String** | Wall-clock time of day in HH:mm, 24-hour. No timezone. |  |



## Enum: DayOfWeekEnum

| Name | Value |
|---- | -----|
| SUNDAY | &quot;sunday&quot; |
| MONDAY | &quot;monday&quot; |
| TUESDAY | &quot;tuesday&quot; |
| WEDNESDAY | &quot;wednesday&quot; |
| THURSDAY | &quot;thursday&quot; |
| FRIDAY | &quot;friday&quot; |
| SATURDAY | &quot;saturday&quot; |
| EVERYDAY | &quot;everyday&quot; |
| WEEKDAYS | &quot;weekdays&quot; |
| WEEKENDS | &quot;weekends&quot; |



