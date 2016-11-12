/** Angular Code **/

angular.module('userForm', [])
    .controller('dataController', ['$scope', function($scope) {
      $scope.master = {};

      $scope.update = function(user) {
        $scope.master = angular.copy(user);


      };

      $scope.reset = function() {
        $scope.user = angular.copy($scope.master);
      };

      $scope.reset();
    }]);

var ctx = document.getElementById("myChart");
    var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ["Food", "Necessities", "Entertainment"],
            datasets: [{
                data: [30, 60, 10],
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

var ctx = document.getElementById("myChart2");
    var myChart2 = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["Ideal", "Actual", "Ideal", "Actual", "Ideal", "Actual"],
            datasets: [
                {
                    label: "Your Progress",
                    //Color is either red ("#ff4f14") or green (#13d65d)
                    backgroundColor: [
                        "#c02dff",
                        "#ff4f14",
                        "#f97b36",
                        "#13d65d",
                        "#368bf9",
                        "#ff4f14"
                    ],
                    borderColor: [
                        "#c02dff",
                        "#ff4f14",
                        "#f97b36",
                        "#13d65d",
                        "#368bf9",
                        "#ff4f14"
                    ],
                    borderWidth: 1,
                    data: [30, 55, 50, 35, 10, 15],
                }
            ]
        },
        options: {
        scales: {
            yAxes: [{
                stacked: true
            }]
        }
    }
    });

$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').focus()
})

/*** jquery Updating ***/

