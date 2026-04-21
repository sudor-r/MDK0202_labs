<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{{title}}</title>
    <link rel="stylesheet" href="/static/css/site.css" />
</head>
<body>
    <header class="header">
        <div class="wrap nav">
            <a class="brand" href="/">
                <img src="/static/images/logo.svg" alt="FishPoint" />
                <span>FishPoint</span>
            </a>
            <nav>
                <a href="/">Главная</a>
                <a href="/catalog">Каталог</a>
                <a href="/about">О магазине</a>
                <a href="/contact">Контакты</a>
            </nav>
        </div>
    </header>

    <main class="wrap content">
        {{!base}}
    </main>

    <footer class="footer">
        <div class="wrap">
            <p>&copy; {{year}} FishPoint. Всё для комфортной рыбалки.</p>
        </div>
    </footer>
</body>
</html>

