from playwright.sync_api import expect

class Home:

    def __init__(self,page):
        self.page = page
        self.nome = "#textName"
        self.botao_sair = self.page.locator("#btnExit")
        self.saldo_da_conta = self.page.locator("#textBalance")

    def validacao_home(self):
        self.page.get_by_text("bem vindo ao BugBank :)")
        