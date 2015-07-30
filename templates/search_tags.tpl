<h1>Search tags</h1>
<div class="content_posts">
    {% for value in values['kwargs']['news']['result'] %}
        <div class="content_post">
            <h1>{{value['title']}}</h1>
            {{value['texto']}}
            <h4>by: {{value['user']['name']}} ,
                <a href="/comments/{{value['_id']}}">
                    {{value['comments']|length}} comments
                </a>
            </h4>
            <h4>
            tags: 
                {% for valu in value['tags'] %}
                    <a href="/search/page/0/tags/{{valu}}">{{valu}}</a>&nbsp;
                {% endfor %}
            </h4>
        </div>
    {% endfor %}
</div>
{% if values['kwargs']['news']['page'] == True %}
    {% if values['kwargs']['news']['page'] != 0 %}
        <a href="/search/page/{{values['kwargs']['news']['page']|int - 1}}/tags/{{values['kwargs']['tags']}}"><</a>
    {% endif %}
    {% if values['kwargs']['news']['page'] +1 < values['kwargs']['news']['n_posts']/10 %}
        <a href="/search/page/{{values['kwargs']['news']['page']|int + 1}}/tags/{{values['kwargs']['tags']}}">></a>
    {% endif %}
{% endif %}