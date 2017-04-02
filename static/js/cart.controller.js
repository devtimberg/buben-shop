'use strict';

var app;
app = angular.module('CartApp', []).config(function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

app.controller('CartCtrl', ['$scope', '$http',
  function($scope, $http) {
    $scope.sum = 0;

      function getCart(callback)  {
        $http.get('/api/cart/').then(function successCallback(response) {
            $scope.listCart = response.data;
            console.log(response.data);
              if (callback) {
                  callback()
              }
          }, function errorCallback(response) {

          });
      }

    getCart(function () {

    });

    $scope.delProductCart = function () {
        // console.log('get_elements =>', url);
        $http.post('/api/delete/?product_id=1').then(function (response) {
          }, function (error) {

          });
    }

  }
]);


