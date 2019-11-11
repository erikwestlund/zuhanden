import Vue from 'vue'

import { library } from '@fortawesome/fontawesome-svg-core'

import {
    faBomb,
    faBrowser,
    faCheckCircle,
    faCircleNotch,
    faExclamationCircle,
    faGraduationCap,

    faInfoCircle,
    faLock,
    faSignIn,
    faSignOut,
    faUniversity,
    faUser,
    faUserCircle,
    faUserGraduate,
    faUserPlus
} from '@fortawesome/pro-duotone-svg-icons'

import {
    // faUserGraduate,
    faUniversity as fasUniversity
} from '@fortawesome/pro-solid-svg-icons'

import {
    faTimes,
    faUniversity as farUniversity
} from '@fortawesome/pro-regular-svg-icons'

import {} from '@fortawesome/pro-solid-svg-icons'

import { FontAwesomeIcon, FontAwesomeLayers } from '@fortawesome/vue-fontawesome'

import { faGithub, faTwitter } from '@fortawesome/free-brands-svg-icons'

library.add(
    faBomb,
    faBrowser,
    faCheckCircle,
    faCircleNotch,
    faExclamationCircle,
    faInfoCircle,
    faGithub,
    faGraduationCap,
    faLock,
    faSignIn,
    faSignOut,
    faTimes,
    faTwitter,
    faUser,
    faUserCircle,
    faUserGraduate,
    faUserPlus,
    faUniversity,
    farUniversity,
    fasUniversity
)

Vue.component('fa-icon', FontAwesomeIcon)
Vue.component('fa-layers', FontAwesomeLayers)
