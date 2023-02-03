# write_properties_stats_yaml() {
#     mkdir -p /root/start9
#     echo 'data:' >> /root/start9/stats.yaml
#     echo '  Hello:' >> /root/start9/stats.yaml
#     echo '    type: string' >> /root/start9/stats.yaml
#     echo '    value: admin' >> /root/start9/stats.yaml
#     echo '    description: This is .' >> /root/start9/stats.yaml
#     echo '    copyable: true' >> /root/start9/stats.yaml
#     echo '    masked: false' >> /root/start9/stats.yaml
#     echo '    qr: false' >> /root/start9/stats.yaml
#     echo '  World:' >> /root/start9/stats.yaml
#     echo '    type: string' >> /root/start9/stats.yaml
#     # echo '    value: "'"$password"'"' >> ./start9/stats.yaml
#     echo '    value: asdfasdf' >> /root/start9/stats.yaml
#     echo '    description: This randomly-generated.' >> /root/start9/stats.yaml
#     echo '    copyable: true' >> /root/start9/stats.yaml
#     echo '    masked: true' >> /root/start9/stats.yaml
#     echo '    qr: false' >> /root/start9/stats.yaml
# }

"""
TODO:
https://github.com/Start9Labs/filebrowser-wrapper/blob/master/docker_entrypoint.sh#L15-L30
"""


#!/usr/bin/env python3


import yaml

data = {
    'data': {
        'Hello': {
            'type': 'string',
            'value': 'admin',
            'description': 'This is .',
            'copyable': True,
            'masked': False,
            'qr': False
        },
        'World': {
            'type': 'string',
            'value': 'asdfasdf',
            'description': 'This randomly-generated.',
            'copyable': True,
            'masked': True,
            'qr': False,
        }
    }
}

with open('/start9/stats.yaml', 'w') as outfile:
    yaml.dump(data, outfile)
