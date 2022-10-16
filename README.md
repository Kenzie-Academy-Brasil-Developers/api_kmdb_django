<h1 align="center">
KMDB
</h1>

## 💻 Projeto

Aplicação de gerenciamento de filmes estilo IMDB com autenticação de usuários.

## 🔨 Implementações

- [x] CR User
- [x] CRUD Movies
- [x] CRUD Reviews

## ✨ Tecnologias

- [x] Django
- [x] Django Rest Framework
- [x] Authentication Routes

# Instruções:
 
### Crie o ambiente virtual
```
python -m venv venv
```
### Ative o venv
```bash
# linux: 

source venv/bin/activate

```

```bash
# windows: 

.\vevn\Scripts\activate

```

### Instale as dependências 
```
pip install -r requirements.txt
```
### Execute as migrações
```
./manage.py migrate
```
### Rode a aplicação
```
./manage.py runserver
```



A APi tem como princípio adicionar filmes, assim como a criação de categorias e características para relacionar ao filme. Essas estapas de criação, somente um superuser pode realizar. 

Também é possível adicionar avaliações aos filmes desde que esse usário seja um crítico. Ou seja, quando for realizar o cadastro no banco de dados, deve-se passar as informações corretas.

A api possui CRUD e relacionamentos 1-N, N-N.

Api realizada interamente em python com django-rest-framework.
