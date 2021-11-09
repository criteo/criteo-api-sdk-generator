#!/usr/bin/env bash
set -ex

SUITE_AND_RUN_ID = "$(curl https://api.github.com/repos/criteo/criteo-api-sdk-generator/actions/workflows/$1/runs \
                | jq -r '.workflow_runs[0] | ((.check_suite_id | tostring) +" "+ (.id | tostring))')"
SUITE_ID = ($SUITE_AND_RUN_ID)[0]
RUN_ID = ($SUITE_AND_RUN_ID)[1]

ARTIFACT_ID = "$(curl https://api.github.com/repos/criteo/criteo-api-sdk-generator/actions/runs/${RUN_ID}/artifacts \
                | jq -r '.artifacts[0].id | tostring')"

$(curl -X POST --data-urlencode \
"payload={
    \"channel\": \"#criteo-api-sdk-generator\",
    \"username\": \"sdk-generation-bot\", \
    \"text\": \"$2 build succeeded.\n Link to build https://github.com/criteo/criteo-api-sdk-generator/actions/runs/${RUN_ID} \n
    Link to download the artifact https://github.com/criteo/criteo-api-sdk-generator/suites/${SUITE_ID}/artifacts/${ARTIFACT_ID}\",
    \"icon_emoji\": \":heavy_check_mark:\"}"
https://hooks.slack.com/services/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)
