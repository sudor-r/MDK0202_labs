import re
from datetime import date

from bottle import Bottle, request, template


EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def _fix_mojibake(value: str) -> str:
    # Fix strings like "ÐÐ»ÐµÐ³" that appear when UTF-8 text is misread as Latin-1.
    if "Ð" in value or "Ñ" in value:
        try:
            return value.encode("latin1").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            return value
    return value


def setup_form_routes(app: Bottle) -> None:
    @app.post("/home")
    def my_form():
        user_name = _fix_mojibake((request.forms.get("USERNAME") or "").strip())
        if user_name:
            user_name = user_name[:1].upper() + user_name[1:]
        email = (request.forms.get("ADRESS") or "").strip()
        question = _fix_mojibake((request.forms.get("QUEST") or "").strip())

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

        result = (
            f"Thanks, {user_name}! The answer will be sent to the mail {email}. "
            f"Access Date: {date.today().isoformat()}"
        )
        return template(
            "form_result",
            title="Результат отправки - FishPoint",
            ok=True,
            message=result,
            question=question,
            year=date.today().year,
        )
