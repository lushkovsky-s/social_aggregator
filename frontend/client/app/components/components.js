import angular from 'angular';
    import PostModule from './post/post.module';

const ComponentsModule = angular.module('app.components',[
       PostModule.name 
]);

export default ComponentsModule;