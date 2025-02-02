var chart;

Highcharts.setOptions({
    global: {
        useUTC: false
    }
});
/**
 * Request data from the server, add it to the graph and set a timeout
 * to request again
 */
function requestData() {
    $.ajax({
        url: '/live-data',
        success: function(point) {
            var series = chart.series[0],
                shift = series.data.length > 5; // shift if the series is
                                                 // longer than 20

            // add the point
            chart.series[0].addPoint(point, true, shift);

            // call it again after one second
            setTimeout(requestData, 5000);
        },
        cache: false
    });
}

$(document).ready(function() {
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container',
            defaultSeriesType: 'spline',
            events: {
                load: requestData
            }
        },
        title: {
            text: '습도'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: '습도(%)',
            }
        },
        series: [{
            name: '시간별 습도',
            data: []
        }]
    });
});

var chart2;
function requestData2() {
    $.ajax({
        url: '/live-data2',
        success: function(point) {
            var series = chart2.series[0],
                shift = series.data.length > 5; // shift if the series is
                                                 // longer than 20

            // add the point
            chart2.series[0].addPoint(point, true, shift);

            // call it again after one second
            setTimeout(requestData2, 5000);
        },
        cache: false
    });
}
$(document).ready(function() {
    chart2 = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container2',
            defaultSeriesType: 'spline',
            events: {
                load: requestData2
            }
        },
        title: {
            text: '온도'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: '온도(℃)',
            }
        },
        series: [{
            name: '시간별 온도',
            data: []
        }]
    });
});


var chart3;
function requestData3() {
    $.ajax({
        url: '/live-data3',
        success: function(point) {
            var series = chart3.series[0],
                shift = series.data.length > 5; // shift if the series is
                                                 // longer than 20

            // add the point
            chart3.series[0].addPoint(point, true, shift);

            // call it again after one second
            setTimeout(requestData3, 5000);
        },
        cache: false
    });
}
$(document).ready(function() {
    chart3 = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container3',
            defaultSeriesType: 'spline',
            events: {
                load: requestData3
            }
        },
        title: {
            text: '먼지'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: '먼지량(㎍/㎥)',
            }
        },
        series: [{
            name: '시간별 먼지',
            data: []
        }]
    });
});


var chart4;
function requestData4() {
    $.ajax({
        url: '/live-data4',
        success: function(point) {
            var series = chart4.series[0],
                shift = series.data.length > 5; // shift if the series is
                                                 // longer than 20

            // add the point
            chart4.series[0].addPoint(point, true, shift);

            // call it again after one second
            setTimeout(requestData4, 5000);
        },
        cache: false
    });
}
$(document).ready(function() {
    chart4 = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container4',
            defaultSeriesType: 'spline',
            events: {
                load: requestData4
            }
        },
        title: {
            text: '먼지'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: '먼지량(㎍/㎥)',
            }
        },
        series: [{
            name: '시간별 먼지',
            data: []
        }]
    });
});


var chart5;
function requestData5() {
    $.ajax({
        url: '/live-data5',
        success: function(point) {
            var series = chart5.series[0],
                shift = series.data.length > 5; // shift if the series is
                                                 // longer than 20

            // add the point
            chart5.series[0].addPoint(point, true, shift);

            // call it again after one second
            setTimeout(requestData5, 5000);
        },
        cache: false
    });
}
$(document).ready(function() {
    chart5 = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container5',
            defaultSeriesType: 'spline',
            events: {
                load: requestData5
            }
        },
        title: {
            text: '먼지'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: '먼지량(㎍/㎥)',
            }
        },
        series: [{
            name: '시간별 먼지',
            data: []
        }]
    });
});


var chart6;
function requestData6() {
    $.ajax({
        url: '/live-data6',
        success: function(point) {
            var series = chart6.series[0],
                shift = series.data.length > 5; // shift if the series is
                                                 // longer than 20

            // add the point
            chart6.series[0].addPoint(point, true, shift);

            // call it again after one second
            setTimeout(requestData6, 5000);
        },
        cache: false
    });
}
$(document).ready(function() {
    chart6 = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container6',
            defaultSeriesType: 'spline',
            events: {
                load: requestData6
            }
        },
        title: {
            text: '먼지'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: '먼지량(㎍/㎥)',
            }
        },
        series: [{
            name: '시간별 먼지',
            data: []
        }]
    });
});