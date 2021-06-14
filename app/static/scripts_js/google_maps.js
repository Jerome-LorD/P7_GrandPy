let map;
let map2;
let p = document.createElement("p");
p.id = "map";

function initMap(location, name) {
    if (location !== undefined) {
        document.querySelector("#resp").appendChild(p);
        let payload = {
            center: location,
            zoom: 15,
        }
        map = new google.maps.Map(document.getElementById("map"), payload);
        new google.maps.Marker({
            position: location,
            map,
            title: name,
        });
    }
}