%rebase('base.tpl')
%from helpers.base_datos import *

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
