import pytest
import playwright
from playwright.sync_api import Page, expect
from page_objects import Registro, Home, Login
from data import data_registro
from confteste import setup_test
from utils import mensagem_erro

def teste_cadastro_valido(page: Page, setup_test):
    page = setup_test
    page.goto("/")
    expect(page).to_have_title("BugBank | O banco com bugs e falhas do seu jeito")

    registro = Registro.Registro(page)
    dados_validos = data_registro.DADOS["valido"]

    registro.clicar_em_registrar()
    registro.inserir_dados_registro(dados_validos["email"], dados_validos["nome"],  dados_validos["senha"], dados_validos["confirmacao_senha"])
    registro.finalizar_cadastro()
    registro.validar_sucesso_mensagem()

def teste_email_vazio(page: Page, setup_test):    
    page = setup_test
    page.goto("/")
    expect(page).to_have_title("BugBank | O banco com bugs e falhas do seu jeito")

    registro = Registro.Registro(page)
    dados_vazios = data_registro.DADOS["vazio"]   
    dados_validos = data_registro.DADOS["valido"]

    registro.clicar_em_registrar()
    registro.inserir_dados_registro(dados_vazios["email"], dados_validos["nome"],  dados_validos["senha"], dados_validos["confirmacao_senha"])
    registro.finalizar_cadastro()
    mensagem_erro(page, "É campo obrigatório")

def teste_nome_vazio(page: Page, setup_test):    
    page = setup_test
    page.goto("/")
    expect(page).to_have_title("BugBank | O banco com bugs e falhas do seu jeito")

    registro = Registro.Registro(page)
    dados_vazios = data_registro.DADOS["vazio"]   
    dados_validos = data_registro.DADOS["valido"]

    registro.clicar_em_registrar()
    registro.inserir_dados_registro(dados_validos["email"], dados_vazios["nome"],  dados_validos["senha"], dados_validos["confirmacao_senha"])
    registro.finalizar_cadastro()
    registro.modal_texto.wait_for(state='visible')
    expect(registro.modal_texto).to_contain_text("Nome não pode ser vazio.")

def teste_senha_vazia(page: Page, setup_test):    
    page = setup_test
    page.goto("/")
    expect(page).to_have_title("BugBank | O banco com bugs e falhas do seu jeito")

    registro = Registro.Registro(page)
    dados_vazios = data_registro.DADOS["vazio"]   
    dados_validos = data_registro.DADOS["valido"]

    registro.clicar_em_registrar()
    registro.inserir_dados_registro(dados_validos["email"], dados_validos["nome"],  dados_vazios["senha"], dados_validos["confirmacao_senha"])
    registro.finalizar_cadastro()
    mensagem_erro(page, "É campo obrigatório")           

def teste_confirmacao_senha_vazia(page: Page, setup_test):    
    page = setup_test
    page.goto("/")
    expect(page).to_have_title("BugBank | O banco com bugs e falhas do seu jeito")

    registro = Registro.Registro(page)
    dados_vazios = data_registro.DADOS["vazio"]
    dados_validos = data_registro.DADOS["valido"]   

    registro.clicar_em_registrar()
    registro.inserir_dados_registro(dados_validos["email"], dados_validos["nome"],  dados_validos["senha"], dados_vazios["confirmacao_senha"])
    registro.finalizar_cadastro()
    mensagem_erro(page, "É campo obrigatório")  

def teste_conta_com_saldo(page: Page, setup_test):
    page = setup_test
    page.goto("/")
    expect(page).to_have_title("BugBank | O banco com bugs e falhas do seu jeito")

    registro = Registro.Registro(page)
    home = Home.Home(page)
    login = Login.Login(page)
    dados_validos = data_registro.DADOS["valido"]

    registro.clicar_em_registrar()
    registro.inserir_dados_registro(dados_validos["email"], dados_validos["nome"],  dados_validos["senha"], dados_validos["confirmacao_senha"])
    registro.opcao_saldo.click()
    registro.finalizar_cadastro()
    registro.validar_sucesso_mensagem()
    login.full_login(dados_validos["email"], dados_validos["senha"])
    home.saldo_da_conta.wait_for(state='visible')
    expect(home.saldo_da_conta).to_contain_text("Saldo em conta R$ 1.000,00")

def teste_conta_sem_saldo(page: Page, setup_test):
    page = setup_test
    page.goto("/")
    expect(page).to_have_title("BugBank | O banco com bugs e falhas do seu jeito")

    registro = Registro.Registro(page)
    home = Home.Home(page)
    login = Login.Login(page)
    dados_validos = data_registro.DADOS["valido"]

    registro.clicar_em_registrar()
    registro.inserir_dados_registro(dados_validos["email"], dados_validos["nome"],  dados_validos["senha"], dados_validos["confirmacao_senha"])
    registro.opcao_saldo.dblclick()
    registro.finalizar_cadastro()
    registro.validar_sucesso_mensagem()
    login.full_login(dados_validos["email"], dados_validos["senha"])
    home.saldo_da_conta.wait_for(state='visible')
    expect(home.saldo_da_conta).to_contain_text("Saldo em conta R$ 0,00")  

def teste_confirmacao_de_senha_diferente(page: Page, setup_test):
    page = setup_test
    page.goto("/")
    expect(page).to_have_title("BugBank | O banco com bugs e falhas do seu jeito")

    registro = Registro.Registro(page)
    dados_validos = data_registro.DADOS["valido"]   

    registro.clicar_em_registrar()
    registro.inserir_dados_registro(dados_validos["email"], dados_validos["nome"],  dados_validos["senha"], "SenhaDeConfirmacaoDiferente")
    registro.finalizar_cadastro()  
    registro.modal_texto.wait_for(state='visible')
    expect(registro.modal_texto).to_contain_text("As senhas não são iguais.")   