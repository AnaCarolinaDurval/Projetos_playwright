from playwright.sync_api import expect

class Login:

    def __init__(self, page):
        self.page = page
        self.input_email= page.locator(".card__login input[type=email]")
        self.input_password= page.locator(".card__login input[type=password]")         
        self.botao_logar= page.locator(".card__login button[type=submit]")
        self.modal_erro = page.locator("#modalText")

    def inserir_email(self, email):
        self.input_email.fill(email)

    def inserir_password(self, password):
        self.input_email.fill(password)    

    def mensagem_erro(self, mensagem):
        element_text_error = self.page.get_by_text(mensagem)
        expect(element_text_error).to_be_visible()
