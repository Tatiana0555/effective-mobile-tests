import allure
from pages.footer_page import FooterPage
from playwright.sync_api import expect


@allure.feature("Footer navigation")
def test_footer_about(page):
    footer = FooterPage(page)
    with allure.step("Кликаем 'О нас'"):
        expect(footer.about_link).to_be_visible()
        footer.about_link.scroll_into_view_if_needed()
        footer.about_link.click()
    with allure.step("Проверяем изменение URL на #about"):
        assert "#about" in page.url


@allure.feature("Footer navigation")
def test_footer_vacancies(page):
    footer = FooterPage(page)
    with allure.step("Кликаем 'Вакансии'"):
        footer.vacancies_link.click()
    with allure.step("Проверяем изменение URL на #specializations"):
        assert "#specializations" in page.url


@allure.feature("Footer navigation")
def test_footer_reviews(page):
    footer = FooterPage(page)
    with allure.step("Кликаем 'Отзывы'"):
        footer.reviews_link.click()
    with allure.step("Проверяем изменение URL на #testimonials"):
        assert "#testimonials" in page.url


@allure.feature("Footer navigation")
def test_footer_contacts(page):
    footer = FooterPage(page)
    with allure.step("Кликаем 'Контакты'"):
        footer.contacts_link.click()
    with allure.step("Проверяем изменение URL на #contact"):
        assert "#contact" in page.url


@allure.feature("Footer navigation")
def test_footer_outstaff(page):
    footer = FooterPage(page)
    with allure.step("Кликаем 'Аутстафф'"):
        footer.outstaff_link.click()
    with allure.step("Проверяем изменение URL на #services"):
        assert "#services" in page.url


@allure.feature("Footer navigation")
def test_footer_employment(page):
    footer = FooterPage(page)
    with allure.step("Кликаем 'Трудоустройство'"):
        footer.employment_link.click()
    with allure.step("Проверяем изменение URL на #services"):
        assert "#services" in page.url


@allure.feature("Footer navigation")
def test_footer_consulting(page):
    footer = FooterPage(page)
    with allure.step("Кликаем 'Консультация'"):
        footer.consult_link.click()
    with allure.step("Проверяем изменение URL на #contact"):
        assert "#contact" in page.url
