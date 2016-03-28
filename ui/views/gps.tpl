% rebase('base.tpl')

<!--Main div to insert in base-->
<div id="main_div_module" class="container main_container">
    <!-- Send hex value by serial div-->
    <div id="send_hex_value" class="container padding_top30">
        <div class="col-xs-2">
            <label class="control-label">Send Hex: </label>
            <button id="show_send_hex_info" class="btn btn-xs btn-info"><i class="icon-info-sign icon-large"></i></button>
        </div>
        <div class="col-xs-6">
          <input id="send_hex_input" class="form-control" type="text" placeholder="hex value to send">
        </div>
        <div class="col-xs-2">
            <button id="send_hex_button" class="btn btn-primary">Send</button>
        </div>
    </div>
    <!-- Send hex info panel div-->
    <div id="send_hex_info" class="container padding_top20" hidden>
        <div class="panel panel-info col-xs-10">
            <div class="panel-body padding_10">
                <div class="row">
                    <label class="control-label"> Send hex values by the UART.</label>
                    <label class="control-label"> You can set the input as 'x00x01x02' or '000102'</label>
                    <label class="control-label"> or '00 01 02' or 'x00 x01 x02'.</label>
                </div>
                <div class="row">
                    <label class="control-label"> The 'x' character and spaces are going to be ignored.</label>.</label>
                </div>
            </div>
        </div>
    </div>
    <!-- Active listener UART and disable it-->
    <div id="uart_state" class="container padding_top20">
        <div class="col-xs-2">
          <label class="control-label">Uart state: </label>
        </div>
        <div class="col-xs-6">
          <div class="btn-group">
              <button class="btn btn-default dropdown-toggle" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                State <span class="caret"></span>
              </button>
              <ul class="dropdown-menu">
                  <li>
                      <a class="uart_connection" value="connected" href="#">Connected</a>
                  </li>
                  <li>
                      <a class="uart_connection" value="disconnected" href="#">Disconnected</a>
                  </li>
              </ul>
          </div>
        </div>
    </div>
    <!-- GPS image -->
    <div id="gps_image_div" class="container padding_top20" align="center" style="position:relative;width:678px;height:275px;">
        <img src="images/gps.jpg" id="gps_image">

        <div style="position:absolute;left:115px;top:65px;width:400px;height:18px;z-index:1;">
        <!--<span id="renglon_1" class="renglon_gps">CH1-4&nbsp; SV30&nbsp; SV25&nbsp; SV02&nbsp; SV23 |MORE CHAN</span>-->
            <span id="renglon_1" class="renglon_gps"></span>
        </div>
        <div style="position:absolute;left:115px;top:82px;width:400px;height:16px;z-index:1;">
            <!--<span id="renglon_2" class="renglon_gps">ELEV&nbsp;&nbsp;&nbsp; &#45;&#45;&nbsp;&nbsp;&nbsp; &#45;&#45;&nbsp;&nbsp;&nbsp; &#45;&#45;&nbsp;&nbsp;&nbsp; &#45;&#45;&nbsp; |&nbsp;&nbsp; &nbsp;&nbsp; URA</span>-->
            <span id="renglon_2" class="renglon_gps"></span>
        </div>
        <div style="position:absolute;left:115px;top:101px;width:400px;height:16px;z-index:1;">
            <!--<span id="renglon_3" class="renglon_gps">SNR&nbsp;&nbsp;&nbsp;&nbsp; &#45;&#45;&nbsp;&nbsp;&nbsp; &#45;&#45;&nbsp;&nbsp;&nbsp; &#45;&#45;&nbsp;&nbsp;&nbsp; &#45;&#45;&nbsp; |&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; |</span>-->
            <span id="renglon_3" class="renglon_gps"></span>
        </div>
        <div style="position:absolute;left:115px;top:119px;width:400px;height:16px;z-index:1;">
            <!--<span id="renglon_4" class="renglon_gps">AZMTH&nbsp;&nbsp; &#45;&#45;&nbsp;&nbsp;&nbsp; &#45;&#45;&nbsp;&nbsp;&nbsp; &#45;&#45;&nbsp;&nbsp;&nbsp; &#45;&#45;&nbsp; |&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; |</span>-->
            <span id="renglon_4" class="renglon_gps"></span>
        </div>

        <input type="button" class="gps_button" value="OP1" style="position:absolute;left:579px;top:44px;width:44px;height:24px;z-index:1;">
        <input type="button" class="gps_button" value="OP2" style="position:absolute;left:579px;top:79px;width:44px;height:24px;z-index:1;">
        <input type="button" class="gps_button" value="OP3" style="position:absolute;left:579px;top:112px;width:44px;height:24px;z-index:1;">
        <input type="button" class="gps_button" value="OP4" style="position:absolute;left:579px;top:143px;width:44px;height:24px;z-index:1;">

        <input type="button" class="gps_button" value="POWER" style="position:absolute;left:579px;top:200px;width:44px;height:24px;z-index:1;">

        <input type="button" class="gps_button" value="SATINFO" style="position:absolute;left:469px;top:153px;width:44px;height:24px;z-index:1;">
        <input type="button" class="gps_button" value="CONTROL" style="position:absolute;left:469px;top:185px;width:44px;height:24px;z-index:1;">
        <input type="button" class="gps_button" value="MODIFY" style="position:absolute;left:469px;top:217px;width:44px;height:24px;z-index:1;">

        <input type="button" class="gps_button" value="STATUS" style="position:absolute;left:411px;top:153px;width:44px;height:24px;z-index:1;">
        <input type="button" class="gps_button" value="SESSIONS" style="position:absolute;left:411px;top:185px;width:44px;height:24px;z-index:1;">
        <input type="button" class="gps_button" value="LOGDATA" style="position:absolute;left:411px;top:217px;width:44px;height:24px;z-index:1;">

        <input type="button" class="gps_button" value="CLEAR" style="position:absolute;left:350px;top:153px;width:44px;height:24px;z-index:1;">

        <input type="button" class="gps_button" value="ENTER" style="position:absolute;left:291px;top:152px;width:44px;height:24px;z-index:1;">
        <input type="button" class="gps_button" value="ALPHA" style="position:absolute;left:291px;top:185px;width:44px;height:24px;z-index:1;">

        <input type="button" class="gps_button" value="NUM0" style="position:absolute;left:271px;top:217px;width:44px;height:24px;z-index:1;">

        <input type="button" class="gps_button" value="NUM3" style="position:absolute;left:220px;top:153px;width:44px;height:24px;z-index:1;">
        <input type="button" class="gps_button" value="NUM6" style="position:absolute;left:220px;top:185px;width:44px;height:24px;z-index:1;">
        <input type="button" class="gps_button" value="NUM9" style="position:absolute;left:220px;top:217px;width:44px;height:24px;z-index:1;">

        <input type="button" class="gps_button" value="NUM2" style="position:absolute;left:165px;top:153px;width:44px;height:24px;z-index:1;">
        <input type="button" class="gps_button" value="NUM5" style="position:absolute;left:165px;top:185px;width:44px;height:24px;z-index:1;">
        <input type="button" class="gps_button" value="NUM8" style="position:absolute;left:165px;top:217px;width:44px;height:24px;z-index:1;">

        <input type="button" class="gps_button" value="NUM1" style="position:absolute;left:115px;top:153px;width:44px;height:24px;z-index:1;">
        <input type="button" class="gps_button" value="NUM4" style="position:absolute;left:115px;top:185px;width:44px;height:24px;z-index:1;">
        <input type="button" class="gps_button" value="NUM7" style="position:absolute;left:115px;top:217px;width:44px;height:24px;z-index:1;">

        <input type="button" class="gps_button" value="LEFT" style="position:absolute;left:75px;top:70px;width:28px;height:29px;z-index:1;">
        <input type="button" class="gps_button" value="RIGHT" style="position:absolute;left:75px;top:103px;width:28px;height:29px;z-index:1;">
    </div>
</div>

<!--Script when send a hex value-->
<script>
$("#send_hex_button").click(function(e){
    e.preventDefault();
    //Post with the button
    $.ajax({
        url: '/send_hex/' + $("#send_hex_input").val(),
        cache:false, type: 'POST'
    });
});
</script>

<!--Click Information button send hex clicked.-->
<script>
$('#show_send_hex_info').click(function(e){
    e.preventDefault();
    $('#send_hex_info').slideToggle();
});
</script>

<!--Script to connect/disconnect UART-->
<script>
$(".uart_connection").click(function(e){
    e.preventDefault();
    //Post to connect
    $.ajax({
        url: '/uart_state/' + $(this).attr("value"),
        cache:false, type: 'POST'
    });
});
</script>

<!--Script when button of GPS pressed-->
<script>
/*
$(".gps_button").click(function(e){
    e.preventDefault();
    //Post with the button
    $.ajax({
        url: '/button_press/' + $(this).val(),
        cache:false, type: 'POST'
    });
});
*/
$(".gps_button").click(function(e){
    e.preventDefault();
    //Post with the button
    $.getJSON('/button_press/' + $(this).val(),
        function(data)
        {
            $('#renglon_1').html(data['renglon1'])
            $('#renglon_2').html(data['renglon2'])
            $('#renglon_3').html(data['renglon3'])
            $('#renglon_4').html(data['renglon4'])
        }
        )
        .fail(function(){
                console.log("Error actualizando la pantalla del gps");
              }
    );
});
</script>




<!-- Actualizar pantalla GPS y bucle-->
<script>
var actualizarpantallaGPS = function()
{
    $.getJSON('/gpslines',
        function(data)
        {
            $('#renglon_1').html(data['renglon1'])
            $('#renglon_2').html(data['renglon2'])
            $('#renglon_3').html(data['renglon3'])
            $('#renglon_4').html(data['renglon4'])
        }
        )
        .fail(function(){
                console.log("Error actualizando la pantalla del gps");
              }
    );
};

actualizarpantallaGPS();

//setInterval(actualizarpantallaGPS, 7000);
</script>