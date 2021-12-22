#!/usr/bin/env bash
# set -ex

# Loop over all PHP generated SDKs
# Install dependencies using composer
# Test using composer

SCRIPT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
GENERATED_PHP_SDKS="${SCRIPT_ROOT}/../generated-sources/php"

echo "Testing SDKs - PHP"

for dir in ${GENERATED_PHP_SDKS}/*/
do
    cd ${dir}
    composer install
    composer test
done
