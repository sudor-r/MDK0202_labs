% rebase("layout.tpl", title=title, year=year)

<section class="hero">
    <div>
        <h1>Рыболовный магазин FishPoint</h1>
        <p>
            Подбираем снасти для хищника и мирной рыбы: от катушек и шнуров
            до готовых наборов приманок.
        </p>
        <a class="button" href="/catalog">Перейти в каталог</a>
    </div>
    <img src="/static/images/hero.svg" alt="Рыбалка" />
</section>

<section class="grid">
    <article class="card">
        <h2>Быстрая отправка</h2>
        <p>Собираем и передаем заказ в доставку в течение 24 часов.</p>
    </article>
    <article class="card">
        <h2>Проверенные бренды</h2>
        <p>В ассортименте товары, которые тестируют наши консультанты.</p>
    </article>
    <article class="card">
        <h2>Подбор под водоём</h2>
        <p>Поможем выбрать снасти под реку, озеро или платник.</p>
    </article>
</section>

<section class="card form-card">
    <h3>Ask a Question</h3>
    <form action="/home" method="post" accept-charset="UTF-8">
        <p>
            <textarea
                rows="2"
                cols="50"
                name="QUEST"
                placeholder="Your question"
                class="fixed-textarea"
            ></textarea>
        </p>
        <p>
            <input
                type="text"
                size="50"
                name="USERNAME"
                placeholder="Ваше имя"
            />
        </p>
        <p>
            <input
                type="text"
                size="50"
                name="ADRESS"
                placeholder="Your email"
            />
        </p>
        <p>
            <input type="submit" value="Send" class="btn btn-default" />
        </p>
    </form>
</section>