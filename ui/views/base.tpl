<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
    <!-- For icon hide and show console.-->
    <link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css" rel="stylesheet">

    <!--Bootstrap navbar-->
    <link rel="stylesheet" href="/css/externs/bootstrap.css">
    <!-- Jquery -->
    <script src="/css/externs/jquery.min.js"></script>
    <!-- Jquery for the resizable-->
    <link rel="stylesheet" href="/css/externs/jquery-ui.css">
    <script src="/css/externs/jquery-ui.min.js"></script>
	<!-- Bootstrap -->
    <script src="/css/externs/bootstrap.min.js"></script>

    <!-- Styles file-->
    <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
    <!-- Navigation Bar -->
    <div id="navbar_top" class="navbar navbar_top navbar-static-top">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" style="background-color:black;" data-toggle="collapse" data-target="#navbar_ex_collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar background_c_white"></span>
                    <span class="icon-bar background_c_white"></span>
                    <span class="icon-bar background_c_white"></span>
                </button>
                <a class="navbar_top_icon"><img height="45" width="45" alt="Brand" src="/images/wifi_icon.png"></a>
            </div>
            <div class="collapse navbar-collapse" id="navbar_ex_collapse">
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="/">Home</a></li>
                    <li><a href="/graphics">Datos</a></li>
                </ul>
            </div>
        </div>
    </div>
    <!-- Main div where tpl are inserted-->
    <div id="main_div_base">
        {{!base}}
    </div>
    <!-- Logger Div-->
    <!-- <div id="navbar_bottom" class="navbar navbar-fixed-bottom navbar_bottom"> -->
        <!-- <div id="resizable_bottom" class="resizable_bottom"> -->
             <!-- Source of log_screen route /logger with the function to fill the log -->
            <!-- <div class="container"> -->
                <!-- <h5>Log <a href="#" id="btn_hide_log" style="margin-left:10px;"><i id="toggle_icon" class="icon-chevron-down" aria-hidden="true"></i></a></h5> -->
                <!-- <iframe id="log_screen" src="/logger" width="100%" height="100px" style="z-index:0;"></iframe> -->
            <!-- </div> -->
        <!-- </div> -->
    <!-- </div> -->
</body>
</html>

<!--LOGGER: Script resizable log.-->
<script>
//Define tamaño minimo del resizable
var default_bottom_width = parseInt($('#navbar_bottom').css('height'));

//Definir tamaño del div y pantalla cuando hago rezise
var set_bottom_width = function(w){
    $('#navbar_bottom').css('height', w + 'px');
    $('#log_screen').css('height', (w-40) + 'px');
}

//Function to resizable the log.
$('#resizable_bottom').resizable({
    handles: "n",
    minHeight: default_bottom_width,
    resize: function(event, ui){
        $('#resizable_bottom').css('position', 'static');
        height = parseInt($('#resizable_bottom').css('height'));
        set_bottom_width(height);
    },
    start: function(event, ui) {
        $('iframe').css('pointer-events','none');
    },
    stop: function(event, ui) {
        $('iframe').css('pointer-events','auto');
    }
});
</script>

<!--LOGGER: Click hide click log-->
<script>
$('#btn_hide_log').click(function(e){
    e.preventDefault();
    var log_screen = $('#log_screen');
    if(log_screen.css('display') === 'none'){
        $("#resizable_bottom").resizable("enable");
        log_screen.show();
        set_bottom_width(parseInt($('#resizable_bottom').css('height'))||default_bottom_width);
        $('#toggle_icon').removeClass('icon-chevron-up').addClass('icon-chevron-down');
        $('#navbar_bottom').css({'z-index':'1'})
    }
    else {
        $("#resizable_bottom").resizable("disable");
        log_screen.hide();
        set_bottom_width(20);
        $('#toggle_icon').removeClass('icon-chevron-down').addClass('icon-chevron-up');
        $('#navbar_bottom').css({'z-index':'0'})
    }
});
</script>

<!--INITIALIZE: Script when document is ready and loops-->
<script>
$(document).ready(function() {
});

//Ejemplo de loop
//setInterval(fill_log, 1000);
</script>