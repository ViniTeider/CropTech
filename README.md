# Projeto Experiencia Criativa do 3° periodo (Flask, Jinja, Bootstrap, MySQL)
Projeto realizado na PUCPR como parte da disciplina de Experiência Criativa, com o objetivo de criar um site de uma empresa de automação. Nesse contexto, criamos um sistema que permite aos clientes gerenciar várias plantas e monitorar os valores dos sensores, como umidade, luminosidade e temperatura, através do site.
O sistema também oferece a opção para o usuário acessar como administrador e gerenciar vários registros do banco de dados diretamente pelo site.

## Rodar o projeto
Para instalar o projeto, o usuário deve apenas baixa-lo (da branch master) e extrair no local desejado <br />
Para rodar o projeto, o usuário deve alterar no arquivo db.py (linha 4), dentro da pasta models, as informações do user e senha de seu sql, também deve criar um Data Bse com o nome desejado e colocar após a barra <br />
exemplo:

```python
instance = 'mysql+pymysql://usuario:senha@localhost:3306/db_com_nome_desejado'
```
É necessario possuir o python instalado para executar o projeto <br />

por fim, o usuário deve instalar as dependencias caso não tenha, as dependencias necessarias estão listadas a baixo: <br />

- Flask 
```bash
pip install Flask
```
- Jinja 
```bash
pip install jinja2
```
- Flask Login
```bash
pip install flask-login
```
- Flask MQTT
```bash
pip install flask-MQTT
```
- SQLAlchemy
```bash
pip install SQLAlchemy
```
