

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

    var uluru = {lat: latitude, long_c: longitude};

    var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 8, center: uluru});

    var marker = new google.maps.Marker({position: uluru, map: map});
  
  )
 
}
