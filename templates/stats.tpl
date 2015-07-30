<div class="content_posts">
    % for value in values:
        <div class="content_post">
            <h1>{{value[0]}}</h1>
            <h3>{{value[1]}}</h3>
            <h4>reply {{value[2]}}</h4>
        </div>
            
    % end
</div>