const server_addr = "http://localhost:5000"

async function post_exercise(name, weight, reps, adjustment_lvl) {
    await fetch(server_addr + "/add_exercise",
        {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name, weight, reps, adjustment_lvl})
        }

    );
}

async function get_workouts() {
    const response = await fetch(server_addr + "/get_workouts")
    const data = await response.json()
    return data
}

async function enter_workouts_to_html() {
    const data = await get_workouts();

    const table = document.querySelector("table")

    const header_row = table.insertRow()
    header_row.insertCell().textContent = "Date"
    data.forEach(workout => {
        const row = table.insertRow()
        row.insertCell().textContent = workout[1]

    })
}

async function send_button_click() {
    let name = document.getElementById("name").value;
    let weight = document.getElementById("weight").value;
    let reps = document.getElementById("reps").value;
    let adjustment_lvl = document.getElementById("adjustment_lvl").value;
    
    await post_exercise(name, weight, reps, adjustment_lvl)
}

enter_workouts_to_html()
