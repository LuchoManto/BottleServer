% rebase('base.tpl')

<!--Main div to insert in base-->
<div id="main_div_module" class="container main_container">
    <!-- Send specific serial div-->
    <div id="specific_serial" class="container padding_top30">
        <div class="col-xs-2">
          <label class="control-label">Send by Serial: </label>
        </div>
        <div class="col-xs-6">
          <input id="send_serial_input" class="form-control" type="text" placeholder="data to send">
        </div>
        <div class="col-xs-2">
            <button id="send_serial_button" class="btn btn-primary">Send</button>
        </div>
    </div>
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
    <div id="uart_state" class="container padding_top30">
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
    <!-- Motor div and link to hide-->
    <a id="motor_div_toggle" href="#"><h2>MOTOR</h2></a>
    <div id="motor_div" class="container" style="display: none;">
        <!-- Engine measurement value div -->
        <div id="engine_value" class="container padding_top10">
            <div class="col-xs-2">
                <label class="control-label">Sensor measurement: </label>
            </div>
            <div class="col-xs-2">
                <button type="button" class="btn btn-primary send_serial" value="GSEx0">Get value</button>
            </div>
        </div>
        <!-- Engine status div -->
        <div id="engine_status" class="container padding_top10">
            <div class="col-xs-2">
                <label class="control-label">Engine Status: </label>
            </div>
            <div class="col-xs-2">
                <button type="button" class="btn btn-success send_serial" value="PWM">On</button>
            </div>
            <div class="col-xs-2">
                <button type="button" class="btn btn-danger send_serial" value="NTP">Off</button>
            </div>
        </div>
        <!-- Engine gain div -->
        <div id="engine_gain" class="container padding_top10">
            <div class="col-xs-2">
                <label class="control-label">Engine Gain: </label>
            </div>
            <div class="col-xs-4">
                <div class="btn-group">
                    <button class="btn btn-default dropdown-toggle" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Gain <span class="caret"></span>
                    </button>
                    <ul class="dropdown-menu">
                        <li><a class="send_serial" value="SGAx0" href="#">0</a></li>
                        <li><a class="send_serial" value="SGAx1" href="#">2</a></li>
                        <li><a class="send_serial" value="SGAx2" href="#">4</a></li>
                        <li><a class="send_serial" value="SGAx3" href="#">8</a></li>
                        <li><a class="send_serial" value="SGAx4" href="#">16</a></li>
                        <li><a class="send_serial" value="SGAx5" href="#">32</a></li>
                        <li><a class="send_serial" value="SGAx6" href="#">64</a></li>
                        <li><a class="send_serial" value="SGAx7" href="#">128</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <!-- Low power div-->
        <div id="low_power" class="container padding_top10">
            <div class="col-xs-2">
                <label class="control-label">Low Power Mode: </label>
            </div>
            <div class="col-xs-2">
                <button type="button" class="btn btn-success send_serial" value="SLP">SLEEP</button>
            </div>
            <div class="col-xs-2">
                <button type="button" class="btn btn-danger send_serial" value="WKP">WAKE UP</button>
            </div>
        </div>
    </div>
    <!-- GPS table and link to hide-->
    <a id="gps_table_toggle" href="#"><h2>GPS</h2></a>
    <div id="gps_table" class="container" style="display: none;">
        <table>
            <tr>
                <th></th>
                <th colspan="7"></th>
                <th><button class="gps_button" value="OP1">op1</button></th>
            </tr>
            <tr>
                <td><button class="gps_button" value="LEFT">&lt;</button></td>
                <td colspan="7"></td>
                <td><button class="gps_button" value="OP2">op2</button></td>
            </tr>
            <tr>
                <td><button class="gps_button" value="RIGHT">&gt;</button></td>
                <td colspan="7"></td>
                <td><button class="gps_button" value="OP3">op3</button></td>
            </tr>
            <tr>
                <td></td>
                <td colspan="7"></td>
                <td><button class="gps_button" value="OP4">op4</button></td>
            </tr>
            <tr>
                <td></td>
                <td><button class="gps_button" value="NUM1">1</button></td>
                <td><button class="gps_button" value="NUM2">2</button></td>
                <td><button class="gps_button" value="NUM3">3</button></td>
                <td><button class="gps_button" value="ENTER">ENTER</button></td>
                <td><button class="gps_button" value="CLEAR">CLEAR</button></td>
                <td><button class="gps_button" value="STATUS">STATUS</button></td>
                <td><button class="gps_button" value="SATINFO">SAT INFO</button></td>
                <td></td>
            </tr>
            <tr>
                <td></td>
                <td><button class="gps_button" value="NUM4">4</button></td>
                <td><button class="gps_button" value="NUM5">5</button></td>
                <td><button class="gps_button" value="NUM6">6</button></td>
                <td><button class="gps_button" value="ALPHA">ALPHA</button></td>
                <td></td>
                <td><button class="gps_button" value="SESSIONS">SESSIONS</button></td>
                <td><button class="gps_button" value="CONTROL">CONTROL</button></td>
                <td></td>
            </tr>
            <tr>
                <td></td>
                <td><button class="gps_button" value="NUM7">7</button></td>
                <td><button class="gps_button" value="NUM8">8</button></td>
                <td><button class="gps_button" value="NUM9">9</button></td>
                <td><button class="gps_button" value="NUM0">0</button></td>
                <td></td>
                <td><button class="gps_button" value="LOGDATA">LOG DATA</button></td>
                <td><button class="gps_button" value="MODIFY">MODIFY</button></td>
                <td><button class="gps_button" value="POWER">POWER</button></td>
            </tr>
        </table>
    </div>
</div>


<!--Script when send a specific value-->
<script>
$("#send_serial_button").click(function(e){
    e.preventDefault();
    //Post with the button
    $.ajax({
        url: '/send_serial/' + $("#send_serial_input").val(),
        cache:false, type: 'POST'
    });
});
</script>

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

<!--Information button send hex value clicked.-->
<script>
$('#show_send_hex_info').click(function(e){
    e.preventDefault();
    $('#send_hex_info').slideToggle();
});
</script>

<!--Script to toggle MOTOR Div-->
<script>
$("#motor_div_toggle").click(function(e){
    e.preventDefault();
    $("#motor_div").toggle();
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

<!--Script to send value of button by serial-->
<script>
$(".send_serial").click(function(e){
    e.preventDefault();
    //Post to connect
    $.ajax({
        url: '/send_serial/' + $(this).attr("value"),
        cache:false, type: 'POST'
    });
});
</script>

<!--Script to toggle GPS Table-->
<script>
$("#gps_table_toggle").click(function(e){
    e.preventDefault();
    $("#gps_table").toggle();
});
</script>

<!--Script when button of GPS pressed-->
<script>
$(".gps_button").click(function(e){
    e.preventDefault();
    //Post with the button
    $.ajax({
        url: '/button_press/' + $(this).val(),
        cache:false, type: 'POST'
    });
});
</script>