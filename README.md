[![Generate Java Sources](https://github.com/criteo/criteo-api-sdk-generator/actions/workflows/generate_java_sources.yml/badge.svg)](https://github.com/criteo/criteo-api-sdk-generator/actions/workflows/generate_java_sources.yml)
[![Generate PHP Sources](https://github.com/criteo/criteo-api-sdk-generator/actions/workflows/generate_php_sources.yml/badge.svg)](https://github.com/criteo/criteo-api-sdk-generator/actions/workflows/generate_php_sources.yml)
[![Generate Python Sources](https://github.com/criteo/criteo-api-sdk-generator/actions/workflows/generate_python_sources.yml/badge.svg)](https://github.com/criteo/criteo-api-sdk-generator/actions/workflows/generate_python_sources.yml)
[![Generate Postman Collections](https://github.com/criteo/criteo-api-sdk-generator/actions/workflows/generate_and_push_postman.yml/badge.svg)](https://github.com/criteo/criteo-api-sdk-generator/actions/workflows/generate_and_push_postman.yml)

# Criteo API - Clients

This project generates code for the client libraries for [Criteo's API](https://developers.criteo.com/)
* **Java**: the SDKs are available on the [criteo/criteo-api-java-sdk](https://github.com/criteo/criteo-api-java-sdk) repository and MavenCentral ([criteo-api-retailmedia-sdk](https://central.sonatype.com/artifact/com.criteo/criteo-api-retailmedia-sdk), [criteo-api-marketingsolutions-sdk](https://central.sonatype.com/artifact/com.criteo/criteo-api-marketingsolutions-sdk) and [criteo-api-commercegrid-sdk](https://central.sonatype.com/artifact/com.criteo/criteo-api-commercegrid-sdk))
* **Python**: the SDKs are available on the [criteo/criteo-api-python-sdk](https://github.com/criteo/criteo-api-python-sdk) repository and on Pypi ([criteo-api-retailmedia-sdk](https://pypi.org/project/criteo-api-retailmedia-sdk/), [criteo-api-marketingsolutions-sdk](https://pypi.org/project/criteo-api-marketingsolutions-sdk/) and [criteo-api-commercegrid-sdk](https://pypi.org/project/criteo-api-commercegrid-sdk/) )
* **PHP**: the SDKs are available on the [criteo/criteo-api-retailmedia-php-sdk](https://github.com/criteo/criteo-api-retailmedia-php-sdk), [criteo/criteo-api-marketingsolutions-php-sdk](https://github.com/criteo/criteo-api-marketingsolutions-php-sdk) and [criteo/criteo-api-commercegrid-php-sdk](https://github.com/criteo/criteo-api-commercegrid-php-sdk) repositories and on Packagist ([criteo-api-retailmedia-sdk](https://packagist.org/packages/criteo/criteo-api-retailmedia-sdk), [criteo-api-marketingsolutions-sdk](https://packagist.org/packages/criteo/criteo-api-marketingsolutions-sdk) and [criteo-api-commercegrid-sdk](https://packagist.org/packages/criteo/criteo-api-commercegrid-sdk)).

In addition it generates Postman API documentation and publishes it [to the Criteo's Postman space](https://www.postman.com/realcriteo). If you are a user looking for more information about Criteo API on Postman please check [this guide](https://developers.criteo.com/marketing-solutions/docs/use-postman-with-the-criteo-marketing-solutions-api).

## Generate the clients

To generate the Java code, run:

```bash 
./gradlew :generator:java:generateClient
```

The generated code can be found under `generated-sources/java` folder.

To generate the Python code, run:

```bash 
./gradlew :generator:python:generateClient
```

The generated code can be found under `generated-sources/python` folder.

To generate the PHP code, run:

```bash 
./gradlew :generator:php:generateClient
```

The generated code can be found under `generated-sources/php` folder.

## Modify templates

You can modify the generated code by changing the templates.
For example, the authentication token auto refresh feature is implemented in 
`generator/{language}/resources/templates/rest.mustache`.

If a template is missing, for example for python sdk, you can copy it from the original repository [Python templates](https://github.com/OpenAPITools/openapi-generator/tree/master/modules/openapi-generator/src/main/resources/python).

## Build Process

The generation of the clients is wrapped in a [buid.gradle](build.gradle) file.
The specific options for each language are defined in other build.gradle files ([python](generated-sources/python/build.gradle), [java](generated-sources/php/build.gradle) and [php](generated-sources/java/build.gradle)).

This script uses [https://api.criteo.com](https://api.criteo.com) public API.

A clean step has been added to the build process in order to delete the folder of previous generated code.
Otherwise some changes will not be applied by openapi-generator.


## Github Actions
Each time a push is done, three separate actions for each of the languages are fired :
- Generate Java Sources
- Generate PHP Sources
- Generate Python Sources

Each of workflows generates output for a respective language.

There is also Generate All Sources action that is runnable on demand from Actions tab.

After running a workflow:
* artefacts will be generated and available for download.
* Postman collections will be generated and published.

### Postman collections
Postman collections are generated only within Github Actions. 

The Postman generation workflow doesn't save artifacts, but instead publishes them
directly  to the Criteo space on Postman.
If you would like to run Postman workflow generation locally you can also use
[nektos/act](https://github.com/nektos/act) to ease automation and testing.

To generate the Postman generation GitHub Action locally make sure Docker is installed and run:

```bash 
act -W .github/workflows/generate_and_push_postman.yml
```


## Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
