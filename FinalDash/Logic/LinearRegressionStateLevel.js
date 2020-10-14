data = 'FinalDash/Data/stateChart.csv'
function init() {
    d3.csv(data, function(states){
        var stateName = states.map(states => states.state_name)
        // console.log(stateName)
        var dropdown = d3.select('#dropdown')

        stateName.forEach((item) => {
            dropdown.append('option').text(item).property('value', item)
        })

        var firstState = dropdown.property('value')
        viz(firstState)
    })
}


function viz(state) {
    d3.csv(data, function(states){
        var vizSet = states.filter(info => info.state_name === state)[0]
        var value = vizSet.score_prediction
        var value1 = vizSet.site_score
        var value2 = vizSet.count
        console.log(vizSet)

        var data = [
            {
                domain: { x: [0, 1], y: [0, 1] },
                value: value,
                title: { text: "Average Predicted Site Score" },
                type: "indicator",
                mode: "gauge+number",
                gauge: {
                    bar: {color: 'blue'},
                    axis: {range: [0, 100]}
                }
            }
        ];
        
        var layout = { width: 600, height: 500, margin: { t: 0, b: 0 } };
        Plotly.newPlot('guage', data, layout);


        var data1 = [
            {
                domain: { x: [0, 1], y: [0, 1] },
                value: value1,
                title: { text: "Average Actual Site Score" },
                type: "indicator",
                mode: "gauge+number",
                gauge: {
                    bar: {color: 'blue'},
                    axis: {range: [0, 100]}
                }
            }
        ];
        
        var layout1 = { width: 600, height: 500, margin: { t: 0, b: 0 } };
        Plotly.newPlot('guage1', data1, layout1);

        var data2 = [
            {
                domain: { x: [0, 1], y: [0, 1] },
                value: value2,
                title: { text: "Number of Superfunds"},
                type: "indicator",
                mode: "number",
                gauge: {
                    bar: {color: 'blue'},
                    axis: {range: [0, 100]}
                }
            }
        ];
        
        var layout2 = { width: 600, height: 250};
        Plotly.newPlot('gauge2', data2, layout2);
    })
}

function optionChanged(newSample) {
    viz(newSample)
  }

init()
