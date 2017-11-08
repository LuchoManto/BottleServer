%rebase('base.tpl')
%from helpers.base_datos import *

<div class="col-xs-6">
    <!-- Graph HTML -->
    <div id="graph">
        <div style="padding-top: 25px;" class="col-xs-6">
            <div class="panel-footer">Mediciones</div>
            <table id="tablaMediciones" class="table table-striped">
                <thead>
                  <tr>
                    <th>Hora</th>
                    <th>Pin</th>
                    <th>Medición</th>
                  </tr>
                </thead>
                <tbody>
                %for row in reversed(pila_medicion):
                  <tr>
                    <td>{{row['hora']}}</td>
                    <td>{{row['pin']}}</td>
                    <td>{{row['medicion']}}</td>
                  </tr>
                %end
                </tbody>
            </table>
        </div>
        <div style="padding-top: 25px;" class="col-xs-6">
            <div class="panel-footer">Log de Comandos</div>
            <table id="tablaComandos" class="table table-striped">
                <thead>
                  <tr>
                      <th>Fecha</th>
                      <th>Hora</th>
                      <th>Comando</th>
                      <th>Respuesta</th>
                  </tr>
                </thead>
                <tbody>
                %for row in reversed(pila_comando):
                    <tr>
                        <td>{{row['fecha']}}</td>
                        <td>{{row['hora']}}</td>
                        <td>{{row['comando']}}</td>
                        <td>{{row['respuesta']}}</td>
                    </tr>
                %end
                </tbody>
            </table>
        </div>
    </div>

    <script>
    var updateTable = function(data){
        var tablaMediciones = document.getElementById("tablaMediciones");
        var tablaComandos = document.getElementById("tablaComandos");


        var datosMediciones = data.pila_medicion;
        var datosComandos = data.pila_comando;
        var lenTablaMediciones = tablaMediciones.rows.length - 1;
        var lenTablaComandos = tablaComandos.rows.length - 1;
        var lenDatosMediciones = datosMediciones.length;
        var lenDatosComandos = datosComandos.length;
        var datosFaltantesMediciones = lenDatosMediciones - lenTablaMediciones;
        var datosFaltantesComandos = lenDatosComandos - lenTablaComandos;

        datosMediciones = datosMediciones.slice(lenDatosMediciones-datosFaltantesMediciones);
        datosComandos = datosComandos.slice(lenDatosComandos-datosFaltantesComandos);

        for (dato in datosMediciones){
            agregarDatoMedicion(datosMediciones[dato], tablaMediciones);
        }

        for (dato in datosComandos){
            agregarDatoComando(datosComandos[dato], tablaComandos);
        }
    };

    var agregarDatoMedicion = function(dato, table){
        // Create an empty <tr> element and add it to the 1st position of the table:
        var row = table.insertRow(1);

        // Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
        var horaCell = row.insertCell(0);
        var pinCell = row.insertCell(1);
        var medicionCell = row.insertCell(2);

        // Add some text to the new cells:
        horaCell.innerHTML = dato.hora;
        pinCell.innerHTML = dato.pin;
        medicionCell.innerHTML = dato.medicion;
    };

    var agregarDatoComando = function(dato, table){
            // Create an empty <tr> element and add it to the 1st position of the table:
        var row = table.insertRow(1);

        // Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
        var fechaCell = row.insertCell(0);
        var horaCell = row.insertCell(1);
        var comandoCell = row.insertCell(2);
        var respuestaCell = row.insertCell(3);

        // Add some text to the new cells:
        fechaCell.innerHTML = dato.fecha;
        horaCell.innerHTML = dato.hora;
        comandoCell.innerHTML = dato.comando;
        respuestaCell.innerHTML = dato.respuesta;
    };


    $(document).ready(function(){
        var url = window.location.origin + '/data';

        setInterval(function(){

            $.getJSON(url, {}, function(data) {
                updateTable(data)
            });

        }, 3000);
    });
    </script>
    <!-- end Graph HTML -->

</div>

<div class="col-xs-6">
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
            <!-- ADC div -->
            <div class="container padding_top20">
                <div class="col-xs-2">
                    <label class="control-label">ADC:</label>
                </div>
                <div class="col-xs-2">
                    <button type="button" class="btn btn-success send_serial" value="ST">Start</button>
                </div>
                <div class="col-xs-2">
                    <button type="button" class="btn btn-danger send_serial" value="s">End</button>
                </div>
            </div>
            <!-- Engine status div -->
            <div id="engine_status" class="container padding_top20">
                <div class="col-xs-2">
                    <label class="control-label">Engine: </label>
                </div>
                <div class="col-xs-2">
                    <button type="button" class="btn btn-success send_serial" value="AMS">On</button>
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

        <div id="set_interval" class="container padding_top20">
                <div class="col-xs-2">
                    <label class="control-label">Set mesuring interval: </label>
                </div>
                <div class="col-xs-2">
                Start: <input type="time" id="start_interval" min="00:00" max="23:59"><br>
                </div>
                <div class="col-xs-2">
                End: <input type="time" id="end_interval" min="00:00" max="23:59"><br>
                </div>
                <button id="set_interval_button" class="btn btn-primary">Set</button>
        </div>
            <div id="interval_tbl" class="container padding_top20">
                 <div class="col-xs-6">
                <table>
                    %if intervals.__len__() != 0:
                    <tr>
                        <th>Interval ID</th>
                        <th>Start time</th>
                        <th>End time</th>
                    </tr>
                    %end
                    %for interval in intervals:
                    <tr>
                        <td>{{interval.id}}</td>
                        <td>{{interval.hour_start}}:{{interval.min_start}}</td>
                        <td>{{interval.hour_end}}:{{interval.min_end}}</td>
                        <td><button class="remove_interval_button btn btn-primary" value="{{interval.id}}">Erase</button></td>
                    </tr>
                    %end
                </table>
                 </div>
            </div>
        <!--Script when send a specific value-->
        <script>

        $("#dato_bd").click(function(e){
            e.preventDefault();
            //Post with the button

            $.ajax({
                url: '/graphic',
                data:
                {
                },
                datatype: "json",
                cache:false, type: 'POST',
                success: function(data){
                    location.reload();
                }
            });


        $("#set_interval_button").click(function(e){
            e.preventDefault();
            //Post with the button

            $.ajax({
                url: '/set_interval',
                data:
                {
                    start: $('#start_interval').val(),
                    end:   $('#end_interval').val()
                },
                datatype: "json",
                cache:false, type: 'POST',
                success: function(data){
                    location.reload();
                }
            });
        });
        </script>

        <script>
        $(".remove_interval_button").click(function(e){
            e.preventDefault();

                $.ajax({
                url: '/remove_interval/' + $(this).attr("value"),
                cache:false, type: 'POST',
                success: function(data){
                    location.reload();
                }
            });
        });
        </script>
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
    </div>
</div>
