import { InertiaApp } from '@inertiajs/inertia-vue'
import Vue from 'vue'

require('./bootstrap')
require('./icons')

Vue.use(InertiaApp)

const app = document.getElementById('app')

new Vue({
    render: h => h(InertiaApp, {
        props: {
            initialPage: JSON.parse(app.dataset.page),
            resolveComponent: name => require(`./Pages/${name}`).default
        }
    })
}).$mount(app)
