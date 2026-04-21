% rebase("layout.tpl", title=title, year=year)

<section>
    <h1>Каталог снастей</h1>
    <p class="muted">Популярные товары для спиннинговой и фидерной рыбалки.</p>
</section>

<section class="grid">
    % for product in products:
    <article class="card product">
        <h2>{{product["name"]}}</h2>
        <p>{{product["desc"]}}</p>
        <p class="price">{{product["price"]}}</p>
        <button type="button">В корзину</button>
    </article>
    % end
</section>

