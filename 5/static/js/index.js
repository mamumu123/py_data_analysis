//add_teach
$(function () {
    $('#teacher').change(function () {
        let tex1 = $("#teacher").find('option:selected').text();
        $('#add_01').text(tex1)
    });
    $('#teaLesson').change(function () {
        let tex2 = $("#teaLesson").find('option:selected').text();
        $('#add_02').text(tex2)
    });
    $('#add1').on('click', function () {
        console.log('============');
        let tex1 = $("#teacher").find('option:selected').text();
        let tex2 = $("#teaLesson").find('option:selected').text();
        //console.log(tex1, tex2);
        var data = {
            "tex1": tex1, "tex2": tex2
        }
        //console.log(data)
        $.ajax({
            url: '/add_teach',
            data: JSON.stringify(data),
            type: 'POST',
            contentType: 'application/json; charset=UTF-8', //指定传递给服务器的是Json格式数据
            success: function () {
                console.log('success')
            }
        })
    })
});
//add_choice
$(function () {
    $('#student').change(function () {
        let tex1 = $("#student").find('option:selected').text();
        $('#add_11').text(tex1)
    });
    $('#stuLesson').change(function () {
        let tex2 = $("#stuLesson").find('option:selected').text();
        $('#add_12').text(tex2)
    });
    $('#add2').on('click', function () {
        console.log('============');
        let tex1 = $("#student").find('option:selected').text();
        let tex2 = $("#stuLesson").find('option:selected').text();
        //console.log(tex1, tex2);
        var data = {
            "tex1": tex1, "tex2": tex2
        }
        //console.log(data)
        $.ajax({
            url: '/add_choice',
            data: JSON.stringify(data),
            type: 'POST',
            contentType: 'application/json; charset=UTF-8', //指定传递给服务器的是Json格式数据
            success: function () {
                console.log('success')
            }
        })
    })
});
//列出学生姓名
$(function () {
    //列出学生姓名
    $('#lesson_btn').on('click', function () {
        let choice = $("#select_lesson").find('option:selected').text();
        //console.log(tex1, tex2);
        var data = {"choice": choice};
        console.log("list", data)
        //console.log(data)
        $.ajax({
            url: '/select_lesson',
            data: JSON.stringify(data),
            type: 'POST',
            contentType: 'application/json; charset=UTF-8', //指定传递给服务器的是Json格式数据
            success: function (data) {
                let json_data = JSON.parse(data);
                // let flag = 1;
                $('#insert_score').html('<table></table>');
                for (var i in json_data) {
                    // if (flag == 1) {
                    //                     //     flag = 0;
                    //                     //     $('#insert_score').html('<table>');
                    //                     // }
                    var tr = '<tr><td class="cID">' + i + '</td><td>' + json_data[i] + '</td><td>' + '<input type="text" class="score_input"></td></tr>';
                    $('#insert_score table').append(tr);
                }
                // $('#insert_score').append('</table>')
                $('#add_score').css('display', 'block');
            }
        })
    })

    //提交成绩表单
    $('#add_score').on('click', function () {
        console.log('-------------------------');
        // var numArr = []; // 定义一个空数组
        var dataForm = [];
        $(".right :input[type=text]").each(function () {
            dataForm.push(this.value);
        })
        console.log(dataForm)
        let choice = $("#select_lesson").find('option:selected').text().split(' ')[0];
        console.log('choice', choice);
        let cID = $('.cID')
        c = []
        for (var i = 0; i < cID.length; i++) {
            c.push(cID.eq(i).text())
        }
        console.log("cID", c)
        let data = {
            "No": choice,
            "cID": c,
            "dataForm": dataForm
        };
        console.log("score:", data)
        // console.info('aaa', numArr);
        // console.log('val  ', val);
        // var test_a = $('form').serializeArray();
        // console.log('test_a', test_a)
        // console.log('serialize:', $("form").serialize());
        // data = new FormData(document.getElementById("input_form"));
        // console.log('new formData', data);

        $.ajax({
            url: '/add_score',
            type: 'post',
            data: JSON.stringify(data),
            contentType: 'application/json; charset=UTF-8', //指定传递给服务器的是Jso
            success: function () {
                console.log('success')
            },
            error: function (err) {
                console.log(err)
            }
        })
    })
});
//查询
$(function () {
    $('#c1').on('click', function () {
        $.ajax({
            url: '/query_stu',
            type: 'POST',
            contentType: 'application/json; charset=UTF-8', //指定传递给服务器的是Json格式数据
            success: function (data) {
                let json_data = JSON.parse(data);
                console.log(json_data);
                let flag = 1;
                for (var i in json_data) {
                    if (flag == 1) {
                        flag = 0;
                        $('#chaxun_show').html('<table>');
                    }
                    var tr = $('<tr><td>' + json_data[i][0] + '</td><td>' + json_data[i][1] + '</td><td>' + json_data[i][2] + '</td><td>' + json_data[i][3] + '</td></tr>');
                    $('#chaxun_show').append(tr);
                }
                $('#chaxun_show').append('</table>')
            }
        })
    });
    $('#c2').on('click', function () {
        $.ajax({
            url: '/query_tea',
            type: 'POST',
            contentType: 'application/json; charset=UTF-8', //指定传递给服务器的是Json格式数据
            success: function (data) {
                let json_data = JSON.parse(data);
                console.log(json_data);
                let flag = 1;
                for (var i in json_data) {
                    if (flag == 1) {
                        flag = 0;
                        $('#chaxun_show').html('<table>');
                    }
                    var tr = $('<tr><td>' + json_data[i][0] + '</td><td>' + json_data[i][1] + '</td><td>' + json_data[i][2] + '</td><td>' + json_data[i][3] + '</td></tr>');
                    $('#chaxun_show').append(tr);
                }
                $('#chaxun_show').append('</table>')
            }
        })
    })
    $('#c3').on('click', function () {
        let name = $('#query_name').val();
        console.log("name", name)
        data = {
            name: name
        };
        $.ajax({
            url: '/query_name',
            data: JSON.stringify(data),
            type: 'POST',
            contentType: 'application/json; charset=UTF-8', //指定传递给服务器的是Json格式数据
            success: function (data) {
                let json_data = JSON.parse(data);
                console.log(json_data);
                let flag = 1;
                for (var i in json_data) {
                    if (flag == 1) {
                        flag = 0;
                        $('#chaxun_show').html('<table>');
                    }
                    var tr = $('<tr><td>' + json_data[i][0] + '</td><td>' + json_data[i][1] + '</td><td>' + json_data[i][2] + '</td><td>' + json_data[i][3] + '</td></tr>');
                    $('#chaxun_show').append(tr);
                }
                $('#chaxun_show').append('</table>')
            }
        })
    })
    $('#c4').on('click', function () {
        $.ajax({
            url: '/query_teato',
            type: 'POST',
            contentType: 'application/json; charset=UTF-8', //指定传递给服务器的是Json格式数据
            success: function (data) {
                let json_data = JSON.parse(data);
                console.log(json_data);
                let flag = 1;
                for (var i in json_data) {
                    if (flag == 1) {
                        flag = 0;
                        $('#chaxun_show').html('<table>');
                    }
                    var tr = $('<tr><td>' + json_data[i][0] + '</td><td>' + json_data[i][1] + '</td><td>' + json_data[i][2] + '</td><td>' + json_data[i][3] + '</td></tr>');
                    $('#chaxun_show').append(tr);
                }
                $('#chaxun_show').append('</table>')
            }
        })
    })
    $('#c5').on('click', function () {
        $.ajax({
            url: '/query_stuto',
            type: 'POST',
            contentType: 'application/json; charset=UTF-8', //指定传递给服务器的是Json格式数据
            success: function (data) {
                let json_data = JSON.parse(data);
                console.log(json_data);
                let flag = 1;
                for (var i in json_data) {
                    if (flag == 1) {
                        flag = 0;
                        $('#chaxun_show').html('<table>');
                    }
                    var tr = $('<tr><td>' + json_data[i][0] + '</td><td>' + json_data[i][1] + '</td><td>' + json_data[i][2] + '</td><td>' + json_data[i][3] + '</td></tr>');
                    $('#chaxun_show').append(tr);
                }
                $('#chaxun_show').append('</table>')
            }
        })
    })
});



