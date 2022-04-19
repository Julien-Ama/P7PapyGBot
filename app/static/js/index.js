let map = null;

function onClickButton() {
    const question = document.getElementById("questionByUser").value
    let form = new FormData();
    form.append("question", question)

    const template =
        `<div class="box-question">
                        <h3>
                            Dis moi bot, ${question} ?
                        </h3>
                    </div>`
    document.getElementById("historical-content").innerHTML += template
    if (map !== null) {
        map.remove()
    }

    fetch("http://127.0.0.1:5000/question", {

        method: "POST",
        body: form
    }).then(function (response) {
        response.json().then(function (responseJsonFormat) {
            document.getElementById("questionByUser").value = ""
            if (responseJsonFormat.wikipedia !== null) {
                console.log("ResponseJsonFormat", responseJsonFormat)
                const description = responseJsonFormat.wikipedia.description
                const url = responseJsonFormat.wikipedia.url
                const title = responseJsonFormat.wikipedia.title

                const geocode = responseJsonFormat.geocode


                // création de la box
                const template =

                    `<div class="box-response">

                        <h3>
                            Voilà la réponse à ta question "${title}"
                        </h3>
                        <p>
                            Voilà ce que je sais : ${description}
                        </p>
                        <a href="${url}" target="_blank">Tiens, clique ici pour en savoir plus !</a>
                    </div>`
                document.getElementById("historical-content").innerHTML += template
                // initMap(geocode.latitude, geocode.longitude)
                map = L.map('map', {
                    center: [geocode.longitude, geocode.latitude],
                    zoom: 13
                });
                L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
                    attribution: '©️ OpenStreetMap contributors'
                }).addTo(map);
            } else {
                (map = null)
                const template =
                    `<div class="box-response">
                        <h3>
                            Ta question était : ${question}
                        </h3>
                        <p>
                            Désolé, je n'ai pas de réponse à ta question.. C'est pas souvent, mais ça arrive !
                        </p>
                        <a href="https://google.com/search?q=${question}" target="_blank">Sinon va voir mon fils Google !</a>

                    </div>`

                document.getElementById("historical-content").innerHTML += template

            }

        })
    })
}

const button = document.getElementById("button-ask-question")
button.addEventListener("click", onClickButton)


