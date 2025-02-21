from playwright.sync_api import Page, expect, Playwright  #API do Playwright que facilita as interações com os navegadores de forma síncrona

def teste_realizar_login_valido(page, playwright):
    chromium = playwright.chromium  #objeto para usar o chromium
    browser = chromium.launch(headless=False) #o launch inicia uma instancia do chromium permitind interações com o navegador
    page = browser.new_page() #abrindo um novo navegador com a intancia criada com o chromium
    page.goto("https://maiscorporativo.tharlei.com/login") #aqui estamos usando a instancia criada para acessar a url que queremos
    expect(page).to_have_title("Login -  Mais Corporativo") #verifica que a tag html title da págima possui esse texto
            
    page.locator("id=data.email").wait_for(state='visible') #espera até que o elemento fique visivel
    page.locator("id=data.email").fill("admin@maiscorporativo.tur.br") #localiza o elemento e insere o valor
    page.locator("id=data.password").wait_for(state='visible')
    page.locator("id=data.password").fill("secret")

    page.locator("input[type=checkbox]").click()
    page.locator("button[title='Mostrar senha']").click()
    page.locator("button[type=submit]").wait_for(state='visible')
    page.locator("button[type=submit]").click() #clica no locator passado

    
    expect(page.get_by_text("Bem-vindo")).to_be_visible()

def test_login_inexistente(page, playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://maiscorporativo.tharlei.com/login")
    expect(page).to_have_title("Login -  Mais Corporativo")

    page.locator("id=data.email").wait_for(state='visible') #espera até que o elemento fique visivel
    page.locator("id=data.email").fill("testeinvalido@teste.com") #localiza o elemento e insere o valor
    page.locator("id=data.password").wait_for(state='visible')
    page.locator("id=data.password").fill("teste")

    page.locator("button[type=submit]").wait_for(state='visible')
    page.locator("button[type=submit]").click() #clica no locator passado

    expect(page.get_by_text("Essas credenciais não correspondem aos nossos registros")).to_be_visible() 

def test_email_invalido(page, playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://maiscorporativo.tharlei.com/login")
    expect(page).to_have_title("Login -  Mais Corporativo")

    page.locator("id=data.email").wait_for(state='visible')
    page.locator("id=data.email").fill("teste")
    page.locator("id=data.password").wait_for(state='visible')
    page.locator("id=data.password").fill("teste")

    page.locator("button[type=submit]").wait_for(state='visible')
    page.locator("button[type=submit]").click()

    is_valid = page.locator("id=data.email").evaluate("el => el.validity.valid") #o evaluate no playwright permite executar pequenos códigos em javaScript  na página web que estamos testando, ou seja ele recebe uma função JavaScript como argumento
    assert is_valid == False
      





                