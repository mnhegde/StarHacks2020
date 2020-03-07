

function initMap(lat,lon) {
    var lowel;
    var map;
    lowel = {lat : lat, lng: lon};
      map = new google.maps.Map(document.getElementById('map'), {
        center: lowel,
        zoom: 8}
      
      )}

 