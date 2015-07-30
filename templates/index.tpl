<h1>UPDATES</h1>
<div class="content_posts">
    {% for value in values[0] %}
        <div class="content_post">
            pepe
            <h1>{{value[0]}}</h1>
            {{value}}
            <h4>by: {{value[1]}} , <a href="/comments/{{value[0]}}">{{value[4]}} comments</a></h4>
            
        </div>
    {% endfor %}
</div>
actual page: {{values[2]}}
total pages: {{values[1][0][0]/10}}
{% if values[2] != 0 %}
    izk
{% endif %}
{% if values[2] < values[1][0][0]/10 %}
    dere
{% endif %}
