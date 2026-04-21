% rebase("layout.tpl", title=title, year=year)

<section class="card">
    <h1>Результат отправки формы</h1>
    % if ok:
    <p class="result-ok">{{message}}</p>
    <p><strong>Your question:</strong> {{question}}</p>
    % else:
    <p class="result-error">{{message}}</p>
    % end
    <p><a class="button" href="/">Вернуться на главную</a></p>
</section>

