#!/bin/sh

# first run
if [ ! -f /settings.json ]; then
cat << EOF > /settings.json
{
    "RPC_USER": "bitcoin",
    "RPC_PASS": "<< GET_PASSWORD_FROM_BITCOIN_PROPERTIES_PANE >>",
    "RPC_HOST": "bitcoind.embassy",
    "RPC_PORT": "8332",
    "BRAIINS_TOKEN": "",
    "ADAFRUIT_USERNAME": "",
    "ADAFRUIT_APITOKEN": "",
    "TWILIO_SID": "",
    "TWILIO_TOKEN" : "",
    "TWILIO_PHONE_NUMBER": "",
    "NOTIFY_PHONE_NUMBER": ""
}
EOF
fi

# # https://github.com/Start9Labs/filebrowser-wrapper/blob/master/docker_entrypoint.sh#L15-L30
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

# write_properties_stats_yaml()

/usr/bin/local python3 stats-yaml.py

# health-check.sh &

# run the application
# exec python -m src
# https://github.com/goshiz/start9labs-havend-wrapper/blob/master/docker_entrypoint.sh
exec /usr/bin/local python3 -m src
