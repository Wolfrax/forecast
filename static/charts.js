function plot_ws(id, Title, yAx, obs) {
    Highcharts.chart(id, {
        chart: {
            type: 'spline',
            shadow: true
        },
        title: {
            text: Title
        },
        xAxis: {
            type: 'datetime',
            offset: 40,
            title: {
                text: 'Time'
            }
        },
        yAxis: yAx,
        colors: ['#6CF', '#39F', '#06C', '#036', '#000'],
        series: obs
    });
}

function plot_rose(obs, id, Title) {
    const categories = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'];
    Highcharts.chart(id, {
            series: obs,
            chart: {
                polar: true,
                type: 'column',
                shadow: true
            },
            title: {
                text: Title
            },
            legend: {
                align: 'right',
                verticalAlign: 'top',
                y: 100,
                layout: 'vertical'
            },
            xAxis: {
                min: 0,
                max: 360,
                type: "",
                tickInterval: 45,
                tickmarkPlacement: 'on',
                labels: {
                    formatter: function () {
                        return categories[this.value / 45];
                    }
                }
            },
            yAxis: {
                endOnTick: false,
                showLastLabel: true,
                title: {
                    text: 'Frequency (%)'
                },
                labels: {
                    formatter: function () {
                        return this.value + '%';
                    }
                },
                reversedStacks: false
            },
            plotOptions: {
                series: {
                    stacking: 'normal',
                    shadow: false,
                    groupPadding: 0,
                    pointPlacement: 'on',
                    borderWidth: 0
                }
            }
        }
    )
}
