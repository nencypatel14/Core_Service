let accessToken = null
let tokenType = null

function deActivateAccounts(){
    let username = document.getElementById('username').value
    let password = document.getElementById('password').value 
      var my_data = {"username": username , "password": password}

      $.ajax
      ({
          method: "post",
          url: "http://0.0.0.0:8001/api/user-management/user/token",
          contentType: 'application/json',
          data: JSON.stringify(my_data),
          success: function(data)
          {
            localStorage.setItem('accessToken', data.access_token);
            localStorage.setItem('tokenType', data.token_type);
            accessToken = data.access_token
            tokenType = data.token_type
            console.log(data,data.access_token);
            window.location = 'main.html';
          },
          error: function (result) {
              console.log("Error", result)
          }
      });
    }

function submitData(){
    let access = localStorage.getItem('accessToken')
    let token = localStorage.getItem('tokenType')

    console.log(typeof(access))
    // console.log(JSON.parse(access), JSON.parse(token))

    // let profileImage = document.getElementById('profileImage').value
    let fname = document.getElementById('fname').value
    let lname = document.getElementById('lname').value
    let phoneNumber = document.getElementById('phoneNumber').value
    let email = document.getElementById('username').value
    let password = document.getElementById('password').value

    let address = document.getElementById('address').value
    let role = document.getElementById('role').value
    var user_data = {"profile_img": '1.png', "first_name":fname, "last_name":lname, "phone_number":phoneNumber, "email": email, "password": password, "address":address, "role":role}
    console.log(JSON.stringify(user_data))
        $.ajax
        ({
            method: "post",
            headers: {
                "Authorization": `${token} ${access}`
            },
            url: "http://0.0.0.0:8001/api/user-management/user/add",
            contentType: 'application/json',
            data: JSON.stringify(user_data),
            success: function(data)
            {
                console.log(data);
            },
            error: function(result)
            {
                console.log("Error", result)
            }
        });
}
