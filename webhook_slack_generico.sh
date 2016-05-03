#!/bin/bash

# 
# Criei o script lendo esta documentacao: https://api.slack.com/incoming-webhooks
#
# Script bem generico para ser alterado dependendo do canal no slack!
#
# Os assuntos configurados por enquanto sao:
# ALERTA   => Tem algo estranho! 
# PROBLEMA => Deu PAU! Parou TUDO!!
# LENTIDAO => Ta lento pra caralho!
# DEBOA    => Ta tudo nos conforme!!
#
#

url=''            # URL do webhook criado no slack <https://hooks.slack.com/services/.....>
usuario='Zabbix Boladão'  # Usuario que envia o alerta do bagulho!
destinatario="$1" # Quem vai receber o alerta. 
assunto="$2"      # O assunto do alerta.

# Coloca um emoticon na mensagem de acordo com o assunto do alerta!
if [ "$assunto" == 'ALERTA' ]; then
    emoticon=':thiking_face:'
elif [ "$assunto" == 'PROBLEMA' ]; then
    emoticon=':rotating_light:'
elif [ "$assunto" == 'LENTIDAO' ]; then
    emoticon=':turtle:'
elif [ "$assunto" == 'DEBOA' ]; then
    emoticon=':spock-hand:'
else
    emoticon=':ghost:'
fi

# Monta a mensagem que vai ser enviada!
mensagem="${assunto}: $3"

# Monta o Payload e envia a requisicao via Curl!
payload="payload={\"channel\": \"${destinatario//\"/\\\"}\", \"username\": \"${usuario//\"/\\\"}\", \"text\": \"${mensagem//\"/\\\"}\", \"icon_emoji\": \"${emoticon}\"}"
curl -X POST --data-urlencode "${payload}" $url
