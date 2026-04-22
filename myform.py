import json
import re
from datetime import date
from pathlib import Path

from bottle import Bottle, request, template


EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
QUESTIONS_FILE = Path("data/questions.json")

LAST_FORM_DATA = {}


def fix_encoding(text: str) -> str:
    """Исправляет кодировку если она была испорчена"""
    if not text:
        return text
    try:
        return text.encode('latin1').decode('utf-8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        return text


def _load_questions() -> dict:
    if not QUESTIONS_FILE.exists():
        return {}
    try:
        with QUESTIONS_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def _save_questions(data: dict) -> None:
    QUESTIONS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with QUESTIONS_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def setup_form_routes(app: Bottle) -> None:
    @app.post("/home")
    def my_form():
        request.forms.encoding = 'utf-8'
        
        user_name = fix_encoding((request.forms.get("USERNAME") or "").strip())
        if user_name:
            user_name = user_name[:1].upper() + user_name[1:]
        email = (request.forms.get("ADRESS") or "").strip()
        question = fix_encoding((request.forms.get("QUEST") or "").strip())

        if not user_name or not email or not question:
            return template(
                "form_result",
                title="Результат отправки - FishPoint",
                ok=False,
                message="Ошибка: заполните все поля формы (имя, email, вопрос).",
                year=date.today().year,
            )

        if not EMAIL_PATTERN.fullmatch(email):
            return template(
                "form_result",
                title="Результат отправки - FishPoint",
                ok=False,
                message="Ошибка: email не соответствует формату example@mail.com.",
                year=date.today().year,
            )

        if len(question) <= 3:
            return template(
                "form_result",
                title="Результат отправки - FishPoint",
                ok=False,
                message="Ошибка: вопрос должен содержать более 3 символов.",
                year=date.today().year,
            )

        if question.isdigit():
            return template(
                "form_result",
                title="Результат отправки - FishPoint",
                ok=False,
                message="Ошибка: вопрос не может состоять только из цифр.",
                year=date.today().year,
            )

        LAST_FORM_DATA[email] = [user_name, question]
        print("DEBUG LAST_FORM_DATA:", LAST_FORM_DATA)

        data = _load_questions()
        user_data = data.get(email, {"username": user_name, "questions": []})
        user_data["username"] = user_name

        questions = user_data.get("questions", [])
        if not isinstance(questions, list):
            questions = []
        if question not in questions:
            questions.append(question)
        user_data["questions"] = questions
        data[email] = user_data
        _save_questions(data)

        result = (
            f"Thanks, {user_name}! The answer will be sent to the mail {email}. "
            f"Access Date: {date.today().isoformat()}. "
            f"Saved questions: {len(questions)}"
        )
        return template(
            "form_result",
            title="Результат отправки - FishPoint",
            ok=True,
            message=result,
            question=question,
            year=date.today().year,
        )
