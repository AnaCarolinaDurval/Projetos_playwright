from playwright.sync_api import expect

class Login:

    def __init__(self, page):
        self.page = page
        self.input_email= page.locator("id=data.email")
        self.input_password= page.locator("id=data.password")   
        self.lembrar_checkbox = page.locator("input[type=checkbox]")
        self.icone_ver_senha = page.locator("button[title='Mostrar senha']")
        self.botao_logar= page.locator("button[type=submit]")


    def inserir_email(self, email):
        self.input_email.fill(email) #localiza o elemento e insere o valor

    def inserir_senha(self, senha):
        self.input_password.fill(senha)


    def check_lembrar_dados(self):
        self.lembrar_checkbox.click()

    def mostrar_senha(self):
        self.icone_ver_senha.click()

    def clicar_botao_logar(self):
        self.botao_logar.click() #clica no locator passado

