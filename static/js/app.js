
//connect to the socket server.
//   var socket = io.connect("http://" + document.domain + ":" + location.port);
var socket = io.connect('127.0.0.1:5000');

//receive details from server
socket.on("data_update", function (data) {
  console.log("Received sensorData :: " + data.data);
  document.getElementById('sensor-data').innerHTML = 'Received data: ' + data.data;
});

