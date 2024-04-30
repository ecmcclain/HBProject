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
                'rgb(0, 0, 0)',
                'rgb(25, 25, 102)',
                'rgb(40, 40, 164)',
                'rgb(70, 70, 210)',
                'rgb(132, 132, 225)',
                'rgb(173, 173, 235)',
                'rgb(214, 214, 245)',
                'rgb(231, 231, 254)',
                'rgb(238, 238, 247)',
                'rgb(255, 255, 255)',
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
                'rgb(0, 0, 0)',
                'rgb(25, 25, 102)',
                'rgb(40, 40, 164)',
                'rgb(70, 70, 210)',
                'rgb(132, 132, 225)',
                'rgb(173, 173, 235)',
                'rgb(214, 214, 245)',
                'rgb(231, 231, 254)',
                'rgb(238, 238, 247)',
                'rgb(255, 255, 255)',
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