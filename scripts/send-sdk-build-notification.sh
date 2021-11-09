#!/usr/bin/env bash
set -ex

RUN_ID="$(curl https://api.github.com/repos/criteo/criteo-api-sdk-generator/actions/workflows/$1/runs \
            | jq -r '.workflow_runs[0].id | tostring')"

result=$(curl -X POST --data-urlencode \
"payload={ \
    \"channel\": \"#criteo-api-sdk-generator\", \
    \"username\": \"sdk-generation-bot\", \
    \"text\": \"$2.\n<https://github.com/criteo/criteo-api-sdk-generator/actions/runs/${RUN_ID}|Link to build>\", \
    \"icon_emoji\": \":$3:\"}" \
    $4 )
