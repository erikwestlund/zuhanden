import Vue from 'vue'

import { library } from '@fortawesome/fontawesome-svg-core'

import {
    faBomb,
    faCheckCircle,
    faCircleNotch,
    faExclamationCircle,
    faInfoCircle,
    faLock,
    faSignIn,
    faSignOut,
    faUniversity,
    faUser,
    faUserCircle,
    faUserPlus
} from '@fortawesome/pro-duotone-svg-icons'

import {
    faUniversity as fasUniversity
} from '@fortawesome/pro-solid-svg-icons'

import {
    faTimes,
    faUniversity as farUniversity
} from '@fortawesome/pro-regular-svg-icons'

import { FontAwesomeIcon, FontAwesomeLayers } from '@fortawesome/vue-fontawesome'

import { faGithub, faTwitter } from '@fortawesome/free-brands-svg-icons'

library.add(
    faBomb,
    faCheckCircle,
    faCircleNotch,
    faExclamationCircle,
    faInfoCircle,
    faGithub,
    faLock,
    faSignIn,
    faSignOut,
    faTimes,
    faTwitter,
    faUser,
    faUserCircle,
    faUserPlus,
    faUniversity,
    farUniversity,
    fasUniversity
)

Vue.component('fa-icon', FontAwesomeIcon)
Vue.component('fa-layers', FontAwesomeLayers)
