

function initMap() {
  path = window.location.pathname.split('/')
  console.log(JSON.stringify(path[2]))

  fetch('/api/farmmaps', {

    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: 'POST',
    body: JSON.stringify(path[2])
  })
  .then(function(response){
    return response.json()
  })
  .then(function (myJson) {
    chords = myJson.split(', ')
    latitude = parseFloat(chords[0])
    longitude = parseFloat(chords[1])
    let location;
    var map;
    location = {lat : latitude, lng: longitude};
    map = new google.maps.Map(document.getElementById('map'), {
        center: location, 
        zoom: 8},
    
    marker = new google.maps.Map(position:location,map:map)
  
  ))
 
}
