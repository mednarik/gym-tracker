const stars = [135850, 52122, 148825, 16939, 9764]
const frameworks = ["React", "Angular", "Vue", "Hyperapp", "Omi"]

const ctx = document.getElementById("myChart")

const myChart = new Chart(ctx, {
    type: "bar",
    data: {
        labels: frameworks,
        datasets: [
            {
                label: "Popular JavaScript Frameworks",
                data: stars,
            },
        ],
    }
})