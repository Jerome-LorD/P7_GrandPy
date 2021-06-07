let map;
function initMap(coords) {
    if (coords !== undefined) {

        map = new google.maps.Map(document.getElementById("map"), {
            center: coords,
            zoom: 15,
        });
        new google.maps.Marker({
            position: coords,
            map,
            // title: "Hello World!",
        });
    }
}