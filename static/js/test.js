function confirmCardSelection(){​​​​​
    fetch(`${​​​​​window.origin}​​​​​/keepCards`, {​​​​​
            method: "POST",
            credentials: "include",
            body: JSON.stringify(selected_card),
            cache: "no-cache",
            headers: new Headers({​​​​​
                "content-type": "application/json"
            }​​​​​)
    }​​​​​).then(cards => cards.json()).then(cards => {​​​​​
        var html = ""
        cards.forEach(card =>{​​​​​
            html += `<div class="col-sm"><img id="${​​​​​card}​​​​​" style="margin-top: 50px" class="card-img-top" src="${​​​​​card}​​​​​" onclick="selectCard(this)"></div>`
        }​​​​​)
        var card_container = document.querySelector("#card_container");
        card_container.innerHTML = html;
    }​​​​​)
}​​​​​