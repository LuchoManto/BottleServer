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
    <!-- Engine measurement value div -->
    <div id="engine_value" class="container padding_top20">
        <div class="col-xs-2">
            <label class="control-label">Sensor measurement: </label>
        </div>
        <div class="col-xs-2">
            <button type="button" class="btn btn-primary send_serial" value="GDIx0">Get value</button>
        </div>
    </div>
    <!-- Engine status div -->
    <div id="engine_status" class="container padding_top20">
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
    <div id="engine_gain" class="container padding_top20">
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
    <div id="low_power" class="container padding_top20">
        <div class="col-xs-2">
            <label class="control-label">Low Power Mode: </label>
        </div>
        <div class="col-xs-2">
            <button type="button" class="btn btn-success send_serial" value="SLP">SLEEP</button>
        </div>
        <div class="col-xs-2">
            <button type="button" class="btn btn-danger send_serial" value="W">WAKE UP</button>
        </div>
    </div>
<div id="set_interval" class="container padding_top20">
        <div class="col-xs-2">
            <label class="control-label">Set mesuring interval: </label>
        </div>
        <div class="col-xs-6">
          <form action="" method="">
           <div id="jsalarmclock">
            <div><div class="leftcolumn">Start:</div> <span><select>

            <option value="1">01</option>
            <option value="1">02</option>
            <option value="1">03</option>
            <option value="1">04</option>
            <option value="1">05</option>
            <option value="1">06</option>
            <option value="1">07</option>
            <option value="1">08</option>
            <option value="1">09</option>
            <option value="1">10</option>
            <option value="1">11</option>
            <option value="1">12</option>

            </select> Hour</span> <span><select>

            <option value="1">01</option>
            <option value="1">02</option>
            <option value="1">03</option>
            <option value="1">04</option>
            <option value="1">05</option>
            <option value="1">06</option>
            <option value="1">07</option>
            <option value="1">08</option>
            <option value="1">09</option>
            <option value="1">10</option>
            <option value="1">11</option>
            <option value="1">12</option>
            <option value="1">13</option>
            <option value="1">14</option>
            <option value="1">15</option>
            <option value="1">16</option>
            <option value="1">17</option>
            <option value="1">18</option>
            <option value="1">19</option>
            <option value="1">20</option>
            <option value="1">21</option>
            <option value="1">22</option>
            <option value="1">23</option>
            <option value="1">24</option>
            <option value="1">25</option>
            <option value="1">26</option>
            <option value="1">27</option>
            <option value="1">28</option>
            <option value="1">29</option>
            <option value="1">30</option>
            <option value="1">31</option>
            <option value="1">32</option>
            <option value="1">33</option>
            <option value="1">34</option>
            <option value="1">35</option>
            <option value="1">36</option>
            <option value="1">37</option>
            <option value="1">38</option>
            <option value="1">39</option>
            <option value="1">40</option>
            <option value="1">41</option>
            <option value="1">42</option>
            <option value="1">43</option>
            <option value="1">44</option>
            <option value="1">45</option>
            <option value="1">46</option>
            <option value="1">47</option>
            <option value="1">48</option>
            <option value="1">49</option>
            <option value="1">50</option>
            <option value="1">52</option>
            <option value="1">53</option>
            <option value="1">54</option>
            <option value="1">55</option>
            <option value="1">56</option>
            <option value="1">57</option>
            <option value="1">58</option>
            <option value="1">59</option>
            <option value="1">60</option>
            </select> Minutes</span>
            <div><div class="leftcolumn">Stop:</div> <span><select></select> Hour</span> <span><select></select> Minutes</span>
           </div>


</div></div></form></div></div>
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
