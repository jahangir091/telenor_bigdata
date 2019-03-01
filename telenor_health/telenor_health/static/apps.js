


(function(){
    'use strict';

angular
    .module('dashboardApp', [])
    .config(function($interpolateProvider) {
        // $httpProvider.defaults.withCredentials = true;
        $interpolateProvider.startSymbol('[{');
        $interpolateProvider.endSymbol('}]');

    });


})();