<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Post</title>
        <link rel="stylesheet" href="static/css/style.css" />
        <link rel="stylesheet" href="static/editor/css/editormd.css" />
    </head>
	<body style="width: 100%">
        <div id="layout">
            <header>
                <h1>Simple example</h1>
            </header>
            <div style="display:none">
                <div> preview </div>
                <div class="markdown-body">
                    <h1 id="h1-hehe"><a name="hehe" class="reference-link"></a><span class="header-link octicon octicon-link"></span>hehe</h1><ul>
                    <li>hehe</li><li>new</li></ul>
                </div>
            </div>
            <form>
            <div id="test-editormd">
                <textarea style="display:none;"></textarea>
            </div>
            <div style="width:90%;margin: 10px auto;">
            <input type="submit" name="submit" value="提交表单 Submit" style="padding: 5px;" /> 
            </div>               
            </form>
        </div>
        <script src="static/js/jquery.js"></script>
        <script src="static/editor/editormd.min.js"></script>
        <script>
            var testEditor;
            $(function(){
                testEditor = editormd("test-editormd",{
					width   : "90%",
                    height  : 640,
                    syncScrolling : "single",
                    path    : "../static/editor/lib/",
                    saveHTMLToTextarea : true
                })
            })

            function convert(){
                var markdown_text = testEditor.getMarkdown();
                var html_text = testEditor.getHTML();
                var preview = testEditor.getPreviewedHTML();
                console.log('markdown:',markdown_text);
                console.log('html:',html_text);
                console.log('preview:', preview);
            }
        </script>
	</body>
</html>
