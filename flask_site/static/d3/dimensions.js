// set the dimensions and margins of the graph
var margin = { top: 20, right: 100, bottom: 30, left: 60 },
  width = 800 - margin.left - margin.right,
  height = 500 - margin.top - margin.bottom;

// Create the svg canvas in the "graph" div
var svg = d3.select("#bar-graph")
  .append("svg")
  .style("width", width + margin.left + margin.right + "px")
  .style("height", height + margin.top + margin.bottom + "px")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
  .attr("class", "svg");


// Get the data
// d3.csv("clickpredictions.csv", function (error, data) {
//   if (error) throw error;

  d3.csv("{{url_for('static', filename='data/clickpredictions.csv')}}", function (error, data) {
  if (error) throw error;


  // Set the ranges
  var x = d3.scaleBand().rangeRound([0, width]).padding(0.1)
  var y = d3.scaleLinear().range([height, 0]);

  // Get every column value - DONE
  var elements = Object.keys(data[0])
    .filter(function (d) {
      return ((d != "click"));
    });
  var selection = elements[3];
  console.log(selection);

  var displayClick = 0;

  data.forEach(function(d) {
    let click = parseInt(d.click)
    displayClick += click;
  })
  console.log(displayClick);

 document.getElementById("clairesmells").innerHTML = displayClick;

 var rowCount = 0
 data.forEach(function(d) {
   if (d.click) {
     rowCount++
   }
 })

 console.log(rowCount);

 var CTR = displayClick/rowCount;
document.getElementById("expectedctr").innerHTML = CTR + "%";


  var chartTitle = "Clicks by " + selection;
  d3.select("#bar-graph-title")
    .text(chartTitle);

  // Groupby device type and then sum clicks - Works
  // clicksTotal has "key" and "value" attributes
  var clicksTotal = d3.nest()
    .key(function (d) { return +d[selection]; }).sortKeys(d3.ascending)
    .rollup(function (v) { return d3.sum(v, function (d) { return d.click; }); })
    .entries(data);
  console.log("TotalClicks");
  console.log()
  console.log(JSON.stringify(clicksTotal));

  var y = d3.scaleLinear()
    .domain([0, d3.max(clicksTotal, function (d) {
      return d.value;
    })])
    .range([height, 0]);

  var x = d3.scaleBand()
    .domain(clicksTotal.map(function (d) { return d.key; }))
    .rangeRound([0, width]).padding(0.2)

  var xAxis = d3.axisBottom()
    .scale(x)

  svg.append("text")
    .attr("class", "x label")
    .attr("text-anchor", "middle")
    .attr("x", width / 2)
    .attr("y", height + 30)
    .text("Categories");

  var yAxis = d3.axisLeft()
    .scale(y)

  svg.append("text")
    .attr("class", "y label")
    .attr("text-anchor", "middle")
    .attr("x", -width / 4)
    .attr("y", -45)
    .attr("dy", ".75em")
    .attr("transform", "rotate(-90)")
    .text("Total Clicks");

  // Draw y axis
  svg.append("g")
    .attr("class", "y axis")
    .call(yAxis);

  // Draw x axis
  svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis)
    .selectAll("text")
    .style("font-size", "8px")
    .style("text-anchor", "end")

  //              Draw the bars - FIRST TIME
  svg.selectAll("rectangle")
    .data(clicksTotal)
    .enter()
    .append("rect")
    .attr("class", "rectangle")
    .attr("x", function (d) { return x(d.key); })
    .attr("y", function (d) { return y(d.value); })
    .attr("width", width / (clicksTotal.length + 1))
    .attr("height", function (d) { console.log('testing', height, d.value); return height - y(d.value); });

  var selector = d3.select("#drop")
    .append("select")
    .attr("id", "dropdown")
    .attr("class", "drop-content")
    .on("change", function (d) {
      selection = document.getElementById("dropdown");

      //                    update bar chart title
      console.log(selection.value)
      var chartTitle = "Clicks by " + selection.value;
      d3.select("#bar-graph-title")
        .text(chartTitle);

      //                    recompute data values
      var clicksTotal = d3.nest()
        .key(function (d) { return +d[selection.value]; }).sortKeys(d3.ascending)
        .rollup(function (v) { return d3.sum(v, function (d) { return d.click; }); })
        .entries(data);

      console.log(selection.value)
      console.log("TotalClicks - DONE")
      console.log(JSON.stringify(clicksTotal));

      // Adjust y-axis
      var ymax = d3.max(clicksTotal, function (d) {
        return d.value;
      });

      y.domain([0, ymax]);
      yAxis.scale(y);

      // Adjust x-axis
      console.log("New x-axis keys:")
      x.domain(clicksTotal.map(function (d) {
        console.log(d.key)
        return d.key;
      }));
      xAxis.scale(x);

      console.log("Height/X/Y")

      svg.selectAll("rect").remove()

      // Draw the new bars
      svg.selectAll(".rectangle")
        .data(clicksTotal)
        .enter()
        .append("rect")
        .attr("class", "rectangle")

        .attr("x", function (d) {
          console.log(x(d.key))
          return x(d.key);
        })

        .attr("y", function (d) {
          console.log(y(d.value))
          return y(d.value);
        })

        .attr("width", width / (clicksTotal.length + 1))

        .attr("height", function (d) {
          newh = height - y(d.value)
          //                            console.log("HEIGHT: " + newh)
          return newh;
        })

      console.log("Bars done")

      // Apply scaled y axis
      d3.selectAll("g.y.axis")
        .transition()
        .call(yAxis);

      // Apply scaled x axis
      d3.selectAll("g.x.axis")
        .transition()
        .call(xAxis);

      //                console.log(selection)
    }); //End of on change function

  selector.selectAll("option")
    .data(elements)
    .enter().append("option")
    .attr("value", function (d) {
      return d;
    })
    .text(function (d) {
      return d;
    })

});
