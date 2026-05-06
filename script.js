const server_addr = "http://192.168.0.207:5000"

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

async function make_html_table(workouts, unique_names) {

    const table = document.querySelector("table")
    table.innerHTML = ""
    
    const header_row = table.insertRow()
    header_row.insertCell().textContent = "Date"

    unique_names.forEach(name => {
        header_row.insertCell().textContent = name
    })

    workouts.forEach(workout => {
        const row = table.insertRow()
        row.insertCell().textContent = workout[1]
        unique_names.forEach(name => {
            row.insertCell()
        })

    })
}

async function make_exercise_menu(unique_names, exercises) {
    const menu = document.getElementById("exercise_menu")
    menu.innerHTML = ""

    unique_names.forEach(unique_name => {
        const div = document.createElement("div")
        div.className = "exercise_row"

        const latest = exercises.filter(e => e[2] === unique_name).at(-1)
        div.innerHTML = `
            <input type="text" value="${unique_name}">
            <input type="text" placeholder="weight" value="${latest ? latest[3] : ''}kg">
            <input type="text" placeholder="reps" value="${latest ? latest[4] : ''}x">
            <input type="text" placeholder="adjustment_lvl" value="${latest ? latest[5] : ''}">
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

async function fill_html_table(exercises) {
    const table = document.querySelector("table")
    exercises.forEach(exercise => {
        const id = exercise[0]
        const workout_id = exercise[1]
        const name = exercise[2]
        const weight = exercise[3]
        const reps = exercise[4]
        const adjustment_lvl = exercise[5]

        const row = table.rows[workout_id]
        const col_index = Array.from(table.rows[0].cells).findIndex(cell => cell.textContent === name)

        row.cells[col_index].textContent = `${weight}kg x ${reps}`
    })
}

//the functions below are button clicks and other directly called functions


async function initialise_html() {
    const [workouts, unique_names, exercises] = await Promise.all([
    get_workouts(),
    get_unique_exercise_names(),
    get_exercises()
    ])

    await make_exercise_menu(unique_names, exercises)
    await make_html_table(workouts, unique_names)
    await fill_html_table(exercises)
}


async function send_button_click(button) {
    const inputs = button.parentElement.querySelectorAll("input")
    const name = inputs[0].value
    const weight = inputs[1].value.replace(/[^0-9.]/g, '')
    const reps = inputs[2].value.replace(/[^0-9]/g, '')
    const adjustment_lvl = inputs[3].value
    
    await post_exercise(name, weight, reps, adjustment_lvl)
    await initialise_html()
}
initialise_html()
