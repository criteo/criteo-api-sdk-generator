technology_stack = 'php'
name_separator = '\\'

sdk_config = files('generatorConfiguration.yaml')
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

  # example: criteo\api\marketingsolutions\v2021_10
  namespace_base = f'@criteo_package@.@criteo_service@.@version_in_namespace@'.replace('.', name_separator)

  artifact_version = is_preview_version ? '0' : criteo_api_version.replace('_', '.')
  # example : 2021.01.0.211110 for stable , 0.0.211110 for preview
  artifact_version += f'.@generator_version@.@formatted_date@'

  task_base_name = f'@criteo_service@-@version_in_namespace@:@language@:sdk'

  additional_properties = [
    'generateApiTests=false',
    'generateModelTests=false',
    'hideGenerationTimestamp=true',
    'removeOperationIdPrefix=true',
  ]
  sdk_generate = custom_target(
    f'@task_base_name@:generate',
    command: [
      cli,
      'generate',
      '--additional-properties', ','.join(additional_properties),
      '--artifact-version', artifact_version,
      '--config', '@INPUT0@',
      '--generator-name', language,
      '--git-repo-id', f'criteo-api-@criteo_service@-@language@-sdk',
      '--git-user-id', 'criteo',
      '--group-id', 'criteo',
      '--input-spec', '@INPUT1@',
      '--invoker-package', namespace_base,
      '--output', client_output_dir_per_version,
      '--package-name', f'criteo-api-@criteo_service@-sdk',
      '--template-dir', templates_dir,
    ],
    input: [sdk_config, spec_path],
    output: f'@task_base_name@:generate',
    build_always_stale: true,
  )

  unwanted_files = [
    client_output_dir_per_version / '.openapi-generator-ignore',
    client_output_dir_per_version / '.travis.yml',
    client_output_dir_per_version / 'git_push.sh',
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
