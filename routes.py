from datetime import datetime

from bottle import Bottle, static_file, template


def setup_routes(app: Bottle) -> None:
    @app.route("/static/<filepath:path>")
    def server_static(filepath):
        return static_file(filepath, root="static")

    @app.route("/")
    def index():
        return template(
            "index",
            title="FishPoint - Рыболовный магазин",
            year=datetime.now().year,
        )

    @app.route("/catalog")
    def catalog():
        products = [
            {
                "name": "Спиннинг River Strike 2.4 м",
                "price": "7 490 руб.",
                "desc": "Универсальный спиннинг для береговой ловли щуки и судака.",
            },
            {
                "name": "Катушка AquaSpin 3000",
                "price": "5 290 руб.",
                "desc": "Легкая катушка с плавным фрикционом и защитой от влаги.",
            },
            {
                "name": "Набор приманок Pike Mix (12 шт.)",
                "price": "1 890 руб.",
                "desc": "Подборка силиконовых приманок под разные условия воды.",
            },
            {
                "name": "Плетёный шнур 0.14 мм, 150 м",
                "price": "1 150 руб.",
                "desc": "Высокая прочность и минимальная растяжимость для точного контроля.",
            },
        ]
        return template(
            "catalog",
            title="Каталог - FishPoint",
            products=products,
            year=datetime.now().year,
        )

    @app.route("/about")
    def about():
        return template(
            "about",
            title="О магазине - FishPoint",
            year=datetime.now().year,
        )

    @app.route("/contact")
    def contact():
        return template(
            "contact",
            title="Контакты - FishPoint",
            year=datetime.now().year,
        )
