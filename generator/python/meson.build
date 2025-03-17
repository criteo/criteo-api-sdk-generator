technology_stack = 'python'
name_separator = '_'

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

  # example: criteo\api\marketingsolutions\v2021_10
  namespace_base = f'@criteo_package@.@criteo_service@.@version_in_namespace@'.replace('.', name_separator)

  artifact_version = is_preview_version ? '0' : criteo_api_version.replace('_', '.')
  # example : 2021.01.0.211110 for stable , 0.0.211110 for preview
  artifact_version += f'.@generator_version@.@formatted_date@'

  task_base_name = f'@criteo_service@-@version_in_namespace@:@language@:sdk'

  sdk_config = custom_target(
    f'@task_base_name@:config',
    command: [generate_config_sh, config_template, namespace_base],
    capture: true,
    output: f'@criteo_service@-@version_in_namespace@.yaml',
  )

  additional_properties = [
    f'apiVersion=@artifact_version@',
    'artifactDescription=@0@ SDK for Criteo API @1@ for @2@ version'.format(language.to_upper(), criteo_service, criteo_api_version),
    'generateApiTests=false',
    'generateModelTests=false',
    'hideGenerationTimestamp=true',
    f'packageUrl=https://github.com/criteo/criteo-api-@language@-sdk',
    f'packageVersion=@artifact_version@',
    f'projectName=@namespace_base@',
    'removeOperationIdPrefix=true',
  ]
  sdk_generate = custom_target(
    f'@task_base_name@:generate',
    command: [
      cli,
      'generate',
      '--additional-properties', ','.join(additional_properties),
      '--artifact-id', f'criteo-api-@criteo_service@-sdk',
      '--config', '@INPUT0@',
      '--generator-name', 'python-prior',
      '--group-id', 'criteo',
      '--input-spec', '@INPUT1@',
      '--invoker-package', 'Criteo\\SDK',
      '--output', client_output_dir_per_version,
      '--package-name', namespace_base,
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
