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
            <div id="test-editormd">
                <textarea style="display:none;"></textarea>
            </div>
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
                    path    : "../static/editor/lib/"
                })
            })
        </script>
	</body>
</html>
