project('criteo.api', version: '0', meson_version: '>=1.1.0')

uvx = find_program('uvx')

cli_package = 'openapi-generator-cli'
cli_version = '6.3.0'
cli = [uvx, cli_package + '@' + cli_version]

fs = import('fs')

criteo_package = meson.project_name()
generator_version = meson.project_version()
formatted_date = get_option('date')
generated_clients_dir_name = 'generated-clients'

subdir('api-specifications')
foreach language : ['java', 'php', 'python']
  subdir('generator' / language)
endforeach
