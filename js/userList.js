$(window).ready(() => {
    let userList = $('#user_list')

    fetch('db.cgi', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
    }).then(response => {
        response.json().then(users => {
            if(users.errors.length) {
                console.log(users.errors)

                return alert('При виконанні запиту сталася помилка. Дивіться консоль і стане ясніше)')
            }

            for(user of users.payload.users) {
                userList.append(
                    `<div class="d-flex justify-content-around col-12">
                        <span>uid: ${user.uid}</span>
                        <span>id: ${user.id}</span>
                        <span>credit: ${user.credit}$</span>
                        <span>registration: ${user.registration}</span>
                    </div>`
                )
            }
        })
    })
})