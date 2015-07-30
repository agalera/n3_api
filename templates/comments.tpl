<div class="content_posts">
    <div class="content_post">
        {% if values['kwargs']['account_type'] == 1 %}
            edit
        {% endif %}
        <h1>{{values['kwargs']['title']}}</h1>
        {{values['kwargs']['texto']}}
        <h4>by: {{values['kwargs']['user']['name']}}</h4>
        <h4>
            tags: 
            {% for valu in values['kwargs']['tags'] %}
                <a href="/search/page/0/tags/{{valu}}">{{valu}}</a>&nbsp;
            {% endfor %}
        </h4>
    </div>

    {% for value in values['kwargs']['comments'] %}
        <div class="content_post">
            {{value['texto']}}
            <h4>by: {{value['user']['name']}}</h4>
        </div>
    {% endfor %}
</div>