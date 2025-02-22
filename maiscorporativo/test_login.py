from playwright.sync_api import Page, expect, Playwright  #API do Playwright que facilita as interações com os navegadores de forma síncrona
from conftest import acessar_pagina
from page_objects import Login

def teste_realizar_login_valido(page, acessar_pagina):
    page = acessar_pagina
    page.goto("https://maiscorporativo.tharlei.com/login") #aqui estamos usando a instancia criada para acessar a url que queremos
    expect(page).to_have_title("Login -  Mais Corporativo") #verifica que a tag html title da págima possui esse texto    
    
    page_objects_login = Login.Login(page)
    
    page_objects_login.input_email.wait_for(state='visible') #espera até que o elemento fique visivel
    page_objects_login.inserir_email("admin@maiscorporativo.tur.br")

    page_objects_login.input_password.wait_for(state='visible')
    page_objects_login.inserir_senha("secret")

    page_objects_login.lembrar_checkbox.wait_for(state='visible')
    page_objects_login.check_lembrar_dados()

    page_objects_login.icone_ver_senha.wait_for(state='visible')
    page_objects_login.mostrar_senha()

    page_objects_login.botao_logar.wait_for(state='visible')
    page_objects_login.clicar_botao_logar()
    
    expect(page.get_by_text("Bem-vindo")).to_be_visible()

def test_login_inexistente(page, acessar_pagina):
    page = acessar_pagina
    page.goto("https://maiscorporativo.tharlei.com/login") #aqui estamos usando a instancia criada para acessar a url que queremos
    expect(page).to_have_title("Login -  Mais Corporativo") #verifica que a tag html title da págima possui esse texto    
    
    page_objects_login = Login.Login(page)
    
    page_objects_login.input_email.wait_for(state='visible') #espera até que o elemento fique visivel
    page_objects_login.inserir_email("testeinvalido@teste.com")

    page_objects_login.input_password.wait_for(state='visible')
    page_objects_login.inserir_senha("teste")

    page_objects_login.botao_logar.wait_for(state='visible')
    page_objects_login.clicar_botao_logar()

    expect(page.get_by_text("Essas credenciais não correspondem aos nossos registros")).to_be_visible() 

def test_email_invalido(page, acessar_pagina):
    page = acessar_pagina
    page.goto("https://maiscorporativo.tharlei.com/login") #aqui estamos usando a instancia criada para acessar a url que queremos
    expect(page).to_have_title("Login -  Mais Corporativo") #verifica que a tag html title da págima possui esse texto    
    
    page_objects_login = Login.Login(page)
    
    page_objects_login.input_email.wait_for(state='visible') #espera até que o elemento fique visivel
    page_objects_login.inserir_email("teste")

    page_objects_login.input_password.wait_for(state='visible')
    page_objects_login.inserir_senha("teste")

    page_objects_login.botao_logar.wait_for(state='visible')
    page_objects_login.clicar_botao_logar()

    is_valid = page.locator("id=data.email").evaluate("el => el.validity.valid") #o evaluate no playwright permite executar pequenos códigos em javaScript  na página web que estamos testando, ou seja ele recebe uma função JavaScript como argumento
    assert is_valid == False
      





                