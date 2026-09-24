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
The specific options for each language are defined in other build.gradle files ([python](generated-sources/python/build.gradle), [java](generated-sources/java/build.gradle) and [php](generated-sources/php/build.gradle)).

This script uses [https://api.criteo.com](https://api.criteo.com) public API.

A clean step has been added to the build process in order to delete the folder of previous generated code.
Otherwise some changes will not be applied by openapi-generator.


## Github Actions

When changes to `api-specifications/**` are pushed to `main`, three workflows fire, one per language:
- Generate Java Sources
- Generate PHP Sources
- Generate Python Sources

Each workflow can also be run manually from the Actions tab (`workflow_dispatch`).

### Generate workflows

Each `generate_*_sources.yml` workflow runs the following pipeline, in order:
1. **Generate** the SDK with `./gradlew :generator:{language}:generateClient`.
2. **Test** the generated SDK against the live API with `python ./scripts/test_sdk.py --language {language}`.
3. **Upload** the generated sources as a workflow artifact (available for download from the run page).
4. **Push** the SDK to the downstream repository (`python ./scripts/push_sdk.py --language {language}`), which is the step that ultimately publishes to MavenCentral / PyPI / Packagist.

### Testing workflows

Pull requests and `update-oas-**` branches are gated by language-specific test workflows that generate and test the SDKs **without** pushing them:
- `test_java.yml`, `test_php.yml`, `test_python.yml` — triggered on pull requests touching `generator/{language}/**` or `api-specifications/**`, and on pushes to `update-oas-**` branches.

A separate `test_scripts.yml` runs `pytest` whenever `scripts/**` changes.

### OAS update workflows

The OpenAPI specifications are kept up to date by three workflows:
- `auto_update_experimental.yml` — runs on a weekly schedule (Monday 16:00 UTC) and on demand; updates the `Experimental` release and commits directly to `main`.
- `auto_update_preview.yml` — same schedule; updates the `Preview` release and commits directly to `main`.
- `update_oas.yml` — manual dispatch only, taking `latest-version` (e.g. `2027-01`) and `release-candidate` (skip cleanup of obsolete versions) inputs; creates an `update-oas-<date>` branch and opens a pull request against `main`.

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
