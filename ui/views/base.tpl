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

  <!-- hasta aca es lo de gaston-->
    <style type="text/css">

#jsalarmclock{
font-family: Tahoma;
font-weight: bold;
font-size: 12px;
}

#jsalarmclock div{
margin-bottom: 0.8em;
}

#jsalarmclock div.leftcolumn{
float: left;
width: 150px;
font-size: 13px;
background-color: lightyellow;
clear: left;
}

#jsalarmclock span{
margin-right: 5px;
}

</style>

<script type="text/javascript">

/***********************************************

* JavaScript Alarm Clock- by JavaScript Kit (www.javascriptkit.com)
* This notice must stay intact for usage
* Visit JavaScript Kit at http://www.javascriptkit.com/ for this script and 100s more

***********************************************/

var jsalarm={
	padfield:function(f){
		return (f<10)? "0"+f : f
	},
	showcurrenttime:function(){
		var dateobj=new Date()
		var ct=this.padfield(dateobj.getHours())+":"+this.padfield(dateobj.getMinutes())+":"+this.padfield(dateobj.getSeconds())
		this.ctref.innerHTML=ct
		this.ctref.setAttribute("title", ct)
		if (typeof this.hourwake!="undefined"){ //if alarm is set
			if (this.ctref.title==(this.hourwake+":"+this.minutewake+":"+this.secondwake)){
				clearInterval(jsalarm.timer)
				window.location=document.getElementById("musicloc").value
			}
		}
	},
	init:function(){
		var dateobj=new Date()
		this.ctref=document.getElementById("jsalarm_ct")
		this.submitref=document.getElementById("submitbutton")
		this.submitref.onclick=function(){
			jsalarm.setalarm()
			this.value="Alarm Set"
			this.disabled=true
			return false
		}
		this.resetref=document.getElementById("resetbutton")
		this.resetref.onclick=function(){
		jsalarm.submitref.disabled=false
		jsalarm.hourwake=undefined
		jsalarm.hourselect.disabled=false
		jsalarm.minuteselect.disabled=false
		jsalarm.secondselect.disabled=false
		return false
		}
		var selections=document.getElementsByTagName("select")
		this.hourselect=selections[0]
		this.minuteselect=selections[1]
		this.secondselect=selections[2]
		for (var i=0; i<60; i++){
			if (i<24) //If still within range of hours field: 0-23
			this.hourselect[i]=new Option(this.padfield(i), this.padfield(i), false, dateobj.getHours()==i)
			this.minuteselect[i]=new Option(this.padfield(i), this.padfield(i), false, dateobj.getMinutes()==i)
			this.secondselect[i]=new Option(this.padfield(i), this.padfield(i), false, dateobj.getSeconds()==i)

		}
		jsalarm.showcurrenttime()
		jsalarm.timer=setInterval(function(){jsalarm.showcurrenttime()}, 1000)
	},
	setalarm:function(){
		this.hourwake=this.hourselect.options[this.hourselect.selectedIndex].value
		this.minutewake=this.minuteselect.options[this.minuteselect.selectedIndex].value
		this.secondwake=this.secondselect.options[this.secondselect.selectedIndex].value
		this.hourselect.disabled=true
		this.minuteselect.disabled=true
		this.secondselect.disabled=true
	}
}

</script>
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
                    <li><a href="/gps">GPS</a></li>
                    <li><a href="/motor">EF-Sensor</a></li>
                </ul>
            </div>
        </div>
    </div>
    <!-- Main div where tpl are inserted-->
    <div id="main_div_base">
        {{!base}}
    </div>
    <!-- Logger Div-->
    <div id="navbar_bottom" class="navbar navbar-fixed-bottom navbar_bottom">
        <div id="resizable_bottom" class="resizable_bottom">
            <!-- Source of log_screen route /logger with the function to fill the log-->
            <div class="container">
                <h5>Log <a href="#" id="btn_hide_log" style="margin-left:10px;"><i id="toggle_icon" class="icon-chevron-down" aria-hidden="true"></i></a></h5>
                <iframe id="log_screen" src="/logger" width="100%" height="100px" style="z-index:0;"></iframe>
            </div>
        </div>
    </div>
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