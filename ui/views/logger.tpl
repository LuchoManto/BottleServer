<html>
<head>
    <!-- Jquery -->
    <script src="/css/externs/jquery-2.1.4.min.js"></script>
    <!-- Style to body of logger -->
    <style>
    .body_styles{
            background:black;
            color:white;
            font-family: Monospace;
    }
    </style>
</head>
<body class="body_styles">
    <div id="log_content"></div>
</body>
</html>

<!--LOGGER: Function to fill the logger-->
<script>
//Function to fill the log.
    var fill_log = function(){
    var escape_html_new_lines = function(text) {
        var htmls = [];
        var lines = text.split(/\n/);
        var tmpDiv = jQuery(document.createElement('div'));
        for (var i = 0 ; i < lines.length ; i++) {
            htmls.push(tmpDiv.text(lines[i]).html());
        }
        return htmls.join("<br>");
    };

    var log = '';
    $.ajax({
        url: '/raw_log/' + log.length,
        success:
            function(data)
            {
                log += data;
                if(data.length > 0){
                    $('#log_content').html(escape_html_new_lines(log));
                    $('html, body').animate({scrollTop: $(document).height()}, 'fast');
                }
            }
    });
};
</script>

<!--INITIALIZE LOGGER LOOP: Script when document is ready and loops-->
<script>
$(document).ready(function() {
    fill_log();
});

setInterval(fill_log, 5000);
</script>