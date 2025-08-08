# **Desafio: Configuração de Ambiente com Docker Compose**

## Introdução

Este desafio tem o objetivo de consolidar o conhecimento adquirido sobre Dockerfile, Docker Compose, redes e volumes. Você será desafiado a configurar um ambiente multi-container para uma aplicação de sua escolha. Além disso, é esperado que você explore o uso de variáveis de ambiente para configurar de forma flexível e segura o ambiente.

## Etapas do Projeto

1. Criação do Dockerfile: Desenvolva um arquivo Dockerfile para uma aplicação de sua escolha, utilizando uma imagem base adequada.
2. Definição do Docker Compose: Configure dois serviços no Docker Compose: o serviço da aplicação e um banco de dados (MySQL, PostgreSQL, MongoDB, etc.).
3. Configuração de Volumes: Garanta a persistência dos dados do banco de dados configurando volumes apropriados.
4. Criação de Rede Customizada: Crie uma rede customizada para permitir a comunicação isolada entre os containers.
5. Utilização de Variáveis de Ambiente: Utilize variáveis de ambiente para configurar diferentes aspectos da aplicação, como URLs do banco de dados, chaves de acesso e outras configurações sensíveis.
6. Documentação: Documente o processo de configuração em um arquivo README.md, incluindo comandos para executar os containers, configurar as variáveis de ambiente e testar a conexão entre eles.

## Instruções Adicionais

- A aplicação pode ser desenvolvida em qualquer linguagem de programação.
- Para garantir a segurança, o banco de dados não deve ser configurado apenas com o usuário root. Crie um usuário para a aplicação, concedendo-lhe apenas as permissões necessárias.
- Para configurar e gerenciar variáveis de ambiente de maneira segura, você pode utilizar ferramentas como scripts Bash, HashiCorp Vault, entre outras soluções de sua preferência.
- Utilize múltiplos estágios e imagens alpine ao usar o Dockerfile para construir a imagem da aplicação.
- Evite a inclusão de valores sensíveis ou de distinção de ambientes diretamente no código.

## Resultados Esperados

- Configuração de um ambiente multi-container funcional com Docker Compose.
- Utilização efetiva de volumes para persistência de dados.
- Configuração de variáveis de ambiente para gerenciar configurações sensíveis.
- Implementação de uma estratégia de segurança para o acesso ao banco de dados, evitando o uso exclusivo do usuário root.
- Documentação clara e detalhada do processo de configuração no arquivo README.md.

## Entrega

Após concluir o desafio, você deve enviar a URL do seu código no GitHub para a plataforma. 

Além disso, que tal fazer um post no LinkedIn compartilhando o seu aprendizado e contando como foi a experiência? É uma excelente forma de demonstrar seus conhecimentos e atrair novas oportunidades!

Feito com 💜 por Rocketseat 👋
