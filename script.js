const stars = [135850, 52122, 148825, 16939, 9764]
const frameworks = ["React", "Angular", "Vue", "Hyperapp", "Omi"]

let stars2 = []
let stars3 = []

stars.forEach(star => {
    stars2.push(star/2)
})

stars.forEach(star => {
    stars3.push(star/5 + 100000)
})

const ctx = document.getElementById("myChart")

const myChart = new Chart(ctx, {
    type: "line",
    data: {
        labels: frameworks,
        datasets: [
            {
                label: "Popular JavaScript Frameworks",
                data: stars,
                tension: 0.4,
                showLine: false,
            },
            {
                label: "frameworks2",
                data: stars2,
                tension: 0.4,

            },
            {
                label: "frameworks3",
                data: stars3,
                tension: 0.4,
            }
        ],
    }
})