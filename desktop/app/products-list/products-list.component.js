angular.
module('productsList').
component('productsList', {
  // Note: The URL is relative to our `index.html` file
  templateUrl: 'app/products-list/products-list.template.html',
  controller: function ProductsListController($http) {
            var self = this;
            $http.get('/data?_collection=products').then(function(response) {
                self.list = response.data;
            });
        }
});