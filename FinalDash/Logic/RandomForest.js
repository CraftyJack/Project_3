var geoData = "Data/superfund_data.csv"
//console.log(geoData.length)

var myMap = L.map("map", {
  // center: [37.09, -95.71],
  center: [37.09, -97.71],
  zoom: 4
});

// Adding tile layer to the map
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);


// Grab the data with d3
d3.csv(geoData, function(data) {
  //console.log(data)
  // Create a new marker cluster group
  var markers = L.markerClusterGroup();

  // Loop through data
  for (var i = 0; i < data.length; i++) {

    // Set the data location property to a variable
    var lat = data[i].latitude
    var lng = data[i].longitude
    // console.log(lat, lng)
    var predict = parseFloat(data[i].score_prediction)

    markers.addLayer(L.marker([lat, lng])
    .bindPopup('<strong>Actual Site Score: </strong>' + data[i].site_score + '<br>' + '<strong>Predicted Site Score </strong>' + predict.toFixed(2) + 
        '<br>' + '<strong> Address: </strong>' + data[i].address + '<br>' + '<strong> Site Probability </strong>' + (data[i].site_probability * 100)+'%'));

    
  }

  // Add our marker cluster layer to the map
  myMap.addLayer(markers);

});