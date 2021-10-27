package com.criteo.marketing.examples;

import com.criteo.marketing.ApiClient;
import com.criteo.marketing.ApiException;
import com.criteo.marketing.ApiResponse;
import com.criteo.marketing.Configuration;
import com.criteo.marketing.api.AnalyticsApi;
import com.criteo.marketing.model.StatisticsReportQueryMessage;
import java.time.OffsetDateTime;
import java.util.Arrays;
import java.util.List;

public class StatisticsApplication {
    public static void main(String[] args) {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setUsername("client-id");
        client.setPassword("client-secret");

        // Uncomment the following line to enable debugging logs.
        // client.setDebugging(true);

        AnalyticsApi myApi = new AnalyticsApi(client);
        List<StatisticsReportQueryMessage.DimensionsEnum> dimensions = Arrays.asList(StatisticsReportQueryMessage.DimensionsEnum.ADSET);
        List<String> metrics = Arrays.asList("Clicks");
        OffsetDateTime startDate = OffsetDateTime.parse("2019-01-01");
        OffsetDateTime endDate = OffsetDateTime.parse("2019-01-31");

        StatisticsReportQueryMessage statisticsReportQueryMessage = new StatisticsReportQueryMessage();

        statisticsReportQueryMessage.dimensions(dimensions);
        statisticsReportQueryMessage.metrics(metrics);
        statisticsReportQueryMessage.startDate(startDate);
        statisticsReportQueryMessage.endDate(endDate);
        statisticsReportQueryMessage.currency("EUR");
        statisticsReportQueryMessage.format("Csv");
        try {
            ApiResponse<byte[]> response = myApi.getAdsetReportWithHttpInfo (statisticsReportQueryMessage);
        } catch (ApiException e) {
            System.out.println(e.getCode());
            System.out.println(e.getResponseBody());
        }
    }
}