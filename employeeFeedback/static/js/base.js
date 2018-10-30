( function (employeeInfo, $) {

    employeeInfo.customAlert = function(message, alert_type) {
        var icon = '';var typeColor = '';
        if (alert_type == 'success'){
            icon = '<i class="fa fa-check-circle-o " ></i> ';
            typeColor = 'green';
        }
        else if(alert_type == 'error'){
            icon = '<i class="fa fa-exclamation-triangle"></i> ';
            typeColor = 'red';
        }

        var jc = $.dialog({
            title:'',
            titleClass:'hide',
            theme:'light',
            content: icon+message,
            typeAnimated: true,
            boxWidth: '40%',
            useBootstrap: false,
            bgOpacity:0.5,
            type:typeColor,
            animation:'bottom',
            closeAnimation:'bottom',
            animationFromElement:false,
            backgroundDismiss:true,
            animationBounce:1.5,
            onOpenBefore: function () {
                $('.jconfirm-content-pane').css('height','auto');
                $('.jconfirm-content').css('overflow','hidden').css('text-align','center').css('font-size','16px');
                $('.jconfirm-closeIcon').hide()
            },
            onOpen: function(){
                setTimeout(function(){
                    jc.close()
                },3000)
            }
        });
    };

    employeeInfo.getResponse = function (reqType, path, sendData, callbacks ,isFormData) {

        isFormData = isFormData || false ;
        var response = {
            type: reqType,
            url: path,
            //data: JSON.stringify(sendData),
            //headers: {
            //    "X-CSRFToken": bookandsave.getCookie('csrftoken')
            //},

            contentType: 'application/json'
        };
        if(isFormData){
            response["contentType"] = false;
            response["processData"] = false;
            response["data"] = sendData;
        }
        else{
            response["dataType"] = "json";
            response["data"] = JSON.stringify(sendData)
        }


        if (callbacks != undefined) {
            if (callbacks["success"]) {
                response["success"] = function (data, textStatus, jqXHR) {
                    callbacks["success"](data, textStatus, jqXHR);
                };
            }

            response["error"] = function (data, textStatus, jqXHR) {
                bookandsave.csrfTokenHandler(data);
                if (callbacks["error"]) {
                    callbacks["error"](data, textStatus, jqXHR);
                }
            };
        }
        $.ajax(response);
    };

}(window.employeeInfo = window.employeeInfo || {}, jQuery));


$(document).ready(function(){
    $("#addEmployeeModal").dialog({
        autoOpen : false,
        modal : true,
        show : "blind",
        hide : "blind"
    });

    $(".add-employee-btn").click(function(){
        $("#addEmployeeModal").dialog("open");
    });

    $('#saveEmployeeDetails').click(function (e) {
        var formData = new FormData($('#addEmployeeForm')[0]);
        if(!formData.get('employeeName') || !formData.get('employeeEmail')){
            employeeInfo.customAlert('Employee Name and Email are mandatory!', 'error');
            return;
        }
        var request = "/api/admin/employee-details/";
        var callbacks = {};
        callbacks["success"] = function () {
            $(".preloader.employee-info").css({'display': 'none'});
            console.log("New employee added");
            window.location.reload()
        };
        callbacks["error"] = function (data) {
            $(".preloader.employee-info").css({'display': 'none'});
            console.log(data);
        };
        $(".preloader.employee-info").show();
        employeeInfo.getResponse("POST", request, formData, callbacks, true);
        e.preventDefault();
    });
});