#!/usr/bin/env bash
set -ex

RUN_ID="$(curl https://api.github.com/repos/criteo/criteo-api-sdk-generator/actions/workflows/$1/runs \
            | jq -r '.workflow_runs[0].id | tostring')"

$(curl -X POST --data-urlencode \
"payload={ \
    \"channel\": \"#criteo-api-sdk-generator\",\
    \"username\": \"sdk-generation-bot\", \
    \"text\": \"$2 build failed.\n <https://github.com/criteo/criteo-api-sdk-generator/actions/runs/${RUN_ID}|Link to build>, \
    \"icon_emoji\": \":x:\"}" \
https://hooks.slack.com/services/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)
