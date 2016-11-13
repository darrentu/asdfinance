/** Angular Code **/

angular.module('userForm', [])
    .controller('dataController', ['$scope', function($scope) {
      $scope.master = {};
      $scope.budget = [20,30,50]; //food, necessaties, entertainment
      $scope.a = 1;
      $scope.update = function(user) {
        $scope.a = $scope.a + 1;
        $scope.budget = [user.food,user.necessities,user.entertainment];
        console.log(user.food);
        console.log(user.necessities);
        console.log(user.entertainment);
        
        var budget2 = JSON.stringify({
                          "f":user.total,
                          "e":user.food,
                          "n":user.necessities,
                          "b":user.entertainment
                          });
            //localStorage.setItem("budget",budget);
            //console.log(budget);
            socket.emit('userinput',budget2);
            var ctxPie2 = document.getElementById("idealPie");
        //console.log($scope.food);
            var idealPie = new Chart(ctxPie2, {
                type: 'pie',
                data: {

                    labels: ["Food (%)", "Necessities (%)", "Entertainment (%)"],

                    datasets: [{
                        data: [$scope.budget[0], $scope.budget[1], $scope.budget[2]],
                    backgroundColor: [
                        "#a8db11",
                        "#db4011",
                        "#11dbac"
                    ],
                    hoverBackgroundColor: [
                        "#a8db11",
                        "#db4011",
                        "#11dbac"
                    ]}]
                }
            });
        };
        /*
        $scope.reset = function() {
            console.log($scope.budget);
            //$scope.user = angular.copy($scope.master);
        }; */
      var socket = io.connect('http://localhost:5000');
      socket.emit('nextday');
      socket.on('parsedmint', function (data) {
        $scope.category = data;
        $scope.totalSpentToday = data.f + data.e + data.n;
        console.log($scope.budget);
        $scope.food = Math.round((data.f/$scope.totalSpentToday)*100);         
        $scope.entertainment = Math.round((data.e/$scope.totalSpentToday)*100);      
        $scope.necessities = Math.round((data.n/$scope.totalSpentToday)*100);        
         
        /*
        console.log($scope.food);
        console.log($scope.entertainment);
        console.log($scope.necessities);
        console.log($scope.totalSpentToday);
        console.log(data);*/

        var ctxPie1 = document.getElementById("actualPie");
            var actualPie = new Chart(ctxPie1, {
                type: 'pie',
                data: {

                    labels: ["Food (%)", "Necessities (%)", "Entertainment (%)"],

                    datasets: [{
                        data: [$scope.food, $scope.necessities, $scope.entertainment],
                    backgroundColor: [
                        "#c02dff",
                        "#f97b36",
                        "#368bf9"
                    ],
                    hoverBackgroundColor: [
                        "#c02dff",
                        "#f97b36",
                        "#368bf9"
                    ]}]
                }
            });
            /*
        var ctxPie2 = document.getElementById("idealPie");
        //console.log($scope.food);
            var idealPie = new Chart(ctxPie2, {
                type: 'pie',
                data: {

                    labels: ["Food (%)", "Necessities (%)", "Entertainment (%)"],

                    datasets: [{
                        data: [$scope.budget[0], $scope.budget[1], $scope.budget[2]],
                    backgroundColor: [
                        "#a8db11",
                        "#db4011",
                        "#11dbac"
                    ],
                    hoverBackgroundColor: [
                        "#a8db11",
                        "#db4011",
                        "#11dbac"
                    ]}]
                }
            });*/

        var ctxRadar = document.getElementById("compRadar");
            var compRadar = new Chart(ctxRadar, {
                type: 'radar',
                data : {
                    labels: ["Food", "Necessities", "Entertainment"],
                    datasets: [
                        {
                            label: "Ideal Percentage (%)",
                            backgroundColor: "rgba(16, 204, 78,0.2)",
                            borderColor: "rgba(16, 204, 78,1)",
                            pointBackgroundColor: "rgba(16, 204, 788,1)",
                            pointBorderColor: "#fff",
                            pointHoverBackgroundColor: "#fff",
                            pointHoverBorderColor: "rgba(16, 204, 78,1)",
                            data: [30, 60, 10]
                        },
                        {
                            label: "Actual Percentage (%)",
                            backgroundColor: "rgba(219, 19, 19,0.2)",
                            borderColor: "rgba(219, 19, 19,1)",
                            pointBackgroundColor: "rgba(219, 19, 19,1)",
                            pointBorderColor: "#fff",
                            pointHoverBackgroundColor: "#fff",
                            pointHoverBorderColor: "rgba(219, 19, 19,1)",
                            data: [$scope.food, $scope.necessities, $scope.entertainment]
                        }
                    ]
                },
                options: {
                    scale: {
                        ticks: {
                            beginAtZero: true
                        }
                    }
                }
            });
    });
      
      

      //$scope.reset();
    }]);

var socket1 = io.connect('http://localhost:5000');

/*** Ideal Graph ***/

$( "#idealGraph" ).click(
  function() {
    $( this ).css("background-color", "rgb(196, 196, 196)");
    $("#actualGraph").css("background-color", "rgb(255, 255, 255)");
    $("#compGraph").css("background-color", "rgb(255, 255, 255)");

    if ($('#idealAdvanced').is(":checked")){
        socket1.emit('mode', 1);
    } else {
        socket1.emit('mode', 3);
    }
  });

$('#idealAdvanced').change(function(){ 
  if($(this).is(':checked') && $("#idealGraph").css("background-color") == "rgb(255, 255, 255)"){
    socket1.emit('mode', 1);
  }
});

/*** Actual Graph ***/

$( "#actualGraph" ).click(
  function() {
    $( this ).css("background-color", "rgb(196, 196, 196)");
    $("#idealGraph").css("background-color", "rgb(255, 255, 255)");
    $("#compGraph").css("background-color", "rgb(255, 255, 255)");

    if ($('#actualAdvanced').is(":checked")){
        socket1.emit('mode', 0);
    } else {
        socket1.emit('mode', 4);
    }
  });

$('#actualAdvanced').change(function(){ 
  if($(this).is(':checked') && $("#actualGraph").css("background-color") == "rgb(255, 255, 255)"){
    socket1.emit('mode', 0);
  }
});

/*** Comparison Graph ***/

$( "#compGraph" ).click(
  function() {
    $( this ).css("background-color", "rgb(196, 196, 196)");
    $("#idealGraph").css("background-color", "rgb(255, 255, 255)");
    $("#actualGraph").css("background-color", "rgb(255, 255, 255)");

    if ($('#compAdvanced').is(":checked")){
        socket1.emit('mode', 5);
    } else {
        socket1.emit('mode', 2);
    }
  });

$('#compAdvanced').change(function(){ 
  if($(this).is(':checked') && $("#compGraph").css("background-color") == "rgb(255, 255, 255)"){
    socket1.emit('mode', 5);
  }
});