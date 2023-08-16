# E-commerce

O objetivo deste projeto é criar um sistema para servir como portfólio.
O projeto ainda está em andamento e tem como foco desenvolver um monólito com as ferramentas listadas abaixo:

> **Backend:** Foi utilizado Python com o framework Django, e estão contempladas regras de negócio, como as relações e cadastros de entidades. (Concluído)

> **Frontend:** O foco deste projeto é o backend. Por esse motivo, para o design, foi utilizado o básico de HTML e CSS, com algumas nuances de Bootstrap. (Concluído)

> **Banco de Dados:** O banco escolhido para este projeto foi o PostgreSQL por ser amplamente utilizado no mercado. (Concluído)

> **Em desenvolvimento:** Embora tenhamos um E-commerce funcional, parte do projeto ainda está em desenvolvimento, pois o desafio é iniciar do zero e entregar um site que possa ser utilizado de fato para negócios.

> **Com isso, os próximos passos do projeto são:**
 
 > *API de sistemas de pagamento:* Até o momento, o software entrega a mensagem de pagamento efetuado com sucesso. No entanto, a parte de backend relacionada ao pagamento é crucial e deve ser feita com muita atenção e tranquilidade;
 
 > ✔ ~~*Integração a um banco de dados robusto:* O projeto concluiu com sucesso a etapa de integração a um banco de dados mais robusto, substituindo o banco de dados padrão SQLite do Django (db.sqlite3).~~
 
 > *Hospedagem:* Meu objetivo é transformar este aplicativo em um portfólio acessível não apenas para desenvolvedores, mas também para pessoas que não têm conhecimento técnico. Para alcançar isso, planejo subir o site em um serviço de hospedagem. Permitindo que recrutadores e profissionais de Recursos Humanos também avaliem meu trabalho.

Fique atento para atualizações futuras sobre a hospedagem do site.


## Requisitos do Projeto

O projeto está sendo desenvolvido em Django com sistema operacional Linux.

As dependências deste projeto estão listadas em requirements.txt.


### Para executar o projeto, siga os passos abaixo:

Com sua virtualenv, na raiz do projeto, instale as dependências do backend com
`pip install -r requirements.txt`

Com todos os pacotes instalados, na raiz do projeto, execute:
- `./manage.py runserver 8000` para subir o backend na porta 8000.
