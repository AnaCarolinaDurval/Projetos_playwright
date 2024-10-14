
import pytest
from playwright.sync_api import expect

def mensagem_erro(page, mensagem):
    element_text_error = page.get_by_text(mensagem)
    expect(element_text_error).to_be_visible()        