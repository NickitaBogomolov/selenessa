from playwright.sync_api import sync_playwright


class BrowserSession:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def __enter__(self):
        return self.page

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.browser.close()
        self.playwright.stop()


def login(page, url, user, password):
    page.goto(url)

    # Ожидание и заполнение полей
    username_field = page.locator("//input[@placeholder='Пользователь']")
    username_field.wait_for()
    username_field.fill(user)

    password_field = page.locator("//input[@placeholder='Пароль']")
    password_field.fill(password)

    submit_button = page.locator("//input[@value='Войти']")
    submit_button.click()


def left_menu_click(page, item):
    xpath = f"//div[@class='themeBoxName' and contains(., '{item}')]"
    left_menu_el = page.locator(xpath)
    left_menu_el.click()


def search(page, item):
    search_field = page.locator("//input[@id='funcPanel_panelEdit_i0']")
    search_field.wait_for()
    search_field.fill(item)

    # Клик на найденный элемент
    item_element = page.locator("//div[@id='cmd_0_0_0_txt']")
    item_element.click()


if __name__ == "__main__":
    with BrowserSession() as page:
        login(
            page,
            "https://1cfresh.com/a/ea/3654418",
            "nick.bog.17@yandex.ru",
            "2aoqEls",
        )
        left_menu_click(page, "Главное")

        search(page, "Платежные поручения")

        input("Нажмите Enter, чтобы закрыть браузер...")
