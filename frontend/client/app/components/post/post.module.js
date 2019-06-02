import angular from 'angular';

import template from './post.component.html';
import './post.component.css';

const postModule = angular.module('post', [])
  .directive('post', () => ({
    restrict: 'E',
    bindings: {},
    scope: {
      fullname: '@',
      username: '@',
      link: '@',
      userPhoto: '@',
      postText: '@',
      postImage: '@',
      postVideo: '@',
      date: '@',
      retweetsCount: '@',
      likesCount: '@',
      repostsCount: '@',
      viewsCount: '@'
    },  
    controller: ['$scope', '$sce', ($scope, $sce) => {
      $scope.trustedPostVideo = $sce.trustAsResourceUrl($scope.postVideo)
    }],
    template
  }));

export default postModule;