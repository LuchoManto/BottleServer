local serial_data = ""
local conexion = nil
-- init mqtt client with keepalive timer 120sec
m = mqtt.Client("clientid", 120)
uart.setup(0,9600,8,0,1)
tmr.alarm(0, 1000, 1, function()
   if wifi.sta.getip() ~= nil then
      tmr.stop(0)
   end
end)
local function listen_uart()
    return uart.on("data", '\n',
      function(data)
        serial_data = serial_data..data
        m:publish("/motoresp/data",serial_data,0,0, function(client) end)
        serial_data = ""
    end, 0)
end
local function stop_uart()
    return uart.on("data")
end
local function parse_msg(msg)
    local GET = {}
    if (msg ~= nil)then
        for k, v in string.gmatch(msg, "(%w+)=(%w+)&*") do
            GET[k] = v
        end
    end
    return GET
end
-- on publish message receive event
m:on("message", function(client, topic, data)
  if data ~= nil then
        GET = parse_msg(data)
        if(GET.uartstate == 'disconnected')
        then
            stop_uart()
        end
        if(GET.uartstate == 'connected')
        then
            listen_uart()
        end
        if(GET.tosend)
        then
            uart.write(0, GET.tosend)
        end
  end
end)
-- for TLS: m:connect("192.168.11.118", secure-port, 1)
m:connect("test.mosquitto.org", 1883, 0, function(client)
    m:subscribe("/motoresp/data",0, function(client) end)
end)
