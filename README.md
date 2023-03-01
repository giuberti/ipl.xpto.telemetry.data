# IPL XPTO Tracking Data

O projeto "IPL XPTO Tracking Data" é um serviço de rastreamento de dados de localização de veículos em tempo real. 
Ele consiste em uma API RESTful que permite a criação, recuperação, atualização e exclusão de dados de localização de veículos.

O servidor foi gerado automaticamente pelo [swagger-codegen](https://github.com/swagger-api/swagger-codegen).
Também usa a biblioteca [Connexion](https://github.com/zalando/connexion) com o Flask.

## Configuração

A porta do servidor e a URL do banco de dados Postgres podem ser configuradas no arquivo `settings.py`. 
Por padrão, o número da porta é definido como `8084`.
Certifique-se de que essas configurações estão corretas antes de executar o serviço.

### Testes

Pode-se usar a collection Postman na pasta `\postman` ou acessar a UI abaixo, onde todos endPoints estao listados:

```
http://localhost:8084/tracking/ui/
```

