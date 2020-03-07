
  path = window.location.pathname.split('/')
  console.log(JSON.stringify(path[2]))

  fetch('/farms', {

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
    console.log(chords)
    let lowell;
    let map;
    lowell = {lat : chords[0], lng: chords[1]};
      map = new google.maps.Map(document.getElementById('map'), {
        center: lowell,
        zoom: 8})

    })
