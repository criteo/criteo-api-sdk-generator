# Run command on each SDK

LANGUAGE=$1

case $LANGUAGE in
    "java")
        TEST_COMMAND="mvn test"
        CLEAN_COMMAND="mvn clean"
        ;;
    *)
        echo "Tests not supported for language $LANGUAGE"
        exit 1
        ;;
esac

for dir in generated-sources/$LANGUAGE/*/
do
    cd $dir

    dir=${dir%*/}
    echo "[INFO] Running command: \"$TEST_COMMAND\" for SDK ${dir##*/}"
    $TEST_COMMAND
    echo "[INFO] Command \"$TEST_COMMAND\" Successful. Cleaning..."
    $CLEAN_COMMAND
    echo "[INFO] Clean successful"

    cd ../../..
done
