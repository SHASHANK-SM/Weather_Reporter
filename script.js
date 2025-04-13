
function getWeather() {
    let city = document.getElementById("city").value;
    let resultDiv = document.getElementById("weather-result");

    if (city === "") {
        resultDiv.innerHTML = "Please enter a city name.";
        return;
    }

    fetch(`/get-weather?city=${city}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                resultDiv.innerHTML = data.error;
            } else {
                resultDiv.innerHTML = `
                    <h2>Weather in ${data.city}</h2>
                    <p>Temperature: ${data.temperature}°C</p>
                    <p>Description: ${data.description}</p>
                    <p>Humidity: ${data.humidity}%</p>
                    <p>Wind Speed: ${data.wind} m/s</p>
                `;
            }
        })
        .catch(error => {
            resultDiv.innerHTML = "Error fetching data.";
        });
}
