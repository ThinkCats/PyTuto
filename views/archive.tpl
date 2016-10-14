<div class="mod-archive__item">
    % for item in articles:
    % year_ = item[0]
	<div id="{{ year_ }}" class="mod-archive__year">{{ year_ }}</div>
	<ul class="mod-archive__list">
    %   for article in item[1]:
    %       time = article.createTime
    %       title = article.title
    %       id = article.id
    %       format_time = ('%s-%s-%s' % (time.year,time.month,time.day))
		<li>
            <time class="mod-archive__time" datetime="{{ time }}">{{ format_time }}</time>
            <span>—</span>
            <a href="/article/{{id}}.html" title="{{ title }}">{{title}}</a>
        </li>
    %   end
	</ul>
    % end
</div>
