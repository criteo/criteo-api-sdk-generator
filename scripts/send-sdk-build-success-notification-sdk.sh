#!/usr/bin/env bash
set -ex

SUITE_AND_RUN_ID="$(curl https://api.github.com/repos/criteo/criteo-api-sdk-generator/actions/workflows/$1/runs \
                | jq -r '.workflow_runs[0] | ((.check_suite_id | tostring) + " "+ (.id | tostring))')"
SUITE_AND_RUN_ID_ARRAY=($SUITE_AND_RUN_ID)
SUITE_ID=${SUITE_AND_RUN_ID_ARRAY[0]}
RUN_ID=${SUITE_AND_RUN_ID_ARRAY[1]}

ARTIFACT_ID="$(curl https://api.github.com/repos/criteo/criteo-api-sdk-generator/actions/runs/${RUN_ID}/artifacts \
                | jq -r '.artifacts[0].id')"

result=$(curl -X POST --data-urlencode \
"payload={ \
    \"channel\": \"#criteo-api-sdk-generator\", \
    \"username\": \"sdk-generation-bot\", \
    \"text\": \"$2 build succeeded.\n<https://github.com/criteo/criteo-api-sdk-generator/actions/runs/${RUN_ID}|Link to build> \n \
<https://github.com/criteo/criteo-api-sdk-generator/suites/${SUITE_ID}/artifacts/${ARTIFACT_ID}|Link to download the artifact>\", \
    \"icon_emoji\": \":green_check_mark:\"}" \
    $3 )
