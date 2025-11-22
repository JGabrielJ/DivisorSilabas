# Divisor de Sílabas
Uma aplicação web feita com Python, Django, Bootstrap, dentre outras bibliotecas que recebe uma palavra qualquer da Língua Portuguesa e retorna sua divisão silábica (fazendo web scraping do site [**dicio.com.br**](https://www.dicio.com.br/)), juntamente com algumas informações adicionais sobre a palavra. O website também possui um sistema de envio de e-mails para quaisquer dúvidas, feedbacks ou erros no funcionamento do programa. **_Atenção: o serviço de envio de e-mails do Django funciona apenas localmente devido a restrições de segurança do Render!!!_**

## Rodando o Website
Atualmente existem duas maneiras de acessar o Divisor de Sílabas, descritas logo abaixo:

### Com o Render (remoto):
- O site pode ser acessado em [**divisorsilabas.onrender.com ↗**](https://divisorsilabas.onrender.com)

### Com o Python (local):
1. Baixe a pasta compactada do projeto clicando em `<> Code → Download ZIP` e depois extraia os arquivos;
- Após concluir os passos descritos abaixo (de acordo com o seu sistema operacional), é só acessar o endereço `127.0.0.1:8000` no seu navegador e você poderá desfrutar do Divisor de Sílabas o quanto quiser.
- Você também pode customizar seu próprio filtro de palavras e suas "palavras secretas" nos arquivos [`rotten.txt`](./eggs-dev/rotten.txt) e [`secrets.json`](./eggs-dev/secrets.json), respectivamente. **_Importante: para que o envio de e-mails funcione corretamente, descomente as referidas linhas nos arquivos [`settings.py (157-162)`](./divisorsilabas_project/settings.py), [`forms.py (58-64)`](./divisor_app/forms.py) e [`views.py (7-8, 37, 41, 48-49, 66-77)`](./divisor_app/views.py)._**

#### No Windows:
2. Instale a versão mais recente do Python através do site [**python.org**](https://www.python.org/downloads/release/python-31210/), de acordo com a arquitetura do seu Windows;
3. Apenas clique duas vezes no arquivo `run_server.bat` e ele fará toda a configuração necessária para a execução do servidor;

#### No Linux / MacOS:
2. Abra o terminal na pasta do projeto e execute a seguinte linha de comando: `sudo apt install python3 python3-pip python3-venv`;
3. Apenas na primeira vez rodando a aplicação, execute o comando `chmod +x run.sh`;
4. Por fim, execute o comando `./run_server.sh` e o Divisor de Sílabas estará pronto para uso.

> Nota do Dev: na versão original do projeto, o PySimpleGUI foi utilizado na criação de uma interface gráfica que atendesse aos requisitos da aplicação. Entretanto, em virtude da biblioteca ter sido descontinuada, decidi reviver o programa transferindo-o para o Django. Esta versão pode ser encontrada em [**ProjetosAcademicos**](https://github.com/JGabrielJ/ProjetosAcademicos/tree/main/DivisorSilabas%20(old)).