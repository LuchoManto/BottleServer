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
                    <td>{{rows.tdate}}</td>
                    <td>{{interval.pin}}</td>
                    <td>{{interval.electrostatic}}</td>
                </tr>
            %end
            </tbody>
        </table>
    </div>
</div>
<!-- end Graph HTML -->