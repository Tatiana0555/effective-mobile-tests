from playwright.sync_api import Page


class FooterPage:
    def __init__(self, page: Page):
        self.page = page

        self.about_link = page.locator("a:has-text('О нас')")
        self.vacancies_link = page.get_by_role("link", name="Вакансии", exact=True)
        self.reviews_link = page.locator("a:has-text('Отзывы')")
        self.contacts_link = page.locator("a:has-text('Контакты')")
        self.outstaff_link = page.locator("a:has-text('Аутстафф')")
        self.employment_link = page.locator("a:has-text('Трудоустройство')")
        self.consult_link = page.locator("a:has-text('Консультация')")
