
async function post_exercise(name, weight, reps, adjustment_lvl) {
    await fetch("http://localhost:5000/add_exercise",
        {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name, weight, reps, adjustment_lvl})
        }

    );
}

async function send_button_click() {
    let name = document.getElementById("name").value;
    let weight = document.getElementById("weight").value;
    let reps = document.getElementById("reps").value;
    let adjustment_lvl = document.getElementById("adjustment_lvl").value;
    
    await post_exercise(name, weight, reps, adjustment_lvl)
}

