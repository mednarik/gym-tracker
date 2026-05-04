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

async function get_unique_exercise_names() {
    const response = await fetch(server_addr + "/get_unique_exercise_names")
    const data = await response.json()
    return data
}

async function get_exercises() {
    const response = await fetch(server_addr + "/get_exercises")
    const data = await response.json()
    return data
}

async function make_html_table() {
    const data = await get_workouts();

    const table = document.querySelector("table")

    
    const header_row = table.insertRow()
    header_row.insertCell().textContent = "Date"

    const unique_names = await get_unique_exercise_names()
    unique_names.forEach(name => {
        header_row.insertCell().textContent = name
    })

    data.forEach(workout => {
        const row = table.insertRow()
        row.insertCell().textContent = workout[1]
        unique_names.forEach(name => {
            row.insertCell()
        })

    })
}

async function fill_html_table() {
    const table = document.querySelector("table")
    const exercises = await get_exercises()
    exercises.forEach(exercise => {
        const id = exercise[0]
        const workout_id = exercise[1]
        const name = exercise[2]
        const weight = exercise[3]
        const reps = exercise[4]
        const adjustment_lvl = exercise[5]

        const row = table.rows[workout_id]
        const col_index = Array.from(table.rows[0].cells).findIndex(cell => cell.textContent === name)

        row.cells[col_index].textContent = `${weight}kg ${reps} reps`
    })
}

//the functions below are button clicks and other directly called functions


async function initialise_html_table() {
    await make_html_table()
    await fill_html_table()
}


async function send_button_click() {
    let name = document.getElementById("name").value;
    let weight = document.getElementById("weight").value;
    let reps = document.getElementById("reps").value;
    let adjustment_lvl = document.getElementById("adjustment_lvl").value;
    
    await post_exercise(name, weight, reps, adjustment_lvl)
    await initialise_html_table()
}

initialise_html_table()
