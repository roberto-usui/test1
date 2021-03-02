# Desafio

Desafio incompleto com bug conhecido no serviço que roda uma simulação de jogo.

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

Serviço utilizará banco sqlite local e será montado no endereço local: http://127.0.0.1:5000

No monento possui 1 endpoints com bug:

GET http://127.0.0.1:5000/basic-game/simulate
Retornaria o vencedor de um jogo pré determinado no banco de dados.


[Descrição desafio](./DESAFIO_PYTHONDX.pdf)
