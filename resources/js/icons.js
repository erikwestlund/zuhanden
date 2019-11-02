import { library } from '@fortawesome/fontawesome-svg-core'

import {
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

import { faUniversity as farUniversity } from '@fortawesome/pro-regular-svg-icons'

import { FontAwesomeIcon, FontAwesomeLayers } from '@fortawesome/vue-fontawesome'

import { faGithub, faTwitter } from '@fortawesome/free-brands-svg-icons'

library.add(
    faGithub,
    faSignIn,
    faSignOut,
    faUser,
    faUserCircle,
    faUserPlus,
    faUniversity,
    farUniversity,
    fasUniversity
)

Vue.component('fa-icon', FontAwesomeIcon)
Vue.component('fa-layers', FontAwesomeLayers)
