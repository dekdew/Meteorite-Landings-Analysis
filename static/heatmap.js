var map, heatmap;

function initMap() {
    console.log('init map')
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 2,
    center: {lat: 0, lng: 0},
    mapTypeId: 'satellite'
  });

  heatmap = new google.maps.visualization.HeatmapLayer({
    data: getPoints(),
    map: map,
    radius: 20
  });

/*  var markers = getPoints();
  var bounds = new google.maps.LatLngBounds();
  for (var i = 0; i < markers.length; i++) {
      bounds.extend(markers[i]);
  }

  map.fitBounds(bounds);*/
}

function getPoints() {

    var json = (function () { 
          var json = null; 
          $.ajax({ 
              'async': false, 
              'global': false, 
              'url': 'https://data.nasa.gov/resource/y77d-th95.json',
              'dataType': "json", 
              'success': function (data) {
                   json = data; 
               }
          });
          return json;
      })();

    contents = []
    for (var i = 0, length = json.length; i < length; i++) {
          var data = json[i];
          if (data.reclat === undefined || data.reclong === undefined) {
            continue;
          }
          contents.push(new google.maps.LatLng(data.reclat, data.reclong));
    }
    return contents
}
