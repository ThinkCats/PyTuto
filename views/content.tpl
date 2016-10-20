% time = article.createTime
% time_deatail = time.strftime('%Y-%m-%d %H:%M:%S')
% format_time = ('%s年%s月%s日' % (time.year,time.month,time.day))
<article class="mod-post mod-post__type-post">
	<header>
		<h1 class="mod-post__title">{{ article.title }}</h1>
	</header>
	<div class="mod-post__entry wzulli">
        <div class="markdown-body  editormd-preview-container">
            {{ !article.preview}}
        </div>
	</div>
	<div class="mod-post__meta">
		<div>
			<div>
				— 于 <time datetime="{{ time_deatail }}">{{ format_time }}</time>发表；
			</div>
			<div>— 文内使用到的标签：<span class="mod_tag"><a href="http://www.wpke.net/tag/%e5%bc%80%e5%8f%91%e8%80%85" rel="tag">开发者</a></span></div>
		</div>
	</div>
</article>
