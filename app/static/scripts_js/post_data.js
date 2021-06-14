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
            let sanitized_quest = jsonResponse.sanitized_quest;
            let answer = jsonResponse.answer;
            let greetings = jsonResponse.greetings;
            if (jsonResponse.coords) {
                var name = jsonResponse.coords.name;
                var address = jsonResponse.coords.address;
            }
            let quest_err = jsonResponse.quest_err;

            let thematic = document.getElementsByClassName('thematic');
            let container = document.getElementsByClassName('grid-container');

            function wait() {
                for (let i = 0; i < thematic.length; i++) {
                    thematic[i].style.cursor = "wait";
                }
                for (let i = 0; i < container.length; i++) {
                    container[i].style.cursor = "wait";
                }
            }

            function initial() {
                for (let i = 0; i < thematic.length; i++) {
                    thematic[i].style.cursor = "initial";
                }
                for (let i = 0; i < container.length; i++) {
                    container[i].style.cursor = "initial";
                }
            }

            function dial(dialogue) {
                if (dialogue !== undefined) {
                    let pre = document.createElement("pre");
                    pre.className = "resp_indiv";
                    let preContent = document.createTextNode(dialogue);
                    pre.appendChild(preContent);
                    document.querySelector("#resp").appendChild(pre);
                }
                document.getElementById("input_quest").value = "";
            }

            setTimeout(function () {
                if (quest_err) {
                    dial(quest_err);
                    initial();
                } else {
                    dial(greetings + name + " se situe à cette adresse --> " + address);
                }

                setTimeout(function () {
                    if (jsonResponse.coords !== "undefined" && name) {
                        let location = jsonResponse["coords"]["location"];
                        let p = document.createElement("p");
                        p.className = "map";
                        document.querySelector("#resp").appendChild(p);
                        dial(initMap(location, name));
                    }
                    setTimeout(function () {
                        dial(answer);
                        initial();
                    }, 2000);
                }, 2000);
            }, 2000);

            wait();

            dial(sanitized_quest);
            document.getElementById("resp").style.display = "block";
        })
})