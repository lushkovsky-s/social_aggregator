import template from './app.component.html';
import './app.component.css';

const AppComponent = {
  template,
  controller: ['$scope', 'apiService', ($scope, apiSerice) => {
    apiSerice.getData()
      .then(data => $scope.posts = data)
  }]
};

export default AppComponent;