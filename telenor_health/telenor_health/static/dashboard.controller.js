
(function(){
    'use strict';

angular
    .module('dashboardApp')
    .controller('DashboardController', function ($scope, $q, $window, $http, $timeout, dataListService) {
        var self = $scope;
    self.printme = "please convert me to angular js";
    self.reportData = null
    self.reportApiUrl = "../../api/report";

    self.setItems = function(){
        dataListService.getDataList(self.reportApiUrl).then(function (datalist) {
            self.reportData = datalist.data;
            membershipRenewalTrendLineChart();
            subscriptinBasedTrendChart();
            channelIdentificationChart();
            averageMembershipDurationChart();
           });


    };

    function membershipRenewalTrendLineChart() {
        var chart = c3.generate({
            bindto: '#renewal_trend_line_chart',
            data: {
                // x: 'x',
                json: self.reportData.renewal_trend,
                type: 'line',
            },
            axis: {
                x: {
                    label: {
                        text: 'Number Of Renew',
                        position: 'outer-center'
                    },

                },
                y: {
                    label: {
                        text: 'Number of Member',
                        position: 'outer-middle'
                    }
                },
            }
        });

    }



    function subscriptinBasedTrendChart() {
        var chart = c3.generate({
            bindto: '#subscription_trend_based_barchart',
            data: {
                json: self.reportData.subscription_trend,
                type : 'pie',
                onclick: function (d, i) { console.log("onclick", d, i); },
                onmouseover: function (d, i) { console.log("onmouseover", d, i); },
                onmouseout: function (d, i) { console.log("onmouseout", d, i); }
            }
        });
    }

    function averageMembershipDurationChart() {
        console.log(self.reportData);
        var chart = c3.generate({
            bindto: '#average_membership_duration_donut_chart',
            data: {
                json: self.reportData.average_membership_duration,
                type : 'donut',
                onclick: function (d, i) { console.log("onclick", d, i); },
                onmouseover: function (d, i) { console.log("onmouseover", d, i); },
                onmouseout: function (d, i) { console.log("onmouseout", d, i); }
            },
    //         donut: {
    //     title: "Average Membership Duration"
    // }
        });
    }

    function channelIdentificationChart(){
        var chart = c3.generate({
            bindto: '#channel_identification_bar_chart',
            data: {
                json: self.reportData.channel_identification_rate,
                type: 'bar'
            },
            bar: {
                width: {
                ratio: 0.5 // this makes bar width 50% of length between ticks
                }
        // or
        //width: 100 // this makes bar width 100px
            }
        });
    }


    self.setItems();


})


})();