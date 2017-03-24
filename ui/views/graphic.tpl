% rebase('base.tpl')
% from helpers.base_datos import *

<!-- Graph HTML -->
<div id="graph">
    <div class="col-xs-6">
        <div class="panel-footer">Medicion DataBase</div>
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
                <tr>
                    <td>{{row.tdate}}</td>
                    <td>{{row.pin}}</td>
                    <td>{{row.electrostatic}}</td>
                </tr>
            %pila_medicion.clear()
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
                    <td>{{row.tdate}}</td>
                    <td>{{row.ttime}}</td>
                    <td>{{row.comand}}</td>
                    <td>{{row.respond}}</td>
                </tr>
            %end
            </tbody>
        </table>
    </div>
</div>
<!-- end Graph HTML -->
