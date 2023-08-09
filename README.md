# Ecommerce

O Objetivo deste projeto é criar um sistema para servir de portfolio.
O projeto ainda está em andamento e tem como foco desevolver um monolito com as ferramentas listadas abaixo:

> **Backend:** Foi utilizado Python com framework Django e está contemplado regras de negócio como as relações e cadastros de entidades. (concluído)

> **Frontend:** O foco deste projeto é backend, por este motivo, para design foi utilizado o básico de HTML e CSS com algumas nuâncias de bootstrap. (concluído)

> **Em desenvolvimento:**  Embora temos um E-commerce funcional, parte do projeto ainda está em desenvolvimento, pois o desafio é inicar do zero e entregar um site que possa ser utilziado de fato, para negócio.

Com isso, os próximos passos do projeto são:

 • *API de contato com whatsapp:* ao iniciar o site perceberá que o númeor está no rodapé da página, tenho como objetio aplicar a API do whatsapp para direcionar o usuário a conversa com o número ali inserido;
 • *API com com sistemas de pagamento:* até o momento, o software entrega a mensagem de pagamento efetuado com sucesso, porém o backend referente a pagamento é crucial que seja feita com muita atenção e tranquilidade, esta parte é crucial para o objetivo final deste projeto;
 • *Integração a um banco de dados robusto:* um desenvolvedor experiente que por algum motivo baixe este APP perceberá rapidamente que o banco de dados utilizado é o fornecido por padrão pelo DJANGO (db.sqlite3), está na fila do projeto alterar para um banco de dados mais robusto;


## Requisitos do Projeto

O projeto está sendo desenvolvido em Django com sistema operacional Linux;

As depedências deste projeto ficam em requirements.txt.


### Para executar o projeto, siga os passos abaixo:

Com sua virtualenv, na raíz do projeto instale as dependências do backend com
`pip install -r requirements.txt`

Com os pacotes todos instalados, na raiz do projeto rode:
- `./manage.py runserver 8000` para subir o backend na porta 8000
