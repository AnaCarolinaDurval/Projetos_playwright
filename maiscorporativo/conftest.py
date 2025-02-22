import pytest
from playwright.sync_api import Page, expect, Playwright

@pytest.fixture(scope="function")
def acessar_pagina(page, playwright):
    chromium = playwright.chromium  #objeto para usar o chromium
    browser = chromium.launch(headless=False) #o launch inicia uma instancia do chromium permitind interações com o navegador
    page = browser.new_page() #abrindo um novo navegador com a intancia criada com o chromium e a url

    yield page

    browser.close()