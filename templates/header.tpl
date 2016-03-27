<html>
    <head>
        <script src="//cdn.tinymce.com/4/tinymce.min.js"></script>
        <script type="text/javascript">
tinymce.init({
    selector: "textarea",
    plugins: [
        "advlist autolink lists link image charmap print preview anchor",
        "searchreplace visualblocks code fullscreen",
        "insertdatetime media table contextmenu paste"
    ],
    toolbar: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image"
});
</script>
        <title>Ñ3 - {{title}}</title>
        <link href="/static/base.css" rel="stylesheet" type="text/css">
    </head>
    <body>
    <div id="container">
        <div id="header">
            <div class="logo">Ñ3</div>
            <div class="login">
                {% if username == None %}
                    <a href="/login">Login</a>
                {% else %}
                    {{username}} - <a href="/logout">Logout</a>
                {% endif %}
            </div>
            <div class="content_menu">
                {% for x in ['news', 'about'] %}
                    {% if x == section %}
                        <a href="/{{x}}" style="color: #999">{{x}}</a>
                    {% else %}
                        <a href="/{{x}}">{{x}}</a>
                    {% endif %}
                {% endfor %}
            </div>
        </div>
        <div id="right_column">
            <h1>Twitter</h1>
            <a class="twitter-timeline" href="https://twitter.com/KiAnXineki" data-widget-id="364465053631664128">Tweets por @KiAnXineki</a>
            <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>


        </div>
        <div class="body">
