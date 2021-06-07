let question = document.querySelector("#form_quest");
let postQuest = document.querySelector("#input_quest");
let url = "/ajax";

function postJsonData(url, data, headers) {
    return fetch(url, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: headers
    })
        .then((response) => response.json())
        .catch(err => console.warn(err));
}

question.addEventListener("submit", function (e) {
    e.preventDefault();
    postJsonData(url, { question: postQuest.value }, {
        'Accept': 'application/json',
        "Content-Type": "application/json"
    })
        .then(jsonResponse => {
            let answer = jsonResponse["answer"]
            let greetings = jsonResponse["greetings"]

            var h2 = document.createElement("h2");
            h2.id = "greetings";
            var h2_content = document.createTextNode(greetings);
            h2.appendChild(h2_content);
            var h2Base = document.getElementById("greetings");
            var responseDiv = h2Base.parentNode;
            responseDiv.replaceChild(h2, h2Base);

            var pre = document.createElement("pre");
            pre.id = "resp_text";
            var pre_content = document.createTextNode(answer);
            pre.appendChild(pre_content);
            var preBase = document.getElementById("resp_text");
            var parentDiv = preBase.parentNode;
            parentDiv.replaceChild(pre, preBase);

            document.getElementById("response").style.display = "block";
            document.getElementById("map").style.height = "400px";
            document.getElementById("input_quest").value = "";

            let coords = jsonResponse["coords"]["location"];

            if (coords) { initMap(coords); }
        })
})