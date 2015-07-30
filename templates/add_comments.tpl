<div class="content_posts">
    Add comment:<br />
    {% if values['username'] != None %}
        <form action="/new_comment/{{values['kwargs']['_id']}}" method="post">
            <textarea rows="5" cols="50" name="texto"></textarea>
            <input type="submit" value="Submit" />
        </form>
    {% else %}
        <a href="/login">require login</a>
    {% endif %}
</div>