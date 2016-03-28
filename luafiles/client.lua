--New module client
local client = {}

local response = {}
local headers = {
    ["Host"] ="gaston",
    ["Content-Type"]= "text/plain",
    ["Content-Length"]= "nil"
}

--Local function to put in string format
local function sprintf(fmt, ...)
    return string.format(fmt, ...)
end

local function make_first_line(code, reason)
    table.insert(response, "HTTP/1.1 "..code.." "..reason.."\r\n")
end

--Recieve as parameter the body text
local function make_headers(body)
    for key, value in pairs(headers) do
        if key == 'Content-Length' then
            value = tostring(#body)
        end
        table.insert(response, sprintf("%s: %s\r\n", key, value))
    end
    table.insert(response, "\r\n")
end

--Function to make a response.
local function get_response(body)
    response={}
    make_first_line("200", "ok")
    make_headers(body)
    table.insert(response, body)
    return table.concat(response)
end

-- Select functions to return
client.get_response = get_response
client.sprintf = sprintf
return client
