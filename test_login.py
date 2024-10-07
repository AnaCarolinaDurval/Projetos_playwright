import pytest
from playwright.sync_api import Page, expect
import playwright
from data import data_login
from confteste import setup_test
from page_objects import Login, Home, Registro

def test_email_incompleto(page: Page, setup_test):
    page = setup_test
    page.goto("/")
    expect(page).to_have_title("BugBank | O banco com bugs e falhas do seu jeito")
    credencial_invalida = data_login.CREDENCIAIS["invalida"]
    page_objects_login = Login.Login(page)

    page_objects_login.input_email.fill(credencial_invalida["email_incompleto"])
    page_objects_login.input_password.fill(credencial_invalida["senha_invalida"])

    page_objects_login.botao_logar.wait_for(state='visible')
    page_objects_login.botao_logar.click()

    page_objects_login.mensagem_erro("Formato inválido")

def test_email_sem_dominio(page: Page, setup_test):
    page = setup_test
    page.goto("/")
    expect(page).to_have_title("BugBank | O banco com bugs e falhas do seu jeito")
    credencial_invalida = data_login.CREDENCIAIS["invalida"]
    page_objects_login = Login.Login(page)

    page_objects_login.input_email.fill(credencial_invalida["email_sem_dominio"])
    page_objects_login.input_password.fill(credencial_invalida["senha_invalida"])

    page_objects_login.botao_logar.wait_for(state='visible')
    page_objects_login.botao_logar.click()

    page_objects_login.mensagem_erro("Formato inválido")

def test_senha_vazia(page: Page, setup_test):
    page = setup_test
    page.goto("/")
    expect(page).to_have_title("BugBank | O banco com bugs e falhas do seu jeito")
    credencial_valida = data_login.CREDENCIAIS["valida"]
    page_objects_login = Login.Login(page)

    page_objects_login.input_email.fill(credencial_valida["email_valido"])
    page_objects_login.botao_logar.wait_for(state='visible')
    page_objects_login.botao_logar.click()

    page_objects_login.mensagem_erro("É campo obrigatório")   

def test_senha_invalida(page: Page, setup_test):
    page = setup_test
    page.goto("/")
    expect(page).to_have_title("BugBank | O banco com bugs e falhas do seu jeito")
    credencial_valida = data_login.CREDENCIAIS["valida"]
    credencial_invalida = data_login.CREDENCIAIS["invalida"]
    page_objects_login = Login.Login(page)

    page_objects_login.input_email.fill(credencial_valida["email_valido"])
    page_objects_login.input_password.fill(credencial_invalida["senha_invalida"])

    page_objects_login.botao_logar.wait_for(state='visible')
    page_objects_login.botao_logar.click()

    page_objects_login.modal_erro.wait_for(state='visible')
    page_objects_login.mensagem_erro("Usuário ou senha inválido. Tente novamente ou verifique suas informações!")  

def test_login_valido(page: Page, setup_test):
    page = setup_test
    page.goto("/")
    expect(page).to_have_title("BugBank | O banco com bugs e falhas do seu jeito")
    credencial_valida = data_login.CREDENCIAIS["valida"]
    page_objects_login = Login.Login(page)
    page_objects_home = Home.Home(page)
    page_objects_registro = Registro.Registro(page)

    page_objects_registro.full_cadastro(credencial_valida["email_valido"], credencial_valida["nome_valido"], credencial_valida["senha_valida"], credencial_valida["senha_valida"])

    page_objects_login.input_email.fill(credencial_valida["email_valido"])
    page_objects_login.input_password.fill(credencial_valida["senha_valida"])

    page_objects_login.botao_logar.wait_for(state='visible')
    page_objects_login.botao_logar.click()
    page_objects_home.validacao_home()
    

