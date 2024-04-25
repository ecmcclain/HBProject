'use strict';

Chart.defaults.color = '#000';
Chart.overrides.doughnut.plugins.legend.position = 'right';
Chart.defaults.layout.padding = 0;

fetch('/get_genres.json')
  .then((response) => response.json())
  .then((responseJson) => {
    const data = responseJson.data.map((genre) => ({
      x: genre.name,
      y: genre.count,
    }));

    console.log(data);
    console.log(data[0]['x']);

    new Chart(document.querySelector('#all_genres'), {
      type: 'doughnut',
      data: {
        labels: data[0]['x'],
        datasets: [
            {
            data: data[0]['y'],
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)',
                'rgb(100, 99, 86)',
                'rgb(30, 162, 180)',
                'rgb(70, 99, 132)',
                'rgb(54, 162, 30)',
                'rgb(10, 99, 10)',
                'rgb(54, 50, 235)',
                'rgb(110, 99, 132)',
                'rgb(170, 162, 80)',
                'rgb(150, 99, 10)',
                'rgb(150, 230, 100)',
              ],
            }
        ]},
      options: {
        plugins: {
            title: {
                display: false,
                text: 'All Genres'
            }
        }
      },
    });
});

fetch('/user_genres.json')
  .then((response) => response.json())
  .then((responseJson) => {
    const data = responseJson.data.map((genre) => ({
      x: genre.name,
      y: genre.count,
    }));

    console.log(data);
    console.log(data[0]['x']);

    new Chart(document.querySelector('#user_genres'), {
      type: 'doughnut',
      data: {
        labels: data[0]['x'],
        datasets: [
            {
            data: data[0]['y'],
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)',
                'rgb(100, 99, 86)',
                'rgb(30, 162, 180)',
                'rgb(70, 99, 132)',
                'rgb(54, 162, 30)',
                'rgb(10, 99, 10)',
                'rgb(54, 50, 235)',
                'rgb(110, 99, 132)',
                'rgb(170, 162, 80)',
                'rgb(150, 99, 10)',
                'rgb(150, 230, 100)',
              ],
            }
        ]},
      options: {
        plugins: {
            title: {
                display: false,
                text: 'Your Genres'
            }
        }
      },
    });
});