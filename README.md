# Desafio

Desafio roda 300 simulação de jogo.

Não sei porque ficou na minha cabeça que era para fazer uma API.

Portanto criei uma API com um endpoint que retorna o resultado.

Tabuleiro está definido em [manage.py](./manage.py), caso seja necessário modifique os valores em
Property e rode o manage.py recreate_db e setup_dev descrito abaixo.

Para rodar siga o seguinte:

```shell
pip3 install -r requirements.txt

python3 manage.py recreate_db

python3 manage.py setup_dev

python3 manage.py runserver
```

ou

```
docker build -t desafio:0.1 .

docker run -p 5000:5000 desafio:0.1

```

Serviço utilizará banco sqlite local e será montado no root do projeto.

No monento possui 1 endpoint:

GET http://127.0.0.1:5000/basic-game/simulate
Retorna valores:
```json
{
    "data": {
        "average_turns": 16.17,
        "most_victories": "impulsive",
        "percentages": {
            "cautious": 0.25666666666666665,
            "impulsive": 0.3,
            "random": 0.18666666666666668,
            "rigorous": 0.25666666666666665
        },
        "timeouts": 0
    },
    "message": "OK"
}
```


[Descrição desafio](./DESAFIO_PYTHONDX.pdf)
