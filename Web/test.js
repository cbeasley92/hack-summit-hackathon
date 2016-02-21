  console.log("Hello");
  function uberLogin(){
            var clientId = "HVXgAbDzXyvreW-pctRCHtrvXbYieGD5";
            var redirect = "http://localhost:7000/submit";
            var responseType = "code";
            
            $.ajax({
                type: "GET",
                url: "https://login.uber.com/oauth/v2/authorize?client_id=" + clientId + "&response_type=" + responseType
            }).done(function(response){
                console.log(response);
            });
        }