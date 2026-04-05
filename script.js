async function get_value(attr) {
          const response = await fetch(`http://localhost:5000/get_attr/${attr}`);
          const data = await response.text();
          return data;
      }
async function post_value(text, attr) {
    await fetch("http://localhost:5000/write_attr",
        {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text: text, attr: attr})
        }

    );
}

async function remove_attr(attr) {
    await fetch(`http://localhost:5000/remove_attr/${attr}`,
        {
        method: "POST",
        }

    );
}

async function req_button_click() {
    let text = document.getElementById("req_input").value;
    let value = await get_value(text);
    document.getElementById("text").textContent = value;
}
async function write_button_click() {
    let text = document.getElementById("write_input1").value;
    let attr = document.getElementById("write_input2").value;
    await post_value(text, attr)
}

async function remove_button_click() {
    let attr = document.getElementById("remove_input").value;
    await remove_attr(attr);
}