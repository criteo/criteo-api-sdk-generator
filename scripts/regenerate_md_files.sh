#!/bin/bash -e

OAS_FILE=criteo-api.json

createMd() {
	ROUTE="$1"
	TAG="$2"
	OPERATIONID="$3"
	DESCRIPTION="$4"

	LOWERCASE_OPERATIONID=$(echo $OPERATIONID | tr '[:upper:]' '[:lower:]')
	MD_FILE="$TAG/$LOWERCASE_OPERATIONID.md"

	echo "---" > "$MD_FILE"
	echo "title: $ROUTE" >>  "$MD_FILE"
	echo "excerpt: $DESCRIPTION" >> "$MD_FILE"
	echo "api:" >> "$MD_FILE"
	echo "  file: $OAS_FILE" >> "$MD_FILE"
	echo "  operationId: $OPERATIONID" >> "$MD_FILE"
	echo "hidden: false" >> "$MD_FILE"
	echo "---" >> "$MD_FILE"
}

createTagIndexMd() {
	TITLE="$1"

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

for ROUTE_TAG_OPERATIONID_DESC in $(cat ../$OAS_FILE | sed 's/\\n/tempPlaceholderForSlashN/g' | jq -r '.paths | keys[] as $path | .[$path] | keys[] as $verb | .[$verb] | .tags[] as $tag | [ $path, $tag, .operationId, .description ] | join("#")' | tr ' ' '\1'); do
	INPUT="$(echo $ROUTE_TAG_OPERATIONID_DESC | tr '\1' ' ' | sed 's/tempPlaceholderForSlashN/\\n/g')"
	ROUTE="$(echo $INPUT | cut -d# -f1)"
	TAG="$(echo $INPUT| cut -d# -f2 | tr '[:upper:]' '[:lower:]')"
	OPERATIONID="$(echo $INPUT| cut -d# -f3)"
	if [[ -z "$OPERATIONID" ]]; then
		OPERATIONID=placeholder # TODO
	fi
	DESCRIPTION="$(echo $INPUT| cut -d# -f4)"

	mkdir -p "$TAG"
	createMd $ROUTE $TAG $OPERATIONID "$DESCRIPTION"
done

for DIR in *; do
	echo "- $DIR" >> _order.yaml
	pushd "$DIR"
	for MDFILE in *md; do
		echo "- $(basename $MDFILE .md)" >> "_order.yaml"
	done

	createTagIndexMd "$DIR"
	popd
done

