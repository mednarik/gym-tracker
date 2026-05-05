const server_addr = "http://10.0.104.133:5000"

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
    table.innerHTML = ""
    
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

async function make_exercise_menu() {
    const exercises = await get_unique_exercise_names()
    const menu = document.getElementById("exercise_menu")
    menu.innerHTML = ""
    exercises.forEach(exercise => {
        const div = document.createElement("div")
        div.className = "exercise_row"
        div.innerHTML = `
            <input type="text" value="${exercise}">
            <input type="text" placeholder="weight">
            <input type="text" placeholder="reps">
            <input type="text" placeholder="adjustment_lvl">
            <button onclick="send_button_click(this)">send</button>
            `
        menu.appendChild(div)
    })
    
    const div = document.createElement("div")
    div.className = "exercise_row"
    div.innerHTML = `
        <input type="text" placeholder="name">
        <input type="text" placeholder="weight">
        <input type="text" placeholder="reps">
        <input type="text" placeholder="adjustment_lvl">
        <button onclick="send_button_click(this)">send</button>
        `
    menu.appendChild(div)

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


async function initialise_html() {
    await make_exercise_menu()
    await make_html_table()
    await fill_html_table()
}


async function send_button_click(button) {
    const inputs = button.parentElement.querySelectorAll("input")
    const name = inputs[0].value
    const weight = inputs[1].value
    const reps = inputs[2].value   
    const adjustment_lvl = inputs[3].value
    
    await post_exercise(name, weight, reps, adjustment_lvl)
    await initialise_html()
}

initialise_html()
