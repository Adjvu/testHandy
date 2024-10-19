from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.commboost.ru/login/#/")
    page.get_by_placeholder("Введите вашу почту").click()
    page.get_by_placeholder("Введите ваш пароль").click()
    page.get_by_role("button", name="Войти").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.commboost.ru/login/#/")
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("button", name="☰").click()
    page.get_by_text("Выйти").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)