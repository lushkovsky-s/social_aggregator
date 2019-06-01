import 'bootstrap-css-only';
import 'normalize.css';

import angular from 'angular';
import appComponent from './app.component';
import ComponentsModule from './components/components';
import APIService from './services/api'

angular.module('app', [ComponentsModule.name])
  .component('app', appComponent)
  .service('apiService', APIService)
  
