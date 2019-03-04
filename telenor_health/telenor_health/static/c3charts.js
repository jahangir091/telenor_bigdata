//
// var data = {
//     "total_member": 100,
//     "subscription_trend": {
//         "unpaid": 60,
//         "paid": 40
//     }
// }
//
// var chart = c3.generate({
//     bindto: '#chart',
//     data: {
//         json: data['subscription_trend'],
//         type : 'pie',
//         onclick: function (d, i) { console.log("onclick", d, i); },
//         onmouseover: function (d, i) { console.log("onmouseover", d, i); },
//         onmouseout: function (d, i) { console.log("onmouseout", d, i); }
//     }
// });