technology_stack = 'java8'
name_separator = '.'

config_template = files('generatorConfiguration.yaml')
generate_config_sh = find_program('generate_config.sh')
templates_dir = meson.current_source_dir() / 'resources' / 'templates'
client_output_dir = generated_clients_dir_name / language

foreach spec_path : api_specifications
  parsed_api_name = fs.stem(spec_path).to_lower()
  api_name_split = parsed_api_name.split('_')
  assert(
    api_name_split.length() == 2,
    'API name must be in the format <service>_<version>',
  )
  criteo_service = api_name_split[0]
  criteo_api_version = api_name_split[1].replace('-', '_')
  is_preview_version = criteo_api_version == 'preview'

  client_output_dir_per_version = client_output_dir / parsed_api_name

  version_in_namespace = criteo_api_version
  if not is_preview_version
    version_in_namespace = f'v@version_in_namespace@'
  endif

  # example : criteo.api.marketingsolutions.v2021_10
  namespace_base = f'@criteo_package@.@criteo_service@.@version_in_namespace@'.replace('.', name_separator)

  artifact_version = is_preview_version ? '0' : criteo_api_version.replace('_', '.')
  # example : 2021.01.0.211110 for stable , 0.0.211110 for preview
  artifact_version += f'.@generator_version@.@formatted_date@'

  # 'com' is Java-specific => example: com.criteo.api.marketingsolutions.v2021_10
  namespace_base = f'com.@namespace_base@'

  # useful when you want templates to be part of the SDK generated
  sdk_main_dir = 'src' / 'main' / 'java' / 'com' / 'criteo' / 'api' / criteo_service / version_in_namespace
  sdk_test_dir = 'src' / 'test' / 'java' / 'com' / 'criteo' / 'api' / criteo_service / version_in_namespace

  task_base_name = f'@criteo_service@-@version_in_namespace@:@language@:sdk'

  sdk_config = custom_target(
    f'@task_base_name@:config',
    command: [generate_config_sh, config_template, sdk_main_dir, sdk_test_dir],
    capture: true,
    output: f'@criteo_service@-@version_in_namespace@.yaml',
  )

  additional_properties = [
    'artifactDescription=@0@ SDK for Criteo API @1@ for @2@ version'.format(language.to_upper(), criteo_service, criteo_api_version),
    f'artifactUrl=https://github.com/criteo/criteo-api-@language@-sdk',
    'dateLibrary=technology_stack',
    'developerEmail=open-source@criteo.com',
    'developerName=Criteo',
    'developerOrganization=Criteo',
    'developerOrganizationUrl=https://www.criteo.com/',
    'disallowAdditionalPropertiesIfNotPresent=false',
    'generateApiTests=false',
    'generateModelTests=false',
    'hideGenerationTimestamp=true',
    'licenseName=Apache License version 2.0',
    'licenseUrl=https://www.apache.org/licenses/LICENSE-2.0.txt',
    'removeOperationIdPrefix=true',
    f'scmConnection=scm:git:git://github.com/criteo/criteo-api-@language@-sdk.git',
    f'scmDeveloperConnection=scm:git:ssh://github.com:criteo/criteo-api-@language@-sdk.git',
    f'scmUrl=https://github.com/criteo/criteo-api-@language@-sdk',
    f'sdkTestDir=@sdk_test_dir@',
  ]
  sdk_generate = custom_target(
    f'@task_base_name@:generate',
    command: [
      cli,
      'generate',
      '--additional-properties', ','.join(additional_properties),
      '--api-package', f'@namespace_base@.api', # com.criteo.api.marketingsolutions.v2021_10.api
      '--artifact-id', f'criteo-api-@criteo_service@-sdk', # criteo-api-marketingsolutions-sdk
      '--artifact-version', artifact_version, # 2021.10.0.211110
      '--config', '@INPUT0@',
      '--generator-name', language,
      '--group-id', 'com.criteo',
      '--input-spec', '@INPUT1@',
      '--model-package', f'@namespace_base@.model',
      '--output', client_output_dir_per_version,
      '--template-dir', templates_dir,
    ],
    input: [sdk_config, spec_path],
    output: f'@task_base_name@:generate',
    build_always_stale: true,
  )

  unwanted_files = [
    client_output_dir_per_version / '.openapi-generator-ignore',
    client_output_dir_per_version / '.travis.yml',
    client_output_dir_per_version / 'build.sbt',
    client_output_dir_per_version / 'git_push.sh',
    client_output_dir_per_version / 'gradle.properties',
    client_output_dir_per_version / 'pom.xml',
    client_output_dir_per_version / 'src' / 'main' / 'AndroidManifest.xml',
  ]
  sdk_rm_unwanted_files = custom_target(
    f'@task_base_name@:rm_unwanted_files',
    command: ['rm', '-f', unwanted_files],
    input: sdk_generate,
    output: f'@task_base_name@:rm_unwanted_files',
  )

  custom_target(
    task_base_name,
    command: ['ls', '-la', client_output_dir_per_version],
    depends: [sdk_generate, sdk_rm_unwanted_files],
    output: task_base_name,
    build_by_default: true,
  )
endforeach
