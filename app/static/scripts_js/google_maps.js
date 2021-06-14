let map;

function initMap(location, name) {
    if (location !== undefined) {
        let payload = {
            center: location,
            zoom: 15,
        }
        map = new google.maps.Map(document.querySelector(".map:last-child"), payload);
        new google.maps.Marker({
            position: location,
            map,
            title: name,
        });
    }
}