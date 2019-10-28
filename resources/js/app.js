import Event from './modules/Event'

import Alert from './components/Alert'
import Flash from './components/Flash'
import NavigationBar from './components/NavigationBar'
import UserLogin from './components/UserLogin'
import UserRegister from './components/UserRegister'

require('./bootstrap')

window.Vue = require('vue')

require('./icons')

window.Event = new Event()

window.flash = function (message, level = 'success', timeout = 3) {
    window.Event.fire('flash', { message, level, timeout })
}

/* eslint no-unused-vars: "off" */
const app = new Vue({
    el: '#app',
    components: {
        Alert,
        Flash,
        NavigationBar,
        UserLogin,
        UserRegister
    }
})
