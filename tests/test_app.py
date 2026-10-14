import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_pagina_inicial_carrega(client):
    resposta = client.get("/")
    assert resposta.status_code == 200


def test_cadastro_sem_login_redireciona(client):
    resposta = client.get("/cadastro")
    assert resposta.status_code == 302


def test_login_com_senha_errada(client):
    resposta = client.post(
        "/login", data={"email": "voluntaria@ongleituras.org", "senha": "errada"}
    )
    assert "incorretos".encode() in resposta.data


def test_login_com_senha_correta(client):
    resposta = client.post(
        "/login",
        data={"email": "voluntaria@ongleituras.org", "senha": "minhasenha123"},
        follow_redirects=True,
    )
    assert "Cadastro".encode() in resposta.data