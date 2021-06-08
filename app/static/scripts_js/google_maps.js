let map;
function initMap(location, name) {
    if (location !== undefined) {

        map = new google.maps.Map(document.getElementById("map"), {
            center: location,
            zoom: 15,
        });
        new google.maps.Marker({
            position: location,
            map,
            title: name,
        });
    }
}