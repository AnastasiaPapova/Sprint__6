import pytest
import allure
from pages.main_page import YandexScooterMainPage
from main_data.all_urls import Urls
from main_data.locators import AnswersQuestionsFAQ
from main_data.test_data import YandexScooterFAQAnswers
from conftest import driver


class TestYandexScooterFAQ:
    @allure.description("Проверяем список вопросов и ответов на главной странице")
    @pytest.mark.parametrize('question, answer, expected_answer',
                             [(AnswersQuestionsFAQ.FIRST_QUESTION_BUTTON, AnswersQuestionsFAQ.FIRST_QUESTION_ANSWER,
                               YandexScooterFAQAnswers.FIRST_ANSWER),
                              (AnswersQuestionsFAQ.SECOND_QUESTION_BUTTON, AnswersQuestionsFAQ.SECOND_QUESTION_ANSWER,
                               YandexScooterFAQAnswers.SECOND_ANSWER),
                              (AnswersQuestionsFAQ.THIRD_QUESTION_BUTTON, AnswersQuestionsFAQ.THIRD_QUESTION_ANSWER,
                               YandexScooterFAQAnswers.THIRD_ANSWER),
                              (AnswersQuestionsFAQ.FOURTH_QUESTION_BUTTON, AnswersQuestionsFAQ.FOURTH_QUESTION_ANSWER,
                               YandexScooterFAQAnswers.FOURTH_ANSWER),
                              (AnswersQuestionsFAQ.FIFTH_QUESTION_BUTTON, AnswersQuestionsFAQ.FIFTH_QUESTION_ANSWER,
                               YandexScooterFAQAnswers.FIFTH_ANSWER),
                              (AnswersQuestionsFAQ.SIXTH_QUESTION_BUTTON, AnswersQuestionsFAQ.SIXTH_QUESTION_ANSWER,
                               YandexScooterFAQAnswers.SIXTH_ANSWER),
                              (AnswersQuestionsFAQ.SEVENTH_QUESTION_BUTTON, AnswersQuestionsFAQ.SEVENTH_QUESTION_ANSWER,
                               YandexScooterFAQAnswers.SEVENTH_ANSWER),
                              (AnswersQuestionsFAQ.EIGHTH_QUESTION_BUTTON, AnswersQuestionsFAQ.EIGHTH_QUESTION_ANSWER,
                               YandexScooterFAQAnswers.EIGHTH_ANSWER)])
    def test_questions(self, question, answer, expected_answer, driver):
        main_page = YandexScooterMainPage(driver)
        main_page.go_to_site(Urls.MAIN_PAGE)
        main_page.click_cookie_accept_button()
        get_answer = main_page.click_main_page_FAQ(question, answer)
        assert get_answer == expected_answer, 'Ответ на вопрос не совпадает с ожидаемым значением'
