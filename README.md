# Hire.me

## Projeto

O projeto consiste em reproduzir um encurtador de URL's (apenas sua API), simples e com poucas funções, porém com espaço suficiente para mostrar toda a gama de desenho de soluções, escolha de componentes, mapeamento ORM, uso de bibliotecas de terceiros, uso de GIT e criatividade.

O projeto consiste de dois casos de uso: 

1. Shorten URL
2. Retrieve URL

### 1 - Shorten URL
![Short URL](http://i.imgur.com/MFB7VP4.jpg)

1. Usuario chama a API passando a URL que deseja encurtar e um parametro opcional **CUSTOM_ALIAS**
    1. Caso o **CUSTOM_ALIAS** já exista, um erro especifico ```{ERR_CODE: 001, Description:CUSTOM ALIAS ALREADY EXISTS}``` deve ser retornado.
    2. Toda URL criada sem um **CUSTOM_ALIAS** deve ser reduzida a um novo alias, **você deve sugerir um algoritmo para isto e o porquê.**
    
2. O Registro é colocado em um repositório (*Data Store*)
3. É retornado para o cliente um resultado que contenha a URL encurtada e outros detalhes como
    1. Quanto tempo a operação levou
    2. URL Original

Exemplos:

* Chamada sem CUSTOM_ALIAS
```
PUT http://shortener/create?url=http://www.bemobi.com.br

{
   "alias": "XYhakR",
   "url": "http://shortener/u/XYhakR",
   "original_url": "http://www.bemobi.com.br",
   "statistics": {
       "time_taken": "10ms",
   }
}
```

* Chamada com CUSTOM_ALIAS
```
PUT http://shortener/create?url=http://www.bemobi.com.br&CUSTOM_ALIAS=bemobi

{
   "alias": "bemobi",
   "url": "http://shortener/u/bemobi",
   "original_url": "http://www.bemobi.com.br",
   "statistics": {
       "time_taken": "12ms",
   }
}
```

* Chamada com CUSTOM_ALIAS que já existe
```
PUT http://shortener/create?url=http://www.github.com&CUSTOM_ALIAS=bemobi

{
   "alias": "bemobi",
   "err_code": "001",
   "description": "CUSTOM ALIAS ALREADY EXISTS"
}
```

### 2 - Retrieve URL
![Retrieve URL](http://i.imgur.com/f9HESb7.jpg)

1. Usuario chama a API passando a URL que deseja acessar
    1. Caso a **URL** não exista, um erro especifico ```{ERR_CODE: 002, Description:SHORTENED URL NOT FOUND}``` deve ser retornado.
2. O Registro é lido de um repositório (*Data Store*)
3. Esta tupla ou registro é mapeado para uma entidade de seu projeto
3. É retornado para o cliente um resultado que contenha a URL final, a qual ele deve ser redirecionado automaticamente

## 🔧 Setup Locally

To use the app in a local environment:

1. First, clone this repo in your machine.
2. Then, put these commands in your terminal inside project folder:
   ```
   $ pip3 install -r requirements.txt
   $ python3 app.py
   ```