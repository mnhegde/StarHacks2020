


function initMap(lat,lon) {
    
  lat = lat.replace('h', '.')
  lon = lon.replace('h', '.')
  lat = lat.parseFloat('${lat}')
  lon = lat.parseFloat('${lon}')
  let lowel;
  let map;
  lowel = {lat : lat, lng: lon};
    map = new google.maps.Map(document.getElementById('map'), {
      center: lowel,
      zoom: 8}
    
    )}

