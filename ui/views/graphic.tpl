%rebase('base.tpl')
%from helpers.base_datos import *

<!-- Graph HTML -->
<div id="graph">
    <div class="col-xs-6">
        <div class="panel-footer">Mediciones</div>
        <table class="table table-striped">
            <thead>
              <tr>
                <th>Fecha</th>
                <th>Pin</th>
                <th>Medición</th>
              </tr>
            </thead>
            <tbody>
                %for row in pila_medicion:
                %hora = row.hora
                %pin = row.pin
                %medicion = row.medicion
              <tr>
                <td>{{hora}}</td>
                <td>{{pin}}</td>
                <td>{{medicion}}</td>
              </tr>
            %end
            </tbody>
        </table>
    </div>
    <div class="col-xs-6">
        <div class="panel-footer">Log de Comandos</div>
        <table class="table table-striped">
            <thead>
              <tr>
                  <th>Fecha</th>
                  <th>Hora</th>
                  <th>Comando</th>
                  <th>Respuesta</th>
              </tr>
            </thead>
            <tbody>
                %for row in pila_comando:
                <tr>
                    <td>{{row.fecha}}</td>
                    <td>{{row.hora}}</td>
                    <td>{{row.comando}}</td>
                    <td>{{row.respuesta}}</td>
                </tr>
            %end
            </tbody>
        </table>
    </div>
</div>
<!-- end Graph HTML -->
