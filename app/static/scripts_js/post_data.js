let question = document.querySelector("#form_quest");
let postQuest = document.querySelector("#input_quest");
let url = "/ajax";

async function postJsonData(url, data, headers) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            body: JSON.stringify(data),
            headers: headers
        });
        return await response.json();

    } catch (err) {
        return console.warn(err);
    }
}

question.addEventListener("submit", function (e) {
    e.preventDefault();
    postJsonData(url, { question: postQuest.value }, {
        'Accept': 'application/json',
        "Content-Type": "application/json"
    })
        .then(jsonResponse => {
            let answer = jsonResponse.answer;
            let greetings = jsonResponse.greetings;
            let name = jsonResponse.coords.name;
            let address = jsonResponse.coords.address;

            setTimeout(function () {
                let h2 = document.createElement("h2");
                h2.id = "greetings";
                let h2_content = document.createTextNode(greetings + name + ", " + address);
                h2.appendChild(h2_content);
                let h2Base = document.getElementById("greetings");
                let responseDiv = h2Base.parentNode;
                responseDiv.replaceChild(h2, h2Base);

                let pre = document.createElement("pre");
                pre.id = "resp_text";
                let pre_content = document.createTextNode(answer);
                pre.appendChild(pre_content);
                let preBase = document.getElementById("resp_text");
                let parentDiv = preBase.parentNode;
                parentDiv.replaceChild(pre, preBase);

                document.getElementById("response").style.display = "block";
                document.getElementById("map").style.height = "400px";
                document.getElementById("input_quest").value = "";

                let location = jsonResponse["coords"]["location"];

                if (location && name) { initMap(location, name); } else {

                }

                for (let i = 0; i < thematic.length; i++) {
                    thematic[i].style.cursor = "initial";
                }
            }, 2000);

            let thematic = document.getElementsByClassName('thematic');
            for (let i = 0; i < thematic.length; i++) {
                thematic[i].style.cursor = "wait";
            }
        })
})