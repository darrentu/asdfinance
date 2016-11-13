/** Angular Code **/

angular.module('userForm', [])
    .controller('dataController', ['$scope', function($scope) {
      $scope.master = {};
      
      var socket = io.connect('http://localhost:5000');
      socket.emit('nextday');
      socket.on('parsedmint', function (data) {

        $scope.category = data;
        $scope.totalSpentToday = data.f + data.e + data.n;
        
        $scope.food = Math.round((data.f/$scope.totalSpentToday)*100);
        $scope.entertainment = Math.round((data.e/$scope.totalSpentToday)*100);
        $scope.necessities = Math.round((data.n/$scope.totalSpentToday)*100);
        console.log($scope.food);
        console.log($scope.entertainment);
        console.log($scope.necessities);
        console.log($scope.totalSpentToday);
        console.log(data);

        var ctxPie = document.getElementById("actualPie");
        var actualPie = new Chart(ctxPie, {
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
                    data: [55, 35, 15]
                }
            ]
        }
    });
        
    
    });
      
      $scope.update = function(user) {
        $scope.master = angular.copy(user);
      };

      $scope.reset = function() {
        $scope.user = angular.copy($scope.master);
      };

      $scope.reset();
    }]);



$('#graphModal').on('shown.bs.modal', function () {
  $('#myInput').focus()
})


