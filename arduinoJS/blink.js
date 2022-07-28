var jf = require("johnny-five");
var circuito = new jf.Board();

circuito.on("ready",blink)

function blink()
{
    var led = new jf.Led(13);
    led.blink(1000);
}