from playwright.sync_api import expect
import pytest
import re

class Registro:

    def __init__(self, page):
        self.page = page
        self.botao_registrar = self.page.locator('button:has-text("Registrar")')
        self.input_email = self.page.locator('.card__register input[type=email]')
        self.input_senha = self.page.locator('.card__register input[name=password]')
        self.input_confirmar_senha = self.page.locator('.card__register input[name=passwordConfirmation]')
        self.input_nome = self.page.locator('.card__register input[type=name]')
        self.input_botao_confirmar = self.page.locator('.card__register button[type=submit]')
        self.botao_fechar_modal = self.page.locator('#btnCloseModal')
        self.modal_texto = self.page.locator('#modalText') 

    def clicar_em_registrar(self):
        self.botao_registrar.wait_for(state='visible')
        self.botao_registrar.click()

    def inserir_dados_registro(self, email, nome, senha, confirmacao_senha):
        self.input_email.fill(email)
        self.input_nome.fill(nome)       
        self.input_senha.fill(senha)
        self.input_confirmar_senha.fill(confirmacao_senha)

    def finalizar_cadastro(self):    
        self.input_botao_confirmar.click()

    def validar_sucesso_mensagem(self):
        self.modal_texto.wait_for(state='visible')
        text_sucesso = self.modal_texto.inner_text()
        pattern = re.compile(r"A conta \d+-\d+ foi criada com sucesso")
        assert pattern.search(text_sucesso), "Mensagem de sucesso incorreta"
        self.botao_fechar_modal.click()

    def full_cadastro(self, email, nome, senha, confirmacao_senha):
        self.clicar_em_registrar()    
        self.inserir_dados_registro(email, nome, senha, confirmacao_senha)
        self.finalizar_cadastro()
        self.validar_sucesso_mensagem()