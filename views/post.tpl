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
            <form id="forms" method="post" action="/post">
                <div class="title-div">
                    Title <input type="text" class="title-input" name="title" />
                </div>
                <div id="content">
                    <textarea style="display:none;" ></textarea>
                </div>
                <div style="width:90%;margin: 10px auto;">
                    <input type="hidden" id="preview-html" name="preview-html">
                    <input type="submit" onclick="submits()" name="submit" value="提交" style="padding: 5px;" />
                </div>
            </form>
        </div>
        <script src="static/js/jquery.js"></script>
        <script src="static/editor/editormd.min.js"></script>
        <script>
            var testEditor;
            $(function(){
                testEditor = editormd("content",{
					width   : "90%",
                    height  : 640,
                    syncScrolling : "single",
                    path    : "../static/editor/lib/",
                    saveHTMLToTextarea : true,
                    onchange: function(){
                        console.log('preview data:',testEditor.getPreviewedHTML())
                        $('#preview-html').val(testEditor.getPreviewedHTML())
                    }
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

            function submits(){
                console.log('....')
                $('#content').submit()
            }

        </script>
	</body>
</html>
