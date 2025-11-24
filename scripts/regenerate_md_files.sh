#!/bin/bash -e
set -o pipefail

OAS_FILE="$1"

createMd() {
	ROUTE="$1"
	TAG="$2"
	OPERATIONID="$3"
	DESCRIPTION="$4"

	LOWERCASE_OPERATIONID=$(echo $OPERATIONID | tr '[:upper:]' '[:lower:]')
	MD_FILE="$TAG/$LOWERCASE_OPERATIONID.md"

	echo "---" > "$MD_FILE"
	echo "title: $ROUTE" >>  "$MD_FILE"
	echo "excerpt: \"$DESCRIPTION\"" >> "$MD_FILE" # double-quote to turn \n to new lines
	echo "api:" >> "$MD_FILE"
	echo "  file: $OAS_FILE" >> "$MD_FILE"
	echo "  operationId: $OPERATIONID" >> "$MD_FILE"
	echo "hidden: false" >> "$MD_FILE"
	echo "---" >> "$MD_FILE"

	echo "- $LOWERCASE_OPERATIONID" >> "$TAG/_order.yaml"
}

createTagIndexMd() {
	TITLE="$(echo "$1" |  sed -e 's/\([A-Z]\)/ \1/g' -e 's/^ //')"

	echo "---" > index.md
	echo "title: ${TITLE^}" >> index.md
	echo "excerpt: ''" >> index.md
	echo "deprecated: false" >> index.md
	echo "hidden: false" >> index.md
	echo "metadata:" >> index.md
	echo "  title: ''" >> index.md
	echo "  description: ''" >> index.md
	echo "  robots: index" >> index.md
	echo "next:" >> index.md
	echo "  description: ''" >> index.md
	echo "---" >> index.md
}

cd reference
rm -rf "Criteo API" && mkdir "Criteo API" && cd "Criteo API"

for ROUTE_TAG_OPERATIONID_DESC in $(cat ../$OAS_FILE | sed 's/\\n/tempPlaceholderForSlashN/g' | jq -r '.paths | keys_unsorted[] as $path | .[$path] | keys_unsorted[] as $verb | .[$verb] | try .tags[] as $tag | [ $path, $verb, $tag, .operationId, .description ] | join("#")' | tr ' ' '\1'); do
	INPUT="$(echo $ROUTE_TAG_OPERATIONID_DESC | tr '\1' ' ' | sed 's/tempPlaceholderForSlashN/\\n/g')"
	ROUTE="$(echo $INPUT | cut -d# -f1)"
	VERB="$(echo $INPUT | cut -d# -f2)"
	TAG="$(echo $INPUT| cut -d# -f3)"
	OPERATIONID="$(echo $INPUT| cut -d# -f4)"
	if [[ -z "$OPERATIONID" ]]; then
		# 'sed' to replace only the first slash, then 'tr' to replace all remaining ones
		OPERATIONID=$(echo $VERB$ROUTE | sed 's#/#_#' | tr '/' '-' | tr '[:upper:]' '[:lower:]')
	fi
	DESCRIPTION="$(echo $INPUT| cut -d# -f5)"

	mkdir -p "$TAG"
	createMd $ROUTE $TAG $OPERATIONID "$DESCRIPTION"
done

for DIR in *; do
	echo "- $DIR" >> _order.yaml

	pushd "$DIR"
	createTagIndexMd "$DIR"
	popd
done

